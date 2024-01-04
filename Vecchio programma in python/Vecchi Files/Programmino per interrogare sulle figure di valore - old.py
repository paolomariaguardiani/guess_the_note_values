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

Width = 700
click = 0
image_center = 52/2, 66/2
image_width_height = 52, 66
Height = 500

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

nota = minima_col_punto

#def draw_note(canvas):
#        canvas.draw_image(minima_col_punto, (52/2, 66/2), (52, 66), (50, 50), (52, 66))
def button():
    global nota, note, click
    
    click += 1
    print click
    if click == 1:
        nota = semibreve
        image_center = 55/2, 24/2
        image_width_height = 55, 24
    if click == 2:
        nota = minima_col_punto
        image_center = 52/2, 66/2
        image_width_height = 52, 66
    if click == 3:
        nota = semiminima
        image_center = 40/2, 65/2
        image_width_height = 40, 65

def draw(canvas):
    global nota
    canvas.draw_polygon([[0, 0], [100, 0], [100, 100], [0, 100]], 3, 'Red', 'Yellow')
    canvas.draw_image(nota, image_center, image_width_height, (50, 50), (image_width_height))
    canvas.draw_text("ciao", (200, 200), 50, "White")


frame = simplegui.create_frame("Quiz sulla notazione e le figure di valore", Width, Height)
frame.set_draw_handler(draw)
frame.add_button("Nota", button, 100)

frame.start()