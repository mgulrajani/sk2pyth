'''try-except blocks , asks Python to do something, 
it tells Python what to do if an exception is raised
when you use try-except blocks , even if there is some error 
during execution and something goes wrong , your program will continue
running 
you will not want to display traceback , end users  /non-technical
instead of confusing messages to the user , you can show a simple
message as to what could be the problem

'''
import os

try:
    print("Give two numbers to divide")
    print("q to quit")

    while True:
        fNum = input('first number')
        if fNum == 'q':
            break
        secondNum = input('second number')
        if secondNum == 'q':
            break
        x = int(fNum) / int(secondNum)

        print(x)
            
        assert (x >= 5),f"x should always be greater than 5"
        if (x < 5):
                raise Exception('value of x cannot be less than 5')
            
        with open('file1.txt') as f:
                read_data = f.read()

            
except FileNotFoundError as fnf:
            print("File does not exist")
except ZeroDivisionError as zd:
            print('Number cannot be divided by zero')
except Exception as e:
            print(e)
finally:
            print('finally block always executes')


