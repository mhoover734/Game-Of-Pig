import tkinter as tk
import random

WIDTH = 550
HEIGHT = 400

#Make sprites
def random_bright_color():
    return f"{random.randint(100,255):x}{random.randint(100,255):x}{random.randint(100,255):x}"
def make_enemy_sprite():
    pattern = [
        "00100000100",
        "00010001000",
        "00111111100",
        "01101110110",
        "11111111111",
        "10111111101",
        "10100000101",
        "00011011000"]
    h = len(pattern)
    w = len(pattern[0])
    img = tk.PhotoImage(width=w, height=h)
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("#"+str(random_bright_color()), (x,y))
    return img
def make_player_sprite():
    h=16
    w=22
    img=tk.PhotoImage(width=w,height=h)
    for y in range(h):
        for x in range(w):
            if 6<=x<=17 and y>=6:
                img.put("white", (x,y))
    return img

root = tk.Tk()
root.title("COSMOS INFILTRATORS")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

player_img = make_player_sprite()
enemy_img = make_enemy_sprite()

ROWS = 4
COLUMNS = 8
CELL = 32

#Make enemies
enemies = []
def create_enemy_formation():
    enemies.clear()
    start_x=100
    start_y=60
    for r in range(ROWS):
        for c in range(COLUMNS):
            x = start_x+c*CELL
            y = start_y+r*CELL
            e = canvas.create_image(x,y,image=enemy_img, anchor="nw")
            enemies.append(e)

#Movements
def move_left(event):
    canvas.move(player, -22, 0)
def move_right(event):
    canvas.move(player, 22, 0)

#Shooting Lasers
lasers = []
def make_laser_sprite():
    img=tk.PhotoImage(width=4,height=10)
    for y in range(10):
        for x in range(4):
            img.put("red", (x,y))
    return img
laser_img = make_laser_sprite()
def shoot(event):
    if len(lasers)>0:
        return
    px1,py1,px2,py2 = canvas.bbox(player)
    l = canvas.create_image((px1+px2)//2, py1, image=laser_img, anchor="s")
    lasers.append(l)
    
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("a", move_left)
root.bind("d", move_right)
root.bind("<space>", shoot)

#Collisions
def collision(a, l):
    #px1, py1, px2, py2 = canvas.bbox()
    ax1, ay1, ax2, ay2 = canvas.bbox(a) #Alien
    lx1, ly1, lx2, ly2 = canvas.bbox(l) #Laser
    return ax1<lx2 and ax2>lx1 and ay1<ly2 and ay2>ly1


#Formation movement
enemy_dx = 4
def move_enemies():
    global enemy_dx
    hit_wall = False
    for enemy in enemies:
        x1, y1, x2, y2 = canvas.bbox(enemy)
        if x2>= WIDTH-10 and enemy_dx > 0:
            hit_wall = True
        if x1 <= 10 and enemy_dx < 0:
            hit_wall = True
    if hit_wall:
        enemy_dx = -enemy_dx #EEEEEEEEEEVILLLLLLLLLLL------------------------------------------
        for enemy in enemies:
            canvas.move(enemy, 0, 15)
    else:
        for enemy in enemies:
            canvas.move(enemy, enemy_dx, 0)
def move_lasers():
    for laser in lasers[:]:
        canvas.move(laser, 0, -15)
        x1, y1, x2, y2 = canvas.bbox(laser)
        if y2 < 0:
            canvas.delete(laser)
            lasers.remove(laser)


#Game loop
alive = True
def game_loop():
    global alive
    if not alive:
        canvas.delete(all) #IMPORTANT----------------------------------------------------------------------------
        canvas.create_text(WIDTH//2, HEIGHT//2, text="GAMER OVER", fill="red", font=("Arial",24))
        return
    move_enemies()
    move_lasers()
    for laser in lasers[:]:
        for enemy in enemies[:]:
            if collision(laser,enemy):
                canvas.delete(laser)
                canvas.delete(enemy)
                #if laser in lasers:
                lasers.remove(laser)
                #if enemy in enemies:
                enemies.remove(enemy)
                break
    for enemy in enemies:
        ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
        px1, py1, px2, py2 = canvas.bbox(player)
        if ey2 >= py1:
            alive = False




    root.after(40, game_loop)

#Start & reset game
def start():
    global player
    player = canvas.create_image(WIDTH//2-player_img.width()//2, HEIGHT*.9, image=player_img, anchor="center")
    game_loop()

def reset(event=None):
    global alive, enemy_dx
    canvas.delete("all")
    lasers.clear()
    enemies.clear()
    alive = True
    enemy_dx = 4
    create_enemy_formation()
    start()
root.bind("r", reset)
reset()
root.mainloop()