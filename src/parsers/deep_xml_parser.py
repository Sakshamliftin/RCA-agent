import xml.etree.ElementTree as ET
import re
import os

class DeepXMLParser:
    """Parses Robot Framework's output.xml with Backward Slicing"""
    
    @staticmethod
    def extract_target_vars(kw, error_msg):
        vars_found = []
        match = re.search(r"Variable '(\$\{.*?\})' not found", error_msg)
        if match:
            vars_found.append(match.group(1))
            
        for arg in kw.findall("arg"):
            if arg.text and '${' in arg.text:
                matches = re.findall(r'(\$\{.*?\})', arg.text)
                vars_found.extend(matches)
        return list(set(vars_found))

    @staticmethod
    def trace_variable_dependencies(flat_kws, start_index, target_vars, depth=1, max_depth=10):
        if depth > max_depth or not target_vars:
            return []
            
        chain = []
        for v in target_vars:
            found = False
            for j in range(start_index - 1, -1, -1):
                prev_kw = flat_kws[j]
                for var_node in prev_kw.findall("var"):
                    if var_node.text and v in var_node.text:
                        assigning_kw_name = prev_kw.attrib.get("name", "Unknown")
                        
                        intent = ""
                        doc_node = prev_kw.find("doc")
                        if doc_node is not None and doc_node.text:
                            intent = doc_node.text.strip()
                            
                        args = [a.text for a in prev_kw.findall("arg") if a.text]
                        logs = [m.text for m in prev_kw.findall("msg") if m.text]
                        
                        chain.append({
                            "depth": depth,
                            "variable": v,
                            "assigning_keyword": assigning_kw_name,
                            "assigning_intent": intent,
                            "assigning_args": ", ".join(args) if args else "None",
                            "assigning_logs": " | ".join(logs[:3]) if logs else "None"
                        })
                        
                        # Recursively trace this keyword's arguments
                        new_target_vars = []
                        for arg in args:
                            if '${' in arg:
                                matches = re.findall(r'(\$\{.*?\})', arg)
                                new_target_vars.extend(matches)
                        
                        if new_target_vars:
                            sub_chain = DeepXMLParser.trace_variable_dependencies(
                                flat_kws, j, list(set(new_target_vars)), depth + 1, max_depth
                            )
                            chain.extend(sub_chain)
                            
                        found = True
                        break
                if found:
                    break
        return chain

    @staticmethod
    def find_lowest_level_failures(xml_path):
        if not os.path.exists(xml_path):
            return []
            
        try:
            tree = ET.parse(xml_path)
        except ET.ParseError:
            return [{"error_message": "XML Parse Error - output.xml is corrupted", "failing_keyword": "N/A"}]
            
        root = tree.getroot()
        flat_kws = list(root.iter("kw"))
        all_elements = list(root.iter())
        lowest_failing_kws = []
        
        for i, kw in enumerate(flat_kws):
            status_node = kw.find("status")
            if status_node is not None and status_node.attrib.get("status") == "FAIL":
                has_failing_child = False
                for child_kw in kw.findall(".//kw"):
                    child_status = child_kw.find("status")
                    if child_status is not None and child_status.attrib.get("status") == "FAIL":
                        has_failing_child = True
                        break
                
                if not has_failing_child:
                    kw_name = kw.attrib.get("name", "Unknown Keyword")
                    msg_node = kw.find("msg[@level='FAIL']")
                    error_msg = msg_node.text if msg_node is not None else "No message found"
                    
                    if kw_name == "Update Robot Status Infra":
                        continue
                        
                    traceback = ""
                    for m in kw.findall(".//msg"):
                        if m.attrib.get("level") == "DEBUG" and m.text and "Traceback" in m.text:
                            traceback = m.text
                            break
                            
                    intent = ""
                    doc_node = kw.find("doc")
                    if doc_node is not None and doc_node.text:
                        intent = doc_node.text.strip()
                            
                    context_logs = []
                    # Find this kw in all_elements and look backwards for messages
                    try:
                        kw_idx = all_elements.index(kw)
                        for elem in reversed(all_elements[:kw_idx]):
                            if elem.tag == "msg":
                                level = elem.attrib.get("level")
                                if level in ["INFO", "TRACE"] and elem.text:
                                    context_logs.insert(0, f"[{level}] {elem.text.strip()}")
                                    if len(context_logs) >= 15:
                                        break
                    except ValueError:
                        pass
                            
                    file_line = ""
                    if traceback:
                        match = re.search(r'File "(.*?)", line (\d+)', traceback)
                        if match:
                            file_line = f"{match.group(1)} (Line {match.group(2)})"
                        else:
                            file_line = "[Line number suppressed by Robot Framework]"
                            
                    # Backward Slicing (Recursive Data Flow Tracking)
                    target_vars = DeepXMLParser.extract_target_vars(kw, error_msg)
                    dependency_chain = DeepXMLParser.trace_variable_dependencies(flat_kws, i, target_vars)

                    lowest_failing_kws.append({
                        "failing_keyword": kw_name,
                        "error_message": error_msg,
                        "traceback": traceback,
                        "intent": intent,
                        "context_logs": context_logs,
                        "file_line": file_line,
                        "target_vars": target_vars,
                        "dependency_chain": dependency_chain
                    })
        return lowest_failing_kws
