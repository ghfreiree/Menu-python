def escolha_menu():
    '''
    Função para exibir o menu de opções e capturar a escolha do usuário.
    - Exibe o menu de opções.
    - Captura a escolha do usuário.
    - Retorna a opção escolhida pelo usuário.
    '''
    
    while True:
        print('''
*-- MENU --*
-------------------------
1 - PERGUNTAS FREQUENTES
2 - QUEM SOMOS
3 - ENTRE EM CONTATO
4 - SAIR
-------------------------
''')
        escolha = int(input('Escolha uma das opções do menu: '))
        if escolha < 1 or escolha > 4:
            print('\n** Opção inválida. Tente novamente. **')
        else:
            confirma = input(f'Você certeza que deseja a opção {escolha}? (Sim ou não) : ')
            if confirma.upper() == 'SIM':
                break
    return escolha

def perguntas():
    '''
    Função para exibir as perguntas frequentes e capturar a escolha do usuário.
    - Exibe as perguntas frequentes
    - Captura a escolha do usuário
    - Retorna a opção escolhida pelo usuário
    '''
    while True:
        print('''
*-- PERGUNTAS FREQUENTES --*
---------------------------------------------------
1 - Como cadastrar no aplicativo? (Portal Paciente)
2 - Onde eu acesso meus resultados?
3 - Esqueceu a senha?
4 - Onde pego as minhas receitas?
5 - Como acessar minha teleconsulta?
---------------------------------------------------
''')
        escolha = int(input('Selecione uma opção de pergunta frequente: '))
        if escolha < 1 or escolha > 5:
            print('\n** Opção inválida, tente novamente. **')
        else:
            break
    return escolha

def imprimir_pergunta(opc_pergunta):
    '''
    Função para imprimir ao usuário a resposta da pergunta escolhida.
    - Imprime a resposta somente da pergunta escolhida pelo usuário
    - Dá a possibilidade do usuário escolher outra pergunta frequente 
    '''
    opc = opc_pergunta
    while True:
        match opc:
            case 1:
                print('''
-------------------------------------------------------------------------------------------------------------------
COMO CADASTRAR NO APLICATIVO? (PORTAL PACIENTE)

1. Acesse o aplicativo
Abra o aplicativo PortalPaciente no seu celular.

2. Realize o login
Faça o login com seu usuário e senha.

3. Clique no menu
Toque no ícone de menu(geralmente representado por três linhas horizontais).

4. Selecionar a opção "Meus Resultados"
No menu, clique no primeiro botão, localizado no canto superior à esquerda, onde está escrito "Meus Resultados".

5. Visualizar resultados
Lá, você pode clicar nas opções "Laboratório" e "Imagem" para acessar seus resultados de exames.

6. Filtrar resultados
Para filtrar os resultados, você pode selecionar uma das opções de período:
Últimos 3 meses
Últimos 6 meses
Último 12 meses
--------------------------------------------------------------------------------------------------------------------
''')
            case 2:
                print('''
-------------------------------------------------------------------------------------------------------------------
COMO CADASTRAR NO APLICATIVO? (PORTAL PACIENTE)

1. Acesse o aplicativo
Abra o aplicativo PortalPaciente no seu celular.

2. Realize o login
Faça o login com seu usuário e senha.

3. Clique no menu
Toque no ícone de menu(geralmente representado por três linhas horizontais).

4. Selecionar a opção "Meus Resultados"
No menu, clique no primeiro botão, localizado no canto superior à esquerda, onde está escrito "Meus Resultados".

5. Visualizar resultados
Lá, você pode clicar nas opções "Laboratório" e "Imagem" para acessar seus resultados de exames.

6. Filtrar resultados
Para filtrar os resultados, você pode selecionar uma das opções de período:
Últimos 3 meses
Últimos 6 meses
Último 12 meses
''')
            case 3:
                print('''
----------------------------------------------------------------------------------------------------------------
ESQUECEU A SENHA?

1. Acesse o aplicativo
Abra o aplicativo PortalPaciente no seu celular e clique em "Acessar Portal".

2. Clique em "Continuar"

3. Toque em "Esqueci minha senha"
Na tela de login, selecione a opção "Esqueci minha senha".

4. Digite seu CPF
Insira o número do seu CPF no campo indicado.

5. Informe sua data de nascimento
Digite sua data de nascimento corretamente.

6. Clique em "Localizar Paciente"
Após preencher os dados, toque no botão "Localizar Paciente" para continuar o processo de redefinição de senha.
----------------------------------------------------------------------------------------------------------------
''')
            case 4:
                print('''
----------------------------------------------------------------------------------------------
ONDE PEGO AS MINHAS RECEITAS?

1. Acesse o aplicativo
Abra o aplicativo PortalPaciente no seu celular.

2. Realize o login
Faça o login com seu usuário e senha.

3. Clique no menu
Toque no ícone de menu no canto superior esquerdo da tela.

4. Selecione "Minhas Receitas"
No menu, clique no bloco escrito "Minhas Receitas", identificado com o ícone de medicamentos.

5. Escolha entre receitas ativas e inativas
Você verá duas opções:
1- (Receitas Ativas)
2- (Receitas Inativas)
Selecione a categoria desejada para visualizar suas receitas.
----------------------------------------------------------------------------------------------
''')
            case 5:
                print('''
--------------------------------------------------------------------------------------------------------------------------------------
COMO ACESSAR MINHA TELECONSULTA

1. Acesse o aplicativo
Abra o aplicativo PortalPaciente no seu celular.

2. Realize o login
Faça o login com seu usuário e senha.

3. Clique no menu
Toque no ícone de menu no canto superior esquerdo da tela.

4. Selecione "Teleconsulta"
No menu, toque na opção "Teleconsulta".

5. Aceite os termos de uso (se for a primeira vez)
Se esta for sua primeira vez acessando, será necessário aceitar os termos de uso antes de continuar.

6. Acesse sua teleconsulta
Se houver uma teleconsulta disponível, ela aparecerá na tela.
Toque em "Acessar" para entrar na consulta.
---------------------------------------------------------------------------------------------------------------------------------------
''')
            case _:
                print('Opção inválida')
        escolha = input('Deseja ver a resposta para outra pergunta? (Sim para ver outra resposta ou não para voltar ao menu principal): ')
        if escolha.upper() == 'SIM':
            print('''
*-- PERGUNTAS FREQUENTES --*
---------------------------------------------------
1 - Como cadastrar no aplicativo? (Portal Paciente)
2 - Onde eu acesso meus resultados?
3 - Esqueceu a senha?
4 - Onde pego as minhas receitas?
5 - Como acessar minha teleconsulta?
---------------------------------------------------
''')
            opc = int(input('Selecione uma opção de pergunta frequente: '))
        else:
            break

