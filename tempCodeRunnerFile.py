import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 50)
    tentativas = 0
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar um número entre 1 e 50.")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        tentativas += 1

        if palpite < 1 or palpite > 50:
            print("O número deve estar entre 1 e 50. Tente novamente.")
        elif palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            break

if __name__ == "__main__":
    jogo_adivinhacao()
