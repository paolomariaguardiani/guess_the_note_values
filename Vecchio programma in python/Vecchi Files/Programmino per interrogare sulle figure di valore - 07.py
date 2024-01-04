###################################################################
#                                                                 #
# http://www.codeskulptor.org/#user43_58nvhj10HS_6.py             #
#                                                                 #
# Programma per interrogare sulla notazione e le figure di valore #
#                                                                 #
# Autore: Paolo Maria Guardiani                                   # 
#                                                                 #
###################################################################


import simplegui
import random

Width = 100

image_center = 52/2, 66/2
image_width_height = 52, 66
Height = 100

lista = [4, 3, 2, 1, 0.5, 0.25, 14, 13, 12, 11, 10.5, 10.25] # ho aggiunto il valore 10 al valore 
                                                                  # delle pause per poterle inserire
                                                                  # nella lista dei valori

random.shuffle(lista)
print type(lista)


# carico le immagini delle figure di valore

semibreve = simplegui.load_image('https://www.dropbox.com/s/luqn0vu7asrvm4s/semibreve.png?dl=1')
minima_col_punto = simplegui.load_image('https://www.dropbox.com/s/tq0zkeydddg0sv7/minima_col_punto.png?dl=1')
minima = simplegui.load_image('https://www.dropbox.com/s/tnlffhw0v477mc7/minima.png?dl=1')
semiminima = simplegui.load_image('https://www.dropbox.com/s/wysh9ppp2x17ndq/semiminima.png?dl=1')
croma = simplegui.load_image('https://www.dropbox.com/s/ql9ygeqhfd6ksnz/croma.png?dl=1')
semicroma = simplegui.load_image('https://www.dropbox.com/s/f368yw0rpzxwb85/semicroma.png?dl=1')

pausa_di_semibreve = simplegui.load_image('https://www.dropbox.com/s/5lol9f9ajd7syri/pause_di_semibreve.png?dl=1')
pausa_di_minima_col_punto = simplegui.load_image('https://www.dropbox.com/s/iul0lashrief6mb/pause_di_minima_col_punto.png?dl=1')
pausa_di_minima = simplegui.load_image('https://www.dropbox.com/s/3goke9ks4n4zlct/pausa_di_minima.png?dl=1')
pausa_di_semiminima = simplegui.load_image('https://www.dropbox.com/s/iqcxzlxachiv1q7/pausa_di_semiminima.png?dl=1')
pausa_di_croma = simplegui.load_image('https://www.dropbox.com/s/2oxooaht5kvudac/pausa_di_croma.png?dl=1')
pausa_di_semicroma = simplegui.load_image('https://www.dropbox.com/s/79v3y6s5ljk40hq/pausa_di_semicroma.png?dl=0')

nota = semibreve

#def draw_note(canvas):
#        canvas.draw_image(minima_col_punto, (52/2, 66/2), (52, 66), (50, 50), (52, 66))
def button():
    global nota, image_center, image_width_height
    valore = 0
    if lista != []:
        valore = lista.pop(-1)
        print valore
         
    

    if valore == 4:
        nota = semibreve
        image_center = 55/2, 24/2
        image_width_height = 55, 24
    if valore == 3:
        nota = minima_col_punto
        image_center = 52/2, 66/2
        image_width_height = 52, 66
    if valore == 2:
        nota = minima
        image_center = 42/2, 66/2
        image_width_height = 42, 66
    if valore == 1:
        nota = semiminima
        image_center = 40/2, 65/2
        image_width_height = 40, 65
    if valore == 0.5:
        nota = croma
        image_center = 52/2, 86/2
        image_width_height = 52, 86
    if valore == 0.25:
        nota = semicroma
        image_center = 70/2, 86/2
        image_width_height = 70, 86
        
    if valore == 14:
        nota = pausa_di_semibreve
        image_center = 59/2, 16/2
        image_width_height = 59, 16
    if valore == 13:
        nota = pausa_di_minima_col_punto
        image_center = 62/2, 18/2
        image_width_height = 62, 18
    if valore == 12:
        nota = pausa_di_minima
        image_center = 58/2, 16/2
        image_width_height = 58, 16
    if valore == 11:
        nota = pausa_di_semiminima
        image_center = 23/2, 61/2
        image_width_height = 23, 61
    if valore == 10.5:
        nota = pausa_di_croma
        image_center = 22/2, 40/2
        image_width_height = 22, 40
    if valore == 10.25:
        nota = pausa_di_semicroma
        image_center = 28/2, 61/2
        image_width_height = 28, 61        
        
        
        
        
def draw(canvas):
    global nota
    canvas.draw_polygon([[0, 0], [100, 0], [100, 100], [0, 100]], 3, 'Red', 'Yellow')
    canvas.draw_image(nota, image_center, image_width_height, (50, 50), image_width_height)
    canvas.draw_text("ciao", (200, 200), 50, "White")


frame = simplegui.create_frame("Quiz sulla notazione e le figure di valore", Width, Height)
frame.set_draw_handler(draw)
frame.add_button("Nota", button, 100)

frame.start()