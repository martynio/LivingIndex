"""Synthetic scenarios and report fixtures only; real report replay is separate."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import economic_engine as engine
from test_economic_research import fixture


def row(measure, value, /, **changes):
    return dict(dict(kind='hypothetical', scenario_id='synthetic-1', country='PL', year=2020,
                     currency='PLN', period='month', basis='person', population='synthetic population',
                     measure=measure, value=value), **changes)


def budget(inc='2000', exp='1500', **changes):
    return engine.national_budget(row('cash_disposable_income', inc),
                                  row('cash_total_expenditure', exp, **changes))


def time_inputs(net='2000', hours='160', cost='100'):
    return [row(measure, value, basis='worker') for measure, value in
            zip(('net_employment_earnings', 'paid_hours', 'cash_cost'), (net, hours, cost))]


def pps(report, category='CP01'):
    raw = json.dumps(report).encode()
    return engine.pps_comparison(raw, hashlib.sha256(raw).hexdigest(), category)


class EngineTests(unittest.TestCase):
    def test_budget(self):
        r = budget()
        self.assertEqual(r['cash_balance'], '500')
        self.assertEqual(r['expenditure_share_percent'], '75.00')
        self.assertFalse(r['production_eligible'])

    def test_deficit(self):
        self.assertEqual(budget('100', '120')['cash_balance'], '-20')
        self.assertEqual(budget('100', '120')['expenditure_share_percent'], '120.00')

    def test_zero_income(self):
        r = budget('0', '10')
        self.assertIsNone(r['expenditure_share_percent'])
        self.assertEqual(r['cash_balance'], '-10')

    def test_decimal_precision(self):
        self.assertEqual(budget('0.30', '0.10')['cash_balance'], '0.20')
        self.assertEqual(budget('3', '1')['expenditure_share_percent'], '33.33')

    def test_context_mismatch(self):
        for key, value in [('country','NL'), ('currency','EUR'), ('period','year'),
                           ('year',2021), ('basis','household'), ('population','other'),
                           ('scenario_id','other')]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                budget(**{key:value})

    def test_national_currency_pair(self):
        inc = row('cash_disposable_income', '10', country='NL', currency='EUR')
        exp = row('cash_total_expenditure', '4', country='NL', currency='EUR')
        self.assertEqual(engine.national_budget(inc, exp)['cash_balance'], '6')

    def test_non_cash_and_pps_rejected(self):
        for key, value in [('measure','consumption_expenditure'), ('currency','PPS_HH'),
                           ('kind','research_observations'), ('production_eligible',True)]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                budget(**{key:value})

    def test_invalid_amounts(self):
        for value in (None, True, 1.0, 'NaN', 'Infinity', '-1', '1e3', '0.0000001'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                budget(exp=value)

    def test_pps_pair(self):
        r = pps(fixture(True), 'CP12')
        self.assertEqual(r['unit'], 'PPS_HH')
        self.assertEqual([x['country'] for x in r['observations']], ['PL','NL'])
        self.assertEqual([x['value'] for x in r['observations']], [11,12])
        self.assertEqual(r['pair_status'], 'review_required')
        self.assertFalse(r['production_eligible'])
        self.assertEqual(r['review']['methodology'], 'pending')

    def test_pps_missing_and_flag(self):
        d = fixture(True)
        d['observations'][0].update(value=None, source_flag='u')
        d.update(missing_cells=1, result='INCOMPLETE_REVIEW_REQUIRED')
        r = pps(d)
        self.assertIsNone(r['observations'][0]['value'])
        self.assertEqual(r['observations'][0]['source_flag'], 'u')
        self.assertEqual(r['pair_status'], 'missing')
        d = fixture(True)
        d['observations'][0]['source_flag'] = 'e'
        self.assertEqual(pps(d)['pair_status'], 'flagged')

    def test_pps_invalid_category_and_digest(self):
        for category in ('TOTAL','CP13','CP02'):
            with self.subTest(category=category), self.assertRaises(ValueError):
                pps(fixture(), category)
        with self.assertRaises(ValueError):
            engine.pps_comparison(b'{}', '0'*64, 'CP01')

    def test_work_time(self):
        r = engine.work_time(*time_inputs())
        self.assertEqual(r['net_hourly_rate'], '12.50')
        self.assertEqual(r['cost_equivalent_paid_hours'], '8.00')
        self.assertFalse(r['production_eligible'])

    def test_work_time_no_intermediate_rounding(self):
        r = engine.work_time(*time_inputs('10','3','100'))
        self.assertEqual(r['net_hourly_rate'], '3.33')
        self.assertEqual(r['cost_equivalent_paid_hours'], '30.00')
        self.assertEqual(engine.work_time(*time_inputs(cost='0'))['cost_equivalent_paid_hours'], '0.00')

    def test_work_time_denominators(self):
        for values in [('0','160','10'), ('100','0','10'), ('100','-1','10'), ('100','160','-1')]:
            with self.subTest(values=values), self.assertRaises(ValueError):
                engine.work_time(*time_inputs(*values))

    def test_work_time_rejects_wrong_measures(self):
        for index, measure in [(0,'gross_earnings'), (1,'actual_hours'), (2,'PPS_HH')]:
            rows = time_inputs()
            rows[index]['measure'] = measure
            with self.subTest(measure=measure), self.assertRaises(ValueError):
                engine.work_time(*rows)

    def test_work_time_context_and_population(self):
        for key, value in [('period','year'), ('basis','household'), ('scenario_id','other'),
                           ('kind','research_observations'), ('currency','EUR')]:
            rows = time_inputs()
            rows[1][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                engine.work_time(*rows)


if __name__ == '__main__':
    unittest.main()
