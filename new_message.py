import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox

import message_manager as messages
import font_manager as fonts


class NewMessage():

    def __init__(self, window, message_id):
        self.message_id = message_id

        self.window = window

        self.window.geometry("500x320")

        self.window.title(f"New Message")

        sender_lbl = tk.Label(window, text="Sender:")

        sender_lbl.grid(row=0, column=0, sticky="E", padx=10, pady=10)

        self.sender_txt = tk.Entry(window, width=40)

        self.sender_txt.grid(row=0, column=1, columnspan=5, sticky="W", padx=10, pady=10)

        recipient_lbl = tk.Label(window, text="Recipient:")

        recipient_lbl.grid(row=1, column=0, sticky="E", padx=10, pady=10)

        self.recipient_txt = tk.Entry(window, width=40)

        self.recipient_txt.grid(row=1, column=1, columnspan=5, sticky="W", padx=10, pady=10)

        subject_lbl = tk.Label(window, text="Subject:")

        subject_lbl.grid(row=2, column=0, sticky="E", padx=10, pady=10)

        self.subject_txt = tk.Entry(window, width=40)

        self.subject_txt.grid(row=2, column=1, columnspan=5, sticky="W", padx=10, pady=10)

        self.message_txt = tkst.ScrolledText(window, width=48, height=6, wrap="word")

        self.message_txt.grid(row=3, column=0, columnspan=6, sticky="W", padx=10, pady=10)

        sender_btn = tk.Button(window, text="Send", command=self.send_msg)

        sender_btn.grid(row=4, column=3, sticky="W", padx=10, pady=10)

        delete_btn = tk.Button(window, text="Cancel", command=self.delete_message)

        delete_btn.grid(row=4, column=4, padx=10, pady=10)

        close_btn = tk.Button(window, text="Close", command=self.close)

        close_btn.grid(row=4, column=5, padx=10, pady=10)

    def send_msg(self):
        """messages.new_message(self.sender_txt.get(), self.recipient_txt.get(), self.subject_txt.get(),
                             self.message_txt.get('1.0', tk.END))
        if messages.new_message(self.sender_txt.get(), self.recipient_txt.get, self.subject_txt.get(),
                                self.message_txt.get('1.0', tk.END)) is None:
            valid = False
            if not valid:
                messagebox.showwarning("Warning", "Your text fields are empty, please enter an email address")"""
        if messages.new_message(self.sender_txt.get(), self.recipient_txt.get, self.subject_txt.get(),
                                self.message_txt.get('1.0', tk.END)) is not None:
            for sender_txt in tk.Entry:
                if sender_txt(hasattr(self.sender_txt.get(), "@")):
                    continue
        valid = True
        if valid:
            messagebox.showinfo('Name', f"Congrats! Your message has been sent to the" + f"{self.recipient_txt.get()}")
            return

    def delete_message(self):
        if self.message_id is not None:
            messages.delete_message(self.message_id)
        self.close()

    def close(self):
        self.window.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    NewMessage(window, None)
    window.mainloop()
