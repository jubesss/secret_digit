import tkinter as tk
import random

def acertar_numero():


    tentativa = int(entrada.get())
    if tentativa == numero_certo:
            resultado['text'] = 'Parabéns! Vc acertou! :D'
    elif tentativa < numero_certo:
            resultado['text'] = 'Tente um número maior (⌒_⌒;)'
    else:
            resultado['text'] = 'Tente um número menor (･_･)'

numero_certo = random.randint(1,50)


janela = tk.Tk()
janela.title('secret digit')
janela.geometry('500x250')
janela.configure(bg='powder blue')

label_instrucao = tk.Label(janela, text='Digite um número entre 1 e 50 para tentar descobrir o número secreto!',bg='skyblue')
label_instrucao.grid(row=0, column=0, pady=20, padx=40)

entrada = tk.Entry(janela)
entrada.grid(row=1, column=0)

botao = tk.Button(janela, text='Descobrir', command=acertar_numero)
botao.grid(row=2, column=0, pady=20)

resultado = tk.Label(janela, text='',fg='midnightblue', bg='skyblue')
resultado.grid(row=3, column=0,pady=20)

janela.mainloop()
