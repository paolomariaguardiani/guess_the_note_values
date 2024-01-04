###################################################################
#                                                                 #
# http://www.codeskulptor.org/#user43_3KjyZWNNGD_17.py             #
#                                                                 #
# Programma per interrogare sulla notazione e le figure di valore #
#                                                                 #
# Autore: Paolo Maria Guardiani                                   # 
#                                                                 #
###################################################################


import simplegui
import random

Width = 900
Height = 700
colore = "Red"
valore = 0

image_center = 28/2, 61/2
image_width_height = 100, 100  # i valori per la pausa di semicroma sono 28, 61.
                             # ho inserito 100, 100, per non farla disegnare nel riquadro 
                             # all'inizio del quiz.

# lista di numeri corrispondenti alle varie figure di valore

lista = [4, 3, 2, 1, 0.5, 0.25, 14, 13, 12, 11, 10.5, 10.25] # ho aggiunto il valore 10 al valore 
                                                                  # delle pause per poterle inserire
                                                               # nella lista dei valori

# i valori corrispondenti alle figure di valore vengono mescolati

random.shuffle(lista)

radius = 1
position = [0, 0]

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
pausa_di_semicroma = simplegui.load_image('https://www.dropbox.com/s/79v3y6s5ljk40hq/pausa_di_semicroma.png?dl=1')

nomi_figure = simplegui.load_image("https://www.dropbox.com/s/48em00b6jid385y/Nomi%20figure.PNG?dl=1")
valori_figure = simplegui.load_image("https://www.dropbox.com/s/k9gfzk3pxnigu8m/Valori%20figure.PNG?dl=1")
rappresentazioni_grafiche = simplegui.load_image("https://www.dropbox.com/s/hy4f1maw0jzwot7/Rappresentazioni%20grafiche.png?dl=1")

nota = pausa_di_semicroma

domanda_1 = ""
domanda_2 = ""
domanda_3 = ""

square = [(0, 0),(0, 0),(0, 0), (0, 0)]

def mouse_click(pos):
    global position, square, radius, colore
    position = pos
    radius = 30
    print position
    colore = "Red"		# se non metto anche qui che colore = "Red", ci sono problemi
    
    ####### prima prova #######
    
    if position[0] in range (10, 151):
        if position[1] in range(210, 291):
            square = [(10, 209),(152, 209),(152, 290), (10, 290)]
            if valore == 4 or valore == 14:
                colore = "Lime"            
    if position[0] in range (160, 290):
        if position[1] in range(210, 285):
            square = [(10 + 148, 209),(152 + 148, 209),(152 + 148, 290), (10 + 148, 290)]
            if valore == 3 or valore == 13:
                colore = "Lime"  
    if position[0] in range (310, 440):
        if position[1] in range(210, 280):
            square = [(10 + 295, 209),(152 + 295, 209),(152 + 295, 290), (10 + 295, 290)]
            if valore == 2 or valore == 12:
                colore = "Lime"  
    if position[0] in range (460, 590):
        if position[1] in range(210, 280):
            square = [(10 + 443, 209),(152 + 443, 209),(152 + 443, 290), (10 + 443, 290)]        
            if valore == 1 or valore == 11:
                colore = "Lime"  
    if position[0] in range (610, 740):
        if position[1] in range(210, 280):
            square = [(10 + 591, 209),(152 + 591, 209),(152 + 591, 290), (10 + 591, 290)] 
            if valore == 0.5 or valore == 10.5:
                colore = "Lime"  
    if position[0] in range (750, 888):
        if position[1] in range(210, 280):
            square = [(10 + 738, 209),(152 + 738, 209),(152 + 738, 290), (10 + 738, 290)]
            if valore == 0.25 or valore == 10.25:
                colore = "Lime"  
    
    ####### seconda prova #######
    
    if position[0] in range (10, 151):
        if position[1] in range(355, 430):
            square = [(8, 356),(152, 356),(152, 435), (8, 435)]
            if valore == 4 or valore == 14:
                colore = "Lime"            
    if position[0] in range (160, 290):
        if position[1] in range(355, 430):
            square = [(10 + 148, 356),(152 + 148, 356),(152 + 148, 435), (10 + 148, 435)]
            if valore == 3 or valore == 13:
                colore = "Lime"  
    if position[0] in range (310, 440):
        if position[1] in range(355, 430):
            square = [(10 + 295, 356),(152 + 295, 356),(152 + 295, 435), (10 + 295, 435)]
            if valore == 2 or valore == 12:
                colore = "Lime"  
    if position[0] in range (460, 590):
        if position[1] in range(355, 430):
            square = [(10 + 443, 356),(152 + 443, 356),(152 + 443, 435), (10 + 443, 435)]  
            if valore == 1 or valore == 11:
                colore = "Lime"  
    if position[0] in range (610, 740):
        if position[1] in range(355, 430):
            square = [(10 + 591, 356),(152 + 591, 356),(152 + 591, 435), (10 + 591, 435)] 
            if valore == 0.5 or valore == 10.5:
                colore = "Lime"  
    if position[0] in range (750, 888):
        if position[1] in range(355, 430):
            square = [(10 + 738, 356),(152 + 738, 356),(152 + 738, 435), (10 + 738, 435)]
            if valore == 0.25 or valore == 10.25:
                colore = "Lime"  

    
    ####### terza prova #######
    
    if position[0] in range (80, 190):
        if position[1] in range(492, 605):
            square = [(77, 492),(196, 492),(196, 609), (77, 609)]
            if valore == 4 or valore == 14:
                colore = "Lime"                        
    if position[0] in range (204, 320):
        if position[1] in range(492, 605):
            square = [(77 + 125, 492),(196 + 125, 492),(196 + 125, 609), (77 + 125, 609)]
            if valore == 3 or valore == 13:
                colore = "Lime"              
    if position[0] in range (329, 440):
        if position[1] in range(492, 605):
            square = [(77 + 250, 492),(196 + 250, 492),(196 + 250, 609), (77 + 250, 609)]
            if valore == 2 or valore == 12:
                colore = "Lime"              
    if position[0] in range(454, 568):
        if position[1] in range(492, 605):
            square = [(77 + 375, 492),(196 + 375, 492),(196 + 375, 609), (77 + 375, 609)]
            if valore == 1 or valore == 11:
                colore = "Lime"              
    if position[0] in range (580, 699):
        if position[1] in range(492, 605):
            square = [(77 + 502, 492),(196 + 502, 492),(196 + 502, 609), (77 + 502, 609)]
            if valore == 0.5 or valore == 10.5:
                colore = "Lime"              
    if position[0] in range (706, 823):
        if position[1] in range(492, 605):
            square = [(77 + 628, 492),(196 + 628, 492),(196 + 628, 609), (77 + 628, 609)]
            if valore == 0.25 or valore == 10.25:
                colore = "Lime"              
    
