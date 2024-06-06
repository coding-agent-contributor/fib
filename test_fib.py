import pytest
from fib import fib

def test_fib_zero():
    assert fib(0) == 0

def test_fib_one():
    assert fib(1) == 1
    
def test_fib_negative():
    assert fib(-5) == 0
    
def test_fib_larger():
    assert fib(10) == 55
