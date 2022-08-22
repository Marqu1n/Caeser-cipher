## Made this program to learn more about python and its functionalities
I am still learning the basics of it

## The way the code works

At the start of the code the user need to choose what they want to do.
if they want to encode, decode with a key or decode by brute force.

After they choose, they type the message and the key (if it exists one).

Then I made 3 functions, one for each aswer for the direction input.

The encrypt and decrypt functions are very similar, for each letter of the message the code checks if is in the alphabet list. 
If it's on it, the code finds the index of the current letter on the alphabet and adds the shift number to the new index(in the decrypt function the code subtracts the shift number).
Then, to avoid the out of index error, the new index is the modulus, if the number is smaller than the length of the alphabet, it doesn't change it.
After that, I assign to the variable the letter that's in the new index.

The brute force function tries every possible with a finite loop that tries every number between 0 and the length of the alphabet.
