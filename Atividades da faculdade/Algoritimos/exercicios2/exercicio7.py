def menu():
    print("\n===== MENU AGENDA =====")
    print("1 - Incluir contato")
    print("2 - Alterar contato")
    print("3 - Excluir contato")
    print("4 - Listar contatos")
    print("5 - Sair")
    return input("Escolha uma opção: ")

agenda = {}  

while True:
    opcao = menu()

    if opcao == "1":
        nome = input("Digite o nome: ").strip()
        telefone = input("Digite o telefone: ").strip()

        if not nome or not telefone:
            print("Nome ou telefone vazio. Tente novamente.")
        elif telefone in agenda:
            print("Telefone já cadastrado!")
        else:
            agenda[telefone] = nome
            print("Contato adicionado com sucesso.")

    elif opcao == "2":
        telefone = input("Digite o telefone do contato a alterar: ").strip()
        if telefone in agenda:
            novo_nome = input("Digite o novo nome: ").strip()
            if not novo_nome:
                print(" Nome vazio. Alteração cancelada.")
            else:
                agenda[telefone] = novo_nome
                print(" Contato alterado com sucesso.")
        else:
            print(" Telefone não encontrado na agenda.")

    elif opcao == "3":
        telefone = input("Digite o telefone do contato a excluir: ").strip()
        if telefone in agenda:
            del agenda[telefone]
            print("Contato excluído com sucesso.")
        else:
            print("Nr telefone não existente.")

    elif opcao == "4":
        if agenda:
            print("\n CONTATOS NA AGENDA:")
            for tel, nome in agenda.items():
                print(f"Nome: {nome} | Telefone: {tel}")
        else:
            print("Agenda vazia.")

    elif opcao == "5":
        print(" Saindo da agenda...")
        break

    else:
        print("Opção inválida. Tente novamente.")
