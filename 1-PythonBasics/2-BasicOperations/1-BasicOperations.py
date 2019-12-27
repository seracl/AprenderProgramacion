# Python - Basic Operators
## Types of Operator
'''
Python language supports the following types of operators.
- Arithmetic Operators
- Comparison (Relational) Operators
- Assignment Operators
- Logical Operators
- Bitwise Operators
- Membership Operators
- Identity Operators
'''

### Arithmetic Operators
'''
Assume variable a holds 10 and variable b holds 20:
- Addition        (+): a + b =    30   | Adds values on either side of the operator.
- Substraction    (-): a – b =   -10   | Subtracts right hand operand from left hand operand.
- Multiplication  (*): a * b =   200   | Multiplies values on either side of the operator.
- Division        (/): b / a =     2   | Divides left hand operand by right hand operand.
- Modulus         (%): b % a =     0   | Divides left hand operand by right hand operand and returns remainder.
- Exponent       (**): a**b  = 10^20   | Performs exponential (power: a**b =10 to the power 20) calculation on operators. 
- Floor Division (//): 9//2  =     4   | The division of operands where the result is the quotient in which the digits after the decimal point are removed. 
									     But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)
'''

### Comparison Operators
'''
Also called Relational operators; 
compare the values on either sides of them and decide the relation among them.

Assume variable a holds 10 and variable b holds 20:
- Equal to                      (==): a == b | If the values of two operands are equal, then the condition becomes true.
- Not equaL to                  (!=): a != b | If values of two operands are not equal, then condition becomes true.
- Not equaL to                  (<>): a <> b | If values of two operands are not equal, then condition becomes true.
- Greather than                  (>): b > a  | If the value of left operand is greater than the value of right operand, then condition becomes true.
- Less than                      (<): b < a  | If the value of left operand is less than the value of right operand, then condition becomes true.
- Greather/Less equal to  (>= or <=): a>=b   | If the value of left operand is greater/less than or equal to the value of right operand, then condition becomes true.
'''

### Assignment Operators
'''
Assume variable a holds 10 and variable b holds 20:
- Assign to               (=): c = a + b | Assigns values from right side operands to left side operand
- Add AND                (+=): c += a    | It adds right operand to the left operand and assign the result to left operand (c += a is equivalent to c = c + a).
- Substract AND          (-=): c -= a    | It substract right operand to the left operand and assign the result to left operand.
- Multiply AND           (*=): c *= a    | It multiply right operand to the left operand and assign the result to left operand.
- Dividey AND            (/=): c /= a    | It divide right operand to the left operand and assign the result to left operand.
- Modulusy AND           (%=): c %= a    | It takes modulus using two operands and assign the result to left operand.
- Exponent AND          (**=): c **= a   | Performs exponential (power) calculation on operators and assign value to the left operand.
- Floor Division AND    (//=): c //= a   | It performs floor division on operators and assign value to the left operand.
'''

### Bitwise Operators
'''
Bitwise operator works on bits and performs bit by bit operation. 
Assume if 
a = 60  | In binary: 0011 1100; 
b = 13  | In binary: 0000 1101; 
we use the above two variables (a and b) as operands:
- Binary AND               (&): a&b = 0000 1100    | Operator copies a bit to the result if it exists in both operands.
- Binary OR                (|): a|b = 0011 1101    | It copies a bit if it exists in either operand.
- Binary XOR               (^): a^b = 0011 0001    | It copies the bit if it is set in one operand but not both.
- Binary Ones Complement   (~): ~a  = 1100 0011    | It is unary and has the effect of 'flipping' bits.
												   | (~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.
- Binary Left Shift       (<<): a << 2 = 240       | The left operands value is moved left by the number of bits specified by the right operand. a << 2 = 240 (means 1111 0000)
- Binary Right Shift      (>>): a >> 2 = 15        | The left operands value is moved right by the number of bits specified by the right operand. a >> 2 = 15 (means 0000 1111)
'''

### Logical Operators
'''
Assume variable a holds 10 and variable b holds 20:
- Logical AND  (AND): (a and b) is true     | If both the operands are true then condition becomes true.
- Logical  OR  ( OR): (a or b) is true      | If any of the two operands are non-zero then condition becomes true.
- Logical NOT  (NOT): Not(a and b) is false | Used to reverse the logical state of its operand.

'''

### Membership Operators
'''
Assume variable a holds 10 and variable b holds 20:
- In     : x in y, here in results in a 1 if x is a member of sequence y.             | Evaluates to true if it finds a variable in the specified sequence and false otherwise.
- Not in : x not in y, here not in results in a 1 if x is not a member of sequence y. | Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.

'''

### Identity Operators
'''
Assume variable a holds 10 and variable b holds 20:
- Is     | x is y, here is results in 1 if id(x) equals id(y).
		 | Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
- Is not | x is not y, here is not results in 1 if id(x) is not equal to id(y).
		 | Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.

'''
