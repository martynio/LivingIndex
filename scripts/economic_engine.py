"""LI-005C research/simulation engine. Never approves production inputs."""
from decimal import Decimal, localcontext, ROUND_HALF_UP
import re

from economic_research import DIVISIONS, normalize

SCHEMA_VERSION = '1.0.0'
CURRENCIES = {'PL': 'PLN', 'NL': 'EUR'}
CONTEXT = ('scenario_id', 'country', 'year', 'currency', 'period', 'basis', 'population')
NUMBER = re.compile(r'-?[0-9]{1,12}(?:\.[0-9]{1,6})?')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def amount(value):
    require(isinstance(value, str) and NUMBER.fullmatch(value), 'Expected bounded decimal string')
    return Decimal(value)


def rounded(value):
    return format(value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), 'f')


def result(mode, kind, **fields):
    return {'schema_version': SCHEMA_VERSION, 'mode': mode, 'kind': kind,
            'production_eligible': False, **fields}


def matched(rows, measures, bases):
    """Validate explicitly hypothetical inputs. Alignment is an assumption, not evidence."""
    require(len(rows) == len(measures), 'Wrong number of inputs')
    for row, measure in zip(rows, measures):
        require(isinstance(row, dict), 'Expected input object')
        require(set(row) == set(CONTEXT) | {'kind', 'measure', 'value'}, 'Unexpected/missing input field')
        require(row['kind'] == 'hypothetical', 'Only hypothetical monetary/time inputs enabled')
        require(row['measure'] == measure, 'Wrong measure')
        require(isinstance(row['country'], str) and row['country'] in CURRENCIES, 'Unsupported country')
        require(row['currency'] == CURRENCIES[row['country']], 'Wrong national currency')
        require(type(row['year']) is int and 1980 <= row['year'] <= 2100, 'Invalid year')
        require(row['period'] in ('month', 'year'), 'Unsupported period')
        require(row['basis'] in bases, 'Wrong population basis')
        for key in ('scenario_id', 'population'):
            require(isinstance(row[key], str) and bool(row[key].strip()), 'Missing scenario definition')
        require(all(row[k] == rows[0][k] for k in CONTEXT), 'Incompatible scenario context')
    context = {k: rows[0][k] for k in CONTEXT}
    return context, [amount(row['value']) for row in rows]


def national_budget(income, expenditure):
    """Hypothetical cash balance only; not statistical savings or observed household income."""
    context, (inc, exp) = matched((income, expenditure),
                                ('cash_disposable_income', 'cash_total_expenditure'),
                                ('person', 'household'))
    require(inc >= 0 and exp >= 0, 'Negative income/expenditure unsupported')
    with localcontext() as ctx:
        ctx.prec = 50
        return result('national_budget', 'hypothetical', context=context,
                      income=format(inc, 'f'), expenditure=format(exp, 'f'),
                      cash_balance=format(inc-exp, 'f'),
                      expenditure_share_percent=rounded(exp*100/inc) if inc else None)


def pps_comparison(raw_report, report_sha256, category):
    """Research-only same-division HBS pair, revalidated from the report bytes."""
    require(category in DIVISIONS, 'Expected CP01-CP12; no total')
    data = normalize(raw_report, report_sha256)
    rows = {row['country']: row for row in data['observations'] if row['category'] == category}
    require(set(rows) == {'PL', 'NL'}, 'Category absent from report')
    missing = any(row['value'] is None for row in rows.values())
    flagged = any(row['source_flag'] is not None for row in rows.values())
    return result('pps_comparison', 'research_observations', category=category, year=2020,
                  source_id=data['source_id'], dataset=data['dataset'], unit=data['unit'],
                  population=data['population'], frequency=data['frequency'],
                  statistic=data['statistic'], provenance=data['provenance'], review=data['review'],
                  observations=[rows['PL'], rows['NL']],
                  pair_status='missing' if missing else 'flagged' if flagged else 'review_required')


def work_time(net_earnings, paid_hours, cost):
    """Hypothetical matched worker: equivalent hours, not observed working time."""
    context, (net, hours, price) = matched((net_earnings, paid_hours, cost),
                                        ('net_employment_earnings', 'paid_hours', 'cash_cost'),
                                        ('worker',))
    require(net > 0 and hours > 0 and price >= 0, 'Nonpositive denominator or negative cost')
    with localcontext() as ctx:
        ctx.prec = 50
        return result('work_time', 'hypothetical', context=context,
                      net_earnings=format(net, 'f'), paid_hours=format(hours, 'f'),
                      cost=format(price, 'f'),
                      net_hourly_rate=rounded(net/hours),
                      cost_equivalent_paid_hours=rounded(price*hours/net))
