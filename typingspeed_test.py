import tkinter as tk
from tkinter import messagebox
import time


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "How razorback-jumping frogs can level six piqued gymnasts!",
            "Pack my box with five dozen liquor jugs."
        ]

        self.current_sentence = tk.StringVar()
        self.current_sentence.set(self.sentences[0])

        self.label_sentence = tk.Label(root, textvariable=self.current_sentence, font=("Helvetica", 14))
        self.label_sentence.pack(pady=10)

        self.entry_typing = tk.Entry(root, font=("Helvetica", 12))
        self.entry_typing.pack(pady=10)

        self.button_start = tk.Button(root, text="Start Typing Test", command=self.start_typing_test)
        self.button_start.pack(pady=10)

    def start_typing_test(self):
        self.button_start.config(state=tk.DISABLED)
        self.entry_typing.delete(0, tk.END)
        self.entry_typing.config(state=tk.NORMAL)
        self.entry_typing.focus()

        start_time = time.time()

        def finish_typing(event):
            typed_text = self.entry_typing.get()
            end_time = time.time()
            elapsed_time = end_time - start_time
            words_per_minute = len(typed_text.split()) / (elapsed_time / 60)

            result_message = f"Your typing speed: {words_per_minute:.2f} WPM"
            tk.messagebox.showinfo("Typing Test Result", result_message)

            self.entry_typing.delete(0, tk.END)
            self.button_start.config(state=tk.NORMAL)

        self.root.bind('<Return>', finish_typing)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
