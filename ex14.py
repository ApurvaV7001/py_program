from sys import argv
script, user_name= argv
prompt=">"

# print("hi %s, i'm the %s script"%(user_name, script))
print(user_name, script)
print("I'd like you ask a few quetions")
print("Do you like me %s"%user_name)
likes=input(prompt)

print("Where do you live? %s"%user_name)
lives=input(prompt)

print("what kind of computer do you have? %s"%user_name)
computer=input(prompt)

print(''' alright you said %r about liking me, 
do you lives in %r and do you want %r computer'''%(likes, lives, computer) )