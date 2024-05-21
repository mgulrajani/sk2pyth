import pytest
import codetobetest as code


@pytest.mark.parametrize("length,expected_area",[(5,25),(3,10),(4,16),(9,81)])
def test_multiple_areas(length,expected_area):
    assert code.Square(length).area() == expected_area
