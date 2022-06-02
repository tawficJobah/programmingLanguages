# course: cmps3500
# date: 12/15/2021
# username: tjobah
# name: Tawfic Jobah
# description: Final Exam
import random
import csv

#converts a list to a string
def listToString(s):   
    str1 = ""   
    for ele in s: 
        str1 += ele  
    return str1 

def spiralPath(lst):
    rStart = 0
    rEnd = len(lst)
    cStart = 0
    cEnd = len(lst[0])
    spiralResults = []
    while (rStart < rEnd and cStart < cEnd):
        for i in range(cStart, cEnd):
            spiralResults.append(lst[rStart][i])
        rStart += 1
        for i in range(rStart, rEnd):
            spiralResults.append(lst[i][cEnd - 1])
        cEnd -= 1
        if (rStart < rEnd):
            for i in range(cEnd - 1, (cStart - 1), -1):
                spiralResults.append(lst[rEnd - 1][i])
            rEnd -= 1
        if (cStart < cEnd):
            for i in range(rEnd - 1, rStart - 1, -1):
                spiralResults.append(lst[i][cStart])
            cStart += 1
    return spiralResults

def sum(lst):
    total = 0
    for number in lst:
        total += int(number)
    return total

def moran(lst):
    total = 0
    for number in str(lst):
        total += int(number)

    if( lst % total != 0):
        return "Neither"
    dividend = int(lst / total)

    for i in range(2, dividend):
        if dividend % i == 0: 
            return "H" 

    return "M"

def shortest_words(sentence):
    words = sentence.split()
    result = []
    for word in words:
        word = word.lower()
        if len(result) == 0:
            result.append(word)
        else:
            if word not in result and word.isalpha() != False:
                if len(word) == len(result[0]):
                    result.append(word)
                elif len(word) < len(result[0]):
                    result = [word]
    result.sort()
    return result
#A function to simulate throwing a 6-sided dice
def throwDice():
  dice = random.randint(1,6)
  dice2 = random.randint(1,6)
  total = dice + dice2
  return total

def readFile(fileName):
    with open(fileName,encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = []
        for row in csv_reader:
            rows.append(row)
    return rows
### Main Code Starts Here...

#reads in the matrix1.csv and calls the function to spiral out the ouput
print()
moranNumbers = readFile('matrix1.csv')
spiralResults = spiralPath(moranNumbers)
print("The Spiaral Path of matrix1.csv is: " ,spiralResults)


#reads sentences into a list
sentence = []
with open('Fundamental_Concepts_in_PLs.txt', encoding='utf8') as f:
    reader = csv.reader(f,delimiter='.')
    #for line in f:
    for line in reader:
        sentence.append((listToString(line).strip()))

moranNumbers = []
with open('moran.txt', encoding='utf8') as f:
    reader = csv.reader(f)
    #for line in f:
    for line in reader:
        moranNumbers.append(int(listToString(line)))

print("Testing all numbers in moran.txt")
print("     Numbers (n)                  Is n a Moran Number?")
print("    ==============          ====================")
for num in moranNumbers:
    temp = (moran(num))
    print(f"{num}                             {temp}")

#calls function for shortest word and formats table
print("Finding the shoertest word in each sentence of undamental_Concepts_in_PLs.txt")
print("       Sentence                 Shortest word")
print("    ==============          ====================")
for sent in sentence:
    shortestWordResults = shortest_words(listToString(sent))
    if sent:
        print(f"{sent}           {shortestWordResults}")

#Initialise a dictionary to store the frequency (tally count) of each of the 6 dice values
tallyChart = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

#Number of throws
n = 1000000

#Let's start the experiment and repeat it n times! Let's complete our tally chart!
for i in range(0,n):
  score = throwDice()
  tallyChart[score] += 1
  
#Let's display the results:
print()
print("Two Dice experiment:")
print("******************")
print()
print(" Dice Value | Frequency | Percentage ")
print("-------------------------------------")
for i in range(2,13):
  frequency = tallyChart[i]
  percentage = round((frequency * 100) / n , 2)
  print("      " + str(i) + "      |    " + str(frequency)+ "    |   " + str(percentage) + "%")

