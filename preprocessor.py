import string

### Import file data ###

with open('myTester.txt') as textFile:
    content = textFile.readlines()

noPuncList = []

for ln in content: 
    noPuncList.append(ln.translate(None, string.punctuation))

for ln in noPuncList: print ln

# for ln in content: print ln

### Remove punctuation & apostrophes ###

### Make all lowercase ###

### Form the vocabulary, make a list of all the unique words in the text file in alphabetical order. ###

### Convert the training AND test data into a set of features based on the vocabulary. ###

### Output the features into files called preprocessed_train.txt & preprocessed_test.txt each w/ the csv vocab at the top plus 'classlabel' ###
