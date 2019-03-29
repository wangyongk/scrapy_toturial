# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 21:15:04 2018

@author: wangyongkang
"""

"""
下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，
给你一个n行m列网格棋盘，棋盘的左下角有一匹马，
请你计算至少需要几步可以将它移动到棋盘的右上角，
若无法走到，则输出-1.
如n=1，m=2,则至少需要1步；
若n=1，m=3,则输出-1。
"""

from collections import deque
 
def BFS(n,m):
	dx = [-1,-1,1,1,-2,-2,2,2]
	dy = [-2,2,-2,2,-1,1,-1,1]
	v = {(x,y):False for x in range(0,n+1) for y in range(0,m+1)}
	v[(0,0)] = True
	q = deque([(0,0,0)])
	while len(q)>0:
		p = q.pop()
		if p[0]==n and p[1]==m:
			return p[2]
		for i in range(0,8):
			x = p[0] + dx[i]
			y = p[1] + dy[i]
			if x>=0 and x<=n and y>=0 and y<=m and v[(x,y)]==False:
				v[(x,y)] = True
				q.append((x,y,p[2]+1))
	return -1
	
print(BFS(3,3))

print("123")
