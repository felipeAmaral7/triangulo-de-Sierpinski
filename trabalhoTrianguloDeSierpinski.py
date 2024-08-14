#DISCENTES:
#FELIPE AMARAL DE MEDEIROS
#TANIZIA DE LIRA FAGUNDES

import turtle
import tkinter as tk

# função que desenha o triângulo dada uma lista 'pontos' de 3 coordenadas
def desenhaTriangulo(t, pontos, cor):
    t.fillcolor(cor)
    t.begin_fill()
    t.up()
    t.goto(pontos[0][0], pontos[0][1])
    t.down()
    t.goto(pontos[1][0], pontos[1][1])
    t.goto(pontos[2][0], pontos[2][1])
    t.goto(pontos[0][0], pontos[0][1])
    t.end_fill()

# estabelece os pontos médios de dois conjuntos de coordenadas
def meioPontos(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def trianSierpinski(t, pontos, grau):
    cores = ['white', 'red', 'blue', 'black', 'green', 'pink', 'purple', 'orange', 'yellow', 'brown']
    
    if grau > 0:
        desenhaTriangulo(t, pontos, cores[grau])
        meioDe0a1 = meioPontos(pontos[0], pontos[1])
        meioDe0a2 = meioPontos(pontos[0], pontos[2])
        meioDe1a2 = meioPontos(pontos[1], pontos[2])

        # chama recursivamente 3 triângulos passando como argumento os pontos médios
        trianSierpinski(t, [pontos[0], meioDe0a1, meioDe0a2], grau - 1)
        trianSierpinski(t, [pontos[1], meioDe0a1, meioDe1a2], grau - 1)
        trianSierpinski(t, [pontos[2], meioDe0a2, meioDe1a2], grau - 1)

# função que aumenta o nível do triangulo de Sierpinski
def aumentarNivel():
    global grau
    if grau < 10:
        grau += 1
        atualizaInfoNivel()

        # Redesenha o triângulo com o novo nível
        t.clear()
        trianSierpinski(t, pontos, grau)

# função para atualizar o texto do nivel
def atualizaInfoNivel():
    texto_nivel.config(text=f"Nível atual: {grau}")

# configuração da tela do Turtle com Tkinter
windows = tk.Tk()
windows.title("Triângulo de Sierpinski")

# Criação de um canvas para o Turtle
canvas = tk.Canvas(master=windows, width=800, height=700)
canvas.pack(side=tk.LEFT) 

# criação e posicionamento do frame
frame = tk.Frame(windows)
frame.pack(side=tk.LEFT, fill=tk.Y)

texto_nivel = tk.Label(frame, text="Nível atual: 1", font=("Helvetica", 14))
texto_nivel.pack(pady=10)

# criação e posicionamento do botão
botao = tk.Button(frame, text="Aumentar Nível", command=aumentarNivel, width=20, height=2)
botao.pack(pady=10)

# configuração da tela do Turtle
window = turtle.TurtleScreen(canvas)

t = turtle.RawTurtle(window)
t.shape('turtle')
t.pensize(1)
t.speed(0)

# lista que contém os pontos iniciais do triângulo
pontos = [[-200, -100], [0, 246], [200, -100]]

# começa no nível 1
grau = 1
trianSierpinski(t, pontos, grau)

# inicia o loop principal das janelas
windows.mainloop()
