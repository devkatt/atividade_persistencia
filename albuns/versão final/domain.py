# domain.py
import db

def cadastrar_album(nome_album, ano_lancamento, nome_artista, album_lancamento_artista):
    db.cadastrar_album(nome_album, ano_lancamento, nome_artista, album_lancamento_artista)

def listar_albuns():
    albuns = db.listar_albuns()
    return albuns

def busca_por_nome_artista(nome_procurado):
    albuns = db.listar_albuns()
    albuns_encontrados = [album for album in albuns if nome_procurado.lower() in album[2].lower()]
    return albuns_encontrados

def busca_por_ano(operador, ano_selecionado):
    albuns = db.listar_albuns()
    albuns_encontrados = []
    for album in albuns:
        ano_album = int(album[1])
        if operador == "Anterior a" and ano_album <= ano_selecionado:
            albuns_encontrados.append(album)
        elif operador == "Posterior a" and ano_album >= ano_selecionado:
            albuns_encontrados.append(album)
        elif operador == "Igual a" and ano_album == ano_selecionado:
            albuns_encontrados.append(album)
    return albuns_encontrados
