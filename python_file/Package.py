class Package:
    def __init__(self, packageName, customerName, pax, cost):
        self.__packageName = packageName
        self.__customerName = customerName
        self.__pax = pax
        self.__cost = cost

    def getPackageName(self):
        return self.__packageName
    
    def getCustomerName(self):
        return self.__customerName

    def getPax(self):
        return self.__pax
    
    def getCost(self):
        return self.__cost
    
    def setPackageName(self, packageName):
        self.__packageName = packageName
    
    def setCustomerName(self, customerName):
        self.__customerName = customerName

    def setPax(self, pax):
        self.__pax = pax

    def setCost(self, cost):
        self.__cost = cost