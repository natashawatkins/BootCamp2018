from month_length import *


def test_month():
    assert month_length('September') == 30
    assert month_length('January') == 31
    assert month_length('February') == 28
    assert month_length('February', leap_year=True) == 29
    assert month_length('') == None