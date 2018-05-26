import string

def removePunctuation(arrayOfStrings):
    noPuncList = []
    for ln in arrayOfStrings: noPuncList.append(ln.translate(None, string.punctuation))
    return noPuncList

def lowercaseize(arrayOfStrings):
    lowerCase = []
    for ln in arrayOfStrings:lowerCase.append(ln.lower())
    return lowerCase

def makeListOFWords(arrayOfStrings):
    allWords = []
    for ln in arrayOfStrings:
        for word in ln.split():allWords.append(word)
    return allWords

def uniquify(arrayOfStrings):
    uniqueWords = []
    for word in arrayOfStrings:
        imUnique = True
        for uwrd in uniqueWords:
            if(word == uwrd or word == "0" or word == "1"):
                imUnique = False
        if(imUnique):
            uniqueWords.append(word)
    return uniqueWords

def alphabetize(arrayOfStrings):
    vocabulary = []
    for word in sorted(arrayOfStrings): vocabulary.append(word)
    return vocabulary


### Import file data ###

with open('trainingSet.txt') as textFile:
    trainingSet = textFile.readlines()

with open('testSet.txt') as textFile:
    testSet = textFile.readlines()

with open('myTester.txt') as textFile:
    myTester = textFile.readlines()


### Remove punctuation & apostrophes ###
trainingNoPunc = removePunctuation(trainingSet)
testNoPunc = removePunctuation(testSet)

testerNoPunc = removePunctuation(myTester)  # test

### Make all lowercase ###
trainingLower = lowercaseize(trainingNoPunc)
testLower = lowercaseize(testNoPunc)

testerLower = lowercaseize(testerNoPunc)  # test

### Make a list of all the unique words in the text file ###
traingingWords = makeListOFWords(trainingLower)
trainingUniqueWords = uniquify(traingingWords)

testerWords = makeListOFWords(testerLower)  # test
testerUniqueWords = uniquify(testerWords)  # test

### alphabatize the vocabulary for easier debugging later ###
vocabulary = alphabetize(trainingUniqueWords)

testerVocab = alphabetize(testerUniqueWords) # test

### Convert the training AND test data into a set of features based on the vocabulary. ###


# def sentamentGrabber(review):
#     return int( review.split("\t",1)[1].strip('\n') )
     
# print sentamentGrabber(testerLower[3])


def featurizer(vocab, reviews):
    feature = []
    for review in reviews:
        vector = []
        for word in vocab:
            wordIsInVocab = False
            for wrd in review.split():
                if(word == wrd): wordIsInVocab = True
            vector.append(1) if wordIsInVocab else vector.append(0)
        vector.append(int(review.split("\t",1)[1].strip('\n')))
        feature.append(vector)
    return feature


testFeatures = featurizer(testerVocab, testerLower)
print testFeatures


# myFeature = featurizer(["about", "above", "across", "after", "begin"], ["we love about", "yo there", "across the pond", "whats up"])

# print myFeature

### Output the features into files called preprocessed_train.txt & preprocessed_test.txt each w/ the csv vocab at the top plus 'classlabel' ###
