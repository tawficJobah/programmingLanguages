#CMPS 3500
#Dice Score Frequency Analysis - www.101computing.net/dice-score-frequency-analysis/
import random

#A function to simulate throwing a 6-sided dice
def throwDice():
  dice = random.randint(1,6)
  dice2 = random.randint(1,6)
  total = dice + dice2
  return total


### Main Code Starts Here...

#Initialise a dictionary to store the frequency (tally count) of each of the 6 dice values
tallyChart = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

#Number of throws
n = 1000000

#Let's start the experiment and repeat it n times! Let's complete our tally chart!
for i in range(0,n):
  score = throwDice()
  tallyChart[score] += 1
  
#Let's display the results:
print(" Dice Value | Frequency | Percentage ")
print("-------------------------------------")
for i in range(2,13):
  frequency = tallyChart[i]
  percentage = round((frequency * 100) / n , 2)
  print("      " + str(i) + "      |    " + str(frequency)+ "    |   " + str(percentage) + "%")