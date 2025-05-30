import tkinter as tk
from datetime import datetime

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch and Clock")

        # Clock Label
        self.clock_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.clock_label.pack(pady=10)

        # Stopwatch Label
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 40))
        self.stopwatch_label.pack(pady=20)

        # Stopwatch buttons frame
        buttons_frame = tk.Frame(root)
        buttons_frame.pack()

        self.start_button = tk.Button(buttons_frame, text="Start", command=self.start)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(buttons_frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(buttons_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=5)

        # Stopwatch variables
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        # Start clock update
        self.update_clock()

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=f"Current Time: {now}")
        self.root.after(1000, self.update_clock)  # update every second

    def update_stopwatch(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

            time_string = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
            self.stopwatch_label.config(text=time_string)
            self.root.after(1000, self.update_stopwatch)

    def start(self):
        if not self.running:
            self.running = True
            self.update_stopwatch()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.stopwatch_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchClockApp(root)
    root.mainloop()

