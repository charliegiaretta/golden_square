from lib.gratitudes import *

def test_gratitudes_add_pizza():
    gratitudes = Gratitudes()
    gratitudes.add('Pizza')
    assert gratitudes.format() == 'Be grateful for: Pizza'

def test_gratitudes_add_ice_cream():
    gratitudes = Gratitudes()
    gratitudes.add('Pizza')
    gratitudes.add('Ice Cream')
    assert gratitudes.format() == 'Be grateful for: Pizza, Ice Cream'
