#errors

#print(10/0)

"""
with open('user_in.txt', 'r') as file:
    file.read()
"""

#handling

try:
    print(10/0)
except ZeroDivisionError:
    print('dont divide by ZERO') 
    
try:
    print(10/0)
except Exception as e:
    print(e, type(e))           
    
try:
    with open('user_in.txt', 'r') as file:
     file.read()
except FileNotFoundError:
    print('file not found in the directory')    
    
try:
    with open('user_in.txt', 'r') as file:
     file.read()    
except Exception as e:
    print(e, type(e)) 
finally:
    print('file closed')        