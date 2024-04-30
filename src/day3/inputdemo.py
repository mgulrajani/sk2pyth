current_number = 1

while current_number <= 2:

    username =  input("Enter your name")
    print(f"Welcome {username}")

    age=int(input("Enter your age"))

    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")

    current_number += 1



prompt = "\n You can give a  message to be passed on"
prompt += "\n Enter 'quit' to end the program"


message = ''

while message != 'quit':
    message=input(prompt)
    print(message)


x=1
while x<=5:
    print('hello')
    x+=1







