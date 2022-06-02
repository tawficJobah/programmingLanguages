import csv 

def spiralPath():
    data = []
    xdata = []
    #FILENAME = 'matrix1.csv'
    #open the file
    with open('matrix1.csv', mode='r', newline='', encoding='utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    csvfile.close()
    for i in data:
        for j in data[i]:
            xdata.append(j)
            return xdata

    print(data)
    print("--> ")
    print(spiralPath(xdata))
    
def moranNums():
    #FILENAME = 'moran.txt'
    data = []
    #open the file
    with open('moran.txt', mode='r') as txtfile:
        x = txtfile.readline()
        x = x.strip()
        if bool(x):
            print(x + "\t\t", end="")
            moranNums(int(x))
            print("")
        for row in x:
            data.append(row)
    txtfile.close()

def shortestSent():
    FILENAME = 'Fundamental_Concepts_in_PLs.txt'
    data = []
    #open the file
    with open(FILENAME) as txtfile:
        txtreader = txtfile.read()
        for row in txtreader:
            data.append(row)
    txtfile.close()



print("Sprial Path: \n")
print("********************\n")
spiralPath()

print("Moran Numbers: \n")
print("********************\n")
moranNums()

print("shortestSent: \n")
print("********************\n")
shortestSent()
