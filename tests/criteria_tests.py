import unittest
from geoportalvalid.criteria import url_resolves

class CriteriaTests(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testSpecificUrl(self):
        testThisUrl = "http://resources.usgin.org/uri-gin/kgs/welllog/R00129772P004/col/"
        anticipatedResult = True
        response = url_resolves(testThisUrl)
        
        self.assertEqual(response, anticipatedResult, "URL did not resolve like you thought it would: " + str(response))
        
    