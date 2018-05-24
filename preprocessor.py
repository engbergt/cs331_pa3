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

for ln in lowerNoPuncList: 
    print ln



### Form the vocabulary, make a list of all the unique words in the text file in alphabetical order. ###

### Convert the training AND test data into a set of features based on the vocabulary. ###

### Output the features into files called preprocessed_train.txt & preprocessed_test.txt each w/ the csv vocab at the top plus 'classlabel' ###
