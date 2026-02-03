import tkinter as tk
import random

# Declare some Constants
WIDTH = 600
HEIGHT = WIDTH*.8
PLAYER_SIZE = WIDTH/10
ENEMY_SIZE = WIDTH/11
MOVE_DISTANCE = PLAYER_SIZE

# Build *our* Window
window = tk.Tk()
window.title("Avoid the Falling Blocks")
phm_instructure = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
phm_instructure.pack()

# Make the Player
player = phm_instructure.create_rectangle(.4*WIDTH, HEIGHT-PLAYER_SIZE, .4*WIDTH+PLAYER_SIZE, HEIGHT, fill="magenta")

# Make a List to Hold Enemies
enemies = []

# Make an "Alive" Boolean
alive = True

# Stall for run_game
stall=True

# Movement Functions
def move_left(event):
    px1,py1,px2,py2 = phm_instructure.bbox(player)
    if px1 > 0 and alive:
        phm_instructure.move(player, -MOVE_DISTANCE, 0)
def move_right(event):
    px1,py1,px2,py2 = phm_instructure.bbox(player)
    if px2 < WIDTH and alive:
        phm_instructure.move(player, MOVE_DISTANCE, 0)

# Binding Buttons
window.bind("a", move_left)
window.bind("d", move_right)

# Enemies
def spawn_enemy():
    x = random.randint(0, 9)*WIDTH/10+WIDTH/20-ENEMY_SIZE/2
    enemy = phm_instructure.create_rectangle(x, HEIGHT/16-ENEMY_SIZE/2, x+ENEMY_SIZE, HEIGHT/16+ENEMY_SIZE/2, fill="cyan")
    enemies.append(enemy)

# Run the Game
def run_game():
    global alive, stall
    if not alive:
        phm_instructure.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="white", font=("Arial", WIDTH//20))
        return
    stall=not(stall)
    if stall:
        spawn_enemy()
    for enemy in enemies:
        phm_instructure.move(enemy, 0, HEIGHT/16)
        if phm_instructure.bbox(enemy) and phm_instructure.bbox(player):
            ex1,ey1,ex2,ey2 = phm_instructure.bbox(enemy)
            px1,py1,px2,py2 = phm_instructure.bbox(player)

            if ex1<px2 and ex2>px1 and ey1<py2 and ey2>py1:
                alive = False

    window.after(35, run_game)

run_game()
window.mainloop()