import time
from datetime import datetime
starttime = datetime.now()



final =""

row1 = [ 3, 5, 0, 7, 0, 0, 0, 8, 0]
row2 = [ 0, 0, 0, 0, 0, 9, 4, 2, 0]
row3 = [ 0, 7, 0, 0, 4, 8, 0, 0, 1]
row4 = [ 8, 0, 0, 0, 2, 4, 5, 0, 0]
row5 = [ 0, 0, 9 ,0, 3, 7, 0, 0, 2]
row6 = [ 0, 3, 0, 0, 0, 6, 7, 0, 0]
row7 = [ 7, 1, 0, 9, 0, 0, 0, 6, 0]
row8 = [ 4, 9, 5, 0, 6, 1, 8, 0, 0]
row9 = [ 0, 0, 0, 0, 0, 3, 1, 0, 0]

hrows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]





def getvertical(index):
    vrow = [row1[index], row2[index], row3[index], row4[index], row5[index], row6[index], row7[index], row8[index], row9[index]]
    return vrow

        



def getgroup(square):
    a1 = [row1[0], row1[1], row1[2], row2[0], row2[1], row2[2], row3[0], row3[1], row3[2]]
    a2 = [row1[3], row1[4], row1[5], row2[3], row2[4], row2[5], row3[3], row3[4], row3[5]]
    a3 = [row1[6], row1[7], row1[8], row2[6], row2[7], row2[8], row3[6], row3[7], row3[8]]

    b1 = [row4[0], row4[1], row4[2], row5[0], row5[1], row5[2], row6[0], row6[1], row6[2]]
    b2 = [row4[3], row4[4], row4[5], row5[3], row5[4], row5[5], row6[3], row6[4], row6[5]]
    b3 = [row4[6], row4[7], row4[8], row5[6], row5[7], row5[8], row6[6], row6[7], row6[8]]

    c1 = [row7[0], row7[1], row7[2], row8[0], row8[1], row8[2], row9[0], row9[1], row9[2]]
    c2 = [row7[3], row7[4], row7[5], row8[3], row8[4], row8[5], row9[3], row9[4], row9[5]]
    c3 = [row7[6], row7[7], row7[8], row8[6], row8[7], row8[8], row9[6], row9[7], row9[8]]
    if square == "a0":

        return a1
    if square == "a1":
        return a2
    if square == "a2":
        return a3
    if square == "b0":
        return b1
    if square == "b1":
        return b2
    if square == "b2":
        return b3
    if square == "c0":
        return c1
    if square == "c1":
        return c2
    if square == "c2":
        return c3

    
def gethorizontal(row, index):
    return row


def start():
    for row in hrows:
        for num in row:
            if num == 0:
                
                index = row.index(num)
                possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for num in gethorizontal(row, index):
                    if num in possible:
                        possible.remove(num)
                for num in getvertical(index):
                    if num in possible:
                        possible.remove(num)

                square = ""
                if hrows.index(row) in [0, 1 ,2]:
                    square = square + "a"
                elif hrows.index(row) in [3, 4 ,5]:
                    square = square + "b"
                else:
                    square = square + "c"
                add = ""
                if index in [0, 1 ,2]:
                    add = 0
                elif index in [3, 4, 5]:
                    add = 1
                elif index in [6, 7, 8]:
                    add = 2
                square = square + str(add)
                for num in getgroup(square):
                    if num in possible:
                        possible.remove(num)
                if len(possible) == 1:
                    row[index] = possible[0]
                else:
                    row[index] = 10
                
    

    tenc = 0
    print("----")
    for row in hrows:
        print(row)
        for num in row:
            if num == 10:
                tenc += 1
                row[row.index(num)] = 0
    return tenc

               
while start() != 0:

    for row in hrows:
        for num in row:
            if num == 10:
                row[row.index(num)] = 0
    start()

endtime = datetime.now()
delta = starttime- endtime
print("Completed puzzle!")
print("This took me ")
print(delta.total_seconds() * -1)
end = input()
