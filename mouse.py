from pymouse import PyMouse

m = PyMouse()

# 获取当前位置
print(m.position())
# 移动位置
m.move(1200, 900)
# 移动并且在xy位置点击,1位左键点击，2为右键点击
m.click(177, 170, 2)
# 获取当前屏幕的尺寸
x, y = m.screen_size()
print(x)
print(y)