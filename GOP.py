import random
points = {"user": 0, "bot": 0}
running = True
total_turns = 1
stall = True

def win_check(temp, turn):
    global points, total_turns, stall
    if points[turn] + temp >= 100:
        if turn == "user":
            print(f"The {turn} won!\nThe score was {points["user"]+temp} to {points["bot"]}.\nStarting new game...\n")
        else:
            print(f"The {turn} won!\nThe score was {points["user"]} to {points["bot"]+temp}.\nStarting new game...\n")
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
    print(f"\nIt's the {turn}'s turn!")
    print(f"The score is currently {points["user"]} to {points["bot"]}.")
    while not(end_turn):
        if win_check(potential_points, turn):
            break
        if turn_number != 1:
            print(f"The {turn} has {potential_points} unbanked points, making a potential score of {points[turn]+potential_points}.")
        if turn == "user":
            if turn_number == 1:
                move = "hold"
            else:
                while True:
                    user_input = input("Enter a move (\"Hold\" or \"Bank\"): ").lower()
                    if user_input not in ("hold", "bank"):
                        print("Unrecognized input, try again.")
                    else:
                        move = user_input
                        break
        elif potential_points > 18:
            move = "bank"
        else:
            move = "hold"
        if move == "hold":
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
    input("Press Enter to continue.")

def total_turn_calc():
    global total_turns, stall
    if stall == False:
        stall = True
        total_turns += 1
        print(f"\n{"-"*20} Turn {total_turns} {"-"*20}")
    else:
        stall = False

print(f"\n{"-"*20} Turn {total_turns} {"-"*20}")
while running:
    game_turn("user")
    total_turn_calc()
    game_turn("bot")
    total_turn_calc()