#def draw_note(canvas):
#        canvas.draw_image(minima_col_punto, (52/2, 66/2), (52, 66), (50, 50), (52, 66))

def nuovo_quiz():
    global lista, image_width_height, domanda_1, domanda_2, domanda_3, radius
    lista = [4, 3, 2, 1, 0.5, 0.25, 14, 13, 12, 11, 10.5, 10.25]
    random.shuffle(lista)
    print lista
    radius = 1
#    image_width_height = 100, 100
#    domanda_1 = ""
#    domanda_2 = ""
#    domanda_3 = ""
    
def nuovo_valore():
    global nota, image_center, image_width_height, valore
    #valore = 0
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
        
def prova_01():
    global domanda_1, domanda_2, domanda_3, radius
    radius = 1
    domanda_1 = "Qual e' il nome delle seguenti figure di valore?"
    nuovo_valore()
    nuovo_quiz()
    domanda_2 = ""
    domanda_3 = ""
    
def prova_02():
    global domanda_1, domanda_2, domanda_3, radius
    radius = 1
    domanda_2 = "Qual e' il valore delle seguenti figure?"
    nuovo_valore()
    nuovo_quiz()
    domanda_1 = ""
    domanda_3 = ""
    
def prova_03():
    global domanda_1, domanda_2, domanda_3, radius
    radius = 1
    domanda_3 = "Come rappresenti graficamente le seguenti figure di valore?"
    nuovo_valore()
    nuovo_quiz()
    domanda_1 = ""
    domanda_2 = ""
        
        
def draw(canvas):
    global nota
    canvas.draw_polygon([[800, 0], [900, 0], [900, 100], [800, 100]], 3, 'Red', 'Yellow')
    canvas.draw_image(nota, image_center, image_width_height, (850, 50), image_width_height)
    canvas.draw_text(domanda_1, (60, 180), 40, "Yellow")
    canvas.draw_text(domanda_2, (10, 50), 30, "Yellow")
    canvas.draw_text(domanda_3, (10, 50), 30, "Yellow")

    canvas.draw_image(nomi_figure, (1331 / 2, 130 / 2), (1331, 130), (Width / 2, Height / 2 - 100), (1331 / 1.5, 130 / 1.5))
    canvas.draw_image(valori_figure, (1333 / 2, 131 / 2), (1333, 131), (Width / 2, Height / 2 + 45), (1333 / 1.5, 131 / 1.5))
    canvas.draw_image(rappresentazioni_grafiche, (1127 / 2, 182 / 2), (1127, 182), (Width / 2, Height / 2 + 200), (1127 / 1.5, 182 / 1.5))
    canvas.draw_polygon(square, 5, colore)
    canvas.draw_circle(position, radius, 5, colore)
    
    
frame = simplegui.create_frame("Quiz sulla notazione e le figure di valore", Width, Height)
frame.set_draw_handler(draw)
frame.set_canvas_background("Grey")

frame.add_label("")
frame.add_label("")

frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_button("Prova N. 1", prova_01, 110)
frame.add_label("")
frame.add_button("Prova N. 2", prova_02, 110)
frame.add_label("")
frame.add_button("Prova N. 3", prova_03, 110)
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_button("Nuovo valore", nuovo_valore, 110)
frame.set_mouseclick_handler(mouse_click)

frame.start()