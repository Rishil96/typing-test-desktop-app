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
        self.header_label = tk.Label(text="PyTypist App",
                                     font=("Helvetica", 24, "bold"),
                                     fg="#333333",  # Dark gray text
                                     bg=APPLICATION_BACKGROUND_COLOR)
        self.header_label.grid(row=0, column=0, columnspan=2)

        self.sub_header_label = tk.Label(text="Test your typing speed here!",
                                         font=("Helvetica", 14),
                                         fg="#666666",  # Medium gray text
                                         bg=APPLICATION_BACKGROUND_COLOR)
        self.sub_header_label.grid(row=1, column=0, columnspan=2)

        # Text Display area for typing test
        self.typing_content = tk.Label(text="Here is some dummy text to type.\nTry your best to finish quickly!",
                                       font=("Courier", 12),
                                       fg="#444444",  # Slightly darker gray
                                       bg="#f5f5f5",
                                       wraplength=400,
                                       justify="center")
        self.typing_content.grid(row=2, column=0, columnspan=2)

        # Text Input field for user to type
        self.typing_box = tk.Entry()
        self.typing_box.grid(row=3, column=0, columnspan=2)

        # Start button
        self.start_button = tk.Button(text="Start Test")
        self.start_button.grid(row=4, column=0)

        # Timer Display
        self.seconds = 60
        self.timer_label = tk.Label(text=f"Time Left 1:00",
                                    font=("Helvetica", 16, "bold"),
                                    fg="#ff4500",  # Orange-red color
                                    bg="#f5f5f5")
        self.timer_label.grid(row=4, column=1)

        # Result Display
        self.recent_typing_speed = 0
        self.typing_speed_label = tk.Label(text=f"Latest Typing Speed: {self.recent_typing_speed} wpm",
                                           font=("Helvetica", 12),
                                           fg="#333333",
                                           bg="#f5f5f5")
        self.typing_speed_label.grid(row=5, column=0)

        self.max_typing_speed = 0
        self.highest_speed_label = tk.Label(text=f"Max Speed: {self.max_typing_speed} wpm",
                                            font=("Helvetica", 12),
                                            fg="#333333",
                                            bg="#f5f5f5")
        self.highest_speed_label.grid(row=5, column=1)

        self.mainloop()


if __name__ == "__main__":
    typing_obj = TypingApp()
