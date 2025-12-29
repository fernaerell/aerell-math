# Learn math with python day 1

a = 10
b = 5

print(a + b) # a add b = 15
print(a - b) # a sub b = 5
print(a * b) # a mul b = 50
print(a / b) # a div b = 2
# Correct! the output:
# 15
# 5
# 50
# 2.0 (division always return float in python maybe)

# let some op // % and **
print(a // b) # ? I think it same like divison but a bit different, my guess = 2 (I don't have any idea for this op)
print(a % b) # Modulus is you can return remainder of division so = 0 because a / b not have remainder
print(a**b) # I don't have idea for this, maybe x * b *  2? if yeah it mean = 100

# Let's check the output:
# 15
# 5
# 50
# 2.0
# 2 < I'm correct but why? // dan / it's has same result, but why?
# 0 < I'm correct
# 100000 < okay this interesting, because different from my estimation

# Learn math with python day 2

# I have to read the information of // and ** operator.
# So // is floor division, what is the different?
# / always return float like 5.5
# // always return integer, example division return 5.5 in // operator can return 5
# because python remove all of decimal number, it is called floor division
# example:
print(7 / 2) # 3.5
# output:
# 3.5

# If use floor division
print(7 // 2)
# output:
# 3

# And than what is ** operator in Python?
# This called exponentiation operator
# I have hear the name, but I don't know what it is mean?

# Okay, I have read the information for exponentiation
# So exponentiation is a short way to make a number multiplyed by it self according with exponential number
# Example:
print(5 ** 2) # It is not mean 5 * 2, but 5 * 5, and if 2 we change with 3, mean is 5 * 5 * 5
# output:
# 25

print(5 ** 3) # 35? Am i wrong?
# output:
# 125 (Yes, I am wrong)

# Wait
# 5 * 5 = 25
# 25 * 5 = ? 5 * 5  = 25, 2 * 5 = 10

# Oh i am missing something
# 5 * 5 = 25 is correct!
# Save the number 2 of 25
# 2 * 5 = 10 is correct!
# 2 + 10 = 12
# and drop down of all numbers
# the result is 125 (Yeah)

# I am just forgot basic math, lol!

# Okay, last for the lesson of this day
print(3 ** 7) # 3 exponential 7
# 1. 3 * 3 = 9
# 2. 9 * 3 = 27
# 3. 27 * 3 = 81
# 4. 81 * 3 = 271
# 5. 271 * 3 = 811
# 6. 811 * 3 = 2733
# 7. 2733 * 3 = 8199
# Let is check, i am correct or wrong
# ouput:
# 2187 (I am wrong again!!)

# 1. 3 * 3 = 9 (correct)
# 2. 9 * 3 = 27 (correct)
# 3. 27 * 3 = 81 (correct)
# 4. 81 * 3 = 271 (wrong, 243)
# 5. 243 * 3 = 729
# 6. 729 * 3 = 2187
# 7. 2187 * 3 = 6561 (I think now is correct)

# but why 3 ** 7 just return 2187? no 6561
# I am make a mistake again
# In math, exponential step 1 is the number it self like:
# 1. 3
# 2. 3 * 3 = 9
# 3. 9 * 3 = 27
# 4. 27 * 3 = 81
# 5. 81 * 3 = 243
# 6. 243 * 3 = 279
# 7. 279 * 3 = 2187

# Okay, my brain want to explode.
# I think enough for today.
# In this lesson we learn basic operator in python like +, -, *, /, % and 
# new operator for me // and **
# Thanks
