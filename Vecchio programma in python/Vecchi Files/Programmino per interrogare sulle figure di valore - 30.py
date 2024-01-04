###################################################################
#                                                                 #
# http://www.codeskulptor.org/#user43_3KjyZWNNGD_30.py            #
#                                                                 #
# Programma per interrogare sulla notazione e le figure di valore #
#                                                                 #
# Autore: Paolo Maria Guardiani                                   # 
#                                                                 #                 
# I suoni per le risposte corrette e sbagliate li ho trovati su   #
# http://www.flashkit.com/soundfx/                                #
#                                                                 #
###################################################################


import simplegui
import random

Width = 900
Height = 700
colore = "Red"
colore_2 = "Aqua"

click_corretti = 0
click_sbagliati = 0
prove_effettuate = 0
valore = 0
messaggio_voto = ""


image_center = 28/2, 61/2
image_width_height = 100, 100  # i valori per la pausa di semicroma sono 28, 61.
                             # ho inserito 100, 100, per non farla disegnare nel riquadro 
                             # all'inizio del quiz.

# lista di numeri corrispondenti alle varie figure di valore

lista = [4, 3, 2, 1, 0.5, 0.25, 14, 13, 12, 11, 10.5, 10.25] # ho aggiunto il valore 10 al valore 
                                                                  # delle pause per poterle inserire
                                                               # nella lista dei valori

# i valori corrispondenti alle figure di valore vengono mescolati
#Do = simplegui.load_sound('https://www.dropbox.com/s/gbznpdurm7vul7y/01%20Do.mp3?dl=1')
#Fa = simplegui.load_sound('https://www.dropbox.com/s/ehqrv7tv2x8h9jy/04%20Fa.mp3?dl=1')
#La = simplegui.load_sound('https://www.dropbox.com/s/b3dsd8k41jv2n0n/06%20La.mp3?dl=1')
#Si = simplegui.load_sound('https://www.dropbox.com/s/itp72g4dvxgdzx9/07%20Si.mp3?dl=1')

suono_giusto = simplegui.load_sound('https://www.dropbox.com/s/bi4mhbeck0b9idz/Electro_-S_Bainbr-7955_hifi.mp3?dl=1')
suono_sbagliato = simplegui.load_sound('https://www.dropbox.com/s/w9je7e0o1fy3lrg/alarma-DESIGNSQ-7820_hifi.mp3?dl=1')

random.shuffle(lista)

#radius = 1
#position = [0, 0]

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
domanda_3_a = ""
square = [(0, 0),(0, 0),(0, 0), (0, 0)]
riquadro = [(0, 0),(0, 0),(0, 0), (0, 0)]
riquadro_voto = [(0, 0),(0, 0),(0, 0), (0, 0)]


def calcola_voto():
    global riquadro_voto, messaggio_voto
    prove_totali = click_corretti + click_sbagliati
    risultato = 0
    riquadro_voto = [(0, 0), (900, 0), (900, 700), (0, 700)]
    if click_corretti != 0:
        risultato = round((float(click_corretti) * 10 / prove_totali), 2) 
        messaggio_voto = "Hai preso " + str(risultato)
        return messaggio_voto
    


def mouse_click(pos):
    global position, square, radius, colore, click_corretti, click_sbagliati
    position = pos
    radius = 30
    print position
    colore = "Red"		# se non metto anche qui che colore = "Red", ci sono problemi
#    Do.play()
#    Si.play()
#    Fa.play()
    
