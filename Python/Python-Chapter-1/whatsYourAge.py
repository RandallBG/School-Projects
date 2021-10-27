name = "Randall";

className= "ClevelandCodes"

age = int(input("How old are you? "))

if(age<=50):
    response="f{name}, that is very hard to believe."
    print(response)
elif age<=60:
    response = str(age) + " is a nice age " + name + "!"
    print(response)
else:
    print("Wow", name, "Where's your cane?")

x = range(int(input("give me a number")))

for i in range(0,len(className), 2):
    print(className[i])

studentList = ""
answer = "y"

while answer.lower() == "y":
    studentName = input("Enter a name")
    studentList += studentName + "\n"
    answer = input("More? (y/n) ")
print("\n", studentList)
print()
