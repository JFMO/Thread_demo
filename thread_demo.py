import threading
from time import sleep, ctime

def demo1():
	for n in range(5):
		print('demo1 --- %d' % n)
		sleep(1)
		
def demo2():
	for n in range(5):
		print('demo2 --- %d' % n)	
		sleep(1)
		
if __name__== '__main__':
	print('--开始--: %s' % ctime())
	
	t1 = threading.Thread(target = demo1)
	t2 = threading.Thread(target = demo2)
	t1.start()
	t2.start()
	
	while True:
		length = len(threading.enumerate())
		print('当前运行的线程数：%d' % length)
		if length <= 1:
			break
			
		sleep(0.5)
