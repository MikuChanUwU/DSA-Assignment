#Royston Loo Yi Shin
#214242Q
#SF1202

import sys

switch = True
switch2 = True

packageList =[{"Customer Name": "liam","Package Name": "bicycle", "Pax":60, "Cost": 800},
            {"Customer Name": "noah","Package Name": "desktop", "Pax":70, "Cost": 900},
            {"Customer Name": "oliver","Package Name": "telephone", "Pax":80, "Cost": 1000},
            {"Customer Name": "elijah","Package Name": "playstation five", "Pax":90, "Cost": 100},
            {"Customer Name": "william","Package Name": "drum", "Pax":100, "Cost": 200},
            {"Customer Name": "james","Package Name": "microphone", "Pax":10, "Cost": 300},
            {"Customer Name": "benjamin","Package Name": "phone", "Pax":20, "Cost": 400},
            {"Customer Name": "lucas","Package Name": "laptop", "Pax":30, "Cost": 500},
            {"Customer Name": "henry","Package Name": "television", "Pax":40, "Cost": 600},
            {"Customer Name": "alexander","Package Name": "speaker", "Pax":50, "Cost": 700}]

def display():
    print("=========================================================")
    print("Customer Name  Package Name   Pax   Package Cost per Pax")
    print("=========================================================")
    for package in packageList:
        print(*package.values(), sep="      ")
    print("=========================================================")

def selectionSort(packageList):
    for i in range(len(packageList)):
        min_idx = i
        for j in range(i+1, len(packageList)):
            if packageList[min_idx]["Package Name"] > packageList[j]["Package Name"]:
                min_idx = j    
        packageList[i], packageList[min_idx] = packageList[min_idx], packageList[i]    

def insertionSort(packageList):
    for i in range(1, len(packageList)):
        key = packageList[i]["Cost"]
        j = i-1
        while j >= 0 and key < packageList[j]["Cost"] :
                packageList[j + 1]["Cost"] = packageList[j]["Cost"]
                j -= 1
        packageList[j + 1]["Cost"] = key

def bucketSort(packageList):
    bucket = []

    # Create empty buckets
    for i in range(len(packageList)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in packageList:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(packageList)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(packageList)):
        for j in range(len(bucket[i])):
            packageList[k] = bucket[i][j]
            k += 1
    return packageList

def bubbleSort(packageList):
    n = len(packageList)
    for i in range(n):
        for j in range(0, n-i-1):
            if packageList[j]['Customer Name'] > packageList[j + 1]['Customer Name']:
                packageList[j], packageList[j+1] = packageList[j+1], packageList[j]

def linearSearch(packageList, n, x):
 
    for i in range(0, n):
        if (packageList[i]["Customer Name"] == x):
            return i
    return -1

