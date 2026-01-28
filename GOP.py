import random
points = {"user": 0, "bot": 0}
total_turns = 1
stall = True

def win_check(temp, turn):
    global points, total_turns, stall
    if points[turn] + temp >= 100:
        if turn == "user":
            print(f"\nThe {turn} won!\nThe score was {points["user"]+temp} to {points["bot"]}.\nStarting new game...\n")
        else:
            print(f"\nThe {turn} won!\nThe score was {points["user"]} to {points["bot"]+temp}.\nStarting new game...\n")
        points["user"] = 0
        points["bot"] = 0
        total_turns = 0
        stall = False
        return True
    return False

def game_turn(turn):
    global running, points
    end_turn = False
    turn_number = 1
    potential_points = 0
    print(f"\nIt's the {turn}'s turn!\n")
    print(f"The score is currently {points["user"]} to {points["bot"]}.")
    while not(end_turn):
        if win_check(potential_points, turn):
            break
        if turn_number != 1:
            print(f"The {turn} has {potential_points} unbanked points, making a potential score of {points[turn]+potential_points}.")
        if turn == "user":
            if turn_number == 1:
                move = "roll"
            else:
                while True:
                    user_input = input("Enter a move -- \"(R)oll\" or \"(B)ank\": ").lower()
                    if user_input not in ("roll", "bank", "r", "b", "quit"):
                        print("Unrecognized input, try again.")
                    elif user_input == "quit":
                        return "quit"
                    else:
                        move = user_input
                        break
        elif potential_points > 18:
            move = "bank"
        else:
            move = "roll"
        if move in ("roll", "r"):
            roll = random.randint(1, 6)
            print(f"The {turn} rolled a {roll}.")
            if roll == 1:
                potential_points = 0
                end_turn = True
                print(f"The {turn}'s turn ended.")
            else:
                potential_points += roll
        else:
            print(f"Stored {potential_points} points.")
            points[turn] += potential_points
            end_turn = True
        turn_number += 1
        if not(end_turn) and turn == "bot":
            if input("Press Enter to continue. ").lower() == "quit":
                return "quit"
    if input("Press Enter to continue. ").lower() == "quit":
        return "quit"

def total_turn_calc():
    global total_turns, stall
    if stall == False:
        stall = True
        total_turns += 1
        print(f"\n{"-"*20} Turn {total_turns} {"-"*20}")
    else:
        stall = False

print(f"\nAt any time, enter \"quit\" to quit.\n\n{"-"*20} Turn {total_turns} {"-"*20}")
while True:
    if game_turn("user") == "quit":
        break
    total_turn_calc()
    if game_turn("bot") == "quit":
        break
    total_turn_calc()
print("\nQuitting...\n")