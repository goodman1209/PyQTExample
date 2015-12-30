class Data(object):
    #code
    def __init__(self):
        name = "Allan"
        self.alias = "Allan Sung"
        print(name)

    def printName(self):
        #print(name) will show error
        print(self.alias)

data = Data()
data.printName()
print(data.__str__)
print(data.__repr__)
print (float(0.2))
print (float(1.0 - 0.8))
#print ((1.0 - 0.8).__str()__)

#from decimal import Decimal
import decimal
a = decimal.Decimal('1.0')
b = decimal.Decimal('0.8')
print(a - b)

name = "t"
#print( name )
name = "tt"
#print( name )
tab = "c:\w"
#print(tab)