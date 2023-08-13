import tkinter as tk
from Automation.automation import startMoveAround
from Automation.automation import stopMoveAround


def start_automation():
    startMoveAround()

def stop_automation():
    stopMoveAround()


app = tk.Tk()
app.title("Star Citizen PTUer")

start_btn = tk.Button(app, text="Start Automation", command=start_automation)
start_btn.pack()

stop_btn = tk.Button(app, text="Stop Automation", command=stop_automation)
stop_btn.pack()


def on_close():
    stopMoveAround()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_close)


app.mainloop()


