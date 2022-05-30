#Royston Loo Yi Shin
#214242Q
#SF1202
import random
from struct import pack

switch = True
switch2 = True

#################################################################################################################################
#Data starts here


packageList =[{"Customer Name": "liam","Package Name": "bicycle", "Pax":60, "Cost": 800},
            {"Customer Name": "noah","Package Name": "desktop", "Pax":70, "Cost": 900},
            {"Customer Name": "liam","Package Name": "telephone", "Pax":80, "Cost": 1000},
            {"Customer Name": "elijah","Package Name": "playstation five", "Pax":90, "Cost": 100},
            {"Customer Name": "william","Package Name": "drum", "Pax":100, "Cost": 200},
            {"Customer Name": "james","Package Name": "drum", "Pax":10, "Cost": 300},
            {"Customer Name": "benjamin","Package Name": "phone", "Pax":20, "Cost": 400},
            {"Customer Name": "lucas","Package Name": "laptop", "Pax":30, "Cost": 500},
            {"Customer Name": "henry","Package Name": "television", "Pax":40, "Cost": 600},
            {"Customer Name": "alexander","Package Name": "speaker", "Pax":50, "Cost": 700}]


#Data ends here
#################################################################################################################################
#Function for algo starts here

def display():
    cycle = 0
    print("="*90)
    print(f"{'Index':^5} | {'Customer Name':<20} | {'Package Name':<20} | {'Pax':^8} | {'Package Cost':>8}")
    print("="*90)
    for package in packageList:
        cycle = cycle + 1
        print(f"{cycle:^5} | {package['Customer Name']:<20} | {package['Package Name']:<20} | {package['Pax']:^8} | {package['Cost']:>8}")
    print("="*90)

def updateDisplay(results):
    cycle = 0
    print("="*90)
    print(f"{'Index':^5}  | {'Customer Name':<20} | {'Package Name':<20} | {'Pax':^8} | {'Package Cost':>8}")
    print("="*90)
    if len(results) == 1:
        print(f"{cycle:^5}  | {results[0]['Customer Name']:<20} | {results[0]['Package Name']:<20} | {results[0]['Pax']:^8} | {results[0]['Cost']:>8}")
        print("="*90)
    else:
        for package in results:
            cycle = cycle + 1
            print(f"{cycle:^5}  | {package['Customer Name']:<20} | {package['Package Name']:<20} | {package['Pax']:^8} | {package['Cost']:>8}")
        print("="*90)
        while True:
            try:
                select = int(input("Select the index of the package you want to update: "))
                if select > len(results) or select <= 0:
                    print("Invalid index")
                else:
                    break
            except ValueError:
                print("Please enter a valid index.")
    while True:
        update = input("Do you want to update the record? (Y/N): ").lower()
        if update == "y":
            while True:
                newCustomerName = input("Enter Customer Name: ").lower()
                if newCustomerName == "":
                    print("Invalid Customer Name")
                else:
                    packageList[select]["Customer Name"] = newCustomerName
                    break
            while True:    
                newPackageName = input("Enter Package Name: ").lower()
                if newPackageName == "":
                    print("Invalid Package Name")
                else:
                    packageList[select]["Package Name"] = newPackageName
                    break
            while True:
                try:
                    packageList[select]["Pax"] = int(input("Enter Pax: "))
                    if packageList[select]["Pax"] <= 0:
                        print("Pax must be greater than 0")
                    else:
                        break
                except ValueError:
                    print("Please enter a number & no decimals")
            while True:
                try:
                    packageList[select]["Cost"] = int(input("Enter Cost: "))
                    if packageList[select]["Cost"] <= 0:
                        print("Cost must be greater than 0")
                    else:
                        break
                except ValueError:
                    print("Please enter a number & no decimals")
            print("Record updated")
            break
        elif update == "n":
            print("Record not updated")
            break
        else:
            print("Invalid input, please try again. Y/N?")

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

def flip(packageList, i):
    start = 0
    while start < i:
        temp = packageList[start]
        packageList[start] = packageList[i]
        packageList[i] = temp
        start += 1
        i -= 1
 
def findMax(packageList, n):
    mi = 0
    for i in range(0,n):
        if packageList[i]["Cost"] > packageList[mi]["Cost"]:
            mi = i
    return mi
 
def pancakeSort(packageList, n):
    curr_size = n
    while curr_size > 1:
        mi = findMax(packageList, curr_size)
        if mi != curr_size-1:
            flip(packageList, mi)
            flip(packageList, curr_size-1)
        curr_size -= 1



def bubbleSort(packageList):
    n = len(packageList)
    for i in range(n):
        for j in range(0, n-i-1):
            if packageList[j]['Customer Name'] > packageList[j + 1]['Customer Name']:
                packageList[j], packageList[j+1] = packageList[j+1], packageList[j]

def linearSearch(packageList, n, x):
    records = []
    for i in range(0, n):
        if (packageList[i]["Customer Name"] == x):
            records.append(packageList[i])
    if len(records) == 0:
        return -1
    else:
        return records

def binarySearch(packageList, x):
    selectionSort(packageList)
    results = []
    low = 0
    high = len(packageList)-1
    while low <= high:
        mid = (low + high) // 2
        if packageList[mid]["Package Name"] == x:
            results.append(packageList[mid])
            left = mid - 1
            while left >= 0 and packageList[left]["Package Name"] == x:
                results.append(packageList[left])
                left -= 1
            right = mid + 1
            while right <= len(packageList)-1 and packageList[right]["Package Name"] == x:
                results.append(packageList[right])
                right += 1
            return results
        elif packageList[mid]["Package Name"] < x:
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
    if l < n and packageList[largest]["Customer Name"] < packageList[l]["Customer Name"]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and packageList[largest]["Customer Name"] < packageList[r]["Customer Name"]:
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

