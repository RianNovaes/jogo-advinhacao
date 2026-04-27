# 25.04.2026
# Depois de meses quase anos eu voltei e fiz esse sistema somente com 1 dia 
# relembrando algumas coisa hoje eu só pedi um desafio pro chatGPT
# e fiz isso tudo de cabeça em um total de 50 minutos

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
    
    if opcao == 1:
        tentativas = 0
        numero = random.randint(1, 100)
        while True:
            tentativas += 1
            try:
                numero_user = int(input("Tente Advinhar o número: "))
            except ValueError:
                print("Digite um número válido")
                continue
            if numero == numero_user:
                print("Acertou!!")
                print(f"Você acertou em {tentativas} tentativas")
                
                historico.append({
                "numero": numero,
                "tentativas": tentativas
                })
                    
                break
            elif numero_user < numero:
                print("O número correto é maior")
            elif numero_user > numero:
                print("O número correto é menor")
    elif opcao == 2:
        print("\n--- Histórico de Jogos ---")
        print("-" * 30)
        if not historico:
            print("Nenhum jogo ainda")
        else:
            for i, jogo in enumerate(historico):
                print(f"Jogo {i+1}: Número {jogo['numero']} | Tentativas {jogo['tentativas']}")
    elif opcao == 3:
        break
    else:
        print("Você não digitou uma opção válida")
    