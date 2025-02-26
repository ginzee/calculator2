
class Calculator:
    """A basic calculator with standard arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
        
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b
    
class ScientificCalculator(Calculator):
    """A scientific calculator that extends the basic Calculator."""
    
    def power(self, base, exponent):
        """Calculate base raised to the exponent."""
        return base ** exponent
    
    def square_root(self, number):
        """Calculate the square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return number ** 0.5