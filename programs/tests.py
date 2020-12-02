def test_dice():         #make sure to save the file the same name 
    assert dice()>=1 and dice()<=6
    answer = dice()
    assert answer <=6



import pytest 
from my_first_module.divisible import divisible 

def test_divisible():
    assert divisible(10,5) == 2
    assert divisible(5,10) == "5 is not divisible by 10"

    