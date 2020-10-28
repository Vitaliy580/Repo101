from tkinter import *

WIDTH = 900
HEIGHT = 300

PAD_W = 10
PAD_H = 100

BALL_RADIUS = 30

BALL_X_CHANGE = 20
BALL_Y_CHANGE = 0

root = Tk()
root.title("Ping Pong")

c = Canvas(root, width=WIDTH, height=HEIGHT, background="#008B8B")
c.pack()

BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2, HEIGHT/2-BALL_RADIUS/2, WIDTH/2+BALL_RADIUS/2, HEIGHT/2+BALL_RADIUS/2, fill="white")

LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="#Da70D6")

RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2, PAD_H, width=PAD_W, fill="#Da70D6")

PAD_SPEED = 20
LEFT_PAD_SPEED = 0
RIGHT_PAD_SPEED = 0

BALL_SPEED_UP = 1.00
BALL_MAX_SPEED = 30
BALL_X_SPEED = 20
BALL_Y_SPEED = 20
right_line_distance = WIDTH - PAD_W

def move_ball():
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center = (ball_top + ball_bot) / 2

def move_pads():
    PADS = {LEFT_PAD:LEFT_PAD_SPEED,
            RIGHT_PAD:RIGHT_PAD_SPEED}
    for pad in PADS:
        c.move(pad, 0, PADS[pad])
        if c.coords(pad)[1]< 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])


def main():
    move_ball()
    move_pads()
    root.after(30, main)

c.focus_set()

def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED

c.bind("<KeyPress>", movement_handler)

def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0

c.bind("<KeyRelease>", stop_pad)

main()

root.mainloop()