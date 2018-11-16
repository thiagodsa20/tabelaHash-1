from classes.TabelaHash import TabelaHash

th = TabelaHash()

# th.listar()

op = 0
while op != 5:
    menu = '''
     === Tabela Hash ===
    1 - Inserir um aluno
    2 - Buscar Alunos
    3 - Remover Aluno
    4 - Exibir tabela Hash
    5 - Sair
    '''
    print(menu)
    op = int(input("Digite o número correspondente a opração desejada: "))
    if op == 1:
        th.cadastra_aluno()
    elif op == 2:
        try:
            matricula = int(input("Digite a matrícula do aluno que deseja buscar: "))
        except ValueError:
            print("Digite apenas valores inteiros!")
        else:
            th.buscar_aluno(matricula)
    elif op == 3:
        try:
            matricula = int(input("Digite a matrícula do aluno que deseja remover: "))
        except ValueError:
            print("Digite apenas valores inteiros!")
        else:
            th.remove_aluno(matricula)
    elif op == 4:
        th.listar()
    elif op == 5:
        print("Tchau!")
    else:
        print("Opção inválida!\n")


