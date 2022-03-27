"""
    ################################ JOGO DA FORCA ##############################
        +--------
        |       |
        |       O           Desenvolvido por: Abhner Adriel C. Silva
        |      /|\\         Curso: Ciência da Computação | Cin-UFPE
        |      / \\         Disciplina: Introdução à programação - 1º Período
        |
       / \
"""

# Módulos utilizados:
import random as rd


# Função para desenhar a forca na tela em função dos erros do jogador:
def desenho_forca(qnt_erros):
    if qnt_erros == 1:
        print(' +--------')
        print(' |       |')
        print(' |       O')
        print(' |')
        print(' |')
        print(' |')
        print('/ \\')
    elif qnt_erros == 2:
        print(' +--------')
        print(' |       |')
        print(' |       O')
        print(' |       |')
        print(' |')
        print(' |')
        print('/ \\')
    elif qnt_erros == 3:
        print(' +--------')
        print(' |       |')
        print(' |       O')
        print(' |      /|')
        print(' |')
        print(' |')
        print('/ \\')
    elif qnt_erros == 4:
        print(' +--------')
        print(' |       |')
        print(' |       O')
        print(' |      /|\\')
        print(' |')
        print(' |')
        print('/ \\')
    elif qnt_erros == 5:
        print(' +--------')
        print(' |       |')
        print(' |       O')
        print(' |      /|\\')
        print(' |      /')
        print(' |')
        print('/ \\')
    elif qnt_erros == 6:
        print(' +--------')
        print(' |       |')
        print(' |       O')
        print(' |      /|\\')
        print(' |      / \\')
        print(' |')
        print('/ \\')
    else:
        print(' +--------')
        print(' |       |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('/ \\')


# Configurações iniciais:
jogo_iniciado, fim_jogo = False, False
lista_palavras = ['Funcionário', 'Apresentador', 'Palhaço', 'Relojoeiro', 'Crocodilo',
                  'Abelha', 'Aviador', 'Barril', 'Austrália', 'Coração', 'Dragão',
                  'Laranja', 'Melancia', 'Goiaba', 'Rio de Janeiro', 'Pernambuco',
                  'Rio Grande do Sul', 'Aracajú', 'Menino Ney', 'Estelionatário',
                  'Matemática', 'Embaixador', 'Agricultor', 'Engenheiro', 'Jesus',
                  'Professor', 'Médico', 'Cientista', 'Astronomia', 'Elefante']
palavra_sorteada = ''
erros_jogador, letras_totais_digitadas, letras_acertadas = 0, [], []

# Loop principal do jogo:
while not fim_jogo:
    # Verificar se o jogo já foi iniciado:
    if not jogo_iniciado:
        print()
        nome = '=' * 20 + ' JOGO DA FORCA ' + '=' * 20
        print(f'{nome:+^57}')
        palavra_sorteada = rd.choice(lista_palavras)
        erros_jogador, letras_totais_digitadas, letras_acertadas = 0, [], []
        jogo_iniciado = True

    # Mostrar forca na tela:
    desenho_forca(erros_jogador)
    
    # Esconder palavra escolhida na tela:
    palavra_escondida = ''
    for char in palavra_sorteada.lower():
        if char in letras_acertadas:
            palavra_escondida += char.upper()
        elif char == ' ':
            palavra_escondida += '  '
        else:
            palavra_escondida += '_ '
    print()
    print(palavra_escondida)
    print()

    # Mostrar letras (caracteres) totais já digitados:
    if not letras_totais_digitadas:
        print("Letras já digitadas: Nenhuma!")
    else:
        print(f"Letras já digitadas: {','.join(letras_totais_digitadas)}")

    # Verificar se o jogador venceu:
    if '_' not in palavra_escondida:
        print('>> Parabéns! Você acertou a palavra escondida! <<')
        fim_jogo = True

    # Verificar se o jogador perdeu:
    if erros_jogador == 6:
        print(f'>> Que pena! Você não acertou a palavra escondida! <<\nA palavra era: "{palavra_sorteada}"')
        fim_jogo = True

    # Tratamento do término do jogo:
    if fim_jogo:
        while True:
            print()
            jogar_novamente = input('Deseja jogar novamente?\n[S]-Sim\n[N]-Não\n>> ').lower()
            
            # Tratamento de erros mais comuns:
            if (not jogar_novamente or len(jogar_novamente) > 1 or jogar_novamente == ' ' or
                    (jogar_novamente != 's' and jogar_novamente != 'n')):
                print('Ops! Entrada inválida. Pressione >> ENTER <<', end=' ')
                input()
                continue
            else:
                if jogar_novamente == 's':
                    fim_jogo = False
                    jogo_iniciado = False
                else:
                    fim_jogo = True
                break
        continue

    # Entrada do jogador:
    while True:
        letra_digitada = input('Digite uma letra: ').lower()
        
        # Tratamento de erros mais comuns:
        if not letra_digitada or len(letra_digitada) > 1 or letra_digitada == ' ':
            print('Ops! Entrada inválida. Pressione >> ENTER <<', end=' ')
            input()
            continue
        elif letra_digitada in letras_totais_digitadas:
            print('Ops! Essa letra já foi escolhida! Pressione >> ENTER <<', end=' ')
            input()
        else:
            break

    # Armazena o total de letras já digitadas:
    letras_totais_digitadas.append(letra_digitada)

    # Verificar se o jogador acertou a letra:
    if letra_digitada in palavra_sorteada.lower():
        letras_acertadas.append(letra_digitada)
    else:
        erros_jogador += 1
    print()
    
