import tkinter as tk
from tkinter import font
from caesar_cipher import caesar_cipher
from vigenere_cipher import vigenere_cipher

class cipher_type:
    def __init__(self):
        self.cipher_type = None
cipher_type = cipher_type()

H = 450
W = 700
root = tk.Tk()

def execute(text, cipher_type, key, encipher):
    # print(cipher_type.cipher_type)
    if cipher_type.cipher_type:
        if cipher_type.cipher_type == 'c':
            Cipher = caesar_cipher()
            try:
                key = int(key)
            except Exception: raise Exception("A key must be an integer value for Caesae cipher!")
        elif cipher_type.cipher_type == 'v':
            Cipher = vigenere_cipher()
    else: raise Exception("Please select a cipher method!")

    if(encipher): return Cipher.encipher(text,key)
    else: return Cipher.decipher(text,key)

canvas = tk.Canvas(root, width=W, height=H)
canvas.pack()

background_image = tk.PhotoImage(file='images/background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relw=1,relh=1)

# frame = tk.Frame(root)
# frame.place(relwidth=0.97, relheight=0.97, relx=0.015, rely=0.015)

label = tk.Label(root, text='CIPHER PORTAL', bg='#F3C8B0')
label.place(anchor='n', rely=0.03, relx=0.5)

frame_buttons = tk.Frame(root, bg='#F3C8B0')
frame_buttons.place(anchor='s', relw=0.3, relh=0.43, rely=0.58, relx=0.75)

def caesar(input): input.cipher_type ='c'
button_caesar = tk.Button(frame_buttons, text="Caesar Cipher", command=lambda: caesar(cipher_type), activeforeground='red')
button_caesar.place(relx=0.3, rely=0.1)

def vigenere(input): input.cipher_type='v'
button_vigenere = tk.Button(frame_buttons, command=lambda: vigenere(cipher_type), text="Vigenere Cipher", activeforeground='red')
button_vigenere.place(relx=0.3, rely=0.3)

frame_key = tk.Frame(root, bg='#F3C8B0')
frame_key.place(anchor='s', relw=0.4, relh=0.075, rely=0.23, relx=0.3)

label_key = tk.Label(frame_key, text='Key: ', bg='#F3C8B0')
label_key.place( relx=0.05, rely=0.2)

key_entry = tk.Entry(frame_key, selectbackground='gray')
key_entry.place( relw=0.7, relh=0.9, rely=0.05, relx=0.25)

frame_input = tk.Frame(root, bg='#F3C8B0')
frame_input.place(anchor='s', relw=0.4, relh=0.3, rely=0.58, relx=0.3)

plaintext = tk.Text(frame_input, selectbackground='gray', wrap='word', bd=0)
plaintext.place( relw=0.98, relh=0.95, rely=0.025, relx=0.01)


frame_output = tk.Frame(root, bg='#F3C8B0')
frame_output.place(anchor='s', relw=0.8, relh=0.3, rely=0.93, relx=0.5)

text_box = tk.Label(frame_output,  font=('Roboto', 12), anchor='nw', justify='left', wraplength=550)
text_box.place( relw=0.98, relh=0.95, rely=0.025, relx=0.01)

def encipher(text, key):
    try: text_box['text'] = execute(text, cipher_type, key, True)
    except Exception as ex: text_box['text'] = ex.args[0]
button_encipher = tk.Button(frame_buttons, text="Encipher", command=lambda: encipher(plaintext.get('1.0',"end-1c"), key_entry.get()), activeforeground='red')
button_encipher.place(relx=0.3, rely=0.6)

def decipher(text, key):
    try: text_box['text'] = execute(text, cipher_type, key, False)
    except Exception as ex: text_box['text'] = ex.args[0]
button_decipher = tk.Button(frame_buttons, text="Decipher", command=lambda: decipher(plaintext.get('1.0',"end-1c"), key_entry.get()), activeforeground='red')
button_decipher.place(relx=0.3, rely=0.8)

root.mainloop()