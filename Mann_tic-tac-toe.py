"""
# for this assignment, I think I will split this program into three different groups 
# One thru three, two thru six, and six thru nine.
# First, I will ask the user to give me a number, then assign that number to a function acording to their input.  

The program will print out three rows, 
and then using a for loop, will replace numbers with letters in the row acording to user input
"""
global victory_achieved
victory_achieved=False

row_one=[1,2,3]
row_two=[4,5,6]
row_thr=[7,8,9]

print(row_one)
print(row_two)
print(row_thr)

range_1=range(1,4)
range_2=range(3,7)
range_3=range(6,10)





def X_player_turn():
    player_input=int(input("Number? "))
    print(f"You picked {player_input}!")
    print()
    if player_input in range_1:
        print("Your in row one!")
        for slot in row_one:
            if slot == player_input:
                # print("Found It!")
                row_one[(slot)-1]="X"
                # print(row_one)
                # print()
            else:
                # print("Not Found")
                # print()
                pass

    elif player_input in range_2:
        print("Your in row two!")
        for slot in row_two:
            if slot == player_input:
                # print("Found It!")
                row_two[(slot)-4]="X"
                # print(row_two)
                # print()
            else:
                # print("Not Found")
                # print()
                pass
    elif player_input in range_3:
        print("Your in row three!")
        for slot in row_thr:
            if slot == player_input:
                #print("Found It!")
                row_thr[(slot)-7]="X"
                # print(row_thr)
                #print()
            else:
                #print("Not Found")
                #print()
                pass

    # elif player_input == None:
    #     print("No Input!")
    else:
        print("Not Valid")

def show_table():
    print(row_one)
    print(row_two)
    print(row_thr)

def O_player_turn():
    player_input=int(input("Number? "))
    print(f"You picked {player_input}!")
    print()
    if player_input in range_1:
        print("Your in row one!")
        for slot in row_one:
            if slot == player_input:
                # print("Found It!")
                row_one[(slot)-1]="O"
                # print(row_one)
                # print()
            else:
                # print("Not Found")
                # print()
                pass

    elif player_input in range_2:
        print("Your in row two!")
        for slot in row_two:
            if slot == player_input:
                # print("Found It!")
                row_two[(slot)-4]="O"
                # print(row_two)
                # print()
            else:
                # print("Not Found")
                # print()
                pass
    elif player_input in range_3:
        print("Your in row three!")
        for slot in row_thr:
            if slot == player_input:
                #print("Found It!")
                row_thr[(slot)-7]="O"
                # print(row_thr)
                #print()
            else:
                #print("Not Found")
                #print()
                pass

    # elif player_input == None:
    #     print("No Input!")
    else:
        print("Not Valid")

def victory_check():
    set_row_one=set(row_one)
    simplified_row=len(set_row_one)
    print(f"row one contains {simplified_row}")
    if simplified_row==1:
        print("Victory Achieved!")
        victory_achieved=1
        return victory_achieved
    else:
        pass

while victory_achieved != 1:
    X_player_turn()
    show_table()
    O_player_turn()
    show_table()
    #victory_check()