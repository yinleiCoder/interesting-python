import turtle, random, time
"""
turtle模块：https://docs.python.org/zh-cn/3/library/turtle.html?highlight=turtle#turtle.forward
"""

class BinayTree(turtle.Turtle):
    def __init__(self, scale_factor=0.2):
        super(BinayTree, self).__init__()
        self.hideturtle()
        self.getscreen().tracer(5, 0)
        self.scale_factor=scale_factor

    def draw_tree_branch(self, branch):
        """
        递归画二叉树
        :param branch: 分支数
        :param t: turtle画笔
        :return: None
        """
        time.sleep(0.0005)
        if branch > 3:
            if 8 <= branch <= 12:
                if random.randint(0, 2) == 0:
                    self.pencolor('lightcoral')
                else:
                    self.pencolor('green')
                self.pensize(branch / 3)
            elif branch < 8:
                if random.randint(0, 1) == 0:
                    self.pencolor('lightcoral')
                else:
                    self.pencolor('green')
                self.pensize(branch / 2)
            else:
                self.pencolor('sienna')
                self.pensize(branch / 10)
            self.forward(branch)
            left = 1.5 * random.random()
            self.right(20 * left)
            right = 1.5 * random.random()
            self.draw_tree_branch(branch - 10 * right)
            self.left(40 * left)
            self.draw_tree_branch(branch - 10 * right)
            self.right(20 * left)
            self.penup()
            self.backward(branch)
            self.pendown()

    def draw_girl_firend_name(self, text):
        """
        画文字
        :param text: 要画的文字
        :return: None
        """
        self.penup()
        self.home()
        self.pencolor('black')
        self.forward(100)
        self.right(90)
        self.forward(50)
        self.pendown()
        self.write(text)
        self.penup()
        self.forward(5)
        self.pendown()

    def draw_flower(self):
        """
        画个小花
        :return:
        """
        self.pencolor('lightcoral')
        self.pensize(1)
        self.setheading(270)
        self.penup()
        self.forward(50)
        self.pendown()
        self.setheading(90)
        for _ in range(36):
            for i in range(4):
                self.forward(40)
                self.right(90)
            self.right(10)
        self.pencolor('black')
        self.setheading(270)
        self.forward(50)

if __name__ == '__main__':
    tree = BinayTree()
    screen = turtle.Screen()
    screen.title('吹梦到西州（BGM）')
    screen.bgcolor('white')
    tree.left(90)
    tree.penup()
    tree.backward(150)
    tree.pendown()
    tree.pencolor('sienna')
    tree.draw_tree_branch(60)
    tree.draw_girl_firend_name('究竟是树劈了腿，还是我们的爱出了轨~')
    tree.draw_flower()
    screen.exitonclick()
