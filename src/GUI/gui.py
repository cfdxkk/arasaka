import tkinter as tk
from Automation.automation import startMoveAround
from Automation.automation import stopMoveAround
from Automation.CarrackMiniGame.CarrackMiniGameStep import carrackGo
from Automation.CarrackMiniGame.CarrackMiniGameStep import carrackStop


def start_automation():
    startMoveAround()

def stop_automation():
    stopMoveAround()


app = tk.Tk()
app.title("Star Citizen PS")
app.geometry("400x400")  # 设置窗口大小为300x200

start_btn = tk.Button(app, text="Start Automation", command=start_automation)
start_btn.pack()

stop_btn = tk.Button(app, text="Stop Automation", command=stop_automation)
stop_btn.pack()

carrack_game_start_btn = tk.Button(app, text="开始自动进行克拉克小游戏", command=carrackGo)
carrack_game_start_btn.pack()

carrack_game_stop_btn = tk.Button(app, text="停止自动进行克拉克小游戏", command=carrackStop)
carrack_game_stop_btn.pack()


def on_close():
    stopMoveAround()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_close)


app.mainloop()


