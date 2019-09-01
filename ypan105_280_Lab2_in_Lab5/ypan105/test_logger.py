import unittest     # Import the Python unit testing framework
from logger import Logger       # Our code to test


    
class LoggerTest(unittest.TestCase):
    ''' Unit tests for our logger functions. '''

    
    def test_info(self):
        ''' Tests the info function. '''
        #Arrange
        t = Target()
        a = Logger(t.set)
        a.info("1")
        
        #Act
        #Assert
        self.assertEqual(t.show(),"[INFO] 1","success")
        print("info test finish")
        pass # TODO
    
    def test_error(self):
        ''' Tests the info function. '''
        #Arrange
        t = Target()
        a = Logger(t.set)
        a.error("1")
        
        #Act
        #Assert
        self.assertEqual(t.show(),"[WARNING] 1","success")
        print("error test finish")
        pass # TODO
    

    
class Target():
    def __init__(self,txt = None):
        self.txt = txt
    def set(self,txt):
        self.txt = txt
    def show(self):
        print(self.txt)
        return(self.txt)
    
    # This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()