import pygame
import numpy as np 
import math
import random 
class Ball : 
	def __init__(self,position,veloccity):# tao 1 chuoi qua bong
		self.pos = np.array(position,dtype=np.float64)
		self.v = np.array(veloccity,dtype=np.float64)
		self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.is_in = True 
def ball_arc(i_,I_,s,e):
	dx = i_[0] - I_[0]
	dy = i_[1] - I_[1]
	ball_ = math.atan2(dy,dx) # tìm góc của quả bóng 
	s = s % ( 2 * math.pi)
	e = e % ( 2 * math.pi)
	if s > e:
		e += 2 * math.pi
	if s <= ball_ <= e or (s <= ball_ + 2 *math.pi <= e):
		return True 


def draw_arc(window,center,radius,s,e):
	p1 = center + (radius*1000) * np.array([math.cos(s),math.sin(s)])
	p2 = center + (radius*1000) * np.array([math.cos(e),math.sin(e)])
	pygame.draw.polygon(window,BLACK,[center,p1,p2],0)

pygame.init()
WIDTH = 800 # chieu dai
HEIGHT = 800 # chieu rong
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
BLACK = (0,0,0)
ORANGE = (255,165,0)    # mau (gg)
RED = (255,0,0)
I_ = np.array([WIDTH/2,HEIGHT/2], dtype=np.float64) # tấm lớn
R_ = 150 #bán kính lớn
r_ = 5  # bán kính nhỏ
i_ = np.array([WIDTH/2,HEIGHT/2-120],dtype=np.float64) # tấm nhỏ
running = True 
a = 0.2 # gia toc
v = np.array([0,0],dtype=np.float64) # vận tốc quả bóng nhỏ
g = 60 # góc của tam giác 
s = math.radians(-g/2) # điểm đầu của cạnh tam giác
e = math.radians(g/2) # điểm cuối của cạnh tam giác đè lên đường tròn
f = 0.01 # làm cho tam giác quay 
balls= [Ball(i_,v)]
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	s += f  
	e += f 
	for ball in balls:
		if ball.pos[1] > HEIGHT or ball.pos[0]<0 or ball.pos[0]>WIDTH or ball.pos[1]<0:
			balls.remove(ball)
			balls.append(Ball(position=[WIDTH // 2, HEIGHT // 2 - 120], veloccity=[random.uniform(-4,4),random.uniform(-1,1)]))
			balls.append(Ball(position=[WIDTH // 2, HEIGHT // 2 - 120], veloccity=[random.uniform(-4,4),random.uniform(-1,1)]))
		ball.v[1] += a 
		ball.pos += ball.v
		kc= np.linalg.norm(ball.pos - I_) # khoảng cách 
		if kc + r_ > R_ : # điều kiện để bóng nảy lên 
			if ball_arc(ball.pos,I_,s,e):
				ball.is_in = False 
			if ball.is_in:
				d = ball.pos - I_ # vecto của 2 tâm khi bóng nhỏ vừa chạm vào đường tròn lớn
				d_=d/np.linalg.norm(d) # vecto don vi cua d
				ball.pos = I_ + (R_-r_) * d_  # đk để bóng không ra khỏi vòng khi v lớn
				t = np.array([-d[1],d[0]], dtype=np.float64) # vecto tiếp tuyến
				x = (np.dot(ball.v,t)/np.dot(t,t))* t #tich vo huong v.t
				ball.v = 2 * x - ball.v # vận tốc mới khi bóng nhỏ va vào đường tròn
				ball.v += t * f # v = r.f

	window.fill(BLACK)
	pygame.draw.circle(window, ORANGE ,I_ , R_ , 3 ) # các bước vẽ hình tròn
	draw_arc(window,I_,R_,s,e) # vẽ tam giác đè lên hình tròn
	for ball in balls :
		pygame.draw.circle(window, ball.color , ball.pos, r_)
	
	pygame.display.flip()
	clock.tick(60)
pygame.quit()
