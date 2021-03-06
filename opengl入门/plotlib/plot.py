from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def drawLine(X, Y, rgb=(0,0,0), ltype =None,lwidth=1,z=0):
    '''

    :param X:
    :param Y:
    :param rgb: 线段颜色
    :param z: z的坐标
    :return:
    '''

    maxV = max(max(X), max(Y))
    # print(maxV)
    # 对x和y的数据进行放缩
    X= X /maxV
    Y = Y/ maxV


    glLineWidth(lwidth)  # 设置线的宽度，单位是像素

    if ltype == None:
        glLineStipple(1, 0xFFFF);  # 设置线型,直线
    else:
        glLineStipple(1, 0x00FF);  # 设置线型,虚线


    glShadeModel(GL_SMOOTH)  # 开启对颜色的线性插值

    if len(X) == len(Y):
        glBegin(GL_LINE_STRIP)  # 绘制连续线段
        glColor4f(rgb[0], rgb[1], rgb[2], 1)
        for i in range(len(X)):
            glVertex3f(X[i], Y[i], z)

        glEnd()

    else:
        assert '数据错误xy数据维度不一样'
        return False


def drawPoints(X, Y, rgb=(0,0,0), size =1,z=0):
    maxV = max(max(X), max(Y))
    # print(maxV)
    # 对x和y的数据进行放缩
    X= X /maxV
    Y = Y/ maxV


    glPointSize(size)  # 设置点的大小



    glShadeModel(GL_SMOOTH)  # 开启对颜色的线性插值

    if len(X) == len(Y):

        glBegin(GL_POINTS)  # 绘制点
        glColor4f(rgb[0], rgb[1], rgb[2], 1)
        for i in range(len(X)):
            glVertex3f(X[i], Y[i], z)

        glEnd()

    else:
        assert '数据错误xy数据维度不一样'
        return False