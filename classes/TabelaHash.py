from excessoes.JaExisteAlunoException import JaExisteAlunoException
from classes.Aluno import Aluno


class TabelaHash:
    def __init__(self):
        self.__tabela_hash = {}
        self.__matriculas = []

    def listar(self):
        if not self.__tabela_hash:
            print("\nTabela Hash vazia!\n")
        else:
            print("\n==== Lista de Alunos ====")
            for chave, valor in self.__tabela_hash.items():
                if isinstance(valor, list):
                    for i in range(0, len(valor)):
                        print("HashCode: %d" % chave)
                        print("Matrícula: %d" % valor[i].matricula)
                        print("Nome: %s" % valor[i].nome)
                        print("Idade %d" % valor[i].idade)
                        print("==============")
                else:
                    print("HashCode: %d" % chave)
                    print("Matrícula: %d" % valor.matricula)
                    print("Nome: %s" % valor.nome)
                    print("Idade: %d" % valor.idade)
                    print("==============")

    def buscar_aluno(self, matricula):
        hash = self.__calcula_hash(matricula)
        if not hash in self.__tabela_hash.keys():
            print("\nAluno de matrícula: %d não está cadastrado!\n" % matricula)
            return False
        else:
            if not isinstance(self.__tabela_hash[hash], list):
                return self.__tabela_hash[hash]
            else:
                for aluno in self.__tabela_hash[hash]:
                    if aluno.matricula == matricula:
                        print("====== Aluno encontrado: ========")
                        print("Matrícula: %d" % aluno.matricula)
                        print("Nome: %s" % aluno.nome)
                        print("Idade: %d" % aluno.idade)
                        print("==============")
                        return aluno

    def remove_aluno(self, matricula):
        hash = self.__calcula_hash(matricula)
        aluno = self.buscar_aluno(matricula)
        try:
            op = int(input("Tem certeza que deseja remover o aluno encontrado? (1 - Sim / 2 - Não)?\n"))
        except ValueError:
            print("Digete valores válidos")
        else:
            if op == 1:
                del self.__tabela_hash[hash]
                self.__matriculas.remove(matricula)
                print("\nAluno removido com sucesso!\n")
            if op == 2:
                print("Aluno não removido.")
            

    def cadastra_aluno(self):
        try:
            aluno = Aluno()
            aluno.matricula = int(input("Insira a matrícula: "))
            if aluno.matricula in self.__matriculas:
                raise JaExisteAlunoException
            aluno.nome = input("Digite o nome do aluno: ")
            aluno.idade = int(input("Digite a idade do aluno: "))
        except ValueError:
            print("Matricula e idade devem ser valores inteiros! Digite Valores válidos!")
        except JaExisteAlunoException:
            print("\nJá existe um aluno com a matrícula escolhida!\n")
        else:
            self.__matriculas.append(aluno.matricula)
            self.__adiciona_aluno_tabela(aluno)

    def __adiciona_aluno_tabela (self, aluno):
        hash = self.__calcula_hash(aluno.matricula)

        if hash not in self.__tabela_hash.keys():
            self.__tabela_hash[hash] = aluno
        else:
            if not isinstance(self.__tabela_hash[hash], list):
                lista = []
                lista.append(self.__tabela_hash[hash])
                lista.append(aluno)
                self.__tabela_hash[hash] = lista
            else:
                lista = []
                for i in self.__tabela_hash[hash]:
                    lista.append(i)
                lista.append(aluno)
                self.__tabela_hash[hash] = lista
        print("\nAluno inserido com sucesso! \n")

    def __calcula_hash(self, matricula):
        return matricula%11


