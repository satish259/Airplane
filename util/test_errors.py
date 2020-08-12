# coding=utf-8
import pytest
from utils.errors import customValueError, validateNonZero


def test_custom_value_error():
    with pytest.raises(ValueError, match=r"Incorrect/invalid key with value value. More Error detail."):
        customValueError('key', 'value', 'More Error detail.')

def test_validateNonZero():
    with pytest.raises(ValueError, match=r"Incorrect/invalid key with value -1."):
        validateNonZero('key',-1)