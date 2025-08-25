import pytest
from app.utils import calculate_bmi, bmi_category

def test_calculate_bmi():
    assert round(calculate_bmi(70, 1.75), 2 == 22.86)
    
def test_bmi_category_underweight():
    assert "Abaixo" in bmi_category(17)
    
def test_bmi_category_normal():
    assert "Peso normal" in bmi_category(22)
    
def test_bmi_category_overweight():
    assert "Sobrepeso" in bmi_category(27)
    
def test_bmi_category_obesity():
    assert "Obesidade" in bmi_category(35)