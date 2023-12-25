import tkinter as tk
import random


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x_speed = random.choice([-2, 2])
        self.y_speed = -2

    def draw(self):
        self.canvas.move(self.id, self.x_speed, self.y_speed)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 or pos[3] >= 500:
            self.y_speed = -self.y_speed
        if pos[0] <= 0 or pos[2] >= 500:
            self.x_speed = -self.x_speed


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x_speed = 0
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x_speed, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= 500:
            self.x_speed = 0

    def move_left(self, event):
        self.x_speed = -3

    def move_right(self, event):
        self.x_speed = 3


def start_game():
    global paddle, ball
    paddle = Paddle(canvas, "blue")
    ball = Ball(canvas, "red")
    canvas.create_rectangle(0, 0, 500, 500, fill="black")
    canvas.pack()
    root.after(10, update)


def update():
    ball.draw()
    paddle.draw()
    if collide(ball, paddle):
        ball.y_speed = -ball.y_speed
    if ball.canvas.coords(ball.id)[3] >= 500:
        game_over()
    else:
        root.after(10, update)


def collide(ball, paddle):
    ball_pos = ball.canvas.coords(ball.id)
    paddle_pos = paddle.canvas.coords(paddle.id)
    if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
        if ball_pos[3] >= paddle_pos[1] and ball_pos[3] <= paddle_pos[3]:
            return True
    return False


def game_over():
    canvas.create_text(250, 250, text="Game Over", fill="white", font=("Helvetica", 24))


root = tk.Tk()
root.title("Breakout Game")
root.geometry("500x500")

canvas = tk.Canvas(root, bg="black", height=500, width=500)
canvas.pack()

start_game_button = tk.Button(root, text="Start Game", command=start_game)
start_game_button.pack()

root.mainloop()
