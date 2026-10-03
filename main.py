"""
Python Logo Drawing using Turtle Graphics
Customized and Refactored
"""

import turtle


class PythonLogo:
    def __init__(self, t: turtle.Turtle):
        self.t = t
        self.blue_color = "#366994"
        self.yellow_color = "#FFD43B"

    def draw_curve(self):
        for _ in range(5):
            self.t.right(15)
            self.t.forward(15)

    def blue_part(self):
        self.t.penup()
        self.t.pencolor(self.blue_color)
        self.t.fillcolor(self.blue_color)
        self.t.goto(-110, -100)
        self.t.pendown()
        self.t.begin_fill()
        self.t.right(180)
        self.t.forward(100 / 3)

        self.draw_curve()
        self.t.forward(15)
        self.t.right(5)
        for _ in range(5):
            self.t.forward(15)
            self.t.right(5)
        self.t.forward(27.58789)
        self.draw_curve()

        self.t.goto(0, 100)
        self.t.goto(0, 110)
        self.t.goto(-100, 110)
        self.t.goto(-100, 110 + 100 / 3)
        self.t.left(90)

        self.draw_curve()
        self.t.forward(15)
        self.t.right(5)
        for _ in range(5):
            self.t.forward(15)
            self.t.right(5)
        self.t.forward(27.58789)
        self.draw_curve()

        self.t.forward(70)

        self.draw_curve()
        self.t.right(5)
        self.t.goto(-70, 10)

        for _ in range(5):
            self.t.left(15)
            self.t.forward(15)
        self.t.left(5)

        self.t.goto(-110, -100)
        self.t.end_fill()

    def yellow_part(self):
        self.t.penup()
        self.t.pencolor(self.yellow_color)
        self.t.fillcolor(self.yellow_color)
        self.t.goto(110, 100)
        self.t.right(90)
        self.t.pendown()
        self.t.begin_fill()
        self.t.right(180)
        self.t.forward(100 / 3)

        self.draw_curve()
        self.t.forward(15)
        self.t.right(5)
        for _ in range(5):
            self.t.forward(15)
            self.t.right(5)
        self.t.forward(27.58789)
        self.draw_curve()

        self.t.goto(0, -100)
        self.t.goto(0, -110)
        self.t.goto(100, -110)
        self.t.goto(100, -110 - 100 / 3)
        self.t.left(90)

        self.draw_curve()
        self.t.forward(15)
        self.t.right(5)
        for _ in range(5):
            self.t.forward(15)
            self.t.right(5)
        self.t.forward(27.58789)
        self.draw_curve()

        self.t.forward(70)

        self.draw_curve()
        self.t.right(5)
        self.t.goto(70, -10)

        for _ in range(5):
            self.t.left(15)
            self.t.forward(15)
        self.t.left(5)

        self.t.goto(110, 100)
        self.t.end_fill()

    def eyes(self):
        # Blue Snake eyes
        self.t.penup()
        self.t.fillcolor("white")
        self.t.pencolor("white")
        self.t.goto(-70, 130)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(10)
        self.t.end_fill()

        # Yellow Snake eyes
        self.t.penup()
        self.t.goto(90, -130)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(10)
        self.t.end_fill()

        self.t.hideturtle()


def main():
    screen = turtle.Screen()
    screen.title("Python Official Logo - Turtle Graphics")
    screen.bgcolor("#ffffff")

    t = turtle.Turtle()
    t.speed(5)  # Normal speed

    logo = PythonLogo(t)
    logo.blue_part()
    logo.yellow_part()
    logo.eyes()

    screen.mainloop()


if __name__ == "__main__":
    main()
