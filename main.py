from tkinter import *
import clipboard
import pyshorteners

root= Tk()
root.resizable(False, False)
root.wm_iconbitmap("notepad.ico")
root.geometry("544x343")
root.title("URL Shortener")
root.configure(bg="gray")

def short_url():
    s = pyshorteners.Shortener()
    url = urlEnt.get()
    final = s.tinyurl.short(url)
    urlvlaue.set(final)

def copy():
    clipboard.copy(urlvlaue.get())
    print('copied succesfilly!!')


Label(root,text="Enter the URL", font="arial 24 bold", bg='gray', fg='cyan').grid(row=1, column=0,padx=100)
# Label(root, text='Credit - Emon', font='arial 20 bold').grid(row=4, column=2, pady=300)

urlvlaue = StringVar()

urlEnt= Entry(root, font="arial 16 bold", width=35)
urlEnt.grid(row=2, column=0)

#urlEnt1= Label(root,textvariable=urlvlaue, font="arial 16 bold")
urlEnt1= Entry(root,textvariable=urlvlaue,width=35 ,font="arial 16 bold")
urlEnt1.grid(row=4, column=0, pady=5)

Label(root, text='Current URL is: ', font='arial 16 bold', fg='cyan', bg='gray').grid(row=3, column=0, pady=14)


Label(root, text='Developed by: Emon Joy', font="arial 12 bold", bg='gray', fg='black').grid(row=6, column=0,pady=60)



Button(root, text='Update URL', font='arial 13 bold', command=short_url).grid(row=5, column=0, pady= 14)
Button(root, text='Copy', font='arial 10 bold', fg='black', bg='red', command=copy).grid(row=4, column=2, padx=10)

root.mainloop()
