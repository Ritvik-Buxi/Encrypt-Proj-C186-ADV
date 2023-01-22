from tkinter import *
from simplecrypt import encrypt, decrypt
from tkinter import filedialog as fd
from tkinter import messagebox
import os

root = Tk()
root.geometry("400x250")
root.config(bg="#99c9f5")

def startDecryption():
    global file_name_entry
    global decryption_text_data
    root.destroy()
 
    decryption_window = Tk()
    decryption_window.geometry("600x500")
    decryption_window.config(bg="#99c9f5")
    
    decryption_text_data = Text(decryption_window, height=20, width=72)
    decryption_text_data.place(relx=0.5,rely=0.35, anchor=CENTER)
    
    btn_open_file = Button(decryption_window, text="Choose File..",relief=FLAT, padx=10, bg="#cbff00", font='arial 13',command=viewData)
    btn_open_file.place(relx=0.5,rely=0.8, anchor=CENTER)

    decryption_window.mainloop()
    
    
def startEncryption():
    global file_name_entry
    global encryption_text_data
    root.destroy()
 
    encryption_window = Tk()
    encryption_window.geometry("600x500")
    encryption_window.config(bg="#99c9f5")
    
    file_name_label = Label(
        encryption_window, text="File Name: ", font='arial 13', bg="#99c9f5")
    file_name_label.place(relx=0.1,rely=0.15, anchor=CENTER)
    
    file_name_entry = Entry(encryption_window, font = 'arial 15')
    file_name_entry.place(relx=0.38,rely=0.15, anchor=CENTER)
    
    btn_create = Button(encryption_window, text="Create", font='arial 13',
                        relief=FLAT, padx=10, bg="#cbff00", command=saveData)
    btn_create.place(relx=0.75,rely=0.15, anchor=CENTER)
    
    encryption_text_data = Text(encryption_window, height=20, width=72)
    encryption_text_data.place(relx=0.5,rely=0.55, anchor=CENTER)
    
    encryption_window.mainloop()
    
def saveData():
    global file_name_entry
    global encryption_text_data
    file_name = file_name_entry.get()
    try:
        with open(file_name+".txt",mode="x") as f:
            data = encryption_text_data.get(1.0,END)
            cipher_code = encrypt("ICE",data)
            hex_str = cipher_code.hex()
            f.write(hex_str)
            file_name_entry.delete(0,END)
            encryption_text_data.delete(1.0,END)
            messagebox.showinfo("Info","Saved The File")
            f.close()

    except FileExistsError:
        with open(file_name+".txt", mode="r") as f:
            data = encryption_text_data.get(1.0, END)
            cipher_code = encrypt("ICE",data)
            hex_str = cipher_code.hex()
            f.write(hex_str)
            file_name_entry.delete(0,END)
            encryption_text_data.delete(1.0,END)
            messagebox.showinfo("Info","Saved The File")
            f.close()
def viewData():
    global decryption_text_data
    text_file = fd.askopenfilename(title="Open a File",filetypes=(("Text Files","*.txt"),))
    with open(text_file, mode="r") as f:
        data = f.read()
        byte_str = bytes.fromhex(data)
        orig = decrypt("ICE",byte_str)
        final_msg = orig.decode("utf-8")
        decryption_text_data.insert(END,final_msg)

heading_label = Label(root, text="Encryption & Decryption",
                      font='arial 18 italic', bg="#99c9f5")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

btn_start_encryption = Button(root, text="Start Encryption", font='arial 13',
                              relief=FLAT, padx=10, bg="#cbff00", command=startEncryption)
btn_start_encryption.place(relx=0.3,rely=0.6, anchor=CENTER)

btn_start_decryption = Button(root, text="Start Decryption", font='arial 13',
                              relief=FLAT, padx=10, bg="#cbff00",  command=startDecryption)
btn_start_decryption.place(relx=0.7,rely=0.6, anchor=CENTER)

root.mainloop()


