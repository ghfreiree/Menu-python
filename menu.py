def escolha_menu():
    '''
    Função para exibir o menu de opções e capturar a escolha do usuário.
    - Exibe o menu de opções.
    - Captura a escolha do usuário.
    - Retorna a opção do menu escolhida pelo usuário.
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

        # Verifica se a escolha está dentro do intervalo válido
        if escolha < 1 or escolha > 4:
            print('\n** Opção inválida. Tente novamente. **')

        # Confirmação da escolha
        else:
            confirm = input(f'Você certeza que deseja a opção {escolha}? (Sim ou não) : ')
            if confirm.upper() == 'SIM':
                break
    return escolha

def perguntas_frequentes():
    '''
    Função para exibir as perguntas frequentes e capturar a escolha do usuário.
    - Exibe as perguntas frequentes
    - Captura a escolha de pergunta do usuário
    - Retorna o número da pergunta escolhida
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

        # Verifica se a escolha está dentro do intervalo válido
        if escolha < 1 or escolha > 5:
            print('\n** Opção inválida, tente novamente. **')
        else:
            break
    return escolha

def imprimir_resposta(opc_pergunta):
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
1 - COMO CADASTRAR NO APLICATIVO? (PORTAL PACIENTE)

1. Acesse o aplicativo
Toque no ícone do aplicativo PortalPaciente no seu celular.
Em seguida, toque no botão "Acessar Portal".

2. Começar o cadastro da senha
Agora, toque em "Cadastrar Senha".
Vai aparecer um campo para digitar o seu CPF.
Digite seu CPF com atenção e toque no botão "Localizar Paciente".

3. Verificar se você é o paciente certo
Se aparecer outro nome que não é o seu, toque em "Alterar Paciente" para voltar e digitar o CPF correto.
Se estiver tudo certo, continue para o próximo passo.

4. Preencher seus dados de contato
Digite o seu e-mail.
Depois, digite o mesmo e-mail novamente para confirmar.
Digite o seu celular com o DDD (exemplo: 11 91234-5678).
Confirme o número do celular no campo seguinte.
Atenção: Esses dados são importantes para você receber informações de agendamentos ou recuperar sua senha, caso esqueça.

5. Confirmar informações pessoais
Escolha a opção correta com o nome completo da sua mãe.
Depois, selecione o ano correto do seu nascimento.

6. Criar uma senha
Crie uma senha de acesso (algo que você vai lembrar).
Digite a mesma senha de novo no campo de confirmação.

7. Finalizar o cadastro
Toque no botão "Cadastrar Senha".
Se tudo estiver certo, vai aparecer uma nova tela.

--------------------------------------------------------------------------------------------------------------------
''')
            case 2:
                print('''
-------------------------------------------------------------------------------------------------------------------
2 - ONDE ACESSO MEUS RESULTADOS?

1. AcessE o aplicativo
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
3 - ESQUECEU A SENHA?

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
4 - ONDE PEGO AS MINHAS RECEITAS?

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
5 - COMO ACESSAR MINHA TELECONSULTA?

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
                print('\n** Opção inválida. Tente novamente. **')

        maisPerguntas = input('Deseja ver a resposta para outra pergunta? (Sim para ver outra resposta ou não para voltar ao menu principal): ')

        # Verifica se o usuário deseja ver outra pergunta
        if maisPerguntas.upper() == 'SIM':
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
        elif maisPerguntas.upper() == 'NÃO' or maisPerguntas.upper() == 'NAO':
            break
        else:
            print('\n** Opção inválida. Tente novamente. **')
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
    escolha = input('Deseja voltar ao menu principal? ("Sim" para voltar ou "não" para sair): ')
    return escolha

def contato():
    '''
    Função para exibir informações de contato com a empresa e permitir ao usuário que ele envie uma mensagem.
    - Exibe as informações de contato 
    - Dá ao usuário a escolha de enviar uma mensagem
    - Retorna essa escolha
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

def coletar_info_usuario():
    '''
    Função para coletar informações do usuário e a mensagem que ele deseja enviar.
    - Coleta os dados em uma lista
    - Exibe as informações e a mensagem do usuário
    - Possibilita ao usuário corrigir as informações fornecidas e a mensagem
    - Dá ao usuário a escolha de voltar ao menu ou sair
    - Retorna essa escolha
    '''
    while True:
        infos = []

        # Coleta as informações do usuário
        nome = input('\nNome*: ')
        infos.append(nome)

        email = input('E-mail*: ')
        infos.append(email)

        # Pergunta se o usuário deseja adicionar um assunto
        # Caso queira, coleta o assunto
        while True:
            validar_assunto = input('Deseja adicionar um assunto? (Sim ou não): ')
            if validar_assunto.upper() == 'SIM':
                assunto = input('Assunto: ')
                infos.append(assunto)
                break
            elif validar_assunto.upper() == 'NÃO' or validar_assunto.upper() == 'NAO':
                infos.append('*Sem assunto*')
                break
            else:
                print('Resposta inválida')

        # Coleta a mensagem do usuário
        mensagem = input('Mensagem*: ')
        infos.append(mensagem)
        print('\nInformações:')

        # Exibe as informações coletadas
        for i in infos:
            print(i)
        
        # Pergunta se as informações estão corretas
        while True:
            correto = input('\nAs informações estão corretas? (Sim ou não): ')
            if correto.upper() == 'SIM':
                print('Mensagem enviada com sucesso!')
                break
            elif correto.upper() == 'NÃO':
                print('\nPor favor, preencha as informações novamente.')
                break
            else:
                print('Resposta inválida\n')
        
        # Pergunta se o usuário deseja voltar ao menu ou sair
        while True:
            voltarMenu = input('\nDeseja voltar ao menu principal? ("Sim" para voltar ou "não" para sair): ')
            if voltarMenu.upper() == 'SIM':
                break
            elif voltarMenu.upper() == 'NÃO':
                break
            else:
                print('Resposta inválida\n')
        if voltarMenu.upper() == 'SIM' or voltarMenu.upper() == 'NÃO':
                break
    return voltarMenu

def executar_menu():
    """
    Função principal para executar o sistema de menu
    - Executa a opção escolhida pelo usuário.
    - Repete o processo até que o usuário decida sair.
    """
    while True:
        escolha = escolha_menu()
        
        # Executa a opção escolhida pelo usuário
        match escolha:
            case 1:
                pergunta = perguntas_frequentes()
                imprimir_resposta(pergunta)
            case 2:
                voltarMenu = quem_somos()
                if voltarMenu.upper() == 'NÃO' or voltarMenu.upper() == 'NAO':
                    print('\nSaindo...')
                    break
                elif voltarMenu.upper() != 'NÃO' and voltarMenu.upper() != 'SIM' and voltarMenu.upper() != 'NAO':
                    print('\n** Opção inválida. Tente novamente. **')
            case 3:
                decisao_mensagem = contato()
                if decisao_mensagem.upper() == 'SIM':
                    voltarMenu = coletar_info_usuario()
                    if voltarMenu.upper() == 'NÃO' or voltarMenu.upper() == 'NAO':
                        print('\nSaindo...')
                        break
                elif decisao_mensagem.upper() != 'SIM' and decisao_mensagem.upper() != 'NÃO' and decisao_mensagem.upper() != 'NAO':
                    print('\n** Opção inválida. Tente novamente. **')
            case 4:
                print('\nSaindo...')
                break
            case _:
                print('\n** Opção inválida. Tente novamente. **')

executar_menu()