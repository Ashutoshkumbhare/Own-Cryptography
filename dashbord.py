##################################################### ready to use #################################################
from tkinter import *
from tkinter import filedialog as fd
import En_De as ed


def Screen1_1():
    global root2
    root.destroy()
    root2 = Tk()
    root2.title("Encrypt")
    root2.geometry("400x250")
    root2.configure(bg="black")
    #Label(root2, text="File name", fg="green", bg="black").place(x=1, y=10)
    # spinbox = Spinbox(root2, from_=1, to=10000).place(x=50, y=35)
    button2 = Button(root2, text="Browse", command=browse_button).place(x=175, y=40)
    Button(root2, text="Exit", height="1", width="20", command=root2.destroy).pack(padx=10, pady=110)
    root2.mainloop()


def browse_button():
    file_name = fd.askopenfilename()
    #Label(root2, text=file_name, fg="white", bg="black").place(x=1, y=10)
    root2.destroy()
    default_code = 1
    code = int(input("Enter file Encrypting Code"))
    while default_code <= code:
        ed.en_file(file_name)
        default_code= default_code+1
    print(file_name, ":is encrypted")



def browse_de_button():
    file_name = fd.askopenfilename()
    #Label(root2, text=file_name, fg="white", bg="black").place(x=100, y=10)
    root2.destroy()
    default_code = 1
    code = int(input("Enter file Decrypting Code"))
    while default_code <= code:
        ed.de_file(file_name)
        default_code = default_code + 1
    print(file_name, ":is decrypted")


def Screen1_2():
    global root2
    root.destroy()
    root2 = Tk()
    root2.title("Decrypt")
    root2.geometry("400x250")
    root2.configure(bg="black")
    #Label(root2, text="File name", fg="green", bg="black").place(x=1, y=10)
    #spinbox = Spinbox(root2, from_=1, to=10000).place(x=50, y=35)
    button2 = Button(root2, text="Browse", command=browse_de_button).place(x=175, y=40)
    Button(root2, text="Exit", height="1", width="20", command=root2.destroy).pack(padx=10, pady=110)
    root2.mainloop()


def Screen():  # main
    global root
    root = Tk()
    root.title("Super security")
    root.configure(bg="black")
    root.geometry("300x250")
    Button(text="Encrypt", height="1", width="20", command=Screen1_1).pack(padx=10, pady=10)
    Button(text="Dectypt", height="1", width="20", command=Screen1_2).pack(padx=10, pady=10)
    Button(text="Exit", height="1", width="20", command=root.destroy).pack(padx=10, pady=10)
    root.mainloop()


############################## mian program ################################################

Screen()
