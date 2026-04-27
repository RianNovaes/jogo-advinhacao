# data inicial 25.04.2026

import random

historico = []

while True:
    print("1 - Jogar")
    print("2 - Ver histórico")
    print("3 - Sair")
    
    try:
        opcao = int(input("Selecionar uma opção: "))
    except ValueError:
        print("Por favor, digite as opções do menu")
        continue
    # Inicia uma nova partida
    if opcao == 1:
        tentativas = 0
        # Define o número secreto da partida
        numero = random.randint(1, 100)
        while True:
            # Conta quantas tentativas o jogador já fez
            tentativas += 1
            try:
                numero_user = int(input("Tente Advinhar o número: "))
            except ValueError:
                print("Digite um número válido")
                continue
            if numero == numero_user:
                print("Acertou!!")
                print(f"Você acertou em {tentativas} tentativas")
                # Registra o resultado da partida no histórico
                historico.append({
                    "numero": numero,
                    "tentativas": tentativas
                })
                break
            
            elif numero_user < numero:
                print("O número correto é maior")
            elif numero_user > numero:
                print("O número correto é menor")
    # Mostra o histórico ao usuário          
    elif opcao == 2:
        print("\n--- Histórico de Jogos ---")
        print("-" * 30)
        if not historico:
            print("Nenhum jogo ainda")
        else:
            for i, jogo in enumerate(historico):
                print(f"Jogo {i+1}: Número {jogo['numero']} | Tentativas {jogo['tentativas']}")
    # Encerra o programa
    elif opcao == 3:
        break
    else:
        print("Você não digitou uma opção válida")
    