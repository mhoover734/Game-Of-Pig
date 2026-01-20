import random
potential_points = 0
final_points = 0
running = True
turn = "user"

def get_inputs():
    if turn_number > 1:
        while True:
            user_input = input("Enter a move (\"Hold\" or \"Bank\"): ").lower()
            if user_input not in ("hold", "bank"):
                print("Try Again")
            else:
                return(user_input)
    else:
        return("hold")

def game_turn(turn):
    global potential_points
    global final_points
    global running
    global turn_number
    end_turn = False
    turn_number = 1
    while not(end_turn):
        if turn == "user":
            move = get_inputs()
        else:
            move = "hold"
        if move == "hold":
            roll = random.randint(1,6)
            print(roll)
            if roll > 1:
                potential_points += roll
            else:
                potential_points = 0
                end_turn = True
        else:
            final_points += potential_points
            end_turn = True
        turn_number += 1
    print(final_points)
    running = False

while running:
    game_turn(turn)
            #if 1, delete potential points, end turn
            #otherwise, add to potential points and go back to getting inputs 
        #if bank, store points
            #turn potential points to final points

    #check for win
        #if win, tell user they win and give option to reset
        #continue to computer turn after reset

    #run computer turn, return to input select

    #check for loss
        #if loss, tell user they lost and give option to reset
        #continue to get inputs after reset

    #