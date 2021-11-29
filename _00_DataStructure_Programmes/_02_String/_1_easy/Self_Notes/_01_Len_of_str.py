'''Operator:
Operators are used to perform operations on variables and values.
Python Operators in general are used to perform operations on values and variables.
These are standard symbols used for the purpose of logical and arithmetic operations.
In this article, we will look into different types of Python operators

Python divides the operators in the following groups:

#Arithmetic Operators

Arithmetic Operators are used to performing mathematical operations like addition,
subtraction, multiplication, and division.
+ Addition: adds two operands x + y
– Subtraction: subtracts two operands x – y
* Multiplication: multiplies two operands x * y
/ Division (float): divides the first operand by the second x / y
% Modulus: returns the remainder when the first operand is
divided by the second
x % y
** Power: Returns first raised to power second x ** y"""

# Examples of Arithmetic Operator
a = 9
b = 4
# Addition of numbers
add = a + b
# Subtraction of numbers
sub = a - b
# Multiplication of number
mul = a * b
# Division(float) of number
div1 = a / b
# Division(floor) of number
div2 = a // b
# Modulo of both number
mod = a % b
# Power
p = a ** b
# print results
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)

""""""

Operator	   Name	            Example
+	          Addition	        x + y
-	          Subtraction	    x - y
*	          Multiplication	x * y
/	          Division	        x / y
%	          Modulus	        x % y
**         	  Exponentiation	x ** y
//	          Floor division	x // y

Assignment operators:
Operator	     Example	  Same As
=	               x = 5	  x = 5
+=	               x += 3	  x = x + 3
-=	               x -= 3	  x = x - 3
*=	               x *= 3	  x = x * 3
/=	               x /= 3	  x = x / 3
%=	               x %= 3	  x = x % 3
//=	               x //= 3	  x = x // 3
**=	               x **= 3	  x = x ** 3
&=	               x &= 3	  x = x & 3
|=	               x |= 3	  x = x | 3
^=	               x ^= 3	  x = x ^ 3
>>=	               x >>= 3	  x = x >> 3
<<=	               x <<= 3	  x = x <<
"""Assignment operators are used to assigning values to the variables.
"""

"""+= Add AND: Add right-side operand with left side operand and
then assign to left operand
a+=b
a=a+b

-= Subtract AND: Subtract right operand from left operand and
then assign to left operand
a-=b
a=a-b

*= Multiply AND: Multiply right operand with left operand and
then assign to left operand
a*=b
a=a*b

/= Divide AND: Divide left operand with right operand and then
assign to left operand
a/=b
a=a/b

%= Modulus AND: Takes modulus using left and right operands
and assign the result to left operand
a%=b
a=a%b

//= Divide(floor) AND: Divide left operand with right operand and
then assign the value(floor) to left operand
a//=b
a=a//b

**= Exponent AND: Calculate exponent(raise power) value using
operands and assign value to left operand
a**=b
a=a**b

&= Performs Bitwise AND on operands and assign value to left
operand
a&=b
a=a&b

|= Performs Bitwise OR on operands and assign value to left
operand
a|=b
a=a|b

^= Performs Bitwise xOR on operands and assign value to left
operand
a^=b
a=a^b

>>= Performs Bitwise right shift on operands and assign value to
left operand
a>>=b
a=a>>b
"""


"""# Examples of Assignment Operators
a = 10
# Assign value
b = a
print(b)
# Add and assign value
b += a
print(b)
# Subtract and assign value
b -= a
print(b)
# multiply and assign
b *= a
print(b)
# bitwise lishift operator
b <<= a
print(b)"""

Comparison operators
Comparison operators — operators that compare values and return true or false .
The operators include: > , < , >= , <= , === , and !== ... Logical operators — operators that combine
multiple boolean expressions or values and provide a single boolean output.
Comparison of Relational operators compares the values. It either returns True or
False according to the condition.
> Greater than: True if the left operand is greater than the right x > y
< Less than: True if the left operand is less than the right x < y
== Equal to: True if both operands are equal x == y
!= Not equal to – True if operands are not equal x != y
>= Greater than or equal to True if the left operand is greater than
or equal to the right
x >= y
<= Less than or equal to True if the left operand is less than or
equal to the right
x <= y

a = 13
b = 33
# a > b is False
print(a > b)
# a < b is True
print(a < b)
# a == b is False
print(a == b)
# a != b is True
print(a != b)
# a >= b is False
print(a >= b)
# a <= b is True
print(a <= b)"""\

#print even numbers using comparison operator
"""numbers = [1,2,3,4,5,6,7,8]

for i in numbers:
    if i % 2 ==  0:
        print(i)

list1 = [i for i in numbers if i % 2 == 0]
print(list1)

n = 0
while n < len(numbers):
    if numbers[n] % 2 == 0:
        print(numbers[n])
    n = n + 1"""

list1 = ["Rakshitha","varun","vinith","kiran"]
list2 = ["Rakshitha","varun","deekshith","chandana","ranjitha"]
if(list1 < list2 ):
    print("Result :","True")
else :
    print("Result :","False")



Logical operators
A logical operator is a symbol or word used to connect two or more expressions such that the value of the
compound expression produced depends only on that of the original expressions and on the meaning of the operator.
Common logical operators include AND, OR, and NOT.

Identity operators
Identity operators are used to compare the objects,not if they are equal, but if they are actually the same object
with the same memory location: Operator.
There are two Identity operators: "is" and "is not" . is - Returns true if both variables are the same object.
"""is and is not are the identity operators both are used to check if two values are located
on the same part of the memory. Two variables that are equal do not imply that they
are identical."""

"""is True if the operands are identical"""


"""a = 10
b = 20
c = a
print(a is not b)
print(a is c)"""

Membership operators
Python Membership Operators
Operator	                                    Description	                                     Example
in	                             Returns True if a sequence with the specified
                                 value is present in the object	                                   x in y
not in	                         Returns True if a sequence with the specified value
                                 is not present in the object	                                  x not in y

"""in and not in are the membership operators; used to test whether a value or variable is
in a sequence.
in True if value is found in the sequence
not in True if value is not found in the sequence
"""

"""# Python program to illustrate
# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]
if (x not in list):
print("x is NOT present in given list")
else:
print("x is present in given list")
if (y in list):
print("y is present in given list")
else:
print("y is NOT present in given list")
"""
#Bitwise operators
OPERATOR	    DESCRIPTION	              SYNTAX
&	              Bitwise AND	           x & y
|	              Bitwise OR	           x | y
~	              Bitwise NOT	            ~x
^	              Bitwise XOR	           x ^ y
>>	              Bitwise right shift	   x>>
<<	              Bitwise left shift	   x<<
"""bitwise operators act on bits and perform the bit-by-bit operations. These are used to
operate on binary numbers."""

"""& Bitwise AND x & y
| Bitwise OR x | y
~ Bitwise NOT ~x
^ Bitwise XOR x ^ y
>> Bitwise right shift x>>y"""

"""# Examples of Bitwise operators
a = 10
b = 4
# Print bitwise AND operation
print(a & b)
# Print bitwise OR operation
print(a | b)
# Print bitwise NOT operation
print(~a)
# print bitwise XOR operation
print(a ^ b)
# print bitwise right shift operation
print(a >> 2)
# print bitwise left shift operation
print(a << 2)"""

Precedence and Associativity of Operators:
"""Precedence and Associativity of Operators: Operator precedence and associativity
determine the priorities of the operator.
"""
"""Operator Precedence
This is used in an expression with more than one operator with different precedence to
determine which operation to perform first."""

"""# Examples of Operator Precedence
# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)
# Precedence of 'or' & 'and'
name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 2:
print("Hello! Welcome.")
else:
print("Good Bye!!")
"""
# Operator Associativity:\

"""# Examples of Operator Associativity
# Left-right associativity
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)
print(100 / 10 * 10)
# Left-right associativity
# 5 - 2 + 3 is calculated as
# (5 - 2) + 3 and not
# as 5 - (2 + 3)
print(5 - 2 + 3)
# left-right associativity
print(5 - (2 + 3))
# right-left associativity
# 2 ** 3 ** 2 is calculated as
# 2 ** (3 ** 2) and not
# as (2 ** 3) ** 2
print(2 ** 3 ** 2)
"""






























'''