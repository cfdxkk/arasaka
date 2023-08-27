import pyautogui
import time

def slowScroll(amount, delay = 0.01, step_size = 1):
	# 确定滚动的方向
	direction = 1 if amount > 0 else -1
	step = step_size * direction
	
	for _ in range(abs(amount) // step_size):
		pyautogui.scroll(step)
		time.sleep(delay)

	# 如果amount不是step_size的倍数，处理余下的滚动
	remainder = abs(amount) % step_size
	for _ in range(remainder):
		pyautogui.scroll(direction)
		time.sleep(delay)