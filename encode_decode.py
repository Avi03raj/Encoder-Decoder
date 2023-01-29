from tkinter import *
import base64

root=Tk()
root.geometry('1545x800')
root.title('Message Encode and Decode')
root.resizable(0,0)
root.configure(background='tomato')

Label(root,text='MESSAGE',font='arial 40 bold',bg='tomato').pack()
Label(root,text='ENCRYPTION AND  DECRYPTION',font='arial 40 bold',bg='tomato').pack()
Label(root,text='AVIRAJ',font='arial 40 bold',bg='tomato').pack(side=BOTTOM)

Text=StringVar()
private_key=StringVar()
mode=StringVar()
Result=StringVar()

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)


def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


Label(root,text='MESSAGE',font='arial 20 bold',bg='tomato').place(x=400,y=180)
Entry(root,textvariable=Text,font='arial 18',bg='powderblue').place(x=800,y=180)

Label(root,text='KEY',font='arial 20 bold',bg='tomato').place(x=400,y=250)
Entry(root,textvariable=private_key,font='arial 18',bg='powderblue').place(x=800,y=250)

Label(root,text='MODE(e-ENCODE/d-Decode)',font='arial 20 bold',bg='tomato').place(x=400,y=320)
Entry(root,textvariable=mode,font='arial 18',bg='powderblue').place(x=800,y=320)


Label(root,text='RESULT',font='arial 18 bold',bg='tomato').place(x=400,y=390)
Entry(root,textvariable=Result,font='arial 18',bg='powderblue').place(x=800,y=390)

Button(root,text='SHOW RESULT',font='arial 18 bold',bg='Lightblue', bd = 16,command=Mode).place(x=450,y=490)
Button(root,text='RESET',font='arial 18 bold',bg='LimeGreen',bd=16,command=Reset).place(x=750,y=490)
Button(root,text='EXIT',font='arial 18 bold',bg='Red',bd=16,command=Exit).place(x=950,y=490)

root.mainloop()