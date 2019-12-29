# Linked Words

Linked is an assignment from the course Computing Algorithms

## Problem Description
The file dictionary.txt contains one word per line. Subsets of these words can ordered such that, with the exception of the first word, the second and third letter of each word is identical to the third last and second last of the preceding word. That is, if the sequence of words is held in the list words then words[i - 1][-3:-1] == words [i][1:3]. Words may only be used once within a sequence.


## Input Format

When running linked_words it accepts one parameter specifying word length

```bash
python linked_words.py 5
```
## Output Format
Result:

```
2966 total words found in sequence
0.375 total time
```

## Design
This uses Depth First Search with backtracking to find the best path

## How To Run
Use python 3 to run the main.py

The program will run from input.txt
