import copy, random, time, sys

# Read in all words of given word length
def readWordsFromFile(wordLength):
    pos1 = wordLength - 1
    pos2 = wordLength - 3
    originalWords = []
    file = open("testfile.txt", "r")

    # read words from file and append if the length matches
    for line in file:
        if len(line) == wordLength + 1:
            originalWords.append(line[0:wordLength])
    return(originalWords)

# Sort words into a dictionary where the words are grouped by characters at the passed in positions
def sortWordsIntoDictionaries(words, pos1, pos2):
    splitDict = {}
    # create dictionary with positional characters as keys and populate lists of corresponding words as values
    for i in range(len(words)):
        key = words[i][pos2:pos1]
        # if no keys added let, create a key and value of list and append the first word
        if len(splitDict) == 0:
            splitDict.setdefault(key, []).append(words[i])

        # else if the key already exists, append it to the list
        elif key in splitDict:
            splitDict[key].append(words[i])

        # else, create a key and value of list and append the first word
        else:
            splitDict.setdefault(key, []).append(words[i])
    return splitDict

def moveCharToBePopped(startDict, currentNode):
    #get the 2nd and 3rd chars of current word
    firstChar = currentNode[1:3]
    leng = len(startDict[firstChar]) - 1
    # retrieve the index of the current word
    i = startDict[firstChar].index(currentNode)
    #switch current word to the last position of the list
    startDict[firstChar][i],  startDict[firstChar][leng] =  startDict[firstChar][leng],  startDict[firstChar][i]
    #remove the word
    startDict[currentNode[1:3]].pop()

def nextBestNode(endCharsOfCurrentNode, startDict):
    pos1 = wordLength - 1
    pos2 = wordLength - 3
    evalNodeMax = 0
    num = 0
    #iterate through list of possible next words
    for evalNode in startDict[endCharsOfCurrentNode]:
        #evalNode = potensial next word, evalChar = lastChars of evalNode, evalNodeLen = length of potensial grandchild nodes
        evalChar = evalNode[pos2:pos1]
        #if eval char is a valid key and has the most potensial grandchildren nodes
        if evalChar in startDict and len(startDict[evalChar]) >= evalNodeMax:
            #adjust the new max grandchildren and save the potensial word
            evalNodeMax = len(startDict[evalChar])
            nextNode = evalNode
    # if nextNode has been assigned a next node, continue
    try:
        nextNode
    except NameError:
        # this will be executed if no optimal solution was found e.g. evalChar not in startDict
        # else assign nextNode to any next node before reference
        nextNode = startDict[endCharsOfCurrentNode].pop()
    # delete the word from the dictionary to avoid duplicates
    else:
        moveCharToBePopped(startDict, nextNode )
    #return next word
    return nextNode


def createSequence(startDict, endDict, currentNode):
    currentSequence = []
    maxLengthSequence = []
    pos1 = wordLength - 1
    pos2 = wordLength - 3

    #iterate through nodes until sequence length is less than 1 and search is empty
    while 1:
        endCharsOfCurrentNode = currentNode[pos2:pos1]
        """ If reaches the end of the sequence pop the last node off and try another path """
        # If there is no corresponding key and nothing in the list to backtrack,
        if endCharsOfCurrentNode not in startDict:
            # if the current sequence is greater than 1
            if len(currentSequence) > 1:
                # pop the last node off the sequence list and make it the current node (Go back a node)
                currentNode = currentSequence.pop()
                endCharsOfCurrentNode = currentNode[pos2:pos1]
            else:
                # else break as it was a bad staring word
                break

        # while there is no values in the list for the next node and there is nothing in the list to backtrack
        while len(startDict[endCharsOfCurrentNode]) == 0:
            # if the current sequence is greater than 1
            if len(currentSequence) > 1:
                # if this is the longest sequence recorded,
                if len(currentSequence) > len(maxLengthSequence):
                    # copy list to keep track of longest list
                    maxLengthSequence = copy.deepcopy(currentSequence)
                # else pop the last node off the sequence list and make it the current node (Go back a node)
                currentNode = currentSequence.pop()
                endCharsOfCurrentNode = currentNode[pos2:pos1]
            else:
                # break it was either a bad search or nothing left to search
                break

        """ if a next node is available, make the move"""
        # if corresponding characters is a key in the dictionary and the key has value in the list
        if endCharsOfCurrentNode in startDict and len(startDict[endCharsOfCurrentNode]) != 0:
            # add current node to sequence list and move to next node
            nextNode = nextBestNode(endCharsOfCurrentNode, startDict)
            currentSequence.append(currentNode)
            currentNode = nextNode
        else:
            # else there was no move available, break
            break
    # return the longest sequence recorded
    return maxLengthSequence

#Find the key with the biggest list
def startValues(startDict, endDict):
    maxLen = 0
    keyTerm = "beg"
    # loop through each key and find the largest list
    # iterate through endDict as it is the key that represents possible next node
    for key in endDict.keys():
        if len(endDict[key]) > maxLen:
            maxLen = len(endDict[key])
            keyTerm = key
    return endDict[keyTerm].pop()

def validation(sequence):
    lastLetters = None

    for word in sequence:
        if(lastLetters is None): lastLetters = (word[-3], word[-2])
        else:
            if(lastLetters != (word[1], word[2])): return False
            lastLetters = (word[-3], word[-2])

    return len(sequence) == len(set(sequence))

""" main """
# initiate values
start = time.process_time()
wordLength = int(sys.argv[1])
pos1 = wordLength - 1
pos2 = wordLength - 3
words = readWordsFromFile(wordLength)
startDict = sortWordsIntoDictionaries(words, 3, 1)
endDict = sortWordsIntoDictionaries(words, pos1, pos2)
startingWord = startValues(startDict, endDict)
# record the time at the start of the search
algoStart = time.process_time()
# find longest sequence length
currentSeq = createSequence(startDict, endDict, startingWord)
# record times for whole program and search
algoTime = time.process_time() - algoStart
timeTaken = time.process_time() - start
#print results
#print(validation(currentSeq))
#print( algoTime, " time taken")
print(len(currentSeq), " total words found in sequence")
print(timeTaken, "total time")
