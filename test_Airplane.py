# coding=utf-8
import pytest
from Airplane import Airplane

ap = Airplane(1, 1, 1, 1)

def test_Airplane_error_consumption_value():
    """
    Negative consumption error
    """
    with pytest.raises(ValueError, match="Incorrect/invalid consumption with value -10."):
        Airplane(1, 1, -10, 0)

def test_Airplane_errorr_refuel():
    """
    Negative refuel error
    """
    with pytest.raises(ValueError, match="Incorrect/invalid fuel_level with value 0."):
        ap.refuel(0)

def test_Airplane_refuel():
    """
    This is a perfect case!
    Trying to refuel correctly
    """
    ap.refuel(99)
    assert ap.fuel_level==100

def test_Airplane_goto_current_location():
    '''
    This is a perfect case!
    This test is to check what happens if someone tries to move plane to current position
    '''
    assert ap.goto(1,1)
    assert ap.fuel_level==1 #no fuel used!

def test_Airplane_goto_new_location():
    '''
    This is a perfect case!
    New valid location
    '''
    ap1 = Airplane(1, 1, 3, 97)
    assert ap1.goto(2,7)


def test_Airplane_goto_new_location_not_enough_fuel():
    '''
    This is a perfect case!
    New valid location
    '''
    ap2 = Airplane(1, 1, 39, 97)
    assert ap2.goto(999,999)==False

def test_Airplane_goto_incorrect_location():
    """
    Negative initY error
    """
    with pytest.raises(ValueError, match="Incorrect/invalid initY with value -1"):
        ap = Airplane(1, -1, 1, 97)

