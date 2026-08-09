import sys, os
sys.path.append(os.getcwd())
from src.main import LocalRCAPipeline
agent = LocalRCAPipeline()
test_cases = ['ATER-27206', 'ATER-27208', 'ATER-27210']
for tc in test_cases:
    print(f'\n{"="*80}')
    print(f'==== Analyzing {tc} ====')
    print(f'{"="*80}\n')
    res = agent.analyze_directory(f'data/poc_dataset/{tc}')
    if res.get('triage_rules'):
        print(f'Rule Engine Match:\n{res["triage_rules"]}')
    else:
        print(f'LLM Analysis:\n{res["llm_analysis"]}')
