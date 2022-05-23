opcao = 0
while opcao != 12:
    try:
        opcao = int(input("""=======-Funcionalidades do sistema-========
        1. Registrar
        2. Fazer login
        3. Editar perfil
        4. Criar currículo
        5. Analisar currículo
        6. Registrar uma empresa
        7. Criar uma vaga
        8. Procurar vaga
        9. Enviar inscrição
        10. Procurar candidato
        11. Membros do grupo (EXTRA)
        12. Sair
===========================================
Digite qual opção você quer abaixo:\n->"""))
        if opcao == 1:
            print("---" * 45 + "\nPara fazer registro, é necessário inserir um e-mail e uma senha válidos. Existem 2 tipos de "
                  "contas:\nA conta de quem for se candidatar e a conta de quem for recrutar.\nBaseado na escolha do "
                  "usuário, ele terá acesso a diferentes áreas e funcionalidades.\nUm usuário poderá ter uma conta de "
                  "candidato e outra de recrutador registrados, porém não com o mesmo e-mail.\nSerão contas "
                  "independentes uma da outra.\nCada conta gera um Id único, com o primeiro dígito sendo 1 para uma "
                  "conta de candidato e 2 para de recrutador.\n" + "---" * 45)
        elif opcao == 2:
            print("---" * 45 + "\nPara fazer login é necessário ter um registro e utilizar o e-mail e a senha cadastrados para "
                  "efetuar o login.\nCaso os dados inseridos estejam errados ou não tenham sido registrados, "
                  "será dado um aviso.\n" + "---" * 45)
        elif opcao == 3:
            print("---" * 45 + "\nA edição do perfil consiste em alterar nome, telefone e/ou endereço (rua, numero, cidade, estado, "
                  "CEP,\ncomplemento). Esses dados iniciam sendo vazios podendo ser preenchidos e voltados a vazios "
                  "se assim o usuário definir.\nÉ necessário ter uma conta e estar logado para editar o perfil.\n" +
                  "---" * 45)
        elif opcao == 4:
            print("---" * 45 + "\nÉ necessário ter uma conta de candidato para criar um curriculo. Dentro desse currículo serão "
                  "preenchidos\nhabilidades, competências, objetivo, resumo, listar experiências, formações e "
                  "idiomas.\nExperiencias e idiomas tem função/cargo, local, data de inicio e termino, estado atual,"
                  "\ninstituição/organizaçao/nome do projeto (depende se é formação ou experiência) etc.\n" + "---" * 45)
        elif opcao == 5:
            print("---" * 45 + "\nÉ necessário ter uma conta de candidato e o currículo cadastrado para ter uma análise.\nA análise "
                  "retorna valores baseado no quanto o currículo está preenchido, explicando o porque um campo é\n"
                  "necessário, mesmo que seja com algo simples (ex. preencher suas habilidades ajuda o recrutador a\n"
                  "saber se você possui o que é necessário para fazer as tarefas que ele precisa\n" + "---" * 45)
        elif opcao == 6:
            print("---" * 45 + "\nÉ necessário ter uma conta de recrutador para registrar uma empresa. Devem ser preenchidos nome, "
                  "cnpj ou\nqualquer outra identificação legal, o endereco da empresa (rua, numero, cidade, "
                  "etc)\nbem como um telefone para contato que se não for preenchido, poderá ser usado o do "
                  "recrutador caso haja necessidade.\n" + "---" * 45)
        elif opcao == 7:
            print("---" * 45 + "\nPara criar uma vaga é necessário ter uma conta de recrutador e uma empresa cadastrada. Devem ser "
                  "preenchidos\num título, o tipo de contrato, uma descrição, o salário, os beneficios oferecidos,"
                  "\na quantidade de vagas oferecidas assim como os requisitos (habilidades, competências,"
                  "\nexperiencia, grau de escolaridade junto da formação).\n" + "---" * 45)
        elif opcao == 8:
            print("---" * 45 + "\nSomente uma conta de candidato pode procurar uma vaga. O usuário pode procurar uma vaga pelo\n"
                  "título bem como localidade, intensificando o filtro se achar necessário (habilidades, "
                  "grau de ensino, etc).\n" + "---" * 45)
        elif opcao == 9:
            print("---" * 45 + "\nÉ necessário ter uma conta de candidato para se inscrever numa vaga. A inscrição envia "
                  "o\ncurrículo do candidato bem como seu nome e contato para a conta do recrutador.\n" + "---" * 45)
        elif opcao == 10:
            print("---" * 45 + "\nÉ necessário ter uma conta de recrutador para procurar por candidatos diretamente.\nPode-se "
                  "procurar adicionando filtros de características que contém num currículo.\n" + "---" * 45)
        elif opcao == 11:
            print("---" * 45 + "\nAdilson Roberto Cavicchioli Junior (94548)\n"
                  "William Barrence Santos Junior (93586)\n"
                  "Albert Oliveira Ribeiro (94807)\n"
                  "Vinicius Prado Mendes (94851)\n"
                  "Matheus Gomes da Silva (95572)\n" + "---" * 45)
        elif opcao == 12:
            print("Você saiu.")
        else:
            print("Opção inválida. Digite uma opção dentre:")
    except ValueError:
        print("Por favor, insira um número entre as opções abaixo:")