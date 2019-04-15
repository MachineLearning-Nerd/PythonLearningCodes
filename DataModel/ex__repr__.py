# This is the example of how to use the __repr__ in python 
class celsius():
    def __init__(self,Fern):
        """ Enter the data into the Fahrenheit """
        self.celsius = (Fern - 32)*(5/9)
    def __repr__(self):
        return "The celsius is:{}".format(self.celsius)  
d = celsius(-40)

# This will be the value done in the __init__
print(d.celsius)
# This will print the values configured by the __repr__ 
print(d)