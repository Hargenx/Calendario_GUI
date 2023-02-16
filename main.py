from tkinter import Label, Entry, Button, Tk
import calendar


#Função para exibir o calendario do ano digitado
def exibir_calendario():
  tela_calendario = Tk()
  tela_calendario.config(background='blue')
  tela_calendario.title("Calendario anual")
  w = 800  # width para o Tk root
  h = 650  # height fpara o Tk root

  # pegamos o width(largura) e height(altura) do sistema
  ws = tela_calendario.winfo_screenwidth()
  hs = tela_calendario.winfo_screenheight()

  # Calcular cordenadas X e Y
  x = (ws / 2) - (w / 2)
  y = (hs / 2) - (h / 2)

  tela_calendario.geometry('%dx%d+%d+%d' % (w, h, x, y))
  ano = int(campo_ano.get())
  conteudo = calendar.calendar(ano)
  verifica_ano = Label(tela_calendario,
                       text=conteudo,
                       font=("Helvetica", 22, "bold"))
  verifica_ano.grid(row=5, column=1, padx=20)
  tela_calendario.mainloop()


tela = Tk()
tela.config(background='green')
tela.title("Calendario")
tela.geometry("500x400")
chamado = Label(tela,
                text="Calendario",
                bg='red',
                padx=100,
                font=("times", 28, "bold"))
ano = Label(tela, text="Digite o ano", padx=100, bg='dark grey')
campo_ano = Entry(tela)
botao = Button(tela,
               text='Exibir Calendario',
               fg='Black',
               bg='Blue',
               command=exibir_calendario)

#Posicionamento
chamado.grid(row=1, column=1)
ano.grid(row=2, column=1)
campo_ano.grid(row=3, column=1)
botao.grid(row=4, column=1)
tela.mainloop()
