import tkinter
from tkinter import filedialog
from tkinter import messagebox
import hashlib


class HashApp:
    def __init__(self) -> None:
        self.algorithms = ('md5', 'sha1', 'sha256', 'sha512')
        self.file_path = ''

        self.window = tkinter.Tk()
        self.window.geometry("500x300")
        self.window.title("hash - Pouria Shaigani")
        # label of file entery :
        top_label = tkinter.Label(self.window, text='Enter a file :')
        top_label.pack(pady=5)
        # file entery :
        open_file_btn = tkinter.Button(self.window, text='open', command=self.select_file)
        open_file_btn.pack()
        # label of radio buttons :
        alg_label = tkinter.Label(self.window, text='Choose an algorithm :')
        alg_label.pack(padx=5)
        # radio boxes :
        self.radio_group = tkinter.IntVar()
        for i, v in enumerate(self.algorithms):
            radio_btn = tkinter.Radiobutton(self.window,
                                            text=v,    # display text
                                            value=i,    # value of each radio btn
                                            variable=self.radio_group,    # grouping these btns
                                            )
            radio_btn.pack()    

        # start hash btn
        hash_btn = tkinter.Button(self.window, text='Start hashing', command=self.hash)
        hash_btn.pack()
        # end
        self.window.mainloop()

    def select_file(self):
        self.file_path = filedialog.askopenfilename()

    def hash(self):
        result = None
        if self.file_path == None or self.file_path == '':
            messagebox.showwarning('warning', 'File is not selected')
        else:
            selected_algorithm = self.radio_group.get()
            with open(self.file_path, 'rb') as file:
                selected_file = file.read()
            for i, v in enumerate(self.algorithms):
                if i == selected_algorithm:
                    h = hashlib.new(v)
                    h.update(selected_file)
                    result = h.hexdigest()               

            messagebox.showinfo('result', result)
            print(result)

    

if __name__ == '__main__':
    HashApp()