def binarySearch(packageList, x):
    packageListCopy = packageList.copy()
    selectionSort(packageListCopy)
    low = 0
    high = len(packageListCopy)-1
    while low <= high:
        mid = (low + high) // 2
        print(low , mid , high)
        if packageListCopy[mid]["Package Name"] == x:
            return mid
        elif packageListCopy[mid]["Package Name"] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def heapify(packageList, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and packageList[largest] < packageList[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and packageList[largest] < packageList[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        packageList[i], packageList[largest] = packageList[largest], packageList[i]  # swap
 
        # Heapify the root.
        heapify(packageList, n, largest)

def heapSort(packageList):
    n = len(packageList)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(packageList, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        packageList[i], packageList[0] = packageList[0], packageList[i]  # swap
        heapify(packageList, i, 0)

while switch:
    print(" 1. Display all records \n 2. Sort record by Customer Name using Bubble sort \n 3. Sort record by Package Name using Selection sort \n 4. Sort record by Package Cost using Insertion sort \n 5. Search record by Customer Name using Linear Search and update record \n 6. Search record by Package Name using Binary Search and update record \n 7. List records range from $X to $Y. e.g $100-200 \n 8. Sort record by Customer Name using Heapsort \n 9. Sort record by Package Cost using Bucket Sort \n 0. Exit Application")
    picker = input("Enter a function number: ")
    if picker == "1":
        display()
    elif picker == "2":
        bubbleSort(packageList)
        display()
    elif picker == "3":
        selectionSort(packageList)
        display()
    elif picker == "4":
        insertionSort(packageList)
        display()
    elif picker == "5":
        search = input("Enter Customer Name: ").lower()
        results = linearSearch(packageList, len(packageList), search)
        if results == -1:
            print("Customer Name not found")
        else:
            print("=========================================================")
            print("Customer Name  Package Name   Pax   Package Cost per Pax")
            print("=========================================================")
            print(*packageList[results].values(), sep="      ")
            print("=========================================================")
            update = input("Do you want to update the record? (Y/N): ").lower()
            while True:
                if update == "y":
                    packageList[results]["Customer Name"] = input("Enter Customer Name: ").lower()
                    packageList[results]["Package Name"] = input("Enter Package Name: ").lower()
                    while True:
                        try:
                            packageList[results]["Pax"] = int(input("Enter Pax: "))
                            if packageList[results]["Pax"] <= 0:
                                print("Pax must be greater than 0")
                            else:
                                break
                        except ValueError:
                            print("Please enter a number")
                    while True:
                        try:
                            packageList[results]["Cost"] = int(input("Enter Cost: "))
                            if packageList[results]["Cost"] <= 0:
                                print("Cost must be greater than 0")
                            else:
                                break
                        except ValueError:
                            print("Please enter a number")
                    print("Record updated")
                    break
                elif update == "n":
                    print("Record not updated")
                    break
                else:
                    print("Invalid input, please try again. Y/N?")

    elif picker == "6":
        search = input("Enter Package Name: ").lower()
        results = binarySearch(packageList, search)
        if results == -1:
            print("Package Name not found")
        else:
            print("=========================================================")
            print("Customer Name  Package Name   Pax   Package Cost per Pax")
            print("=========================================================")
            print(*packageList[results].values(), sep="      ")
            print("=========================================================")
            update = input("Do you want to update the record? (Y/N): ").lower()
            while True:
                if update == "y":
                    packageList[results]["Customer Name"] = input("Enter Customer Name: ").lower()
                    packageList[results]["Package Name"] = input("Enter Package Name: ").lower()
                    while True:
                        try:
                            packageList[results]["Pax"] = int(input("Enter Pax: "))
                            if packageList[results]["Pax"] <= 0:
                                print("Pax must be greater than 0")
                            else:
                                break
                        except ValueError:
                            print("Please enter a number")
                    while True:
                        try:
                            packageList[results]["Cost"] = int(input("Enter Cost: "))
                            if packageList[results]["Cost"] <= 0:
                                print("Cost must be greater than 0")
                            else:
                                break
                        except ValueError:
                            print("Please enter a number")
                    print("Record updated")
                    break
                elif update == "n":
                    print("Record not updated")
                    break
                else:
                    print("Invalid input, please try again. Y/N?")
    elif picker == "7":
        while True:
            try:
                range1 = int(input("Enter minimum cost: "))
                if range1 <= 0:
                    print("Number must be greater than 0")
                else:
                    break
            except ValueError:
                print("Please enter a number")
        while True:
            try:
                range2 = int(input("Enter maximum cost: "))
                if range2 <= 0:
                    print("Number must be greater than 0")
                else:
                    break
            except ValueError:
                print("Please enter a number")
        print("Customer Name  Package Name   Pax   Package Cost per Pax")
        print("=========================================================")
        for i in range(len(packageList)):
            if packageList[i]["Cost"] >= range1 and packageList[i]["Cost"] <= range2:
                print(*packageList[i].values(), sep="      ")
        print("=========================================================")
    elif picker == "8":
        heapSort(packageList)
        display()
    elif picker == "9":
        bucketSort(packageList)
        display()
    elif picker == "0":
        print("Goodbye.")
        switch = False
    else:
        print("Invalid input, please enter a valid function number.")