As we have mentioned previously, it is legal to make more than one assignment to the same variable. A new assignment
makes an existing variable refer to a new value (and stop referring to the old value).

    airtime_remaining = 15
    print(airtime_remaining)
    airtime_remaining = 7
    print(airtime_remaining)
    
 The output of this program is:
    15
    7
    
because the first time airtime_remaining is printed, its value is 15, and the second time, its value is 7.

It is especially important to distinguish between an assignment statement and a Boolean expression that tests for
equality. Because Python uses the equal token (=) for assignment, it is tempting to interpret a statement like a = b
as a Boolean test. Unlike mathematics, it is not! Remember that the Python token for the equality operator is ==.

Note too that an equality test is symmetric, but assignment is not. For example, if a == 7 then 7 == a. But in
Python, the statement a = 7 is legal and 7 = a is not.

In Python, an assignment statement can make two variables equal, but because further assignments can change either
of them, they don’t have to stay that way:
