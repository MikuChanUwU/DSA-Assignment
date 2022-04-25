from python_class.Package import Package
import shelve

switch = True

while switch:
    print(" 1. Display all records \n 2. Sort record by Customer Name using Bubble sort \n 3. Sort record by Package Name using Selection sort \n 4. Sort record by Package Cost using Insertion sort \n 5. Search record by Customer Name using Linear Search and update record \n 6. Search record by Package Name using Binary Search and update record \n 7. List records range from $X to $Y. e.g $100-200 \n 0. Exit Application")
    picker = input("Enter a function number: ")
    if picker == "1":
        print("|   Package Name   |   Customer Name   |   No. of Pax   |   Package Cost per Pax   |")
        for packages in ():
            try:
                packageDict = {}
                db = shelve.open("package", "r")
                packageDict = db["Package"]
            except:
                print("Unable to open up package shelve")
                db.close()
                break
            package = packageDict[]
            pack = Package(packageID, packageName, customerName, noOfPax, cost)
            print(pack)

    elif picker == "2":
        pass
    elif picker == "3":
        pass
    elif picker == "4":
        pass
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