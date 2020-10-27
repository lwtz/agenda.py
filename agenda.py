# var global
AGENDA = {}


def save():
    exportAgenda('database.csv')


def load():
    try:
        with open('database.csv', 'r') as arquivo:
            linha = arquivo.readlines()
            for linhas in linha:
                detalhes = linhas.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                idade = detalhes[3]
                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'idade': idade,
                }
    except KeyError:
        print('Contato Inexistente')
    except Exception as erro:
        print(erro)


def searchContac(nome):
    try:
        print('Nome:', nome)
        print('Telefone: ', AGENDA[nome]['telefone'])
        print('Email: ', AGENDA[nome]['email'])
        print('Idade: ', AGENDA[nome]['idade'])
    except KeyError:
        print('Contato Inexistente')
    except Exception as erro:
        print('Aconteceu um erro.')


def printContact():
    if AGENDA:  # se tiver algo dentro ele retorna True
        for contato in AGENDA:
            print('Nome:', contato)
            print('Telefone: ', AGENDA[contato]['telefone'])
            print('Email: ', AGENDA[contato]['email'])
            print('Idade: ', AGENDA[contato]['idade'])
            print("\n")
    else:
        print('Agenda vazia')


def adicionar_editar_contatos(nome, tel, mail, idade):
    AGENDA[nome] = {
        'telefone': tel,
        'email': mail,
        'idade': idade,
    }
    save()
    print("{} add com sucesso \n".format(nome))


def detalhesContato():
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    idade = input('Digite a idade: ')
    return telefone, email, idade


def deletarContact(nome):
    try:
        AGENDA.pop(nome)
        save()
        print("Contato: {} excluido \n".format(nome))
    except KeyError:
        print('Contato Inexistente')
    except Exception as erro:
        print('Aconteceu um erro.')


def exportAgenda(fileName):
    try:
        with open(fileName, 'w') as file:
            for linha in AGENDA:
                telefone = AGENDA[linha]['telefone']
                email = AGENDA[linha]['email']
                idade = AGENDA[linha]['idade']
                file.write('{nm},{tel},{mail},{id} \n'.format(nm=linha,
                                                              tel=telefone,
                                                              mail=email,
                                                              id=idade))
        print('Agenda salva')
    except Exception as erro:
        print('Ocorreu algum erro. {}'.format(erro))


def importAgenda(fileName):
    try:
        with open(fileName, 'r') as arquivo:
            linha = arquivo.readlines()
            for linhas in linha:
                detalhes = linhas.strip().split(',')
                print(detalhes)
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                idade = detalhes[3]
                adicionar_editar_contatos(nome, telefone, email, idade)

    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as erro:
        print('Ocorreu algum erro. {}'.format(erro))


def imprimirMenu():
    print('-' * 15)
    print('1 - Mostrar contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('8 - Importar agenda')
    print('9 - Exportar agenda')
    print('0 - Fechar agenda')
    print('-' * 15)


load()

while True:
    imprimirMenu()
    escolha = input('Escolha um opção: ')
    if escolha == '1':
        printContact()
    elif escolha == '2':
        nomeMenu = input('Nome do contato para buscar:')
        searchContac(nomeMenu)
    elif escolha == '3':
        addMenu = input('Nome do contato para adicionar:')
        try:
            AGENDA[addMenu]
            print('Contato já existente')
            continue
        except KeyError:
            telefone, email, idade = detalhesContato()
            adicionar_editar_contatos(addMenu, telefone, email, idade)
    elif escolha == '4':
        addMenu = input('Nome do contato para editar:')
        try:
            AGENDA[addMenu]
            print('Editando contato: ', addMenu)
            telefone, email, idade = detalhesContato()
            adicionar_editar_contatos(addMenu, telefone, email, idade)
        except KeyError:
            print('Contato inexistente')
    elif escolha == '5':
        delMenu = input('Nome do contato para deletar:')
        deletarContact(delMenu)
    elif escolha == '8':
        nomeArq = input('Nome do arquivo: ')
        importAgenda(nomeArq)
    elif escolha == '9':
        nomeArq = input('Nome do arquivo: ')
        exportAgenda(nomeArq)
    elif escolha == '0':
        print('Saindo')
        exit()
    else:
        print('Opção Inválida')
