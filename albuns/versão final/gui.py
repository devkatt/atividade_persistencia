# gui.py
from tkinter import *
from tkinter import messagebox
import domain

class App:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro e Listagem de Álbuns")

        self.label = Label(master, text="Escolha uma opção:")
        self.label.pack()

        self.button_cadastrar = Button(master, text="Cadastrar Álbum", command=self.cadastrar_album)
        self.button_cadastrar.pack()

        self.button_listar = Button(master, text="Listar Álbuns", command=self.listar_albuns)
        self.button_listar.pack()

        self.button_buscar_artista = Button(master, text="Buscar por Nome do Artista", command=self.buscar_por_nome_artista)
        self.button_buscar_artista.pack()

        self.button_buscar_ano = Button(master, text="Buscar por Ano do Álbum", command=self.buscar_por_ano)
        self.button_buscar_ano.pack()

    def cadastrar_album(self):
        nome_album = input('Nome do álbum: ')
        ano_lancamento = input('Ano de lançamento: ')
        nome_artista = input('Nome da banda/artista: ')
        album_lancamento_artista = input('Álbum de lançamento do artista (sim/não): ')

        domain.cadastrar_album(nome_album, ano_lancamento, nome_artista, album_lancamento_artista)
        messagebox.showinfo("Cadastro de Álbum", "Álbum cadastrado com sucesso!")

    def listar_albuns(self):
        albuns = domain.listar_albuns()

        for album in albuns:
            print(f'Nome do álbum: {album[0]}')
            print(f'Ano de lançamento: {album[1]}')
            print(f'Nome da banda/artista: {album[2]}')
            print(f'Álbum de lançamento do artista: {album[3]}')
            print('-' * 30)

    def buscar_por_nome_artista(self):
        nome_procurado = input('Digite o nome do artista: ')
        albuns_encontrados = domain.busca_por_nome_artista(nome_procurado)

        print(f'\nÁlbuns do artista "{nome_procurado}":')
        for album in albuns_encontrados:
            print(album)

    def buscar_por_ano(self):
        operador = input('Selecione o operador (Anterior a/Posterior a/Igual a): ')
        ano_selecionado = int(input('Digite o ano: '))
        albuns_encontrados = domain.busca_por_ano(operador, ano_selecionado)

        print(f'\nÁlbuns do ano {operador} {ano_selecionado}:')
        for album in albuns_encontrados:
            print(album)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
