import tkinter as tk
import time

class FocusTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("专注时钟")
        self.master.geometry("300x200")

        self.label = tk.Label(master, text="专注时间 (分钟):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.start_button = tk.Button(master, text="开始专注", command=self.start_timer)
        self.start_button.pack()

        self.time_label = tk.Label(master, text="", font=("Helvetica", 48))
        self.time_label.pack()

        self.remaining_time = 0

    def start_timer(self):
        try:
            minutes = int(self.entry.get())
            self.remaining_time = minutes * 60
            self.update_timer()
        except ValueError:
            self.time_label.config(text="90")

    def update_timer(self):
        if self.remaining_time > 0:
            mins, secs = divmod(self.remaining_time, 60)
            self.time_label.config(text=f"{mins:02}:{secs:02}")
            self.remaining_time -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.time_label.config(text="时间到！")

if __name__ == "__main__":
    root = tk.Tk()
    timer = FocusTimer(root)
    root.mainloop()
