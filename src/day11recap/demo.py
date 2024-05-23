def replace_char_at_index(str,newstr,index):
    if index < 0 or index >= len(str):
        raise ValueError("Index is out of range for the given string.")
    
    return str[:index] + newstr + str[index + 1:]

s = "These words are separated by spaces"
print( s.split(" ") )


ans=input("which is your fav programming language ?")

s1=s[:4]
s = s.replace(s1,ans)
print("new s data")
print(s)



newans = replace_char_at_index(s,"not so fav",12)
print(newans)

num_of_years = input("how many years experience with this language")

num_of_years = int(num_of_years)
print(type(num_of_years))

val = "False"
val2 = bool(val)
num = int(val2)
print(num)

try:
    ans=float(input("Type a number to add:"))
    print(f"100 + {100 + ans}")

except:
    print("you did not put a valid number")

print("Program terminated gracefully")


word="football"

if "b" in word:
    print(f"{word} contains b")
else:
    print(f"{word} doesnot contain b")


x,y=5,10

if x>y:
    print("x is greater")
elif x < y:
    print("x is lesser value than y")
elif (x+5)==y:
    print("equal to y on adding 5 to x")
