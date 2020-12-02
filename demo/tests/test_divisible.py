import pytest
from my_first_module.divisible import divisible

def test_divisible():
    assert divisible(10,5) == 2
    assert divisible(5,10) == '5 is not divisible by 10'

