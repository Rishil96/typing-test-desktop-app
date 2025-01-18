import tkinter as tk

APPLICATION_BACKGROUND_COLOR = "#f5f5f5"


class TypingApp(tk.Tk):

    def __init__(self):
        super().__init__()
        # Initial Configurations
        self.title("PyTypist App")
        self.minsize(width=500, height=500)
        self.configure(bg=APPLICATION_BACKGROUND_COLOR)

        # Display title
        self.header_label = tk.Label(text="PyTypist App")
        self.header_label.grid(row=0, column=0, columnspan=2)

        self.sub_header_label = tk.Label(text="Test your typing speed here!")
        self.sub_header_label.grid(row=1, column=0, columnspan=2)

        # Text Display area for typing test
        self.typing_content = tk.Label(text="here is some dummy text to type")
        self.typing_content.grid(row=2, column=0, columnspan=2)

        # Text Input field for user to type
        self.typing_box = tk.Entry()
        self.typing_box.grid(row=3, column=0, columnspan=2)

        # Start button
        self.start_button = tk.Button(text="Start Test")
        self.start_button.grid(row=4, column=0)

        # Timer Display
        self.seconds = 60
        self.timer_label = tk.Label(text=f"Time Left 1:00")
        self.timer_label.grid(row=4, column=1)

        # Result Display
        self.recent_typing_speed = 0
        self.typing_speed_label = tk.Label(text=f"Latest Typing Speed: {self.recent_typing_speed} wpm")
        self.typing_speed_label.grid(row=5, column=0)

        self.max_typing_speed = 0
        self.highest_speed_label = tk.Label(text=f"Max Speed: {self.max_typing_speed} wpm")
        self.highest_speed_label.grid(row=5, column=1)

        self.mainloop()
