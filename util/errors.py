# coding=utf-8
def customValueError(k, v, moreDetail='') -> object:
    """
    Simple value error for key, value pairs from order.
    """
    raise ValueError('Incorrect/invalid {} with value {}. '.format(k, v) + moreDetail)


def validateNonZero(k, v):
    """
    Simple function to check all values are greater than zero.
    Error raised if not.
    """
    if int(v)>0:
        return v
    else:
        customValueError(k, v)