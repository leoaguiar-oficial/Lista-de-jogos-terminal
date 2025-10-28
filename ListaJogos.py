import json

def carregar_jogos():
    try:
        
        with open("jogos.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def salvar_jogo(jogo):
    if "("not in jogo or ")" not in jogo:
        print("⚠️ Dica: você pode adicionar a plataforma entre parênteses, ex: 'God of War (PS5)'")
    lista_jogos = carregar_jogos()
    lista_jogos.append(jogo)
    with open("jogos.json", "w") as arquivo:
        json.dump(lista_jogos, arquivo, indent=4)
    input('\nPressione "Enter" para voltar ao Menu...')

def listar_jogos():
    lista_jogos = carregar_jogos()
    if lista_jogos:
        print('\nJogos zerados: ')
        for i, jogo in enumerate(lista_jogos, 1):
            print(f"{i}. {jogo}")
    else:
        print("\nNenhum jogo zerado!")
    input('\nPressione "Enter" para voltar ao Menu...')

def alterar_jogo():
    lista_jogos = carregar_jogos()
    listar_jogos()
    try:
        indice = int(input('Digite o número do jogo que deseja alterar: ')) - 1
        if 0 <= indice < len(lista_jogos):
            novo_nome = input('Digite o novo nome: ')
            lista_jogos[indice] = novo_nome
            with open('jogos.json', 'w') as arquivo:
                json.dump(lista_jogos, arquivo, indent=4)
                print('Jogo alterado com sucesso!')
        else:
            print('Número inválido!')
    except ValueError:
        print('Entrada inválida. Digite um número. ')
    input('\nPressione "Enter" para voltar ao Menu...')

def remover_jogo():
    lista_jogos = carregar_jogos()
    listar_jogos()
    try:
        indice = int(input('Digite o número do jogo que deseja remover: ')) - 1
        if 0 <= indice < len(lista_jogos):
            removido = lista_jogos.pop(indice)
            with open('jogos.json', 'w') as arquivo:
                json.dump(lista_jogos, arquivo, indent=4)
                print('Jogo removido com sucesso!')
        else:
            print('Número inválido!')
    except ValueError:
        print('Entrada inválida. Digite um número. ')
    input('\nPressione "Enter" para voltar ao Menu...')

def menu():
    while True:
        print('\n + MENU +')
        print('1. Adicionar jogo zerado\n')
        print('2. Listar jogos zerados.\n')
        print('3. Alterar jogo\n')
        print('4. Remover jogo\n')
        print('5. Sair\n')
        escolha = input('Selecione: ')

        if escolha == '1' or escolha.lower() == 'Adicionar jogo zerado':
            jogo = input('Digite o jogo que você zerou: ')
            salvar_jogo(jogo)
            print(f"jogo '{jogo}' salvo com sucesso!")

        elif escolha == '2' or escolha.lower() == 'Listar jogos zerados':
            listar_jogos()
        
        elif escolha == '3' or escolha.lower() == 'Alterar jogo':
            alterar_jogo()
        
        elif escolha == '4' or escolha.lower() == 'Remover jogo':
            remover_jogo()

        elif escolha == '5' or escolha.lower() == 'Sair':
            print('Saindo, até a próxima..')
            break

        else:
            print('Escolha inválida!')

menu()