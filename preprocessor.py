import string

### Import file data ###

with open('myTester.txt') as textFile:
    content = textFile.readlines()


### Remove punctuation & apostrophes ###

noPuncList = []

for ln in content: 
    noPuncList.append(ln.translate(None, string.punctuation))


### Make all lowercase ###

lowerNoPuncList = []

for ln in noPuncList: 
    lowerNoPuncList.append(ln.lower())


### make a list of all the unique words in the text file ###

allWords = []

for ln in lowerNoPuncList:
    for word in ln.split():
        allWords.append(word)

uniqueWords = []

for word in allWords:
    imUnique = True
    for uwrd in uniqueWords:
        if(word == uwrd or word == "0" or word == "1"):
            imUnique = False
    if(imUnique):
        uniqueWords.append(word)


### alphabeticatize the list for easier debugging later ###

alphabetizedWords = []

for word in sorted(uniqueWords):
    alphabetizedWords.append(word)


### Form the vocabulary ###


### Convert the training AND test data into a set of features based on the vocabulary. ###

### Output the features into files called preprocessed_train.txt & preprocessed_test.txt each w/ the csv vocab at the top plus 'classlabel' ###
