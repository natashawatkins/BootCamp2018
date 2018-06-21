from operate import *
import pytest


def test_operate():
    assert operate(1, 1, '+') == 2
    assert operate(1, 1, '-') == 0
    assert operate(3, 4, '*') == 12
    assert operate(12, 3, '/') == 4
    with pytest.raises(TypeError) as excinfo:
        operate(1, 1, 1)
    assert excinfo.value.args[0] == "oper must be a string"
    with pytest.raises(ZeroDivisionError) as excinfo:
        operate(1, 0, '/')
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo:
        operate(1, 0, 'x')
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"