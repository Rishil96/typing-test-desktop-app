import tkinter as tk
import random

APPLICATION_BACKGROUND_COLOR = "#f5f5f5"
FONT_STYLE = "Helvetica"
TOTAL_TEST_TIME_SECONDS = 36
TEST_STARTING_POINT = 30

class TypingApp(tk.Tk):

    def __init__(self, name):
        super().__init__()
        self.name = name
        # Attributes
        self.seconds = TOTAL_TEST_TIME_SECONDS
        self.typing_speed = 0
        self.typing_accuracy = 0
        self.words_list = self.get_word_list()
        self.current_test_sentence = ""
        self.total_characters_typed = 0
        self.incorrect_characters_typed = 0

        # Initial Configurations
        self.title("PyTypist App")
        self.minsize(width=600, height=350)
        self.configure(bg=APPLICATION_BACKGROUND_COLOR)

        # Configure the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Display title
        self.header_label = tk.Label(text="PyTypist App",
                                     font=(FONT_STYLE, 24, "bold"),
                                     fg="#333333",  # Dark gray text
                                     bg=APPLICATION_BACKGROUND_COLOR)
        self.header_label.grid(row=0, column=0, columnspan=2, pady=(20, 5), sticky="ew")

        self.sub_header_label = tk.Label(text=f"Hi {self.name}, Test your typing speed here!",
                                         font=(FONT_STYLE, 14),
                                         fg="#666666",  # Medium gray text
                                         bg=APPLICATION_BACKGROUND_COLOR)
        self.sub_header_label.grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky="ew")

        # Text Display area for typing test
        self.typing_content = tk.Label(text="Here is some dummy text to type.\nTry your best to finish quickly!",
                                       font=("Courier", 14, "bold"),
                                       fg="#444444",  # Slightly darker gray
                                       bg=APPLICATION_BACKGROUND_COLOR,
                                       wraplength=500,
                                       justify="center")
        self.typing_content.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew", padx=20)

        # Text Input field for user to type
        self.typing_box = tk.Entry(font=(FONT_STYLE, 12, "normal"))
        self.typing_box.bind("<KeyRelease>", self.key_press_event)
        self.typing_box.config(state="disabled")
        self.typing_box.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew", padx=20, ipady=5)

        # Start button
        self.start_button = tk.Button(text="Start Test", command=self.start_test)
        self.start_button.grid(row=4, column=0, pady=10, padx=20, sticky="ew")

        # Timer Display
        self.timer_label = tk.Label(text=f"{TEST_STARTING_POINT} second test",
                                    font=(FONT_STYLE, 16, "bold"),
                                    fg="#ff4500",  # Orange-red color
                                    bg=APPLICATION_BACKGROUND_COLOR)
        self.timer_label.grid(row=4, column=1, pady=10, padx=20, sticky="ew")

        # Result Display
        self.typing_speed_label = tk.Label(text=f"Speed: {self.typing_speed} wpm",
                                           font=(FONT_STYLE, 12),
                                           fg="#333333",
                                           bg=APPLICATION_BACKGROUND_COLOR)
        self.typing_speed_label.grid(row=5, column=0, pady=10, sticky="ew", padx=20)

        self.typing_accuracy_label = tk.Label(text=f"Accuracy: {self.typing_accuracy}%",
                                              font=(FONT_STYLE, 12),
                                              fg="#333333",
                                              bg=APPLICATION_BACKGROUND_COLOR)
        self.typing_accuracy_label.grid(row=5, column=1, pady=10, sticky="ew", padx=20)

        self.mainloop()

    def update_timer(self):
        self.start_button.config(state="disabled")
        # Countdown before starting test
        if self.seconds > TEST_STARTING_POINT:
            self.seconds -= 1
            self.timer_label.config(text=f"Test starts in {self.seconds % TEST_STARTING_POINT}")
            self.after(1000, self.update_timer)
        # Actual test start point, enable typing box
        elif self.seconds == TEST_STARTING_POINT:
            self.seconds -= 1
            # Enable typing box state
            self.typing_box.config(state="normal")
            # Place cursor on typing box
            self.typing_box.focus_set()
            self.timer_label.config(text=f"Time Left 0:{self.seconds}")
            self.after(1000, self.update_timer)
        # Test running state, maintain timer
        elif self.seconds > 0:
            self.seconds -= 1
            if self.seconds < 10:
                self.timer_label.config(text=f"Time Left 0:0{self.seconds}")
            else:
                self.timer_label.config(text=f"Time Left 0:{self.seconds}")
            self.after(1000, self.update_timer)
        # Test over state
        else:
            self.timer_label.config(text="Time's up!")
            self.reset_test()

    @staticmethod
    def get_word_list() -> list:
        with open("words.txt") as f:
            contents = f.readlines()
            word_list = [word.strip() for word in contents if len(word)  >= 3]

        return word_list

    def generate_test_sentence(self, num_words=10):
        sentence = " ".join(random.sample(self.words_list, num_words))
        return sentence

    def display_test_sentence(self):
        random_sentence = self.generate_test_sentence()
        self.current_test_sentence = random_sentence
        self.typing_content.config(text=random_sentence)

    def key_press_event(self, e):

        typed_text = self.typing_box.get()

        # Avoid counting characters when backspace is pressed
        if e.keysym == "BackSpace":
            return

        # Check if full sentence was typed correctly
        if typed_text == self.current_test_sentence:
            self.display_test_sentence()
            self.typing_box.delete(0, tk.END)
            self.total_characters_typed += 1
        # Check for inaccuracies in typed sentence
        elif typed_text != self.current_test_sentence[:len(typed_text)]:
            self.typing_box.config(fg="red")
            self.incorrect_characters_typed += 1
        else:
            self.typing_box.config(fg="green")
            self.total_characters_typed += 1

    def start_test(self):
        # Start timer
        self.update_timer()
        # Generate test sentence
        self.display_test_sentence()

    def reset_test(self):
        # Reset UI functionalities as it was before starting the test
        self.start_button.config(state="normal")
        self.typing_box.delete(0, tk.END)
        self.typing_box.config(state="disabled")
        self.seconds = TOTAL_TEST_TIME_SECONDS

        # Calculate and display typing speed and accuracy
        self.typing_speed = round((self.total_characters_typed / 5) * 2, 2)
        self.typing_accuracy = round(((self.total_characters_typed - self.incorrect_characters_typed) / self.total_characters_typed) * 100, 2)
        self.typing_speed_label.config(text=f"Speed: {self.typing_speed} wpm")
        self.typing_accuracy_label.config(text=f"Accuracy: {self.typing_accuracy}%")

        # Reset characters typed
        self.total_characters_typed = 0
        self.incorrect_characters_typed = 0
