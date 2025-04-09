# this is a comment
# variable: is a container that stores something -> number, name,
# Start buy declaring a variable
# Assign a avalue to that variable
# String -> a data type that is composed of a sequence of characters
firstName = "John"
lastName = "Doe"
welcomeMessage = "Hello " + firstName + " " + lastName + ", welcome home!"  # concatenation
requestForGift = f" Hi {firstName}, did you bring me a gift?"
# print(firstName)
# print(lastName)
# print(welcomeMessage)
# print(requestForGift)

#  characters
letterA = 'a'
letterB = 'b'
letterC = 'c'

# print(letterB)

# python has an interesting feature called type casting:

#  numbers - int, float, double, long
age = 100
price = 9.9
year = 2025
pi = 3.142142142

# print(age)
# print(year)
# print(price)
# print(pi)

aboutMe = (f" Hi my name is {firstName} {lastName}, I am {age} years old. We are in the year "
           f"{year} and the price of biscuits is {price}")

# print(aboutMe)


# operators ->
"""
Operator allows you to perform mathematical operations on operands or numbers.

* - mulitply
- : minus/ subtraction
/ : division
// : division that return an integer 0 -> infinity and 0-> -ve inifinity
% : modulus - divisibilities 4/2 -> no remainder  
= : assignment operator 
"""

numberOfVehicles = 100
numberOfPassengers = 200
numberOfTrips = 20
tax =10
price = 25


#  simple mulitiplication:
product = numberOfVehicles * numberOfPassengers
totalPrice = price* numberOfTrips* numberOfVehicles
# subtraction
netPay = totalPrice - tax
# modulus - divisor -> remainder ==0
remainder = numberOfTrips % price

divide = numberOfTrips / price
doubledivide = numberOfTrips // price

# print(f"=======================================")
# print(f"Number Of Vehicles: {numberOfVehicles}")
# print(f"Number Of Passenger: {numberOfPassengers}")
# print(f"PRICE: {totalPrice}")
# print(f"NET-PAY: {netPay}")
# print(f"REMAINDER: {remainder}")
# print(f"DIVIDE: {divide}")
# print(f"DDIVIDE: {doubledivide}")
# print(f"=======================================")



# array : 0....x
basketOfGroceries = ["mangoes", "apples", "corriander", "oranges", "bananas", "macadamia","thorn-melons"]
# an index is basically the position of an element in an array. It always starts from 0 in terms of counting
# basketSize = len(basketOfGroceries)
# print(basketSize)
# print(basketOfGroceries[-1])
# print(basketOfGroceries)


# for...loope

# for grocery in basketOfGroceries:
#     print(f" ==> {grocery}")













# string
# characters make string
# bananas
# print(basketOfGroceries[0][:])








# Numbersger
# - int, float, complex
x = 10 #integer
y = -10 #integer
z = 10.98 # float
a = 10j #complex number


numberOfTrips = "10" # changing this to a string -> casting...
numberOfTrips = str(numberOfTrips)


# Strings

quote = "I have a dream !"
quoteEnding = "To swim with the sharks!"


# Booleans - True .... False
a = 10
b =10

condition = (a >= b)



# lists - collection of items...

fruits = ["mango", "apple", "orange", "banana", "tomatoe"]
grades = [10,20,30,40,50,60]
name = "Doe"


"""

Task 1:
Create two variable( firstNumber and secondNumber), Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Example
Print the following:
SUM: 8
DIFFERENCE: -2
PRODUCT: 15 



"""


"""
- Boolean ( Truth table)
- operators : not, AND, OR 
- Conditional Statements ( if..else, if...elif..else, match..case..case_)
- functions  
"""

isRaining = True
isFlooded = True
output = "Just dress lightly"

numberOfumbrellas = 10
heightOfWater = 100
if isRaining and isFlooded and numberOfumbrellas == 10 and heightOfWater >= 100:
    output = "wear gumboots + heavy clothing"
elif heightOfWater == 100:
    output = f"Water levels are quite high, they are at {heightOfWater}m."
else:
    output = "The weather look ok today, enjoy!"

isRaining = False
isFlooded = False

if isRaining or isFlooded:
    output = "Embrace yourself"
elif numberOfumbrellas < 10:
    output ="We have sufficient number of umbrellas"
else:
    output = "the sun is shinning"

userEmail =''
userName =""

if len(userEmail) ==0:
    # userEmail = input("Enter your email: ")
    output = "Enter Email address"
elif userEmail and userName:
    output = "Enter username"
else:
    output = "What is going on!"

userEmailLength = len(userEmail) >= 9
match userEmailLength:
    case True:
        output = "Enter your email!"
    case False:
        output = "Email is to short!"
    case _:
        output = "we can proceed to validation"


"""
COMBINED PROBLEM SOLVING SESSION
================================================
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird

"""
number = -50
if number%2 != 0: # checks if even
    output = "odd n Weird..."
elif number%2 == 0 and number <=5 and number>=2:
    output = "Not Weird but between 2 and 5"
elif number %2 == 0   and number >=6 and number <=20:
    output = "Weird but between 6 and 20"
elif number %2 ==0  and number >=-200 and number <=0:
    output = "Weird and plainly even! BUT -VE"
elif number >20:
    output = "Not Weird but greater than 20"
else:
    output = "let me get back to you!"
print("=================================")
print(f"NUMBER:{number}, {output}")
print("=================================")




"""
- variables ( data types: int, double, strings, lists, tuples, dictionary) 
- arithmetic operators ( /, *, +, -, //, **)
- boolean operators ( not, and, or) 
--------------------------------------------------------------------------
- control flows : if...else, if...elif...else, match...case...case _
-

"""



