import purchase_recommendation
import pytest

def test_pur_rec_1():
    assert purchase_recommendation.purchase_recommendation("EUR") != ""
    
def test_pur_rec_wrong_currency():
    with pytest.raises(ValueError):
        purchase_recommendation.purchase_recommendation("EUROIA")    
        
def test_pur_rec_wrong_no_currency():
    with pytest.raises(TypeError):
        purchase_recommendation.purchase_recommendation()        