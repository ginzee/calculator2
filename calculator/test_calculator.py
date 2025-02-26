import pytest
from calculator import Calculator, ScientificCalculator

class TestCalculator:
    """Tests for the Calculator class."""
    
    def test_add(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0
    
    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(1, 1) == 0
        assert calc.subtract(0, 5) == -5

class TestScientificCalculator:
    """Tests for the ScientificCalculator class."""
    
    def test_power(self):
        calc = ScientificCalculator()
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1
        assert calc.power(2, -1) == 0.5
    
    def test_square_root(self):
        calc = ScientificCalculator()
        assert calc.square_root(9) == 3
        assert calc.square_root(0) == 0
        assert calc.square_root(2) == pytest.approx(1.4142, rel=1e-4)