from tkinter import *
from tkvideo import tkvideo
from bancoDados_BeautySalon import *
import time

# Tela inicial, configurações
root = Tk()
root.title("Sistema Gerenciador - Beauty Salon")
root.geometry("490x560+610+153")
root.iconbitmap(default='c:/Users/Ivonete/Downloads/icone.ico')
root.resizable(width=1,height=1)

# Funções
def nova_janela():
    root.destroy()
    time.sleep(0.3)
    master1 = Tk()
    master1.title("Banco de Dados")
    master1.geometry("490x560+400+153")
    master1['bg'] = 'light pink'

    #Caixa de Entrada
    caixaNome = Entry(master1, bd=3, font=("Calibri", 12), justify=CENTER)
    caixaNome.place(width=240, height=33, x=215, y=128)

    caixaTelefone = Entry(master1, bd=3, font=('Calibri',12), justify=CENTER)
    caixaTelefone.place(width=240, height=33, x=215, y=198)

    caixaServico = Entry(master1, bd=3, font=('Calibri', 12), justify=CENTER)
    caixaServico.place(width=240, height=33, x=215, y=268)

    caixaHorario = Entry(master1, bd=3, font=('Calibri', 12), justify=CENTER)
    caixaHorario.place(width=240, height=33, x=215, y=338)

    #Texto
    textoIncial= Label(master1, text='Insira os dados:', bg='light pink', font=('Arial',25,'bold')).place(width=300, height=25,x=100,y=55)
    textoNome= Label(master1, text="Nome: ", bg='light pink', fg='black', font=('Arial',15,'bold')).place(width=120, height=25,x=55,y=130)
    textoTelefone= Label(master1, text='Telefone: ', bg='light pink', fg='black', font=('Arial',15,'bold')).place(width=120, height=25,x=55,y=200)
    textoServico= Label(master1, text='Serviço: ', bg='light pink', fg='black', font=('Arial',15,'bold')).place(width=120, height=25,x=55,y=270)
    textoHorario= Label(master1, text='Horário: ', bg='light pink', fg='black', font=('Arial',15,'bold')).place(width=120, height=25,x=55,y=340)

    # Funções
    def inserir():
      Clientes.create(
        Nome = caixaNome.get(),
        Telefone = caixaTelefone.get(),
        Serviço = caixaServico.get(),
        Horário = caixaHorario.get(),
      )

    def excluir():
      nomeExluir = caixaNome.get()
      x = Clientes.delete().where(Clientes.Nome == nomeExluir).execute()

    def editar():
      #Abrindo uma nova janela para obter a resposta do usuário
      master1.quit()
      telaEditar = Tk()
      telaEditar.geometry("290x230+610+153")

      #Texto
      textoinicial = Label(telaEditar, text='Nome do(a) cliente que deseja alterar: ', font=('Arial', 12)).place(x=10, y=10)
      textonomeNovo = Label(telaEditar, text='Novo nome: ', font=('Arial',12)).place(x=100, y=90)

      #Caixa de Entrada
      nomeEditar = Entry(telaEditar, bd=3, font=("Calibri", 12), justify=CENTER)
      nomeEditar.place(width=220, height=30, x=30, y=40)

      nomeNovo = Entry(telaEditar, bd=3, font=("Calibri", 12), justify=CENTER)
      nomeNovo.place(width=220, height=30, x=30, y=120)

      # Função banco de dados, editar
      def salvar():
        c = Clientes.select().where(Clientes.Nome == nomeEditar.get()).get()
        c.Nome = nomeNovo.get()
        c.save()

      #Botão
      btn = Button(telaEditar, bd=4, text='SALVAR', font=('Arial',12,'bold'), justify=CENTER, command=salvar)
      btn.place(width=100, height=50, x=90, y=160)

      telaEditar.mainloop()

    #Botões
    botao_inserir = Button(master1, bd=4,text='INSERIR',font=('Arial',12,'bold'),justify=CENTER,command=inserir)
    botao_inserir.place(width=100, height=50, x=55, y=450)

    botao_excluir = Button(master1, bd=4, text='EXCLUIR', font=('Arial',12,'bold'), justify=CENTER, command=excluir)
    botao_excluir.place(width=100, height=50, x=200, y=450)

    botao_editar = Button(master1, bd=4, text='EDITAR', font=('Arial',12,'bold'), justify=CENTER,command=editar)
    botao_editar.place(width=100, height=50, x=345, y=450)

#Variaveis globais
esconda_senha = StringVar()

#Importar imagens
img_fundo = PhotoImage(file="c:/Users/Ivonete/Downloads/imgfundo.png")
img_botao = PhotoImage(file="c:/Users/Ivonete/Downloads/imgbotao.png")

# Criação de labels
label_fundo = Label(root, image=img_fundo)
label_fundo.pack()
# read video to display on label
#player = tkvideo('c:/Users/Ivonete/Downloads/imgfundo.mp4',label_fundo, loop=1 ,size=(490,560))
#player.play()

# Criação de caixas de entrada
entrada_idAcesso = Entry(root, bd=2, font=("Arial", 15), justify=CENTER)
entrada_idAcesso.place(width=334, height=38, x=79, y=192)

entrada_senha = Entry(root, textvariable=esconda_senha, show="*", bd=2, font=("Arial", 15), justify=CENTER)
entrada_senha.place(width=334, height=38, x=79, y=298)

#Criação de botões
botao_entrar = Button(root, bd=0,image=img_botao, command=nova_janela)
botao_entrar.place(width=170, height=60, x=160, y=398)

root.mainloop()

