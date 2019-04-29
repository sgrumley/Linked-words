The file dictionary.txt contains one word per line. Subsets of these words can ordered such that, with the exception of the first word, the second and third letter of each word is identical to the third last and second last of the preceding word. That is, if the sequence of words is held in the list words then words[i - 1][-3:-1] == words [i][1:3]. Words may only be used once within a sequence.  
 
This implementation finds such sequences separately for words of length x which can be specified by passing a command line argument


