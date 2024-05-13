import tkinter as tk
import tkinter.scrolledtext as tkst

import font_manager as fonts
import message_manager as messages


def set_text(text_area, content):
    text_area["state"] = "normal"
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)
    text_area["state"] = "disabled"


def close_interface():
    exit()


class LabelMessages:
    def __init__(self, window):
        self.window = window
        self.window.geometry("600x320")
        self.window.title("Label Messages")

        list_messages_btn = tk.Button(window, text="List All Messages Labelled", command=self.list_messages)
        list_messages_btn.grid(row=0, column=0, padx=10, pady=10)

        self.lbl_txt = tk.Entry(window, width=10)
        self.lbl_txt.grid(row=0, column=1, padx=10, pady=10)

        label_messages_btn = tk.Button(window, text="Add Label to Messages", command=self.label_messages)
        label_messages_btn.grid(row=0, column=2, padx=10, pady=10)

        self.id_txt = tk.Entry(window, width=3)
        self.id_txt.grid(row=0, column=3, padx=10, pady=10)

        close_btn = tk.Button(window, text="Close", command=close_interface)
        close_btn.grid(row=0, column=4, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=60, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_messages()

    def list_messages(self):
        search_label = self.lbl_txt
        LabelSearch = search_label.get()
        str(LabelSearch)

        message_list = messages.list_all()
        set_text(self.list_txt, message_list)
        self.status_lbl.configure(text="List Messages button was clicked!")

        if len(LabelSearch) > 0:
            message_list = messages.list_all(LabelSearch)
            set_text(self.list_txt, message_list)

    def label_messages(self):
        """messages.set_label(int(self.id_txt.get(),self.lbl_txt.get())
        message_list = messages.list_all()
        set_text(self.list_txt, message_list)"""
        try:
            messages.set_label(int(self.id_txt.get()), self.lbl_txt.get())
            message_list = messages.list_all()
            set_text(self.list_txt, message_list)
        except ValueError:
            return


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    LabelMessages(window)
    window.mainloop()
