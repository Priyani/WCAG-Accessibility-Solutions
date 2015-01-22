#! /usr/bin/env python 3.4

import unittest
import fleischKincaid as fk

testTexts = ['''Mary had a little lamb it's fleece was white as snow.''',
             '''the quick brown fox jumps over the lazy dog.''',
             '''supercallifragilistic, is a very peculiar word.''',
             '''The Australian platypus is seemingly a hybrid of 
             a mammal and reptilian creature''',
             '''This sentence, taken as a reading passage unto itself, 
             is being used to prove a point.'''
            ]


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        '''Checks that the word counter can count words.
        '''
        answers = [11, 9, 6, 13, 16]
        for i in range(len(testTexts)):
            left = fk.wordCount(testTexts[i])
            right = answers[i]
            msgOut = "{0} should have {2} words, and the FUT generates {1}"\
                .format(testTexts[i], left, right)
            self.assertEqual(left, right, msg = msgOut)
            
    def test2(self):
        ''' Checks that the syllable counter can count syllables predictably'''
        testTxt = testTexts[0].split()
        answers = [2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1]
        for i in range(len(testTxt)):
            left = fk.syllableCountWord(testTxt[i])
            right = answers[i]
            msgOut = "{0} should have {1} syllables, and the FUT generates {2}"\
                .format(testTxt[i], right, left)
            self.assertEqual(left, right, msg = msgOut)
    
    def test2a(self):
        '''checks that the syllable counter can count syllables in text'''
        answers = [15, 11, 16, 25, 26]
        for i in range(len(testTexts)):
            left = fk.syllableCount(testTexts[i])
            right = answers[i]
            msgOut = "{0} should have {1} syllables, and the FUT generates {2}"\
                .format(testTexts[i], right, left)
            self.assertEqual(left, right, msg = msgOut)        
    def test3(self):
        '''checks that the sentence counter can count sentences'''
        answers = [1, 1, 1, 1, 1]
        for i in range(len(testTexts)):
            left = fk.sentenceCount(testTexts[i])
            right = answers[i]
            msgOut = "{0} should have {1} sentences, and the FUT generates {2}"\
                .format(testTexts[i], right, left)
            self.assertEqual(left, right, msg = msgOut)
    
    def test4(self):
        '''sentence count check for green ham and eggs'''
    
        text = open("ghe.txt","rt").read()
        left = fk.sentenceCount(text)
        right = 127
        msgOut = "'Green ham and eggs' should have {0} sentences, and the FUT generates {1}"\
            .format( right, left)
        self.assertEqual(left, right, msg = msgOut)
    
    def test5(self):
        '''checks the ease ratio against calculated values'''
        answers = [80.306, 94.3, -24.855, 30.948, 53.12]
        for i in range(len(testTexts)):
            left = fk.ease(testTexts[i])
            right = answers[i]
            msgOut = "{0} should have an ease of {1}, and the FUT generates {2}"\
                .format(testTexts[i], right, left)
            self.assertAlmostEqual(left, right, places =3, msg = msgOut)
    
    def test6(self):
        '''ease count check for green ham and eggs'''
    
        text = open("ghe.txt","rt").read()
        left = fk.ease(text)
        right = 97.857
        msgOut = "'Green ham and eggs' should have an ease of {0}, and the FUT generates {1}"\
            .format( right, left)
        self.assertAlmostEqual(left, right, places = 3, msg = msgOut)
    
    def test7(self):
        '''checks the grade level against calculated values'''
        answers = [4.791, 2.342, 18.2167, 12.172, 9.825]
        for i in range(len(testTexts)):
            left = fk.grade(testTexts[i])
            right = answers[i]
            msgOut = "{0} should have an ease of {1}, and the FUT generates {2}"\
                .format(testTexts[i], right, left)
            self.assertAlmostEqual(left, right, places =3, msg = msgOut)
    
    def test8(self):
        '''ease count check for green ham and eggs'''
    
        text = open("ghe.txt","rt").read()
        left = fk.grade(text)
        right = 1.132
        msgOut = "'Green ham and eggs' should have a grade level of {0}, and the FUT generates {1}"\
            .format( right, left)
        self.assertAlmostEqual(left, right, places = 3, msg = msgOut)
if __name__ == '__main__':
    unittest.main(verbosity = 3)