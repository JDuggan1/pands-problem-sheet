import sys   
result = 0  
print(11)

def collatz():   

    number = int(11)    
    if number % 2 == 0:    
        result = number//2    
        print (result)    
        if result == 1:    
            print('finally u got it')    
            sys.exit()    
    if number % 2 == 1:    
        result = 3 * number + 1    
        print (result)

while result != 1:  
    collatz()
