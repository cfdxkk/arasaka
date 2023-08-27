from Common.slowScroll import slowScroll
import time
import threading
import pyautogui

carrackMiniGameWorker = None
carrackMiniGameWorkerStopEvent = None

def carrack(stop_event):
	slowScroll(100000, 0.01, 1000)
	if not stop_event.is_set():
		pyautogui.keyDown('F5')
		time.sleep(3)
		pyautogui.keyDown('F5')
		time.sleep(3)
		pyautogui.keyDown('F5')
		if not stop_event.is_set():
			time.sleep(15)
			if not stop_event.is_set():
				slowScroll(-4500, 0.01, 100)
	print('bye')

def carrackGo():
	time.sleep(5)
	global carrackMiniGameWorker
	global carrackMiniGameWorkerStopEvent
	carrackMiniGameWorkerStopEvent = threading.Event()
	carrackMiniGameWorker = threading.Thread(target=carrack, args=(carrackMiniGameWorkerStopEvent,))
	carrackMiniGameWorker.start()

def carrackStop():
	global carrackMiniGameWorker
	global carrackMiniGameWorkerStopEvent
	carrackMiniGameWorkerStopEvent.set()
	carrackMiniGameWorker.join()
	print('stop')
