print('FizzBuzz Program')

user_value = int(input('enter the number :'))
my_list = []

for value in range(1, user_value+1):
    result = ""
    
    if value % 3 == 0:
        result = result + "fizz"
        if value % 5 == 0:
            result = result + "buzz"
            
    elif value % 5 == 0:
        result = result + "buzz"
        
    else:
        result = value        
    my_list.append(result)

print(my_list)    