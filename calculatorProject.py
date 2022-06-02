   # course: cmps3500
   # CLASS Project
   # PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR
   # date: 09/10/09
   # Student 1: Tawfic Jobah
   # Student 2: Edgar Rosales
   # Student 3: Dylan Anzaldo
   # description: Implementation of a statistics summary Calculator


#sorting algorithm from ----------------
#https://stackabuse.com/sorting-algorithms-in-python/
import csv
import statistics
import math
import collections

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list
def merge_sort(nums):
    # If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each half
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)
#checks to see if the value can be converted to float from string
def is_number(temp):
    try:
        float(temp)
        return True
    except ValueError:
        return False
# function to get unique values
def unique(list1):
    # initialize a null list
    unique_list = []     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return len(unique_list)
# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)
#Function to get the median of the list
def Median(lst):
    lenOfList = len(lst)
    #lst.sort()
    temp = lst #bubble_sort(lst)
    if lenOfList % 2 == 0:
        median1 = temp[lenOfList//2]
        median2 = temp[lenOfList//2 - 1]
        median = (median1 + median2)/2
        return median
    else:
        median = temp[lenOfList//2]
        return median
#function to return the percentile of the list
def percentile(data, perc: int):
    #temp = list(data)
    size = len(data)
    #bubble_sort(data)
    return sorted(data)[int(math.ceil((size * perc) / 100)) - 1]
def mode(data):
    frequency={}
    for number in data:
        frequency.setdefault(number,0)
        frequency[number]+=1
    highestFreq = max(frequency.values())
    highestFreqLst=[]
    for number, freq in frequency.items():
        if freq == highestFreq:
            highestFreqLst.append(number)
    return highestFreq
def standardD(data):
    mean = Average(data)   # mean
    var  = sum(pow(x-mean,2) for x in data) / len(data)  # variance
    std  = math.sqrt(var)  # standard deviation
    return std
def variance(lst):
    avg = Average(lst)
    var = sum((x-avg)**2 for x in lst) / len(lst)
    return var
# Pass a list to this function to check for maximum number
def max_check(x):
  max_val = x[0] 
  for check in x: 
    if check > max_val: 
      max_val = check 
  return max_val
# Pass a list to this function to check for minimum number
def min_check(x):
  min_val = x[0] 
  for check in x: 
    if check < min_val: 
      min_val = check 
  return min_val
#driver function
def most(lst):
    data = collections.Counter(lst)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(lst):
        return 0
    else:
        return mode_val


fileName = input("Please enter the file name: ")

with open(fileName, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    headings = next(spamreader)
    #checks to see if the file is empty
    if(len(headings)):
        print()
    else:
        raise ValueError('---File is empty---')
    rows = []
    for row in spamreader:
        temp = []
        for column in range(0, len(row)):
            if(is_number(row[column])):
                temp.append(float(row[column]))
        rows.append(temp)

#finds the max length of rows
maxRows = 0
for row in rows:
    if(maxRows < len(row)):
        maxRows = len(row)
#deletes rows that doesnt have all the data
data = []
for row in rows:
    if(len(row) == maxRows):
        data.append(row)

#check to make sure that all lists are the same size
if len(set(map(len, data))) not in (0, 1):
    raise ValueError('not all lists have same length!')       


#transposes the matrix so columns and rows are flipped
t_matrix = zip(*data)
searchT_matrix = zip(*data)

##########################################################
####################Search function#######################
print("--Input q to quit the search function--")
userinput = 0
while userinput != 'q':
    print("--------------Search Function-------------------")
    userinput = input("Please enter Number to search for: ")
    userinputC = input("Please enter The column number you would like to search in: ")
    searchT_matrix = zip(*data)
    if(userinput != 'q'):
        rowNumber = 0
        presentNumber = 0
        try:
            for column in searchT_matrix:
                for row in column:
                    if(row == float(userinput)):
                        presentNumber +=1
                        print(f'\t {userinput} is present in column: {userinputC} row: {rowNumber}.')    
                    rowNumber += 1
            print("-----------------------------------------------------------------")
            print(f'\t {userinput} is present {presentNumber} times in column: {userinputC}.')
        except:
            print("---The Inputs must be numerical Data---")
################################################################
count = []
uniq = []
mean = []
med = []
mode = []
standDeviation = []
var = []
p20 = []
p40 = []
p50 = []
p60 = []
p80 = []
smallest = []
biggest = []
for row in t_matrix:
    #Merge_Sort the row before calculations 
    temp = []
    temp = merge_sort(row)

    count.append(len(temp))
    uniq.append(unique(temp))
    mean.append(Average(temp))
    med.append(Median(temp))
    mode.append(statistics.mode(row))
    standDeviation.append(standardD(row))
    var.append(variance(temp))
    p20.append(percentile(temp,20))
    p40.append(percentile(temp,40))
    p50.append(percentile(temp,50))
    p60.append(percentile(temp,60))
    p80.append(percentile(temp,80))
    smallest.append(min_check(temp))
    biggest.append(max_check(temp))
#print("Descriptor     [Column A, Column B]")
print("**-----------------------------------------------------**")
print("Count         ", count) 
print("Unique        ", uniq)
print("Mean          ", mean)
print("Median        ", med)
print("Mode          ", mode)
print("SD            ", standDeviation)
print("Variance      ", var)
print("Minimum       ", smallest)
print("P20           ", p20)
print("P40           ", p40)
print("P50           ", p50)
print("P60           ", p60)
print("P80           ", p80)
print("Maximum       ", biggest)