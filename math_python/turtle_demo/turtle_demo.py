import turtle
"""
python的turtle模块：
https://docs.python.org/zh-cn/3/library/turtle.html?highlight=turtle#turtle.forward
TurtleScreen/Screen 方法
    窗口控制
        bgcolor() 背景颜色
        bgpic() 背景图片
        clearscreen()
        resetscreen()
        screensize() 屏幕大小
        setworldcoordinates() 设置世界坐标系
    动画控制
        delay() 延迟
        tracer() 追踪
        update() 更新
    使用屏幕事件
        listen() 监听
        onkey() | onkeyrelease() 当键盘按下并释放
        onkeypress() 当键盘按下
        onclick() | onscreenclick() 当点击屏幕
        ontimer() 当达到定时
        mainloop() | done() 主循环
    设置与特殊方法
        mode()
        colormode() 颜色模式
        getcanvas() 获取画布
        getshapes() 获取形状
        register_shape() | addshape() 添加形状
        turtles() 所有海龟
        window_height() 窗口高度
        window_width() 窗口宽度
    输入方法
        textinput() 文本输入
        numinput() 数字输入
    Screen 专有方法
        bye() 退出
        exitonclick() 当点击时退出
        setup() 设置
        title() 标题
  ----------------------------------------------------------------------------      
海龟动作
    移动和绘制
        forward() | fd() 前进
        backward() | bk() | back() 后退
        right() | rt() 右转
        left() | lt() 左转
        goto() | setpos() | setposition() 前往/定位
        setx() 设置x坐标
        sety() 设置y坐标
        setheading() | seth() 设置朝向  
        home() 返回原点
        circle() 画圆
        dot() 画点
        stamp() 印章
        clearstamp() 清除印章
        clearstamps() 清除多个印章
        undo() 撤消
        speed() 速度
    获取海龟的状态
        position() | pos() 位置
        towards() 目标方向
        xcor() x坐标
        ycor() y坐标
        heading() 朝向
        distance() 距离
    设置与度量单位
        degrees() 角度
        radians() 弧度
    --------------------------------------------------------------
画笔控制
    绘图状态
        pendown() | pd() | down() 画笔落下
        penup() | pu() | up() 画笔抬起
        pensize() | width() 画笔粗细
        pen() 画笔
        isdown() 画笔是否落下
    颜色控制
        color() 颜色
        pencolor() 画笔颜色
        fillcolor() 填充颜色
    填充
        filling() 是否填充
        begin_fill() 开始填充
        end_fill() 结束填充
    更多绘图控制
        reset() 重置
        clear() 清空
        write() 书写
    -------------------------------------
海龟状态
    可见性
        showturtle() | st() 显示海龟
        hideturtle() | ht() 隐藏海龟
        isvisible() 是否可见
    外观
        shape() 形状
        resizemode() 大小调整模式
        shapesize() | turtlesize() 形状大小
        shearfactor() 剪切因子
        settiltangle() 设置倾角
        tiltangle() 倾角
        tilt() 倾斜
        shapetransform() 变形
        get_shapepoly() 获取形状多边形
    使用事件
        onclick() 当鼠标点击
        onrelease() 当鼠标释放
        ondrag() 当鼠标拖动
    特殊海龟方法
        begin_poly() 开始记录多边形
        end_poly() 结束记录多边形
        get_poly() 获取多边形
        clone() 克隆
        getturtle() | getpen() 获取海龟画笔
        getscreen() 获取屏幕
        setundobuffer() 设置撤消缓冲区
        undobufferentries() 撤消缓冲区条目数
"""


class Boy(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.screen_width, self.screen_height = self.getscreen().screensize()

    def draw_wall(self):
        self.pensize(3)
        self.penup()
        self.sety(self.screen_height/2)
        self.pendown()
        self.right(90)
        self.forward(self.screen_height/2)
        self.right(90)
        self.circle(20, 180)
        self.right(90)
        self.forward(self.screen_height/2)

    def draw_heart(self):
        self.pensize(3)
        self.pencolor('red')
        self.penup()
        self.setpos(-80, self.screen_height/2-80)
        self.pendown()
        self.left(90)
        self.pensize(10)
        self.begin_fill()
        self.circle(25, 230)
        self.pensize(10)
        self.forward(70)
        self.seth(40)
        self.forward(70)
        self.right(5)
        self.circle(25, 210)
        self.seth(30)
        self.fillcolor("red")
        self.end_fill()
        self.seth(-90)
        self.pensize(3)
        self.forward(30)
        self.penup()
        self.setpos(-80, self.screen_height/2-200)
        self.pencolor('black')
        self.pendown()
        self.write("Long live the Queen!", True, align="center")

    def draw_boy(self):
        self.penup()
        self.sety(self.screen_height/2-60)
        self.pendown()
        self.setheading(90)
        self.circle(-65, 240)
        self.left(80)
        self.forward(220)
        self.penup()
        self.setpos(40, self.screen_height/2-40)
        self.pendown()
        self.dot(13, 'black')
        self.penup()
        self.setpos(90, self.screen_height/2-65)
        self.pendown()
        self.dot(13, 'black')
        self.penup()
        self.setpos(42, self.screen_height/2-90)
        self.left(45)
        self.pendown()
        self.forward(5)
        self.left(45)
        self.forward(5)
        self.right(45)
        self.forward(5)
        self.left(45)
        self.forward(5)
        self.penup()
        self.setpos(16, self.screen_height/2-58)
        self.pendown()
        self.pencolor('pink')
        self.pensize(10)
        self.right(135)
        self.forward(10)
        self.penup()
        self.setpos(100, self.screen_height/2-90)
        self.pendown()
        self.forward(10)
        self.left(135)
        self.right(45)

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.title('比心小子')
    screen.bgcolor('white')
    # screen.screensize(2000, 1500)
    boy = Boy()
    boy.draw_wall()
    boy.draw_boy()
    boy.draw_heart()
    screen.mainloop()



"""def square(side_length=100, right_angle=90):
    for i in range(4):
        forward(side_length)
        right(right_angle)
shape('turtle')
side_length = 5
for i in range(60):
    side_length += 5
    square(side_length)
    right(5)"""
