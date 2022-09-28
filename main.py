from itertools import count

faculdade = list()
aluno = dict()


id_gerado = count(start=1)
def get_id():
    return next(id_gerado)
    
def exibir_menu():
    print()
    print("\033[33m-\033[0m" * 30)
    print("\033[1;34m      MENU PRINCIPAL     \033[0m")
    print("\033[33m-\033[0m" * 30)
    print("\033[1;34m[ 1 ]\033[0m" + "\033[1m CADASTRAR ALUNO\033[0m")
    print("\033[1;34m[ 2 ]\033[0m" + "\033[1m LISTAR TODOS OS ALUNOS\033[0m")
    print("\033[1;34m[ 3 ]\033[0m" + "\033[1m VISUALIZAR CADASTRO DE ALUNO\033[0m")
    print("\033[1;34m[ 4 ]\033[0m" + "\033[1m EDITAR ALUNO\033[0m")
    print("\033[1;34m[ 5 ]\033[0m" + "\033[1m EXCLUIR ALUNO\033[0m")
    print("\033[1;34m[ 0 ]\033[0m" + "\033[1m FINALIZAR SESSÃO\033[0m")


def cadastrar_aluno():
    while True:
        aluno.clear()
        aluno['id'] = str(get_id())
        aluno['nome'] = input("\033[1;34mNome do aluno:  \033[0m").upper()
        aluno['curso'] = input("\033[1;34mCurso:  \033[0m")
        aluno['semestre'] = input("\033[1;34mSemestre:  \033[0m")
        faculdade.append(aluno.copy())
        print("\nID = {}, NOME = {}, CURSO = {}, SEMESTRE = {}°".format(aluno['id'], aluno['nome'], aluno['curso'],
                                                                       aluno['semestre']))
        print("\033[1mALUNO CADASTRADO COM SUCESSO!\033[0m")

        while True:
            novo_cadastro = input("\n\033[1;34mDESEJA REALIZAR MAIS UM CADASTRO? [1-SIM | 2-NÃO]\n\033[0m")
            if novo_cadastro in '12':
                break
            print("\033[1;031mPOR FAVOR, DIGITE UMA OPÇÃO VÁLIDA\n\033[0m")
        if novo_cadastro == "2":
            break
    print()


def listar_aluno():
    print("\033[1;033mLISTA DE ALUNOS CADASTRADOS:\033[0m")
    for a in faculdade:
        print("ID = {id}, NOME = {nome}, CURSO = {curso}, SEMESTRE = {semestre}°".format(**a))


def visualizar_aluno():
    encontrado = 0
    nome_aluno = input("\033[1mDIGITE O NOME DO ALUNO: \n\033[0m").upper()
    resultado = list(filter(lambda aluno: aluno['nome'] == nome_aluno, faculdade))
    for a in resultado:
        print("ID = {id}, NOME = {nome}, CURSO = {curso}, SEMESTRE = {semestre}°".format(**a))
        encontrado += 1
    if encontrado == 0:
        print("\033[0;31mCADASTRO NÃO ENCONTRADO\n\033[0m")


def editar_aluno():
    encontrado = 0
    id_aluno = input("\033[1mDIGITE O ID DO ALUNO A SER EDITADO:\n\033[0m")
    for i in range(len(faculdade)):
        if faculdade[i]['id'] == id_aluno:
            while True:
                opcao = input("\n\033[1;34mQUAL CAMPO DESEJA EDITAR? [1-NOME | 2-CURSO | 3-SEMESTRE]\033[0m""\033[0;31m\n[* PARA CANCELAR DIGITE 0]\n\033[0m")
                if opcao == "1":
                    faculdade[i]['nome'] = input("\033[1;34mNome do aluno:  \033[0m").upper()
                    print("\033[1;34mCADASTRO EDITADO COM SUCESSO!\n\033[0m")
                elif opcao == "2":
                    faculdade[i]['curso'] = input("\033[1;34mCurso:  \033[0m")
                    print("\033[1;34mCADASTRO EDITADO COM SUCESSO!\n\033[0m")
                elif opcao == "3":
                    faculdade[i]['semestre'] = input("\033[1;34mSemestre:  \033[0m")
                    print("\033[1;34mCADASTRO EDITADO COM SUCESSO!\n\033[0m")
                elif opcao == "0":
                    break
                else:
                    print("\033[0;31mOPÇÃO INVÁLIDA!\n\033[0m")
                encontrado += 1
    if encontrado == 0:
        print("\033[0;31mCADASTRO NÃO ENCONTRADO\n\033[0m")



def excluir_aluno():
    encontrado = 0
    id_aluno = input("\033[1mDIGITE O ID DO ALUNO A SER EXCLUÍDO:\n\033[0m")
    for i in range(len(faculdade)):
        if faculdade[i]['id'] == id_aluno:
            del faculdade[i]
            print("\033[1;34mCADASTRO EXCLUÍDO COM SUCESSO!\n\033[0m")
            encontrado +=1
    if encontrado == 0:
        print("\033[0;31mCADASTRO NÃO ENCONTRADO\n\033[0m")


while True:
    exibir_menu()
    opcao = input("\n\033[1mDIGITE A OPÇÃO DESEJADA:  \033[0m")

    if opcao == "1":
        print()
        cadastrar_aluno()
    elif opcao == "2":
        print()
        listar_aluno()
    elif opcao == "3":
        print()
        visualizar_aluno()
    elif opcao == "4":
        print()
        editar_aluno()
    elif opcao == "5":
        print()
        excluir_aluno()
    elif opcao == "0":
        print("\n\033[1;34mSESSÃO ENCERRADA\033[0m")
        print("\033[1;34mOBRIGADO POR USAR NOSSO SISTEMA\033[0m")
        break
    else:
        print("\033[0;31mOPÇÃO INVÁLIDA!\n\033[0m")


    
