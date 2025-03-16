import pytest
from calculator.calculator import Calculator

def test_calculator():
    calc = Calculator()
    result = calc.evaluate("3 + 5")
    assert result == 8
    result = calc.evaluate("10 / 2")
    assert result == 5.0
    assert calc.get_history().shape[0] == 2

