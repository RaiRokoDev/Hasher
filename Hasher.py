from tkinter import *
from tkinter import ttk
from hashlib import sha1, sha224, sha256, sha384, sha512

def hash_it(arg):
    global r_var, text, hash_sum
    text_i = str(text.get(1.0, END))
    var = r_var.get()
    if var == 0:
        output = sha1(text_i[:-1].encode('latin1')).hexdigest()
    if var == 1:
        output = sha224(text_i[:-1].encode('latin1')).hexdigest()
    if var == 2:
        output = sha256(text_i[:-1].encode('latin1')).hexdigest()
    if var == 3:
        output = sha384(text_i[:-1].encode('latin1')).hexdigest()
    if var == 4:
        output = sha512(text_i[:-1].encode('latin1')).hexdigest()

    hash_sum.delete(1.0, END)
    hash_sum.insert(1.0, output)

def main_window():
    window = Tk()
    window.title('Converting to hash')
    window.geometry('500x180')
    window.resizable(width=False, height=False)
    window['bg'] = 'grey13'

    global r_var
    r_var = IntVar()
    r_var.set(0)
    r0 = Radiobutton(text='', variable = r_var, value = 0)
    r1 = Radiobutton(text='', variable = r_var, value = 1)
    r2 = Radiobutton(text='', variable = r_var, value = 2)
    r3 = Radiobutton(text='', variable = r_var, value = 3)
    r4 = Radiobutton(text='', variable = r_var, value = 4)

    r0['bg'] = 'grey13'
    r0['fg'] = 'black'
    r1['bg'] = 'grey13'
    r1['fg'] = 'black'
    r2['bg'] = 'grey13'
    r2['fg'] = 'black'
    r3['bg'] = 'grey13'
    r3['fg'] = 'black'
    r4['bg'] = 'grey13'
    r4['fg'] = 'black'

    r0.place(x=10, y=10)
    r1.place(x=10, y=45)
    r2.place(x=10, y=80)
    r3.place(x=10, y=115)
    r4.place(x=10, y=150)

    r0text = Label(text='SHA1')
    r1text = Label(text='SHA224')
    r2text = Label(text='SHA256')
    r3text = Label(text='SHA384')
    r4text = Label(text='SHA512')

    r0text['bg'] = 'grey13'
    r0text['fg'] = 'white'
    r1text['bg'] = 'grey13'
    r1text['fg'] = 'white'
    r2text['bg'] = 'grey13'
    r2text['fg'] = 'white'
    r3text['bg'] = 'grey13'
    r3text['fg'] = 'white'
    r4text['bg'] = 'grey13'
    r4text['fg'] = 'white'

    r0text.place(x=50, y=10)
    r1text.place(x=50, y=45)
    r2text.place(x=50, y=80)
    r3text.place(x=50, y=115)
    r4text.place(x=50, y=150)


    hat1 = Label(text='Enter text')
    hat1['bg'] = 'grey13'
    hat1['fg'] = 'white'
    hat1.place(x=250, y=5)

    global text
    text = Text(width=44, height=2)
    text.place(x=113, y=35)
    text['bg'] = 'white'

    scroll = Scrollbar(command=text.yview)
    scroll.place(x=470, y=35, width=20, height=40)
    scroll['bg'] = 'grey13'
    text.config(yscrollcommand=scroll.set)

    hasher = Button(text='Convert', width=17, height=1)
    hasher.bind('<Button-1>', hash_it)
    hasher['bg'] = 'grey13'
    hasher['fg'] = 'white'
    hasher.place(x=220, y=79)

    global hash_sum
    hash_sum = Text(width=44, height=3)
    hash_sum.place(x=113, y=116)
    hash_sum['bg'] = 'white'

    window.mainloop()

main_window()
