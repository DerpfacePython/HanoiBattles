import random, sys

towers = [["R8", "R7", "R6", "R5", "R4", "R3", "R2", "R1"], [], [], [], [], [], [], [], [], [],
          ["B8", "B7", "B6", "B5", "B4", "B3", "B2", "B1"]]
coded_output = []
turn = 0
turn_ids = ["R", "B"]
checkr = 0
checkb = 0
invalid_move = 0


# The main Hanoi function.
def play_hanoi(input_string):
    global turn, checkr, checkb, invalid_move
    if invalid_move == 5:
        print("Bot " + str(turn) + " loses!")
        sys.exit()
    coded_output = []
    user_input = input_string.split(" ")
    block = turn_ids[turn] + user_input[0]
    for a in range(6):
        if block in towers[a] and block == towers[a][-1]:
            if int(user_input[1]) == 10 and turn == 0 and len(towers[10]) != 0 and checkr == 0:
                print("This move is not allowed.")
                invalid_move += 1
                play_hanoi(input_string)
                return None
            elif len(towers[10]) == 0:
                checkr += 1
            if int(user_input[1]) == 0 and turn == 1 and len(towers[0]) != 0 and checkb == 0:
                print("This move is not allowed.")
                invalid_move += 1
                play_hanoi(input_string)
            elif len(towers[0]) == 0:
                checkb += 1
            del towers[a][-1]
            try:
                block_under = towers[int(user_input[1])][-1]
            except IndexError:
                block_under = None
            if block_under == None or int(block_under[1]) > int(block[1]):
                invalid_move = 0
                towers[int(user_input[1])].append(block)
                for a in range(len(towers)):
                    coded_output.append("".join(towers[a]))
                coded_output = "/".join(coded_output)
                print(coded_output)
                if turn == 0:
                    turn = 1
                    play_hanoi(random_bot(coded_output))
                else:
                    turn = 0
                    play_hanoi(random_bot(coded_output))
            else:
                print("This move is not allowed.")
                invalid_move += 1
                play_hanoi(input_string)
        else:
            print("This move is not allowed.")
            invalid_move += 1
            play_hanoi(input_string)


# BOTS
def random_bot(output_string):
    return str(random.randint(1, 9)) + " " + str(random.randint(1, 9))

# Initialisation.
for b in range(len(towers)):
    coded_output.append("".join(towers[b]))
coded_output = "/".join(coded_output)
play_hanoi(random_bot(coded_output))
