import codetobetest as code1
import pytest

def test_add():
    result=code1.add(4,4)
    assert result == 9


def test_add_with_strings():
    result=code1.add('hello','world')
    assert result == 'helloworld'

def test_divide():
    result =  code1.divide(2,2)
    assert result == 1


@pytest.mark.xfail(reason="Number cannot be divided by zero")
def test_divide_by_zero():
     result =  code1.divide(2,0)
    

