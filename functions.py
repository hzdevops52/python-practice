def function(username , **user_info):
    print('*'*20)
    
    print(f'welcome {username}')
    
    for key, value in user_info.items():
        print(f'{key} is {value}')
        
    print(f'thankyou for signing In.....')
    
    print('*'*20)

function('hassan', age=21, email='hzdevops@gmail.com')    