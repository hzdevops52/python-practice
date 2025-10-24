#write a file
with open('user_info.txt', 'a') as file:
    file.write('text here\n')
    
#read a file
with open('user_info.txt', 'r') as file:
    print(file.read())
    

#file as list
with open('user_info.txt', 'r') as file:
    content = file.readlines()
    
    #print(content)
    
for line in content:
    print(line)       