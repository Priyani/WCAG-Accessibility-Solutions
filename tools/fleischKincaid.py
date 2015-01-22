#! /usr/bin.env python 3.4

def wordCount(text):
    '''Finds the number of words in a text from the spaces inbetween the words
    Returns an integer'''
    spaces = len(text.split())
    if spaces == 0:
        spaces =1
    return (spaces)
    
    
def syllableCountWord(word):
    '''finds the number of syllables in a given word.  
    Returns an integer'''
    word = word.lower()
    count = 0
    vowels = "a e i o u y".split()
    i = 0
    while i < len(word):
        if word[i] in vowels:
            count += 1
            try:
                nextLetter = word[i+1]
                if nextLetter in vowels:
                    i += 1 #to skip next vowel (adds 1 afterwards as well)
            except IndexError:
                pass #silences index error caused by vowels near end of words
        i += 1
    return (count)

def syllableCount(text):
    '''analyses whole text and returns syllables'''
    syllables = 0
    for word in text.split():
        syllables += syllableCountWord(word)
    return (syllables)
    
def sentenceCount(text):
    '''finds the number of sentences in a given string of text.
    Returns an Integer'''
    sentenceDelimiters = ['.', '!', '?']
    try:
        if text[-1] not in sentenceDelimiters:
            text = text +"."
        count = 0
        for token in sentenceDelimiters:
            count += text.count(token)
        return (count)
    except Exception as e:
        print (e)
        return (1)#return 1 as this will be a division next
    
def getComponents(text):
    '''gets the component ratios for calculating ease, and grade level,
    returns a tuple of (wordSentenceRatio, syllableWordRatio)'''
    sentences = sentenceCount(text)
    words = wordCount(text)
    syllables = syllableCount(text)
    wordSentenceRatio = float(words) / float(sentences)
    syllableWordRatio = float(syllables)/float(words)
    return (wordSentenceRatio, syllableWordRatio)
    
def ease(text):
    '''the Flesch-Kincaid (FK) reading ease is the ease by which a passage of text 
    can be read.
    Lower Numbers mark easier Passages.  
    
    a score of 90-100 can be easily understood by the average 11 yr old,
    A score of 60-70 should be easily understood by a 13-15 yr old student
    A score of below 30 indicates a university graduate
    Returns as a float
    '''
    wordSentenceRatio, syllableWordRatio = getComponents(text)
    score = 206.835
    wordSentenceRatio *= 1.015
    syllableWordRatio *= 84.6
    score -= wordSentenceRatio
    score -= syllableWordRatio
    return (score)
    
def grade(text):
    '''from a given piece of text 
    returns the flesch-kincaid reading level of the text as a float'''
    wordSentenceRatio, syllableWordRatio = getComponents(text)
    score = -15.59
    wordSentenceRatio *= 0.39
    syllableWordRatio *= 11.8
    score += wordSentenceRatio
    score += syllableWordRatio
    return (score)