import pytest
from src.long_responses import *

def test_long_responses_help():
    assert help() != ""
    
def test_long_responses_help_parametr():
    with pytest.raises(TypeError):
        help(0)    
        
def test_long_responses_unknown():
    assert unknown() != ""
    
def test_long_responses_unknown_parametr():  
    with pytest.raises(TypeError):
        unknown(0)          