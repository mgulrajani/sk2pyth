import math
import codetobetest as code

class TestCircle:
    def setup_method(self,method):
        print(f"Setting up test for {method}")
        self.circle =code.Circle(3)

    def teardown_method(self,method):
         print(f"Tearingdown  {method}")
         del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius **2


    def test_perimeter(self):
        actual =  self.circle.perimeter()
        expected = 2*math.pi*self.circle.radius
        assert actual ==  expected

 
 