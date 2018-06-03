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

def featureFileize(vocab, feature, name):
    f = open(name,"w+")
    for idx, word in enumerate(vocab):
        f.write(word + ",")
    f.write("classlabel \n")
    for each in feature:
        for idx, num in enumerate(each):
            f.write(str(num))
            f.write(",") if idx != len(each)-1 else f.write("")
        f.write("\n")
    f.close()

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
trainingFeatures = featurizer(vocabulary, trainingLower)
testFeatures = featurizer(vocabulary, testLower)

testerFeatures = featurizer(testerVocab, testerLower)  # test

### Output the features into files called preprocessed_train.txt & preprocessed_test.txt each w/ the csv vocab at the top plus 'classlabel' ###
featureFileize(vocabulary, trainingFeatures, "preprocessed_train.txt")
featureFileize(vocabulary, testFeatures, "preprocessed_test.txt")

featureFileize(testerVocab, testerFeatures, "tester.txt")  # test


##############################################
############ Classification Step #############
##############################################

print testerFeatures

### Train: Learn parameters used by the classifier from the training data. ###

# P(CD = false) = (# recs in training data w/ CD = false) / (# of records in training data)
# P(CD = true) = (# recs in training data w/ CD = true) / (# of records in training data)

# Get 4 Probs. for each feature (attribute): 1) ff, ft, tf, tt.. e.g. ff = (# of records w/ Feature = false & CD = false) / (# of records w/ CD = false)

# Inference: alpha * P(CD) * P(feature1|CD) * P(feature2|CD) * ... * P(featureN|CD)

### Test: Classify the data in the testSet.txt data file. ###

# Predict: compare the inference stuff with CD = true to CD = false. The larger of the two is the prediction for CD. May ignore alpha.

### Compare the predicted class label of each sentence in the test data to the actual class label (# correct / total predictions) ###

### Output the accuracy of the naive Bayes classifier ###