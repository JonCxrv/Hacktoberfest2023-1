import random

def main():
    # Cria uma lista de perguntas
    perguntas = [
        ("Qual é o formato para representar um texto em Python?", "str"),
        ("Qual é o formato para representar um número inteiro em Python?", "int"),
        ("Qual é o formato para representar um número decimal em Python?", "float"),
        ("Qual é o formato para representar uma lista de valores em Python?", "list"),
        ("Qual é o formato para representar um dicionário de valores em Python?", "dict"),
        ("Qual é o formato para representar uma tupla de valores em Python?", "tuple"),
    ]

    # Inicia o jogo
    pontos = 0
    for pergunta, resposta in perguntas:
        # Gera uma resposta aleatória
        resposta_aleatoria = random.choice(["str", "int", "float", "list", "dict", "tuple"])

        # Solicita a resposta do jogador
        resposta_jogador = input(f"Qual é a resposta para a pergunta '{pergunta}'? (str, int, float, list, dict, tuple): ")

        # Verifica a resposta do jogador
        if resposta_jogador == resposta:
            pontos += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta!")

    # Exibe o resultado do jogo
    print(f"Pontuação final: {pontos}")

if __name__ == "__main__":
    main()
