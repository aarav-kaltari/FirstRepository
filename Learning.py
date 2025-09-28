age=11
name="Aarav"
print("My name is",name,"and I am",age,"years old.")

a=3+5
b=8-2
c=4*2
d=16/2
e=7890%7
print(a,b,c,d,e)

weather="sunny"
if weather=="sunny":
    print("Let's play outside!")
else:
    print("Let's stay inside!")

for number in range (1,6):
    print(number)

# new challenge using for loop
firstNNumbers = 1000
sumOfFirstNNumbers = 0
for number in range(1,firstNNumbers+1):
    sumOfFirstNNumbers = sumOfFirstNNumbers+number
    averageOfFirstNNumbers = sumOfFirstNNumbers/number
print("The sum of",firstNNumbers,"numbers is",sumOfFirstNNumbers)
print("The average of first",firstNNumbers, "numbers is",averageOfFirstNNumbers)
# challenge code ended