#    click_sbagliati += 1
#    print click_sbagliati
    ####### prima prova #######
    
    if position[0] in range (10, 151):
        if position[1] in range(210, 291):
            square = [(10, 209),(152, 209),(152, 290), (10, 290)]
            if valore == 4 or valore == 14:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (160, 290):
        if position[1] in range(210, 285):
            square = [(10 + 148, 209),(152 + 148, 209),(152 + 148, 290), (10 + 148, 290)]
            if valore == 3 or valore == 13:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (310, 440):
        if position[1] in range(210, 280):
            square = [(10 + 295, 209),(152 + 295, 209),(152 + 295, 290), (10 + 295, 290)]
            if valore == 2 or valore == 12:
                colore = "Lime" 
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (460, 590):
        if position[1] in range(210, 280):
            square = [(10 + 443, 209),(152 + 443, 209),(152 + 443, 290), (10 + 443, 290)]        
            if valore == 1 or valore == 11:
                colore = "Lime"  
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (610, 740):
        if position[1] in range(210, 280):
            square = [(10 + 591, 209),(152 + 591, 209),(152 + 591, 290), (10 + 591, 290)] 
            if valore == 0.5 or valore == 10.5:
                colore = "Lime"  
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (750, 888):
        if position[1] in range(210, 280):
            square = [(10 + 738, 209),(152 + 738, 209),(152 + 738, 290), (10 + 738, 290)]
            if valore == 0.25 or valore == 10.25:
                colore = "Lime"  
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    
    ####### seconda prova #######
    
    if position[0] in range (10, 151):
        if position[1] in range(355, 430):
            square = [(8, 356),(152, 356),(152, 435), (8, 435)]
            if valore == 4 or valore == 14:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (160, 290):
        if position[1] in range(355, 430):
            square = [(10 + 148, 356),(152 + 148, 356),(152 + 148, 435), (10 + 148, 435)]
            if valore == 3 or valore == 13:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (310, 440):
        if position[1] in range(355, 430):
            square = [(10 + 295, 356),(152 + 295, 356),(152 + 295, 435), (10 + 295, 435)]
            if valore == 2 or valore == 12:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (460, 590):
        if position[1] in range(355, 430):
            square = [(10 + 443, 356),(152 + 443, 356),(152 + 443, 435), (10 + 443, 435)]  
            if valore == 1 or valore == 11:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (610, 740):
        if position[1] in range(355, 430):
            square = [(10 + 591, 356),(152 + 591, 356),(152 + 591, 435), (10 + 591, 435)] 
            if valore == 0.5 or valore == 10.5:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (750, 888):
        if position[1] in range(355, 430):
            square = [(10 + 738, 356),(152 + 738, 356),(152 + 738, 435), (10 + 738, 435)]
            if valore == 0.25 or valore == 10.25:
                colore = "Lime" 
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()

    
    ####### terza prova #######
    
    if position[0] in range (80, 190):
        if position[1] in range(492, 605):
            square = [(77, 492),(196, 492),(196, 609), (77, 609)]
            if valore == 4 or valore == 14:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (204, 320):
        if position[1] in range(492, 605):
            square = [(77 + 125, 492),(196 + 125, 492),(196 + 125, 609), (77 + 125, 609)]
            if valore == 3 or valore == 13:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (329, 440):
        if position[1] in range(492, 605):
            square = [(77 + 250, 492),(196 + 250, 492),(196 + 250, 609), (77 + 250, 609)]
            if valore == 2 or valore == 12:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range(454, 568):
        if position[1] in range(492, 605):
            square = [(77 + 375, 492),(196 + 375, 492),(196 + 375, 609), (77 + 375, 609)]
            if valore == 1 or valore == 11:
                colore = "Lime" 
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (580, 699):
        if position[1] in range(492, 605):
            square = [(77 + 502, 492),(196 + 502, 492),(196 + 502, 609), (77 + 502, 609)]
            if valore == 0.5 or valore == 10.5:
                colore = "Lime" 
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    if position[0] in range (706, 823):
        if position[1] in range(492, 605):
            square = [(77 + 628, 492),(196 + 628, 492),(196 + 628, 609), (77 + 628, 609)]
            if valore == 0.25 or valore == 10.25:
                colore = "Lime"
                click_corretti += 1
                suono_giusto.play()
            else:
                click_sbagliati += 1
                suono_sbagliato.play()
    

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
    global domanda_1, domanda_2, domanda_3, domanda_3_a, radius, riquadro, colore_2
    radius = 1
    riquadro = [(2, 202), (896, 203), (895, 298), (4, 299)]
    colore_2 = "Aqua"
    domanda_1 = "Qual e' il nome delle seguenti figure di valore?"
    nuovo_valore()
    nuovo_quiz()
    domanda_2 = ""
    domanda_3 = ""
    domanda_3_a = ""
    
def prova_02():
    global domanda_1, domanda_2, domanda_3, domanda_3_a, radius, riquadro, colore_2
    radius = 1
    riquadro = [(4, 353), (896, 353), (895, 442), (4, 442)]
    colore_2 = "Pink"
    domanda_2 = "Qual e' il valore delle seguenti figure?"
    nuovo_valore()
    nuovo_quiz()
    domanda_1 = ""
    domanda_3 = ""
    domanda_3_a = ""
    
def prova_03():
    global domanda_1, domanda_2, domanda_3, domanda_3_a, radius, riquadro, colore_2
    radius = 1
    riquadro = [(74, 490), (828, 490), (828, 610), (74, 610)]
    colore_2 = "Yellow"
    domanda_3 = "Come rappresenti graficamente" 
    domanda_3_a = "le seguenti figure di valore?"
    nuovo_valore()
    nuovo_quiz()
    domanda_1 = ""
    domanda_2 = ""
        
        
def draw(canvas):
    global nota
    canvas.draw_polygon([[800, 0], [900, 0], [900, 100], [800, 100]], 3, 'Red', 'Yellow')
    canvas.draw_image(nota, image_center, image_width_height, (850, 50), image_width_height)
    canvas.draw_text(domanda_1, (60, 180), 40, colore_2)
    canvas.draw_text(domanda_2, (60, 180), 40, colore_2)
    canvas.draw_text(domanda_3, (60, 140), 40, colore_2)
    canvas.draw_text(domanda_3_a, (60, 180), 40, colore_2)

    canvas.draw_image(nomi_figure, (1331 / 2, 130 / 2), (1331, 130), (Width / 2, Height / 2 - 100), (1331 / 1.5, 130 / 1.5))
    canvas.draw_image(valori_figure, (1333 / 2, 131 / 2), (1333, 131), (Width / 2, Height / 2 + 45), (1333 / 1.5, 131 / 1.5))
    canvas.draw_image(rappresentazioni_grafiche, (1127 / 2, 182 / 2), (1127, 182), (Width / 2, Height / 2 + 200), (1127 / 1.5, 182 / 1.5))
    canvas.draw_polygon(square, 5, colore)
    canvas.draw_polygon(riquadro, 7, colore_2)
    
    canvas.draw_text("Risposte corrette = " + str(click_corretti), (20, 660), 20, "Yellow")
    canvas.draw_text("Risposte sbagliate = " + str(click_sbagliati), (250, 660), 20, "Pink")
    canvas.draw_text("Prove effettuate = " + str(click_corretti + click_sbagliati), (470, 660), 20, "Aqua")
    
    canvas.draw_polygon(riquadro_voto, 20, "Green", "#737373")                                                                                                    
    canvas.draw_text(messaggio_voto, (250, 300), 50, "Yellow")
    
    #canvas.draw_circle(position, radius, 5, colore)
    
    
frame = simplegui.create_frame("Quiz sulla notazione e le figure di valore", Width, Height)
frame.set_draw_handler(draw)
frame.set_canvas_background("#737373")

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
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_button("Calcola il voto", calcola_voto, 110)

frame.start()