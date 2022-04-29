switch = True

packageList =[{"Customer Name": "liam     ","Package Name": "Package 4 ", "Pax": 60 , "Cost": 800},
            {"Customer Name": "noah     ","Package Name": "Package 5 ", "Pax": 70 , "Cost": 900},
            {"Customer Name": "oliver   ","Package Name": "Package 6 ", "Pax": 80 , "Cost": 1000},
            {"Customer Name": "elijah   ","1Package Name": "Package 7 ", "Pax": 90 , "Cost": 100},
            {"Customer Name": "william  ","Package Name": "Package 8 ", "Pax": 100, "Cost": 200},
            {"Customer Name": "james    ","Package Name": "Package 9 ", "Pax": 10 , "Cost": 300},
            {"Customer Name": "benjamin ","Package Name": "Package 10", "Pax": 20 , "Cost": 400},
            {"Customer Name": "lucas    ","Package Name": "Package 1 ", "Pax": 30 , "Cost": 500},
            {"Customer Name": "henry    ","Package Name": "Package 2 ", "Pax": 40 , "Cost": 600},
            {"Customer Name": "alexander","Package Name": "Package 3 ", "Pax": 50 , "Cost": 700}]

def display():
    print("Customer Name  Package Name   Pax   Package Cost per Pax")
    print("=========================================================")
    for package in packageList:
        print(*package.values(), sep="      ")
    print("=========================================================")
    

def insertionSort(packageList):
    for i in range(1, len(packageList)):
        key = packageList[i]
        j = i-1
        while j >= 0 and key < packageList[j]["Package Name"] :
                packageList[j + 1]["Package Name"] = packageList[j]["Package Name"]
                j -= 1
        packageList[j + 1]["Package Name"] = key

def bubbleSort(packageList):
    n = len(packageList)
    for i in range(n):
        for j in range(0, n-i-1):
            if packageList[j]['Customer Name'] > packageList[j + 1]['Customer Name']:
                packageList[j], packageList[j+1] = packageList[j+1], packageList[j]

while switch:
    print(" 1. Display all records \n 2. Sort record by Customer Name using Bubble sort \n 3. Sort record by Package Name using Selection sort \n 4. Sort record by Package Cost using Insertion sort \n 5. Search record by Customer Name using Linear Search and update record \n 6. Search record by Package Name using Binary Search and update record \n 7. List records range from $X to $Y. e.g $100-200 \n 0. Exit Application")
    picker = input("Enter a function number: ")
    if picker == "1":
        display()
    elif picker == "2":
        bubbleSort(packageList)
        display()
    elif picker == "3":
        pass
    elif picker == "4":
        insertionSort(packageList)
        display()
    elif picker == "5":
        pass
    elif picker == "6":
        pass
    elif picker == "7":
        pass
    elif picker == "0":
        print("Goodbye.")
        switch = False
    else:
        print("Invalid input, please enter a valid function number.")