def quem_somos():
    '''
    Função para exibir um texto descritivo sobre os desenvolvedores.
    - Dá ao usuário a escolha de voltar ao menu ou sair
    - Retorna essa escolha
    '''
    print('''
*-- QUEM SOMOS --*
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Somos Pedro Gomes 19 anos, Lucas Lopes 20 anos e Gustavo Freire 18 anos, Estudantes de Análise e desenvolvimento de sistemas na Fiap - Unidade lins. Unidos pelo interesse em tecnologia e inovação na área da saúde, estamos desenvolvendo um projeto com objetivo de reduzir a taxa de absenteismo médico de 20% para 10%.

Nosso foco é criar soluções acessíveis e funcionais que facilitem o uso da telemedicina e dos serviços de saúde digital, especialmente para pessoas que enfrentam dificuldades tecnológicas. Acreditamos que, com as ferramentas certas, é possível melhorar a experiência do paciente, otimizar o sistema de saúde e garantir mais presença nas consultas.

Nosso compromisso é com a inclusão, eficiência e impacto real.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''')
    escolha = int(input('Voltar ao menu principal ou sair? (1 para voltar ou 2 para sair): '))
    return escolha

def contato():
    '''
    Função para exibir informações de contato com a empresa e permitir ao usuário que ele envie uma mensagem.
    - Exibe as informações de contato 
    - Dá ao usuário a escolha de enviar uma mensagem
    '''
    print('''
*-- CONTATO --*
-------------------------------------------------------------------------------------------------------------------------------
Se você tiver alguma dúvida ou precisar de mais informações, não hesite em entrar em contato conosco. Estamos aqui para ajudar!
Entre em contato conosco para mais informações sobre nossos serviços de telemedicina.

Informações de contato:

- Telefone: 0800 123 4567
- Email: contato@fmusp.com.br
- Endereço: Av. Dr. Enéas Carvalho de Aguiar, 255 - Cerqueira César, São Paulo - SP
-------------------------------------------------------------------------------------------------------------------------------
''')

    escolha = input('Deseja enviar uma mensagem? (Sim ou não): ')
    return escolha

def coletar_info_contato():
    '''
    Função para coletar dados do usuário e a mensagem que ele deseja enviar.
    - Coleta os dados em uma lista
    - Exibe as informações e a mensagem do usuário
    - Possibilita ao usuário corrigir as informações fornecidas e a mensagem
    - Dá ao usuário a escolha de voltar ao menu ou sair
    - Retorna essa escolha
    '''
    while True:
        infos = []

        nome = input('\nNome*: ')
        infos.append(nome)

        email = input('E-mail*: ')
        infos.append(email)

        validar_assunto = input('Deseja adicionar um assunto? (Sim ou não): ')
        if validar_assunto.upper() == 'SIM':
            assunto = input('Assunto: ')
            infos.append(assunto)
    
        mensagem = input('Mensagem*: ')
        infos.append(mensagem)
        print('\nInformações:')
        for i in infos:
            print(i)
        
        confirma = input('\nAs informações estão corretas? (Sim ou não): ')
        if confirma.upper() == 'SIM':
            print('Mensagem enviada com sucesso!')
            escolha = int(input('\nVoltar ao menu principal ou sair? (1 para voltar ou 2 para sair): '))
            break
        else:
            print('\nPor favor, preencha as informações novamente.')
    return escolha

def executar_menu():
    """
    Função principal para executar o sistema de menu
    - Executa a opção escolhida pelo usuário.
    - Repete o processo até que o usuário decida sair.
    """
    while True:
        escolha = escolha_menu()
        if escolha == 1:
            opc_pergunta = perguntas()
            imprimir_pergunta(opc_pergunta)
        elif escolha == 2:
            quem_somos_info = quem_somos()
            if quem_somos_info != 1:
                print('Saindo...')
                break
        elif escolha == 3:
            mensagem = contato()
            if mensagem.upper() == 'SIM':
                infos = coletar_info_contato()
                if infos != 1:
                    print('Saindo...')
                    break
        elif escolha == 4:
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

executar_menu()