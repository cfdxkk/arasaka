import pyautogui
import time
from Common.setInterval import setInterval

# def step():
#     # 这里放你的pyautogui相关代码
#     pyautogui.moveTo(100, 100)

moveAroundWorker = None

def moveAround():
    # 这里放你的pyautogui相关代码
		pyautogui.keyDown('w')
		time.sleep(2)
		pyautogui.keyUp('w')
		time.sleep(1)

		pyautogui.keyDown('a')
		time.sleep(2)
		pyautogui.keyUp('a')
		time.sleep(1)

		pyautogui.keyDown('s')
		time.sleep(2)
		pyautogui.keyUp('s')
		time.sleep(1)

		pyautogui.keyDown('d')
		time.sleep(2)
		pyautogui.keyUp('d')
		time.sleep(1)

def startMoveAround():
	time.sleep(5)
	global moveAroundWorker 
	moveAroundWorker = setInterval(moveAround, 5)
	moveAroundWorker.start()

def stopMoveAround():
	global moveAroundWorker
	if moveAroundWorker:
			moveAroundWorker.stop()
