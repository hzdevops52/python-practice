msg = "hzdevops"

print(msg[0:5])

print(msg.upper())
print(msg.lower())
print(msg.split())
print(msg.title())

user_list = ['user1', 'user2', 'user3']

print(user_list)

user_list.append('user4')
print(user_list)

user_list.insert(1, 'user5')
print(user_list)

user_list.remove('user4')
print(user_list)

user_list.sort()
print(user_list)

user_list.sort(reverse=True)
print(user_list)

#length
print(len(user_list))

#pop
print(user_list.pop())
print(user_list.pop(1))


marks = [90 , 40, 39, 66, 50]

print(marks)
print(min(marks))
print(max(marks))
print(sum(marks))