
# Fabio do Prado Araujo - Curso: Análise e Desenvolvimento de Sistemas

# Lista de estudantes cadastrados
estudantes_cadastrados = []

while True:
    # Mostrando tela com menu principal, e suas opções.
    print("Menu Principal\n")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair\n")

    # Criando opção de coleta de item selecionado pelo usuário
    opcao = int(input("Digite uma opção válida: "))
    print(f"Voce selecionou a opção {opcao}\n")

    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
        print(f"Voce digitou uma opção válida. {opcao}\n")

    if opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
        print(f"EM DESENVOLVIMENTO\n")

    elif opcao == 1:
        while True:
            # Mostrando menu secundário de operações
            print("Menu de operações - Opções")
            print("1. Incluir")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Excluir")
            print("9. Voltar ao menu principal\n")

            # Criando opção secundária de coleta de item selecionado pelo usuário
            opcao_secundaria = int(input("Digite uma opção secundária válida: "))
            print(f"Voce selecionou a opção {opcao_secundaria}\n")

            if opcao_secundaria == 1 or opcao_secundaria == 2 or opcao_secundaria == 3 \
                    or opcao_secundaria == 4:
                print(f"Voce digitou uma opção válida. {opcao_secundaria}\n")

            if opcao_secundaria == 3 or opcao_secundaria == 4:
                print(f"EM DESENVOLVIMENTO.{opcao_secundaria}\n")

            if opcao_secundaria == 1:
                nome_estudante = input("Digite o nome do estudante: ")
                print(f"Estudante {nome_estudante} cadastrado com sucesso!\n")
                estudantes_cadastrados.append(nome_estudante)

            elif opcao_secundaria == 2:
                if len(estudantes_cadastrados) == 0:
                    print("Não há estudantes cadastrados!\n")
                else:
                    print(f"Os seguintes estudantes foram encontrados: {estudantes_cadastrados}\n")

            elif opcao_secundaria == 9:
                print("Voce digitou para voltar ao menu principal\n")
                break

            else:
                print("Voce digitou uma opção invalida.\n")
                print("Voltando ao Menu de operações\n")

    elif opcao == 0:
        print("Voce digitou para sair.")
        break

    else:
        print("Voce digitou uma opção invalida.\n")
        print("Voltando ao Menu Principal\n")
