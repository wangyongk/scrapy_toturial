# # -*- coding: utf-8 -*-
# """
# Created on Tue Jul 31 07:38:45 2018
#
# @author: wangyongkang
# """
#
# num = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
# unit = ['亿', '万', '仟', '佰', '拾', '']
# baseList = [100000000, 10000, 1000, 100, 10, 1, 0]
# level=2
# base = baseList[level]
# print(base)


import pygame

pygame.init()
screen = pygame.display.set_caption('康托尘埃')
screen = pygame.display.set_mode([487, 487])
screen.fill([255, 255, 255])
pygame.display.flip()

cantor = [1, ]  # 起点集，最小像素为1

while (cantor[-1] + 1) * 3 < 1000:
    st = (cantor[-1] + 1) * 2  # 下一迭代起点
    tep = []
    for i in cantor:
        tep.append(st + i)  # 重复上一子集
    cantor.extend(tep)
# print(cantor[-1]) # 输出最大像素起点
for i in cantor:
    for j in cantor:
        screen.set_at([i, j], [0, 0, 0])
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


# import turtle as tl
#
# def draw_smalltree(tree_length,tree_angle):
#     '''
#     绘制分形树函数
#     '''
#     if tree_length >= 3:
#         tl.forward(tree_length) #往前画
#         tl.right(tree_angle)  #往右转
#         draw_smalltree(tree_length - 10,tree_angle)#画下一枝，直到画到树枝长小于3
#
#         tl.left(2 * tree_angle)  #转向画左
#         draw_smalltree(tree_length -10,tree_angle) #直到画到树枝长小于3
#
#         tl.rt(tree_angle) #转到正向上的方向，然后回溯到上一层
#         if tree_length <= 30:  #树枝长小于30，可以当作树叶了，树叶部分为绿色
#             tl.pencolor('green')
#         if tree_length > 30:
#             tl.pencolor('brown')  #树干部分为棕色
#         tl.backward(tree_length)  #往回画，回溯到上一层
#
#
#
# def main():
#     tl.penup()
#     #tl.pencolor('green')
#     tl.left(90)  #因为树是往上的，所以先把方向转左
#     tl.backward(250) #把起点放到底部
#     tl.pendown()
#     tree_length = 100  #我设置的最长树干为100
#     tree_angle = 20  #树枝分叉角度，我设为20
#     draw_smalltree(tree_length,tree_angle)
#     tl.exitonclick()  #点击才关闭画画窗口
#
# if __name__ == '__main__':
#     main()

#
# from tkinter import *
# from random import randint
#
# def paint(LX1, LX2, LY1, LY2):
#     xscale = float(canvas["width"]) / (LX2 - LX1)
#     yscale = float(canvas["height"]) / (LY2 - LY1)
#     xstep = (LX2 - LX1) / (float(canvas["width"]))
#     ystep = (LY2 - LY1) / (float(canvas["height"]))
#     x = LX1
#     while x < LX2:
#         y = LY1
#         while y < LY2:
#             c = count(complex(x, y))
#             if c == COUNT_LIMIT:
#                 color = "black"
#             else:
#                 color = random_color[c-1]
#             canvas.create_rectangle((x - LX1) * xscale, (y - LY1) * yscale,
#                                     (x - LX1) * xscale, (y - LY1) * yscale, fill=color, outline = color, tags="pic")
#             y += ystep
#         x += xstep
#
# def count(c):
#     z = complex(0,0)
#     for i in range(COUNT_LIMIT):
#         z = z*z + c
#         if abs(z) > 2: return i
#     return COUNT_LIMIT
#
# COUNT_LIMIT = 1000
# LX1 = -2.0
# LX2 = 2.0
# LY1 = -2.0
# LY2 = 2.0
#
# random_color = []
# for i in range(COUNT_LIMIT):
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#
#     r = "%02x" % r
#     g = "%02x" % g
#     b = "%02x" % b
#     random_color.append("#"+r+g+b)
# window = Tk()
# window.title("曼德布罗特分形")
#
# canvas = Canvas(window, width=500, height=500, bg="white")
# canvas.pack()
#
# paint(LX1, LX2, LY1, LY2)
#
# window.mainloop()