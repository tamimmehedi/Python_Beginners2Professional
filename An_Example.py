The following program implements a simple guessing game:

  import random        # We cover random numbers in the
  rng = random.Random()# modules chapter, so peek ahead if you  want. "rng" stands for "random number generator".
  number = rng.randrange(1, 1000) # Get random number between [1 and 1000).

  guesses = 0
  message = ""

  while True:
    guess = int(input(message + "\nGuess my number between 1 and 1000: "))
    guesses += 1
    if guess > number:
      message += str(guess) + " is too high.\n"
    elif guess < number:
       message += str(guess) + " is too low.\n"
    else:
      break
  input("\n\nGreat, you got it in "+str(guesses)+" guesses!\n\n")

This program makes use of the mathematical law of trichotomy (given real numbers a and b, exactly one of these
three must be true: a > b, a < b, or a == b).
At line 18 there is a call to the input function, but we don’t do anything with the result, not even assign it to a variable.
This is legal in Python. Here it has the effect of popping up the input dialog window and waiting for the user to respond
before the program terminates. Programmers often use the trick of doing some extra input at the end of a script, just
to keep the window open.
Also notice the use of the message variable, initially an empty string, on lines 6, 12 and 14. Each time through the
loop we extend the message being displayed: this allows us to display the program’s feedback right at the same place
as we’re asking for the next guess.
