import curses
import csv
import os
from Structures.Users import *
menu = ['Play', 'Scoreboard', 'User Selection', 'Reports', 'Bulk Loading', 'Exit']
circularList = CircularLinkedList()

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def imprimir_pedirRuta(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y,x, text)

    stdscr.refresh();

#def cargaMasiva(stdscr, nombre):
def cargaMasiva(stdscr, archi):
    stdscr.clear()
    nombre =str(archi, 'utf-8') + ".csv"
    #imprimir_pedirRuta(stdscr, nombre)
    #stdscr.getch()
    #creating instace of CircularLinked

    with open(nombre) as csvfile:
        reader = csv.DictReader(csvfile)
        nuevovar = '\n\t\t\t\t\t\t\t'
        #file = open("archivo.txt", "w")
        for row in reader:
            nuevovar = nuevovar + row['Usuario'] + '\n\t\t\t\t\t\t\t'
            circularList.add(NodeUser(row['Usuario']))
        #file.close()
        #imprimir_pedirRuta(stdscr,nuevovar)
        circularList.graph()
        #stdscr.getch()

def userSelectionShow(stdscr, user):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2
    y = h//2
    aux = user
    stdscr.addstr(y,x, "<-------" + user.name + "------->")
    key2 = stdscr.getch()
    if key2 == curses.KEY_RIGHT:
        userSelectionShow(stdscr,user.next)
        stdscr.clear()
        stdscr.getch()
    elif key2 == curses.KEY_LEFT:
        userSelectionShow(stdscr,user.previous)

    stdscr.getch()


    stdscr.refresh();

def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)
    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_RED)
    # specify the current selected row
    current_row = 0
    # print the menu
    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            #print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            variable = menu[current_row]
            #imprimir_pedirRuta(stdscr, str(current_row))
            #stdscr.getch()
            if current_row is 0: #play
                imprimir_pedirRuta(stdscr, "jugarr")
                stdscr.getch()

            elif current_row is 1: #scoreborad
                imprimir_pedirRuta(stdscr, "scoreborad")
                stdscr.getch()
            elif current_row is 2: #userSelectrion
                imprimir_pedirRuta(stdscr, "userselection")
                usuario = circularList.head
                userSelectionShow(stdscr, usuario)

            elif current_row is 3: #reports
                imprimir_pedirRuta(stdscr, "Ingrese el numero de reporte: \n 1.......Usuarios \n \n Numero: ")
                curses.echo()
                opcion = stdscr.getstr()
                stdscr.getch()

            elif current_row is 4:
                imprimir_pedirRuta(stdscr, "inserte el nombre del archivo .csv: ")
                #win = create_centered_window(10, 40, 'Introduzca su nombre')
                #name = get_name(win)
                #win.erase()

                #win = create_centered_window(5, 20, 'Saludo')
                #win.addstr('hello,{}'.format(name).encode())
                #imprimir_pedirRuta(stdscr, "inserte ruta:")

                #valor = curses.noecho()
                #stdscr.getch()
                curses.echo()
                name = stdscr.getstr()
                #imprimir_pedirRuta(stdscr, name)
                #stdscr.getch()
                cargaMasiva(stdscr,name)

            else:
                print_center(stdscr,variable)
                stdscr.getch()


            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                break

        print_menu(stdscr, current_row)


curses.wrapper(main)
