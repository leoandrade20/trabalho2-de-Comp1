#NOME: LEONARDO ANDRADE
#DATA: 07/06/2019
#TURMA: EL2 | 10H~12H   #PROFESSOR: PEDRO

#DESCRIÇÃO: TRABALHO 2 DO CURSO DE COMPUTAÇÃO I - BANCO DE DADOS PARA A COPA DO MUNDO, ARMAZENA AS INFORMAÇÕES DE CADA JOGADOR EM UM ARQUIVO TEXTO DO PAÍS DE SUA SELEÇÃO.

#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - menu()

def menu():

    print()
    print('[1] Criar uma seleção.')
    print('[2] Acrescentar um jogador a uma seleção já existente.')
    print('[3] Deletar um jogador de uma seleção já existente.')
    print('[4] Atualizar o número de gols de um determinado jogador.')
    print('[5] Consultar dados por seleção,idade, artilharia entre outros.')
    
    print()
    print('[0] Sair.')
    print()

#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - menu2()

def menu2():

    print()
    print('***********************CONSULTA**************************')
    print()

    print('Escolha uma opção abaixo para consultar os dados a partir dessa opção.')
    print()

    print('[A]Seleção (Exibe a lista de jogadores de uma seleção, junto com a idade,clube atual,posição e gols na Copa do Mundo.')
    print('[B]Idade (Exibe todos os jogadores abaixo da idade solicitada).')
    print('[C]Clube (Exibe todos os jogadores que jogam no clube solicitado, juntamente com seus respectivos países.)')
    print('[D]Artilharia (Exibe os artilheiros desta edição da Copa do Mundo).')
    print()
    
    print('[S] Sair.')
    print()

#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - abre_e_cria()

def abre_e_cria(nome):      #Abre o arquivo a partir do nome, caso ele não exista, um arquivo com o nome é criado.

    try:
    
        arquivo = open(nome + '.txt','r+')

        return arquivo

    except FileNotFoundError: 
    
        arquivo = open(nome + '.txt','w')    
        
        arquivo.close()

#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - fecha()       #Fecha qualquer arquivo

def fecha(arquivo):
    
    arquivo.close()

#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - preenche1()   #Dado um jogador e seus dados, acrescenta-se seus dados a um dicionario, e este dicionario a uma lista.

def preenche1():

    print()
    print('Digite o nome do jogador juntamente com seus dados para inseri-lo na seleção.')
    print()

    selecao = []

    jogador = {'Nome':' ','Idade':-1,'Time atual':' ','Posição':' ','Gols':-1}      #Dicionario vazio.
    
    num = len(selecao)
    cont = 1

    while (num <= 22) and (cont == 1):
        
        jogador = {'Nome':' ','Idade':-1,'Time atual':' ','Posição':' ','Gols':-1}

        nome = input('Nome do jogador: ')
        idade = int(input('Idade: '))
        time = input('Time que atua: ')
        posicao = input('Posição: ')
        gols = int(input('Gols na Copa do Mundo: '))
        
        jogador['Nome'] = nome
        jogador['Idade'] = idade
        jogador['Time atual'] = time                    #Preenchimento das lacunas do dicionario.
        jogador['Posição'] = posicao 
        jogador['Gols'] = gols
        

        print('Deseja acrescentar mais um jogador?')
        print()

        print('[S]Sim.')
        print('[N]Não.')
        print()
        
        selecao += [jogador]                        #Acréscimo do dicionario a lista de jogadores

        escolha = input('Escolha: ')
        
        if (escolha == 'S') or (escolha == 's'):

            cont = 1
        
        elif (escolha == 'N') or (escolha == 'n'):

            cont = 0
    
    return selecao                              #Retorna-se a lista de jogadores, onde cada um é um dicionario.

#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - transform()               #Transforma um arquivo de uma seleção numa lista de dicionarios, onde cada dicionario é um jogador.

def transform(arquivo):

    linhas = arquivo.readlines()

    selecao =[]

    for elem in range(len(linhas)):

        dados = []
        info = ''
        cont = 0

        for char in (linhas[elem]):

            if (char != ';') and (cont < 4):            #Junta os caracteres para formar uma informação.

                info += char

            elif (char == ';'):                     #Quando um caractere for igual a ";", fecha a informaçao e atribui a lista de dados.

                dados += [info]
                info = ''
                cont += 1
            
            elif (cont == 4) and (char != '\n'):    #Atua na parte dos gols, concatenando as strings da posição da lista.

                info += char
                
            elif(cont == 4) and (char == '\n'):     #Atribui o novo info (nesse caso os gols) para a lista de dados.

                dados += [info]
                info = ''

        selecao += [dados]

    dicio_selecao = []                      #Valor inicial da lista, que será preenchida por dicionarios

    for jogadores in range (len(selecao)):

        jogador = {'Nome':' ','Idade':-1,'Time atual':' ','Posição':' ','Gols':-1}
        
        jogador['Nome'] = selecao[jogadores][0]
        jogador['Idade'] = int(selecao[jogadores][1])
        jogador['Time atual'] = selecao[jogadores][2]
        jogador['Posição'] = selecao[jogadores][3]
        jogador['Gols'] = int(selecao[jogadores][4])
        
        dicio_selecao += [jogador]      #Cada jogador, agora transformado num dicionario, é adicionado na lista

    return dicio_selecao                

