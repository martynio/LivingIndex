"""Compare browser arithmetic against the accepted Python engine; synthetic values only."""
from decimal import Decimal
import json
from pathlib import Path
import random
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from economic_engine import national_budget, work_time
from test_economic_engine import row


def run():
    rng = random.Random(27)
    cases, expected = [], []
    for _ in range(250):
        a, b, c = [f'{Decimal(rng.randrange(1, 10**18))/Decimal(1000000):.6f}' for _ in range(3)]
        cases.extend([['budget', [a, b]], ['work', [a, b, c]]])
        budget = national_budget(row('cash_disposable_income', a), row('cash_total_expenditure', b))
        expected.append({'balance': budget['cash_balance'], 'share': budget['expenditure_share_percent']})
        work = work_time(row('net_employment_earnings', a, basis='worker'),
                         row('paid_hours', b, basis='worker'), row('cash_cost', c, basis='worker'))
        expected.append({'rate': work['net_hourly_rate'], 'equivalent': work['cost_equivalent_paid_hours']})
    js = "const api=require('./web/assets/js/dashboard.js');let x=JSON.parse(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(x.map(([f,args])=>api[f](...args))));"
    actual = json.loads(subprocess.check_output(['node', '-e', js], input=json.dumps(cases).encode(), cwd=ROOT))
    assert len(actual) == len(expected) == 500
    for i, (a, b) in enumerate(zip(actual, expected)):
        if 'balance' in a:
            assert Decimal(a.pop('balance')) == Decimal(b.pop('balance')), i
        assert a == b, (i, a, b)
    print('500 deterministic synthetic cross-language arithmetic cases PASS')


if __name__ == '__main__':
    run()
