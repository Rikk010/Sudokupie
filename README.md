# Sudokupie
My try on sudoku solving


This will not solve all sudokus

It works like this:

All zeros are unknowns, it loops trough each list searching for a 0,
if it finds one it creates a list [1, 2, 3, 4, 5, 6, 7, 8, 9] and for every number in the horizontal, vertical row and the 3x3 where the 0 is in, it removes it from the list. If 1 number is left the 0 turns to that number otherwise it turns it to a 10.

When the whole loop is done it changes the 10's to 0's and does the same
It stops when no 0's and 10's are left
