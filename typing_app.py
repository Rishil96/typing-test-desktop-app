import tkinter as tk

APPLICATION_BACKGROUND_COLOR = "#f5f5f5"


class TypingApp(tk.Tk):

    def __init__(self):
        super().__init__()
        # Initial Configurations
        self.title("PyTypist App")
        self.minsize(width=600, height=350)
        self.configure(bg=APPLICATION_BACKGROUND_COLOR)

        # Configure the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Display title
        self.header_label = tk.Label(text="PyTypist App",
                                     font=("Helvetica", 24, "bold"),
                                     fg="#333333",  # Dark gray text
                                     bg=APPLICATION_BACKGROUND_COLOR)
        self.header_label.grid(row=0, column=0, columnspan=2, pady=(20, 5), sticky="ew")

        self.sub_header_label = tk.Label(text="Test your typing speed here!",
                                         font=("Helvetica", 14),
                                         fg="#666666",  # Medium gray text
                                         bg=APPLICATION_BACKGROUND_COLOR)
        self.sub_header_label.grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky="ew")

        # Text Display area for typing test
        self.typing_content = tk.Label(text="Here is some dummy text to type.\nTry your best to finish quickly!",
                                       font=("Courier", 12),
                                       fg="#444444",  # Slightly darker gray
                                       bg=APPLICATION_BACKGROUND_COLOR,
                                       wraplength=400,
                                       justify="center")
        self.typing_content.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew", padx=20)

        # Text Input field for user to type
        self.typing_box = tk.Entry()
        self.typing_box.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew", padx=20)

        # Start button
        self.start_button = tk.Button(text="Start Test")
        self.start_button.grid(row=4, column=0, pady=10, padx=20, sticky="ew")

        # Timer Display
        self.seconds = 60
        self.timer_label = tk.Label(text=f"Time Left 1:00",
                                    font=("Helvetica", 16, "bold"),
                                    fg="#ff4500",  # Orange-red color
                                    bg=APPLICATION_BACKGROUND_COLOR)
        self.timer_label.grid(row=4, column=1, pady=10, padx=20, sticky="ew")

        # Result Display
        self.recent_typing_speed = 0
        self.typing_speed_label = tk.Label(text=f"Latest Typing Speed: {self.recent_typing_speed} wpm",
                                           font=("Helvetica", 12),
                                           fg="#333333",
                                           bg=APPLICATION_BACKGROUND_COLOR)
        self.typing_speed_label.grid(row=5, column=0, pady=10, sticky="ew", padx=20)

        self.max_typing_speed = 0
        self.highest_speed_label = tk.Label(text=f"Max Speed: {self.max_typing_speed} wpm",
                                            font=("Helvetica", 12),
                                            fg="#333333",
                                            bg=APPLICATION_BACKGROUND_COLOR)
        self.highest_speed_label.grid(row=5, column=1, pady=10, sticky="ew", padx=20)

        self.mainloop()


if __name__ == "__main__":
    typing_obj = TypingApp()