#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - preenche2()               #Dadas as informarções pelo o usuario, a função transforma no modelo .txt para o arquivo

def preenche2(arquivo,selecao):     #Parâmetros arquivo e selecao (lista de dicionarios com as info dos jogadores).    

    arquivo.seek(0,2)               #Torna o fim do arquivo como referência.

    for cont in range(len(selecao)):

        if (selecao[cont] != ''):

            for dados in (selecao[cont]):
            
                if (dados == 'Gols'):

                    arquivo.write(str(selecao[cont][dados]) + '\n')

                else:

                    arquivo.write(str(selecao[cont][dados]) + ';')

    return arquivo

#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - delet_1()             #Apaga o jogador requisitado pelo usuario
    
def delet_1(selecao):           #Tem como parametro o dicionario retornado

    print()

    print('Digite o nome do jogador:')
    nome = input()

    achei = False
    cont = 0
    resultado = -1

    while (not achei) and (cont < len(selecao)):    #Procura o jogador pelo nome até o limite da quantidade de jogadores

        if (selecao[cont]['Nome'] == nome):

            achei = True
            result = cont
        
        else:

            cont += 1

    if (achei == True):

        selecao[result] =''
    

    return selecao

#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - abre_eZera()     #Abre o arquivo de onde se deseja deletar o jogador, possibilitando alteração total do arquivo.

def abre_eZera(nome):

    arquivo = open(nome + '.txt','w')

    return arquivo

#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - att_Gols()            #Atualiza os gols de um jogador, a partir do seu nome.

def att_Gols(selecao):          #Recebe uma lista de dicionarios

    print()

    print('Digite o nome do jogador: ')
    nome_do_Jogador = input()

    qtde_Jogadores = len(selecao)
    cont = 0
    
    print()

    att_Gols = int(input('Digite a quantidade de gols atualizada: '))
    
    achei = False

    while (not achei) and (cont < qtde_Jogadores):  

        if (selecao[cont]['Nome'] == nome_do_Jogador):      #Quando o nome dado é igual ao nome do dicionario.

            selecao[cont]['Gols'] = att_Gols                #Atualização do numero de gols

            achei = True
        
        else:

            cont += 1
            achei = False

    return selecao                              #Retorna a lista de dicionarios, atualizada
    
#------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÃO - exibe()

def exibe(selecao):                 #Exibe a lista de dicionarios em forma de tabela.

    qtde_Jogadores = len(selecao)
    
    qtde_letrasNome = []
    maior_nome = 0

    for jogador in range (qtde_Jogadores):           
        
        qtde_letrasNome += [len(selecao[jogador]['Nome'])]             #Quantidades de letras dos nomes sao armazenados numa lista

    for verificador_nome in (qtde_letrasNome):

        if (verificador_nome > maior_nome):                         #Verifica-se o maior nome

            maior_nome = verificador_nome

    qtde_letrasTime = []
    maior_Time = 0

    for jogador in range (qtde_Jogadores):                              

        qtde_letrasTime += [len(selecao[jogador]['Time atual'])]    #O tamanho de cada time é armazenado numa lista

    for verificador_time in (qtde_letrasTime):

        if (verificador_time > maior_Time):             #Verifica-se o maior nome

            maior_Time = verificador_time

    maior_posicao = len('meio-campo')                   #A posição com maior quantidade de letras é 'meio-campo', que é fixo.
    
    print()
    print('*********************************DADOS DA SELEÇÃO*************************************')
    print()

    print('NOME',end = ' '*(maior_nome))
    print('IDADE',end = ' '*(maior_nome))               #O espaçamento dos índices se dá pelos maiores valores dos dados
    print('CLUBE',end = ' '*(maior_Time))
    print('POSIÇÃO',end = ' '*(maior_posicao))
    print('GOLS' + '\n')

    qtde_Jogadores = len(selecao) 

    for linhas in range (qtde_Jogadores):           
        
        for dados in (selecao[linhas]):             

            if (dados == 'Gols'):

                print(selecao[linhas][dados],'\n')

            elif (dados == 'Nome'):

                print(selecao[linhas][dados],end= ' '*(maior_nome - (len(selecao[linhas][dados])) + 6))     #Alinhamento de todos os clubes
        
            elif (dados == 'Idade'):

                print(selecao[linhas][dados],end= ' '*(maior_nome))     #As idades sempre terão apenas 2 digitos.

            elif (dados == 'Time atual'):

                print(selecao[linhas][dados],end= ' '*(maior_Time - (len(selecao[linhas][dados])) + 6))     #Alinhamento de todas as posições
        
            elif (dados == 'Posição'):

                print(selecao[linhas][dados],end= ' '*(maior_posicao - (len(selecao[linhas][dados])) + 9)) #Alinhamento dos gols
                

