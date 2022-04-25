from python_file.Package import Package

switch = True

packageList = Package[{"Customer 1": 1,"Package 4": 4, "Pax": 60, "Cost": 800},
                    {"Customer 2": 2,"Package 5": 5, "Pax": 70, "Cost": 900},
                    {"Customer 3": 3,"Package 6": 6, "Pax": 80, "Cost": 1000},
                    {"Customer 4": 4,"Package 7": 7, "Pax": 90, "Cost": 100},
                    {"Customer 5": 5,"Package 8": 8, "Pax": 100, "Cost": 200},
                    {"Customer 6": 6,"Package 9": 9, "Pax": 10, "Cost": 300},
                    {"Customer 7": 7,"Package 10": 10, "Pax": 20, "Cost": 400},
                    {"Customer 8": 8,"Package 1": 1, "Pax": 30, "Cost": 500},
                    {"Customer 9": 9,"Package 2": 2, "Pax": 40, "Cost": 600},
                    {"Customer 10": 10,"Package 3": 3, "Pax": 50, "Cost": 700}]


while switch:
    print(" 1. Display all records \n 2. Sort record by Customer Name using Bubble sort \n 3. Sort record by Package Name using Selection sort \n 4. Sort record by Package Cost using Insertion sort \n 5. Search record by Customer Name using Linear Search and update record \n 6. Search record by Package Name using Binary Search and update record \n 7. List records range from $X to $Y. e.g $100-200 \n 0. Exit Application")
    picker = input("Enter a function number: ")
    if picker == "1":
        print("|   Package Name   |   Customer Name   |   No. of Pax   |   Package Cost per Pax   |")
        for package in packageList:
            print("|", package.get_package_name(), "|", package.get_customer_name(), "|", package.get_quantity(), "|", package.get_cost(), "|")

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