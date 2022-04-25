from python_class.Package import Package
import shelve, uuid, pathlib

def generate_ID(inputDict):
    generatedID = str(uuid.uuid4())
    if generatedID in inputDict:
        generate_ID(inputDict)
    return generatedID

databaseFolder = str(pathlib.Path.cwd()) + "\\databases"

packageBase = shelve.open(databaseFolder + "\\package", "c")

packageDict = {}

#Data 1

packageID = generate_ID(packageDict)
customerName = "Customer 1"
packageName = "Package 2"
quantity = "3000"
cost = "4000"

package = Package(packageID, packageName, customerName, quantity, cost)

packageDict[packageID] = package

#Data 2

packageID = generate_ID(packageDict)
customerName = "Customer 2"
packageName = "Package 3"
quantity = "4000"
cost = "5000"

package = Package(packageID, packageName, customerName, quantity, cost)

packageDict[packageID] = package

#Data 3

packageID = generate_ID(packageDict)
customerName = "Customer 3"
packageName = "Package 4"
quantity = "5000"
cost = "6000"

package = Package(packageID, packageName, customerName, quantity, cost)

packageDict[packageID] = package

#Data 4

packageID = generate_ID(packageDict)
customerName = "Customer 4"
packageName = "Package 5"
quantity = "6000"
cost = "7000"

package = Package(packageID, packageName, customerName, quantity, cost)

packageDict[packageID] = package

#Data 5

packageID = generate_ID(packageDict)
customerName = "Customer 5"
packageName = "Package 6"
quantity = "7000"
cost = "8000"

package = Package(packageID, packageName, customerName, quantity, cost)

packageDict[packageID] = package

#Data 6

packageID = generate_ID(packageDict)
customerName = "Customer 6"
packageName = "Package 7"
quantity = "8000"
cost = "9000"

package = Package(packageID, packageName, customerName, quantity, cost)

packageDict[packageID] = package

#Data 7

packageID = generate_ID(packageDict)
customerName = "Customer 7"
packageName = "Package 8"
quantity = "9000"
cost = "10000"

package = Package(packageID, packageName, customerName, quantity, cost)

packageDict[packageID] = package

#Data 8

packageID = generate_ID(packageDict)
customerName = "Customer 8"
packageName = "Package 9"
quantity = "10000"
cost = "1000"

package = Package(packageID, packageName, customerName, quantity, cost)

packageDict[packageID] = package

#Data 9

packageID = generate_ID(packageDict)
customerName = "Customer 9"
packageName = "Package 10"
quantity = "1000"
cost = "2000"

package = Package(packageID, packageName, customerName, quantity, cost)

packageDict[packageID] = package

#Data 10

packageID = generate_ID(packageDict)
customerName = "Customer 10"
packageName = "Package 1"
quantity = "2000"
cost = "3000"

package = Package(packageID, packageName, customerName, quantity, cost)

packageDict[packageID] = package

packageBase["Packages"] = packageDict

packageBase.close()