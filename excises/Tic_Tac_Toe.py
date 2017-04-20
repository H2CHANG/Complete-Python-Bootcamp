import numpy as np

result=[0,0,0,0,0,0,0,0,0]
marker = False

def show():
    for i in range(len(result)):
        #print(i)
        print(result[i],end='')
        if(i %3 == 2):
            print("\n------")
            continue
        print('|',end='')
def go_through():
    empty=[]
    for i in range(len(result)):
        if result[i] == 0:
            empty.append(i)
    return empty

def choice(empty):
    print("there is or are avaiable")
    print(empty)
    i = int(input("which one you choose"))
    return i

def set_position1(i):
    result[i] = '$'

def set_position2(i):
    result[i] = '*'

def player1():
    empty = go_through()
    i     = choice(empty)

    set_position1(i)


def player2():
    empty = go_through()
    i     = choice(empty)
    set_position2(i)

def test_row():
    player_1 = 0
    player_2 = 0
    row_array = np.array(result).reshape(3,3)
    for i in range(0,3):
        if row_array[i][0] == row_array[i][1] == row_array[i][2]:
            if row_array[i][0]== '$':
                player_1 +=1
            else:
                player_2 +=1
    return (player_1, player_2)


def test_col():
    player_1 = 0
    player_2 = 0
    row_array = np.array(result).reshape(3,3)
    for i in range(0,3):
        if row_array[0][i] == row_array[1][i] == row_array[2][i]:
            if row_array[0][i]== '$':
                player_1 +=1
            else:
                player_2 +=1
    return (player_1, player_2)

def test_cross():
    player_1 = 0
    player_2 = 0
    row_array = np.array(result).reshape(3,3)
    if row_array[0][0] == row_array[1][1] == row_array[2][2]:
            if row_array[0][0] == '$':
                player_1 +=1
            else:
                player_2 +=1
    if row_array[0][2] == row_array[1][1] == row_array[2][0]:
            if row_array[0][2]== '$':
                player_1 +=1
            else:
                player_2 +=1
    return (player_1, player_2)

def test_result():

   player_1, player_2 = test_row()
   i , j = test_col()
   player_1 += i
   player_2 += j
   i, j = test_cross()
   player_1 += i
   player_2 += j
   print("player_1 win",player_1, "lines")
   print("player_2 win",player_2, "lines")



def main():
    show()
    i = 0
    first = int(input("which one is first, 1 or 2"))
    if first == 1:
        while(i<9):
            if i % 2 == 0:
                player1()
                show()
            else:
                player2()
                show()
            i += 1
    else:
        while(i<9):
            if i %2 ==0:
                player2()
                show()
            else:
                player1()
                show()
            i += 1
    test_result()

main()
