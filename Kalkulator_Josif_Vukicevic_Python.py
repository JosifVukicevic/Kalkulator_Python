from tkinter import *

izuzetak = ""


def press(num):
    global izuzetak


    izuzetak = izuzetak + str(num)

    equation.set(izuzetak)



def equalpress():
    try:

        global izuzetak


        total = str(eval(izuzetak))

        equation.set(total)

        izuzetak = ""


    except:

        equation.set(" Pogrešan unos! ")
        izuzetak = ""



def clear():
    global izuzetak
    izuzetak = ""
    equation.set("")



if __name__ == "__main__":
    # GUI
    gui = Tk()

    # pozadina
    gui.configure(background="gray")


    # naslov
    gui.title("Kalkulator - Created by Josif Vukicevic")

    # dimenzije prozora
    gui.geometry("270x150")

    # instanca klase
    equation = StringVar()

    # labela koja prikazuje tekst
    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=70)

    # dugmad
    dugme1 = Button(gui, text=' 1 ', fg='black', bg='light green',
                     command=lambda: press(1), height=1, width=7)
    dugme1.grid(row=2, column=0)

    dugme2 = Button(gui, text=' 2 ', fg='black', bg='light green',
                     command=lambda: press(2), height=1, width=7)
    dugme2.grid(row=2, column=1)

    dugme3 = Button(gui, text=' 3 ', fg='black', bg='light green',
                     command=lambda: press(3), height=1, width=7)
    dugme3.grid(row=2, column=2)

    dugme4 = Button(gui, text=' 4 ', fg='black', bg='light green',
                     command=lambda: press(4), height=1, width=7)
    dugme4.grid(row=3, column=0)

    dugme5 = Button(gui, text=' 5 ', fg='black', bg='light green',
                     command=lambda: press(5), height=1, width=7)
    dugme5.grid(row=3, column=1)

    dugme6 = Button(gui, text=' 6 ', fg='black', bg='light green',
                     command=lambda: press(6), height=1, width=7)
    dugme6.grid(row=3, column=2)

    dugme7 = Button(gui, text=' 7 ', fg='black', bg='light green',
                     command=lambda: press(7), height=1, width=7)
    dugme7.grid(row=4, column=0)

    dugme8 = Button(gui, text=' 8 ', fg='black', bg='light green',
                     command=lambda: press(8), height=1, width=7)
    dugme8.grid(row=4, column=1)

    dugme9 = Button(gui, text=' 9 ', fg='black', bg='light green',
                     command=lambda: press(9), height=1, width=7)
    dugme9.grid(row=4, column=2)

    dugme0 = Button(gui, text=' 0 ', fg='black', bg='light green',
                     command=lambda: press(0), height=1, width=7)
    dugme0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='light blue',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='light blue',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    mnozenje = Button(gui, text=' * ', fg='black', bg='light blue',
                      command=lambda: press("*"), height=1, width=7)
    mnozenje.grid(row=4, column=3)

    dijeljenje = Button(gui, text=' / ', fg='black', bg='light blue',
                    command=lambda: press("/"), height=1, width=7)
    dijeljenje.grid(row=5, column=3)

    jednakost = Button(gui, text=' = ', fg='black', bg='yellow',
                   command=equalpress, height=1, width=7)
    jednakost.grid(row=5, column=2)

    izbrisi = Button(gui, text='Izbriši', fg='black', bg='red',
                   command=clear, height=1, width=7)
    izbrisi.grid(row=5, column='1')

    tacka_decimala = Button(gui, text='.', fg='black', bg='light blue',
                     command=lambda: press('.'), height=1, width=7)
    tacka_decimala.grid(row=6, column=3)

    gui.mainloop()