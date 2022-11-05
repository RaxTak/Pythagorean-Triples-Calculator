from math import *
def is_integer(num):
        try:
                int(num)
                return True
        except ValueError:
                return False
                

    #2m, m^2 -1, m^2 + 1
while True:
        
        m = input("ENTER 2m > ")
        while not is_integer(m) or int(m) < 3:
                print ("Enter a valid integer or integer above 3!")
                m = input("ENTER 2m > ")
       
        x = int(m)
        y = pow(x/2, 2) - 1
        z = pow(x/2, 2) + 1
        print(str(x) + ", " + str(y) + ", " + str(z))