def cocktailSort(packageList):
    n = len(packageList)
    swapped = True
    start = 0
    end = n-1
    while swapped == True:
        swapped = False
        for i in range(start, end):
            if (packageList[i]["Package Name"] > packageList[i + 1]["Package Name"]):
                packageList[i], packageList[i + 1] = packageList[i + 1], packageList[i]
                swapped = True
        if swapped == False:
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if (packageList[i]["Package Name"] > packageList[i + 1]["Package Name"]):
                packageList[i], packageList[i + 1] = packageList[i + 1], packageList[i]
                swapped = True
        start = start + 1

def radixSort(packageList):
    bucket = [[] for i in range(10)]
    maxLength = 0
    for i in packageList:
        if len(str(i["Cost"])) > maxLength:
            maxLength = len(str(i["Cost"]))
    for i in range(maxLength):
        for j in packageList:
            bucket[int(j["Cost"]/(10**i)) % 10].append(j)
        packageList = []
        for z in bucket:
            packageList.extend(z)
    return packageList

def shellSort(packageList):
    n = len(packageList)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = packageList[i]
            j = i
            while j >= gap and packageList[j-gap]["Customer Name"] > temp["Customer Name"]:
                packageList[j] = packageList[j-gap]
                j -= gap
            packageList[j] = temp
        gap //= 2

def bogoSort(packageList):
    attempts = 0
    while not isSorted(packageList):
        shuffle(packageList)
        attempts += 1
        print("\rAttempts: " + str(attempts), end="")
    print(f"\nSorted after {attempts} attempts")
    
def isSorted(packageList):
    for i in range(len(packageList)-1):
        if packageList[i]["Customer Name"] > packageList[i+1]["Customer Name"]:
            return False
            
    return True

def shuffle(packageList):
    for i in range(len(packageList)):
        j = random.randrange(len(packageList))
        packageList[i], packageList[j] = packageList[j], packageList[i]
        

#Function for algo ends here
########################################################################################################################################
#Console Function starts here


while switch:
    print("1. Display all records \n" 
    "2. Sort record by Customer Name using Bubble sort \n"
    "3. Sort record by Package Name using Selection sort\n" 
    "4. Sort record by Package Cost using Insertion sort \n" 
    "5. Search record by Customer Name using Linear Search and update record \n" 
    "6. Search record by Package Name using Binary Search and update record \n" 
    "7. List records range from $X to $Y. e.g $100-200 \n" 
    "8. Sort record by Customer Name using Heapsort \n" 
    "9. Sort record by Package Cost using Pancake sort \n" 
    "10. Sort record by Package Name using Cocktail sort \n" 
    "11. Sort record by Package Cost using Radix sort \n" 
    "12. Sort record by Customer Name using Shell sort \n" 
    "13. Add new record \n" 
    "14. Delete a specific record \n" 
    "dumb. Sort record by Customer Name using Bogo sort \n"
    "0. Exit Application")
    picker = input("Enter a function number: ").lower()
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
            updateDisplay(results)
    elif picker == "6":
        search = input("Enter Package Name: ").lower()
        results = binarySearch(packageList, search)
        if results == -1:
            print("Package Name not found")
        else:
            updateDisplay(results)
    elif picker == "7":
        while True:
            try:
                range1 = int(input("Enter minimum cost: "))
                if range1 <= 0:
                    print("Number must be greater than 0")
                else:
                    break
            except ValueError:
                print("Please enter a number & no decimals")
        while True:
            try:
                range2 = int(input("Enter maximum cost: "))
                if range2 <= 0:
                    print("Number must be greater than 0")
                else:
                    break
            except ValueError:
                print("Please enter a number & no decimals")
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
        pancakeSort(packageList, len(packageList))
        display()
    elif picker == "10":
        cocktailSort(packageList)
        display()
    elif picker == "11":
        radixSort(packageList)
        display()
    elif picker == "12":
        shellSort(packageList)
        display()
    elif picker == "13":
        while True:
            newCustomerName = input("Enter New Customer Name: ").lower()
            if newCustomerName == "":
                print("Customer Name cannot be empty")
            else:
                break
        while True:
            newPackageName = input("Enter New Package Name: ").lower()
            if newPackageName == "":
                print("Package Name cannot be empty")
            else:
                break
        while True:
            try:
                newPax = int(input("Enter New Pax: "))
                if newPax <= 0:
                    print("Pax must be greater than 0")
                else:
                    break
            except ValueError:
                print("Please enter a number & no decimals")
        while True:
            try:
                newCost = int(input("Enter New Cost: "))
                if newCost <= 0:
                    print("Cost must be greater than 0")
                else:
                    break
            except ValueError:
                print("Please enter a number & no decimals")
        packageList.append({"Customer Name": newCustomerName, "Package Name": newPackageName, "Pax": newPax, "Cost": newCost})
        print("Record added")
    elif picker == "14":
        display()
        search = input("Enter Customer Name: ").lower()
        results = linearSearch(packageList, len(packageList), search)
        if results == -1:
            print("Customer Name not found")
        else:
            print("Are you sure? (Y/N)")
            while True:
                delete = input("Enter your choice: ").lower()
                if delete == "y":
                    del packageList[results]
                    print("Record deleted")
                    break
                elif delete == "n":
                    print("Record not deleted")
                    break
                else:
                    print("Invalid input, please try again. Y/N?")
    elif picker == "dumb":
        bogoSort(packageList)
        display()
    elif picker == "0":
        print("Goodbye.")
        switch = False
    else:
        print("Invalid input, please enter a valid function number.")


#Console Function ends here
###############################################################################################################################