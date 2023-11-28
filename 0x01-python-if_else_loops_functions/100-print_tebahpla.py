#!/usr/bin/python3
# Print the alphabet in reverse order
# alternating upper and lower case

for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - 32 if c % 2 == 1 else c)), end="")
