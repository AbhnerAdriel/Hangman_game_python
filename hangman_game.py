################################ JOGO DA FORCA ################################

import random as rd


# Estados da forca
FORCA = [
    """
 +--------
 |       |
 |
 |
 |
 |
/ \\
""",
    """
 +--------
 |       |
 |       O
 |
 |
 |
/ \\
""",
    """
 +--------
 |       |
 |       O
 |       |
 |
 |
/ \\
""",
    """
 +--------
 |       |
 |       O
 |      /|
 |
 |
/ \\
""",
    """
 +--------
 |       |
 |       O
 |      /|\\
 |
 |
/ \\
""",
    """
 +--------
 |       |
 |       O
 |      /|\\
 |      /
 |
/ \\
""",
    """
 +--------
 |       |
 |       O
 |      /|\\
 |      / \\
 |
/ \\
"""
]


def desenhar_forca(erros):
    print(FORCA[erros])


def escolher_palavra(lista):
    return rd.choice(lista).lower()


def mostrar_palavra(palavra, letras_acertadas):
    resultado = ""
    for letra in palavra:
        if letra == " ":
            resultado += "  "
        elif letra in letras_acertadas:
            resultado += letra.upper() + " "
        else:
            resultado += "_ "
    return resultado


def entrada_valida(letra, letras_usadas):
    if not letra or len(letra) != 1 or letra == " ":
        print("Entrada inválida!")
        return False
    if letra in letras_usadas:
        print("Você já digitou essa letra!")
        return False
    return True


def jogar():
    palavras = [
        'funcionário', 'apresentador', 'palhaço', 'relojoeiro', 'crocodilo',
        'abelha', 'aviador', 'barril', 'austrália', 'coração', 'dragão',
        'laranja', 'melancia', 'goiaba', 'rio de janeiro', 'pernambuco',
        'rio grande do sul', 'aracaju', 'menino ney', 'estelionatário',
        'matemática', 'embaixador', 'agricultor', 'engenheiro', 'jesus',
        'professor', 'médico', 'cientista', 'astronomia', 'elefante'
    ]

    palavra = escolher_palavra(palavras)
    erros = 0
    letras_usadas = []
    letras_acertadas = []

    while True:
        print("\n" + "=" * 20 + " JOGO DA FORCA " + "=" * 20)

        desenhar_forca(erros)

        palavra_escondida = mostrar_palavra(palavra, letras_acertadas)
        print("\n", palavra_escondida, "\n")

        print("Letras usadas:", ", ".join(letras_usadas) if letras_usadas else "Nenhuma")

        # Vitória
        if "_" not in palavra_escondida:
            print("🎉 Você venceu!")
            break

        # Derrota
        if erros == 6:
            print(f"💀 Você perdeu! A palavra era: {palavra}")
            break

        # Entrada
        while True:
            letra = input("Digite uma letra: ").lower()
            if entrada_valida(letra, letras_usadas):
                break

        letras_usadas.append(letra)

        if letra in palavra:
            letras_acertadas.append(letra)
        else:
            erros += 1


def main():
    while True:
        jogar()
        op = input("\nJogar novamente? (s/n): ").lower()
        if op != 's':
            print("Até a próxima!")
            break


if __name__ == "__main__":
    main()
