import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        #Arrange
        x = 1
        y = 2
        a = maths.add(x,y)
        #Act
        #Assert
        self.assertEqual(a,x+y,"success")
        print("add test finish")
        pass # TODO
    
    def test_add1(self):
        ''' Tests the add function. '''
        #Arrange
        x = 10
        y = 2
        n = 16
        a = maths.add(x,y,n)
        #Act
        #Assert
        self.assertEqual(a,"C","success")
        print("add test 1 finish")
        pass # TODO

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        #Arrange
        l = 5
        b = maths.fibonacci(l)
        #Act
        #Assert
        self.assertEqual(b,5)
        print("fibonacci test finish")
        pass # TODO


    def test_conv0(self):
        ''' Tests the convert_base function. '''
        #Arrange
        num = 10
        n = 5
        c = maths.convert_base(num, n)
        #Act
        #Assert
        self.assertEqual(c,"20")
        print("convert_base test 0 finish")
        pass # TODO

    def test_conv1(self):
        ''' Tests the convert_base function. '''
        #Arrange
        num = 15
        n = 16
        c = maths.convert_base(num, n)
        #Act
        #Assert
        self.assertEqual(c,"F")
        print("convert_base test 1 finish")
        pass # TODO
    
    def test_factorial(self):
        num = 3
        self.assertEqual(num,6)
        
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