#______________________________________________PROGRAMA PRINCIPAL________________________________________________#

#FUNÇÃO - main()        #Função que contém todas as outras funções.

def main():
    
    print()
    print('-------------------------------BANCO DE DADOS DA COPA DO MUNDO--------------------------------')
    print()

    print('Bem vindo! O que deseja realizar?')
    
    menu()

    opc = int(input('Digite a opção escolhida: '))
    
    while (opc != 0):

        if (opc <= 5) and (opc > 0):

            if (opc == 1):                      #Cria uma nova seleção

                print()

                print('*******************NOVA SELEÇÃO******************')
                print()

                print('Digite o país da seleção:')
                nome = input()
                
                abre_e_cria(nome)                     #Não retorna nada, apenas cria um novo arquivo

                print()

                print('Sua nova seleção foi criada! Deseja continuar?')
                print()
                
                print('*****************************MENU PRINCIPAL************************************')
                menu()

                opc = int(input('Digite a opção que deseja realizar:  '))
                print()
        
            elif (opc == 2):                            #Adiciona jogadores

                print()

                print('*******************ACRESCENTAR JOGADORES******************')
                
                print()

                print('Digite o país da seleção:')
                nome = input()

                aberto = abre_e_cria(nome)          #Retorna o arquivo aberto e armazena na variavel "aberto"
                lista= preenche1()                  #Retorna a lista de jogadores e armazena na variavel "lista"
                preenche2(aberto,lista)             #Retorna o arquivo preenchido com a lista de jogadores
                fecha(aberto)                       #Fecha o arquivo aberto
                
                print()
                
                print('*****************************MENU PRINCIPAL************************************')
                menu()

                opc = int(input('Digite a opção que deseja realizar: '))
                print()

            elif (opc == 3):

                print()

                print('**********************APAGAR JOGADORES**********************')

                print()

                print('Digite o país da seleção:')
                nome = input()

                aberto = abre_e_cria(nome)
                new = transform(aberto)
                editado = delet_1(new)
                aberto2 = abre_eZera(nome)
                preenche2(aberto2,editado)
                fecha(aberto)
                fecha(aberto2)

                print()

                print('*****************************MENU PRINCIPAL************************************')
                menu()
                
                opc = int(input('Digite a opção que deseja realizar: '))
                print() 
            
            elif (opc == 4):

                print()
                print('********************ATUALIZAR GOLS***********************')
                print()

                print('Digite a seleção do jogador:')
                nome = input()

                print()

                aberto = abre_e_cria(nome)
                new = transform(aberto)
                editado = att_Gols(new)
                aberto2 = abre_eZera(nome)
                preenche2(aberto2,editado)
                fecha(aberto)
                fecha(aberto2)

                print()

                print('*****************************MENU PRINCIPAL************************************')
                menu()
                
                opc = int(input('Digite a opção que deseja realizar: '))
                print()
                
            elif (opc == 5):
                
                menu2()
                opc2 = input('Digite a opção escolhida: ')
                
                while (opc2 != 's') and (opc2 != 'S'):

                    while (opc2 == 'A') or (opc2 == 'a'):
                        
                        print()
                        print('Digite o nome do arquivo onde está a seleção.')
                        selecao = input()

                        aberto = abre_e_cria(selecao)
                        lista = transform(aberto)
                        exibe(lista)
                        fecha(aberto)
                    
                        print()
                            
                        menu2()

                        opc2 = input('Digite a opção que deseja realizar: ')
                        
                print('***************************************************')
                menu()

                opc = int(input('Digite a opção que deseja realizar: '))
                print()
                

                        
                

        else:
            
            opc = int(input('Opção inválida! Digite novamente: '))


    print()

    print('Obrigado por utilizar nosso banco de dados !')
#______________________________________________FIM DO PROGRAMA DO PRINCIPAL___________________________________________#

main()  #Chamada da função principal.
