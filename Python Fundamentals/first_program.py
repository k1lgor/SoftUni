from tkinter import *
from tkinter.font import BOLD

window = Tk()
window.geometry("400x400")
window.title("ETA Calculator")

# photo = PhotoImage(file='calculator.png')
# window.iconphoto(True, photo)
window.config(background='black')

label = Label(window,
              text="БЕБУУУУУУ\nМЕБУУУУУУУ\n<3",
              font=('arial', 20, 'bold'),
              bg='black',
              #   image=photo,
              compound='center')
label.config(background='white')
label.pack()
label.place(x=115, y=140)

window.mainloop()
