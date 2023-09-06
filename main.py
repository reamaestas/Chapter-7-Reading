print("----for loops---")
#num is the loop variable
for num in range(4):
	print(num)
	print("Hello" * num)
print("done!")
print("\n--- Set Start and Stop Values-------")
#for num in range (start_value, stop_value):
   # do something/loop body
for num in range(1, 4):
   print("Hello" * num)
print("\n----Step Value--------")
#for num in range(start_value, stop_value, step_value):
   # do something/loop body
for num in range(0, 21, 5):
	print(num)
	#counts by fives
print("-------")
for num in range(50, 39, -1):
	print(num)
	#counts DOWN if step value is negative
print("-----STARTING CODE-------")
for num in range(8):
  print(num)

# Change the start, stop, and step values in range to solve tasks 1 - 6 in the text below:
print("----- 1 -------")
  # 1. Print the numbers 0 - 5.
for num in range(6):
  print(num)
	
print("----- 2 -------")
  # 2. Print the numbers 33 - 45, including 45.
for num in range(33,46):
  print(num)

print("----- 3 -------")
  # 3. Print only the odd numbers from 0 - 20.
for num in range(1,20,2):
  print(num)

print("----- 4 -------")
  # 4. Print the numbers 25, 35, 45…95.
for num in range(25,96,10):
  print(num)

print("----- 5 -------")
  # 5. Print the numbers from -3 to -10.
for num in range(-10,-2):
  print(num)
print("--does this work too?---")
for num in range(-3,-11,-1):
  print(num)
print("----- 6 -------")
  # 6. Print by 3’s from 15 to -21.
for num in range(15,-22, -3):
  print(num)
  
# Tip: Use the 'clear' button in the console to remove old outputs.

print("----print a for loop these variables to set the range----\n")
start_value = int(input("Enter the FIRST number to print: "))
stop_value = int(input("Enter the LAST number to print: "))
step_value = int(input("Enter the step value for the loop: "))

for num in range(start_value, stop_value + 1, step_value):
	print(num)

for num in range(start_value, stop_value - 1, step_value):
	print(num)
print("------------")
word = "Python"

for num in range(len(word)):
    print(word*num)

print("\n----REPEATING A CHECK--------\n")
num = 7

for number in range(num):
   if number%3 == 0:
      print(number, "is divisible by 3.")
   else:
      print(number, "is NOT divisible by 3.")
	
print("------IDK WHY THIS HAPPENS W/OUT THE INDENTION------")
for number in range(num):
   if number%3 == 0:
      print(number, "is divisible by 3.")
else:
      print(number, "is NOT divisible by 3.")

print("-------------")
text = 'Coding ROCKS!'
num_vowels = 0

for char in text:
   if char in 'aeiou':
      num_vowels += 1

print(text, "contains", num_vowels, "lowercase vowels.")
print("-------------")
'''
if condition:
   for var_name in range(value):
      # Loop body
elif other_condition:
   for char in string:
      # Loop body
else:
   for step in range(20):
      print("Python ROCKS!")
'''
print("----ACCUMULATOR PATTERN---------")
num = 6
total = 0

for integer in range(1, num+1):
   total += integer

print(total)

# use num+1 to include the last index in the range
print("-------------")
# The accumulator pattern can also decrease a running total!
total = 1000
decrease_by = 25

for step in range(10):
   total -= decrease_by

print(total)
print("-------------")

total = 0
for step in range(5):
	total += 2
print(total)

print("------ FOR LOOP TO WHILE LOOP-------")
for num in range(21):
   print(num)

num = 0
while num < 21:
   print(num)
   num += 1

print("-----PRACTICE CONVERT FOR TO WHILE--------")

letters = 'abcdefghijklmnopqrstuvwxyz'
for_string = ''
num_letters = 8

for index in range(num_letters):
   for_string += letters[index]

print(for_string)  # Displays 'abcdefgh'

# Follow the instructions in the text to rewrite a for loop a while loop.
letters = 'abcdefghijklmnopqrstuvwxyz'
while_string = ''
num_letters = 8
index = 0

while index < num_letters:
	while_string += letters[index]
	index += 1
	
print(while_string)

print("------INPUT VALIDATION-------")

num_choice = 0

while num_choice <= 0:
    num_choice = int(input('Choose a positive number: '))
    if num_choice <= 0:
      print('Invalid number')

#different than definite iteration

print("\n----for loop PROS AND CONS---------")
'''
Easier to set up than while loops.

Must have a definite start and end point, and these must be declared in the for statement.

Can loop through strings and collections without using an index value (e.g. for char in 'hello':).

Automatically updates the loop variable.

It is hard to accidentally create an infinite Python for loop.

Can be used in place of some while loops, but not all.

Do not work for input validation.
'''
print("\n----while loop PROS AND CONS---------")
'''
More flexible than for loops.

ANY for loop can be re-written as a while loop.

Do not need to know beforehand how many times the loop needs to run.

Can be used for input validation.

while loops require more work to build.

Making an infinite while loop is easy.

'''
print("-----ending loop with BREAK--------")
for iteration in range(42):
   print('This is iteration number:', iteration+1)

   if iteration > 4:
      break

print("The loop is done!")
'''
Line 2 repeats 6 times with values of iteration from 0 to 5.

The sixth time through the loop, iteration is 5 and the condition in line 4 (iteration > 4) evaluates to True for the first time.

As a result, the program flow reaches the break statement. The loop immediately stops, even though range(42) would normally keep the loop going.

Control moves to the first line of code after the loop.
'''
print("-------------")

