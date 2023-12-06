def cadastro():
    while True:
        nome = input('Digite o seu nome (ou 0 para encerrar): ')
        
        if nome == "0":
            break  # Encerra o loop se o usuário digitar "0"
        
        idade = int(input('Digite sua idade: '))
        sexo = input('Digite o seu sexo (M ou F): ')
        telefone = input('Digite o seu telefone: ')

        # Salva as informações em um arquivo
        with open('meu_nome.txt', 'a') as file:
            file.write(f'{nome}|{idade}|{sexo}|{telefone}\n')

def main():
    cadastro()

if __name__ == "__main__":
    main()
