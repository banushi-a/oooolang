# oooolang
Esoteric Language Based on Circular Symbols

## BASICS
oooolang is similar to Brainf*ck and Turing Machines as they rely on tapehead memoory manipulation to perform their calculations. The following symbols are used to manipulate the tapehead:

O = increases memory pointer, or moves the pointer to the right 1 block.  

o = decreases memory pointer, or moves the pointer to the left 1 block.  

Ø = increases value stored at the block pointed to by the memory pointer  

ø = decreases value stored at the block pointed to by the memory pointer  

0 = like c while(cur_block_value != 0) loop.  

. = if block currently pointed to's value is not zero, jump back to [  

® = like c getchar(). input 1 character.  

© = like c putchar(). print 1 character to the console  

## Some rules:
Any arbitrary character besides the 8 listed above should be ignored by the compiler or interpretor.

All memory blocks on the "array" are set to zero at the beginning of the program. And the memory pointer starts out on the very left most memory block.

Loops may be nested as many times as you want. But all 0 must have a corresponding .
