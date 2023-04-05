import pytest
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series

def test_fibonacci_1():
    actual=fibonacci(0)
    expected=0
    assert expected==actual

def test_fibonacci_2():
    actual=fibonacci(1)
    expected=1
    assert expected==actual    


def test_fibonacci_3():
    actual=fibonacci(2)
    expected=1
    assert expected==actual

def test_fibonacci_4():
    actual=fibonacci(3)
    expected=2
    assert expected==actual

def test_fibonacci_5():
    actual=fibonacci(7)
    expected=13
    assert expected==actual

####################################################


def test_lucas_1():
    actual=lucas(0)
    expected=2
    assert expected==actual

def test_lucas_2():
    actual=lucas(1)
    expected=1
    assert expected==actual    


def test_lucas3():
    actual=lucas(2)
    expected=3
    assert expected==actual

# def test_lucas_4():
#     actual=lucas(3)
#     expected=4
#     assert expected==actual

def test_lucas_5():
    actual=lucas(7)
    expected=29
    assert expected==actual

############################

def test_sum_1():
    actual=sum_series(1)
    expected=1
    assert actual==expected

def test_sum_2():
    actual=sum_series(0,2,1)
    expected=2
    assert expected==actual    

def test_sum_3():
    actual=sum_series(1,2,1)
    expected=1
    assert expected==actual   

def test_sum_4():
    actual=sum_series(3,2,1)
    expected=4
    assert expected==actual       

def test_sum_5():
    actual=sum_series(4,2,1)
    expected=7
    assert expected==actual           

def test_sum_6():
    actual=sum_series(5,2,1)
    expected=11
    assert expected==actual           


def test_sum_7():
    actual=sum_series(7,0,1)
    expected=13
    assert expected==actual          