import codetobetest as code
import pytest

@pytest.fixture
def my_rectangle():
    return code.Rectangle(4,5)


@pytest.mark.skip(reason="this feature is under maintenance")
def test_area(my_rectangle):
    assert my_rectangle.area() == 20


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() ==18

