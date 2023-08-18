"""
Test for else-if-used
"""


def ok0():
    """Should not trigger on elif"""
    pass


def ok1():
    """If the orelse has more than 1 item in it, shouldn't trigger"""
    pass


def ok2():
    """If the orelse has more than 1 item in it, shouldn't trigger"""
    pass


def not_ok0():
    pass


def not_ok1():
    pass


# Regression test for https://github.com/apache/airflow/blob/f1e1cdcc3b2826e68ba133f350300b5065bbca33/airflow/models/dag.py#L1737
def not_ok2():
    print(1)

