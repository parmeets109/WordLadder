import unittest     #importing Unittest library for testing
import wordladder   #importing wordladder.py file in the test file

class TestWordLadder(unittest.TestCase):           #Defining the test class which will contain all the test functions

    def test_same(self):                    #this function will test the function same.
        result=wordladder.same("hit","cog")        #the test function will take these two values and test the function.
        self.assertEqual(result,3)                  #Assert function s a debugging aid that tests the function.
                                                    # Here, it will check whether the value in result is equal to the specified value or not.

    def test_build(self):       #this function will build the test function
        list=[]
        list+=wordladder.build("bead",wordladder.words,wordladder.seen,list)
        self.assertEqual(list,["bead","dead","head","lead","mead","read",])

    def test_checkStart(self):    #This function tests for the start word
        result = wordladder.startWordCheck("hey")
        self.assertEqual(result,"hey")

    def test_checkTarget(self):             #This function tests for the target word
        result = wordladder.targetWordCheck("bye")
        self.assertEqual(result, "bye")

    def test_checkMustWord(self):           #This function tests the must word
        result = wordladder.MustWordCheck("")
        self.assertEqual(result, "")

    def test_blacklist(self):           #this function tests the blaclist code
        result = wordladder.blacklisted("hot,pot")
        self.assertEqual(result,["hot","pot"])

    def test_path(self):                #this function tests the path of the output
        result = wordladder.pathSelection("s")
        self.assertTrue(result)
        result = wordladder.pathSelection("l")
        self.assertFalse(result)

    def test_find(self):           # This function tests the main execution
        result1=wordladder.startWordCheck("far")
        result2=wordladder.targetWordCheck("bar")
        result3=wordladder.pathSelection("l")
        result4=wordladder.pathSelection("s")
        self.assertEqual(True,wordladder.find(result1,wordladder.words,wordladder.seen,result2,result3))
        self.assertEqual(True,wordladder.find(result1, wordladder.words, wordladder.seen, result2, result4))

