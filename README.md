guessMyNumber
A guessing game where the program stores a random generated integer whose value the user will have to guess.

What I did:

I used the random library class "randint()" function to specify the lower and upper range of a random number to generate. I used the variable "flag" to initialize the program condition to "True". Initialized the variable "guess" to start at zero. The "while" keyword specifies a loop control structure until the variable "flag" is set to "False" by the program. The game will start from the beginning using the "if not guess.isdigit()" if the user input is not an integer. The "elif int(guess) < num" tells the user the number is too low if the user's input is too low. The "elif (guess) > num" tells the user that the number is too high if the user's input is too high. The "else" keyword tells the user that the user's number is correct.

What I learned:

I learned how to use different variables; integers, strings, and boolean values. To store a random number, print strings containing output and the user's guess, and how to use a boolean value when the user guesses correctly.
