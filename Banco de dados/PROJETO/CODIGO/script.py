import mysql.connector

# Configurações de Conexão
config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'nota_fiscal',
    'raise_on_warnings': True
}

# Estabelecer Conexão
try:
    conexao = mysql.connector.connect(**config)
    if conexao.is_connected():
        print('Conexão ao MySQL bem-sucedida!')
        cursor = conexao.cursor()

        # INSERINDO REGISTROS NA TABELA CLIENTES 
        sql_inserir_dados_clientes = '''
            INSERT INTO nota_fiscal.clientes 
            (id, nome_completo, razao_social, cpf, cnpj, data_nascimento, email, telefone, cep, logradouro, numero, complemento, bairro, municipio, uf)
            VALUES
            (1, 'João Silva', NULL, '12345678901', NULL, '1990-05-15', 'joao.silva@email.com', '1234567890', '12345678', 'Rua Principal', '123', 'Apto 101', 'Centro', 'Cidade A', 'SP'),
            (2, NULL, 'Oliveira ME', NULL, '98765432000112', '1985-08-22', 'maria.oliveira@email.com', '9876543210', '87654321', 'Avenida Secundária', '456', 'CASA E DECORAÇÃO 202', 'Bairro Norte', 'Cidade B', 'RJ'),
            (3, NULL, 'Pereira & Cia', NULL, '12345678901234', '1978-03-10', 'carlos.pereira@email.com', '1122134455', '54321098', 'Travessa da Esquina', '789', 'Sala 303', 'Bairro Sul', 'Cidade C', 'MG'),
            (4, 'Ana Souza', NULL, '45678901234', NULL, '1982-11-28', 'ana.souza@email.com', '987654321', '54321098', 'Rua das Flores', '789', 'Bloco 2, Ap 405', 'Jardim Primavera', 'Cidade D', 'SP'),
            (5, 'José Oliveira', NULL, '78901234567', NULL, '1975-07-14', 'jose.oliveira@email.com', '1122334155', '12345678', 'Avenida Principal', '4567', 'CASA E DECORAÇÃO 102', 'Centro', 'Cidade E', 'RJ'),
            (6, NULL, 'Santos Construções', NULL, '98765432000134', '1990-02-20', 'mariana.santos@email.com', '9980776655', '87654321', 'Rua do Comércio', '321', 'Sala 201', 'Bairro Comercial', 'Cidade F', 'MG'),
            (7, NULL, 'Lima & Associados', NULL, '12345678900234', '1988-09-03', 'fernanda.lima@email.com', '1122334451', '12345678', 'Rua das Árvores', '987', 'Apto 301', 'Jardim das Flores', 'Cidade G', 'SP'),
            (8, 'Gabriel Costa', NULL, '34567890122', NULL, '1973-12-18', 'gabriel.costa@email.com', '9988776605', '87654321', 'Avenida Central', '654', 'CASA E DECORAÇÃO 405', 'Centro', 'Cidade H', 'RJ'),
            (9, 'Isabela Rocha', NULL, '56789012345', NULL, '1995-04-25', 'isabela.rocha@email.com', '1122334425', '54321098', 'Travessa dos Campos', '543', 'Sala 102', 'Bairro Novo', 'Cidade I', 'MG'),
            (10, NULL, 'Almeida Construções', NULL, '87654321012345', '1980-07-31', 'lucas.almeida@email.com', '9988776611', '87654321', 'Rua das Montanhas', '876', 'CASA E DECORAÇÃO 203', 'Bairro Residencial', 'Cidade J', 'SP'),
            (11, 'Patrícia Nunes', NULL, '98765430921', NULL, '1989-11-14', 'patricia.nunes@email.com', '1122334450', '12345678', 'Avenida dos Lagos', '1234', 'Apto 504', 'Lagoa Azul', 'Cidade K', 'RJ'),
            (12, NULL, 'Santos & Filhos', '1098765444', NULL, '1972-06-08', 'rafaela.santos@email.com', '9988006235', '54321098', 'Travessa das Pedras', '876', 'CASA E DECORAÇÃO 102', 'Bairro Pedregulho', 'Cidade L', 'MG'),
            (13, NULL, 'Lima Incorporações', NULL, '98765432000234', '1998-03-22', 'sergio.lima@email.com', '1122334495', '87654321', 'Rua do Progresso', '543', 'Sala 201', 'Bairro Industrial', 'Cidade M', 'SP'),
            (14, 'Vanessa Costa', NULL, '34567890123', NULL, '1985-08-05', 'vanessa.costa@email.com', '9988776600', '12345678', 'Avenida da Praia', '654', 'CASA E DECORAÇÃO 405', 'Praia Grande', 'Cidade N', 'RJ'),
            (15, 'William Oliveira', NULL, '56789012355', NULL, '1977-02-10', 'william.oliveira@email.com', '1122934455', '54321098', 'Travessa das Oliveiras', '543', 'Sala 102', 'Bairro das Oliveiras', 'Cidade O', 'MG'),
            (16, NULL, 'Almeida & Filhos', NULL, '87654321000545', '1993-05-18', 'camila.almeida@email.com', '9988773655', '87654321', 'Rua das Flores', '876', 'CASA E DECORAÇÃO 203', 'Bairro Florido', 'Cidade P', 'SP'),
            (17, 'Denis Nunes', NULL, '98765432109', NULL, '1976-11-30', 'denis.nunes@email.com', '1122334457', '12345678', 'Avenida Central', '1234', 'Apto 504', 'Centro', 'Cidade Q', 'RJ'),
            (18, 'Elaine Santos', NULL, '10987654321', NULL, '1990-04-15', 'elaine.santos@email.com', '9988336656', '54321098', 'Travessa dos Campos', '543', 'Sala 102', 'Bairro dos Campos', 'Cidade R', 'MG'),
            (19, NULL, 'Lima Empreendimentos', NULL, '98765432101234', '1982-02-28', 'felipe.lima@email.com', '1122334455', '87654321', 'Rua da Liberdade', '543', 'Sala 201', 'Bairro Liberdade', 'Cidade S', 'SP'),
            (20, 'Gisele Costa', NULL, '34567890124', NULL, '1974-09-10', 'gisele.costa@email.com', '9988776005', '12345678', 'Avenida dos Girassóis', '654', 'CASA E DECORAÇÃO 405', 'Jardim das Flores', 'Cidade T', 'RJ');
            '''
        cursor.execute(sql_inserir_dados_clientes)

        # use "commit()" para editar o banco
        conexao.commit()

        print(f"""
            {40*'*'}
            DADOS DE CLIENTES INSERIDOS COM SUCESSO
            {40*'*'}
        """)
        
        # INSERIDOS REGISTROS NA TABELA DE PRODUTOS
        dados_produtos = [
            (1, 'Produto 1',   '1234567890123', 'CASA E DECORAÇÃO', 99.99,  50,  'UN',  'Observação do Produto 1', '1'),
            (2, 'Produto 2',   '9876543210987', 'ELETRÔNICOS',      149.99, 30,  'UN',  'Observação do Produto 2', '1'),
            (3, 'Produto 3',   '4567890123456', 'ELETRÔNICOS',      19.99,  20,  'UN',  'Observação do Produto 3', '1'),
            (4, 'Produto 4',   '1111222233334', 'CASA E DECORAÇÃO', 29.99,  100, 'UN',  'Observação do Produto 4', '1'),
            (5, 'Produto 5',   '5555666677778', 'CASA E DECORAÇÃO', 89.99,  80,  'PR',  'Observação do Produto 5', '1'),
            (6, 'Produto 6',   '8765432109876', 'ELETRÔNICOS',      49.99,  120, 'UN',  'Observação do Produto 6', '1'),
            (7, 'Produto 7',   '5432109876543', 'CASA E DECORAÇÃO', 69.99,  60,  'UN',  'Observação do Produto 7', '1'),
            (8, 'Produto 8',   '1234543212345', 'ELETRÔNICOS',      129.99, 40,  'UN',  'Observação do Produto 8', '1'),
            (9, 'Produto 9',   '5555444433332', 'ELETRÔNICOS',      24.99,  150, 'UN',  'Observação do Produto 9', '1'),
            (10, 'Produto 10', '9876543210001', 'CASA E DECORAÇÃO', 19.99,  200, 'UN',  'Observação do Produto 10', '1'),
        ]

        # Preparar a instrução SQL
        sql_inserir_dados_produtos = '''
        INSERT INTO nota_fiscal.produtos 
        (id, nome, codigo_barras, categoria, preco, saldo_estoque, unidade_comercial, observacao, ativo)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        '''

        # Executar a inserção usando executemany
        cursor.executemany(sql_inserir_dados_produtos, dados_produtos)
        conexao.commit()

        # for dado in dados_produtos:
        #     print(f'Inserindo {dado} no banco de dados')
        #     sql_inserir_dados_produtos = f'''INSERT INTO nota_fiscal.produtos 
        #     (id, nome, codigo_barras, categoria, preco, saldo_estoque, unidade_comercial, observacao, ativo)
        #     VALUES {dado};'''
        #     cursor.execute(sql_inserir_dados_produtos)
        #     conexao.commit()
        #     print(f'Linha {dado} inserida com sucesso')

        print(f"""
        {40*'*'}
        DADOS DE PRODUTOS INSERIDOS COM SUCESSO
        {40*'*'}
        """)
        

        # OUTRA TENTATIVA DE INSERIR
        sql_inserir_dados_produtos = '''
        INSERT INTO nota_fiscal.produtos 
        (id, nome, codigo_barras, categoria, preco, saldo_estoque, unidade_comercial, observacao, ativo)
        VALUES
        (1, 'Cadeira de Escritório', '1234567890123', 'CASA E DECORAÇÃO', 199.99, 50, 'UN', 'Cadeira ergonômica com suporte lombar', 1),
        (2, 'Smartphone Modelo X', '9876543210987', 'ELETRÔNICOS', 799.99, 30, 'UN', 'Tela AMOLED, câmera de alta resolução', 1),
        (3, 'Geladeira Frost Free', '4567890123456', 'ELETRODOMÉSTICOS', 1499.99, 20, 'UN', 'Duplex, eficiente em consumo de energia', 1),
        (4, 'Livro: "Aventuras Fantásticas"', '1111222233334', 'LIVROS E ENTRETENIMENTO', 29.99, 100, 'UN', 'Best-seller de ficção científica', 1),
        (5, 'Sapato Social Masculino', '5555666677778', 'MODA', 89.99, 80, 'PR', 'Couro legítimo, elegante para ocasiões especiais', 1),
        (6, 'Kit de Maquiagem', '8765432109876', 'SAÚDE E BELEZA', 49.99, 120, 'UN', 'Paleta de sombras, batons e pincéis', 1),
        (7, 'Ferro de Passar a Vapor', '5432109876543', 'ELETRODOMÉSTICOS', 69.99, 60, 'UN', 'Compacto e eficiente para passar roupas', 1),
        (8, 'Câmera de Segurança IP', '1234543212345', 'ELETRÔNICOS', 129.99, 40, 'UN', 'Monitoramento remoto por aplicativo', 1),
        (9, 'Livro: "História Antiga"', '5555444433332', 'LIVROS E ENTRETENIMENTO', 24.99, 150, 'UN', 'Exploração de civilizações antigas', 1),
        (10, 'Camiseta Casual', '9876543210001', 'MODA', 19.99, 200, 'UN', 'Algodão confortável, disponível em diversas cores', 1),
        (11, 'Secador de Cabelo Profissional', '2222111122221', 'SAÚDE E BELEZA', 79.99, 50, 'UN', 'Potente e com múltiplas velocidades', 1),
        (12, 'Panela Elétrica de Arroz', '3333222211110', 'ELETRODOMÉSTICOS', 59.99, 70, 'UN', 'Prepara arroz de forma prática e rápida', 1),
        (13, 'Livro: "Mistérios do Universo"', '1111222233335', 'LIVROS E ENTRETENIMENTO', 34.99, 90, 'UN', 'Exploração do cosmos e fenômenos cósmicos', 1),
        (14, 'Tênis Esportivo', '5555666677779', 'MODA', 59.99, 110, 'PR', 'Design moderno e confortável para atividades físicas', 1),
        (15, 'Kit de Maquiagem Profissional', '8765432109877', 'SAÚDE E BELEZA', 99.99, 30, 'UN', 'Paleta completa para maquiadores profissionais', 1),
        (16, 'Aspirador de Pó Portátil', '5432109876544', 'ELETRODOMÉSTICOS', 89.99, 45, 'UN', 'Compacto e eficiente para a limpeza diária', 1),
        (17, 'Smartwatch Fitness', '1234543212346', 'ELETRÔNICOS', 149.99, 25, 'UN', 'Monitora atividades físicas e saúde', 1),
        (18, 'Livro: "A Arte da Cozinha"', '5555444433333', 'LIVROS E ENTRETENIMENTO', 44.99, 80, 'UN', 'Receitas e técnicas culinárias', 1),
        (19, 'Bolsa Feminina Elegante', '9876543210002', 'MODA', 39.99, 100, 'UN', 'Design sofisticado e espaçoso', 1),
        (20, 'Secador de Cabelo Compacto', '2222111122222', 'SAÚDE E BELEZA', 49.99, 60, 'UN', 'Leve e ideal para viagens', 1),
        (21, 'Ferro de Passar a Vapor', '5432109876545', 'ELETRODOMÉSTICOS', 79.99, 40, 'UN', 'Com base antiaderente', 1),
        (22, 'Caixa de Som Bluetooth', '1234543212347', 'ELETRÔNICOS', 109.99, 35, 'UN', 'Conexão sem fio para dispositivos móveis', 1),
        (23, 'Livro: "Aventuras Submarinas"', '5555444433334', 'LIVROS E ENTRETENIMENTO', 29.99, 120, 'UN', 'Exploração dos oceanos e vida marinha', 1),
        (24, 'Sandália Feminina', '9876543210003', 'MODA', 29.99, 150, 'PR', 'Confortável e elegante para o dia a dia', 1),
        (25, 'Chapinha para Cabelo', '2222111122223', 'SAÚDE E BELEZA', 69.99, 50, 'UN', 'Placas de cerâmica para alisamento perfeito', 1),
        (26, 'Cafeteira Elétrica', '5432109876546', 'ELETRODOMÉSTICOS', 89.99, 30, 'UN', 'Prepara café rapidamente', 1),
        (27, 'Livro: "Viagens pelo Mundo"', '5555444433335', 'LIVROS E ENTRETENIMENTO', 39.99, 80, 'UN', 'Relatos de viagens ao redor do globo', 1),
        (28, 'Mochila Esportiva', '9876543210004', 'MODA', 49.99, 60, 'UN', 'Ideal para atividades ao ar livre', 1),
        (29, 'Barbeador Elétrico', '2222111122224', 'SAÚDE E BELEZA', 59.99, 40, 'UN', 'Preciso e fácil de usar', 1),
        (30, 'Liquidificador Potente', '5432109876547', 'ELETRODOMÉSTICOS', 99.99, 20, 'UN', 'Prepara sucos e vitaminas', 1);

        '''
        cursor.execute(sql_inserir_dados_produtos)
        conexao.commit()

        print(f"""
        {40*'*'}
        DADOS DE PRODUTOS INSERIDOS COM SUCESSO
        {40*'*'}
        """)
         
        # INSERINDO REGISTROS NA TABELA DE FORNECEDORES
        sql_inserir_dados_fornecedores = '''
        INSERT INTO nota_fiscal.fornecedores 
        (id, razao_social, cnpj, email, telefone, cep, logradouro, numero, complemento, bairro, municipio, uf, observacao, ativo)
        VALUES
        (1, 'NORDESTE IND COM ART METAIS LTDA', '12345678000100', 'nordeste@email.com', '1122334400', '12345678', 'Rua Principal', '123', 'Apto 101', 'Centro', 'Cidade A', 'SP', 'Especializado em eletrônicos', 1),
        (2, 'RECIFE IPUTINGA', '98765432100012', 'iputinga@outlook.com.br', '9988776655', '87654321', 'Avenida Secundária', '456', 'CASA E DECORAÇÃO 202', 'Bairro Norte', 'Cidade B', 'RJ', 'Fornecimento de moda masculina', 1),
        (3, 'Louças Brasil LTDA', '12345678901234', 'loucas@gmail.com', '1122334455', '54321098', 'Travessa da Esquina', '789', 'Sala 303', 'Bairro Sul', 'Cidade C', 'MG', 'Atende diversos segmentos', 1),
        (4, 'Adilson Batista dos Santos Comércio e Serviços LTDA', '45678901234567', 'comercio@outlook.com', '9876543210', '54321098', 'Rua das Flores', '789', 'Bloco 2, Ap 405', 'Jardim Primavera', 'Cidade D', 'SP', 'Especializado em produtos de decoração', 1),
        (5, 'J.P Indústria LTDA', '78901234567890', 'jp@jp.com.br', '1122334155', '12345678', 'Avenida Principal', '4567', 'CASA E DECORAÇÃO 102', 'Centro', 'Cidade E', 'RJ', 'Fornecimento de eletrônicos de última geração', 1),
        (6, 'IABC Indústria de Cosméticos LTDA', '10987654321098', 'contato@iabc.com', '9980776655', '87654321', 'Rua do Comércio', '321', 'Sala 201', 'Bairro Comercial', 'Cidade F', 'MG', 'Produtos variados para comércio', 1),
        (7, 'Mundial Acessórios e Variedades.', '12345678900234', 'suporte@mudial.com', '1122334451', '12345678', 'Rua das Árvores', '987', 'Apto 301', 'Jardim das Flores', 'Cidade G', 'SP', 'Fornecimento de móveis para escritório', 1),
        (8, 'G L de Almeida Comércio e Indústria', '34567890122222', 'contato@gl.com', '9988776605', '87654321', 'Avenida Central', '654', 'CASA E DECORAÇÃO 405', 'Centro', 'Cidade H', 'RJ', 'Produtos variados para o mercado', 1),
        (9, 'Esplanada Indústria e Comércio S/A', '56789012345098', 'esplanada@hotmail.com', '1122334425', '54321098', 'Travessa dos Campos', '543', 'Sala 102', 'Bairro Novo', 'Cidade I', 'MG', 'Fornecimento de produtos diversos', 1),
        (10, 'KELVIA LOPES PEREIRA DE ARAUJO', '87654321011111', 'kelvia@gmail.com', '9988776611', '87654321', 'Rua das Montanhas', '876', 'CASA E DECORAÇÃO 203', 'Bairro Residencial', 'Cidade J', 'SP', 'Especializado em produtos para construção', 1);

        '''
        cursor.execute(sql_inserir_dados_fornecedores)
        conexao.commit()

        print(f"""
        {40*'*'}
        DADOS DE FORNECEDORES INSERIDOS COM SUCESSO
        {40*'*'}
        """)

        # INSERINDO REGISTROS NA TABELA DE PEDIDOS 
        sql_inserir_dados_pedidos = '''
        INSERT INTO nota_fiscal.pedidos 
        (id, clientes_id, data_compra, status, valor_total, frete, tipo_pagamento, descricao)
        VALUES
        (1, 1, '2023-01-15', 'PROCESSANDO PAGAMENTO', 150.00, 10.00, 'BOLETO', 'Pedido em andamento'),
        (2, 2, '2023-02-20', 'CANCELADO', 300.50, 15.00, 'CARTÃO DE CRÉDITO', 'Pagamento não autorizado'),
        (3, 3, '2023-03-10', 'PREPARANDO PEDIDO', 75.99, 8.50, 'PIX', 'Pedido em preparação'),
        (4, 4, '2023-04-05', 'ENVIADO', 200.25, 12.00, 'CARTÃO DE CRÉDITO', 'Pedido enviado para entrega'),
        (5, 5, '2023-05-12', 'ENTREGUE', 450.80, 20.00, 'PIX', 'Pedido entregue com sucesso'),
        (6, 16, '2023-06-18', 'PROCESSANDO PAGAMENTO', 80.50, 9.00, 'BOLETO', 'Aguardando confirmação de pagamento'),
        (7, 7, '2023-07-23', 'PREPARANDO PEDIDO', 120.75, 15.00, 'CARTÃO DE CRÉDITO', 'Pedido em preparação'),
        (8, 8, '2023-08-30', 'ENVIADO', 600.00, 25.00, 'PIX', 'Pedido enviado para entrega'),
        (9, 1, '2023-09-05', 'PROCESSANDO PAGAMENTO', 90.20, 10.00, 'BOLETO', 'Aguardando confirmação de pagamento'),
        (10, 20, '2023-10-08', 'PREPARANDO PEDIDO', 180.75, 18.00, 'CARTÃO DE CRÉDITO', 'Pedido em preparação'),
        (11, 1, '2023-11-15', 'CANCELADO', 100.00, 10.00, 'CARTÃO DE CRÉDITO', 'Pagamento não autorizado'),
        (12, 2, '2023-11-20', 'CANCELADO', 300.50, 15.00, 'CARTÃO DE CRÉDITO', 'Pagamento não autorizado'),
        (13, 3, '2023-03-10', 'PREPARANDO PEDIDO', 200.75, 18.00, 'CARTÃO DE CRÉDITO', 'Pedido em preparação'),
        (14, 4, '2023-12-05', 'ENVIADO', 200.25, 12.00, 'CARTÃO DE CRÉDITO', 'Pedido enviado para entrega'),
        (15, 15, '2023-12-12', 'ENTREGUE', 450.80, 20.00, 'PIX', 'Pedido entregue com sucesso'),
        (16, 6, '2023-06-18', 'PROCESSANDO PAGAMENTO', 80.50, 9.00, 'BOLETO', 'Aguardando confirmação de pagamento'),
        (17, 7, '2023-07-23', 'PREPARANDO PEDIDO', 120.75, 15.00, 'CARTÃO DE CRÉDITO', 'Pedido em preparação'),
        (18, 8, '2023-08-30', 'ENVIADO', 600.00, 25.00, 'PIX', 'Pedido enviado para entrega'),
        (19, 9, '2023-09-05', 'PROCESSANDO PAGAMENTO', 90.20, 10.00, 'BOLETO', 'Aguardando confirmação de pagamento'),
        (20, 10, '2023-10-08', 'PREPARANDO PEDIDO', 180.75, 18.00, 'CARTÃO DE CRÉDITO', 'Pedido em preparação');

        '''
        cursor.execute(sql_inserir_dados_pedidos)
        conexao.commit()

        print(f"""
        {40*'*'}
        DADOS DE PEDIDOS INSERIDOS COM SUCESSO
        {40*'*'}
        """)

        # INSERINDO REGISTROS NA TABELA DE NOTA FISCAL
        sql_inserir_dados_notas_fiscais = '''
        INSERT INTO nota_fiscal.notas_fiscais 
        (id, pedidos_id, modelo, serie, numero, chave_acesso, data_emissao, observaçao) -- OBSERVAÇÃO COM Ç
        VALUES
        (1, 1, '55', '1', '0001234',   '45678901234568890123456', '2023-01-15 08:30:00', 'Nota fiscal em processamento'),
        (2, 2, '55', '1', '0005678',   '56789012345678902234567', '2023-02-20 09:45:00', 'Nota fiscal CANCELADA'),
        (3, 3, '55', '1', '0009123',   '67890123456789012345677', '2023-03-10 10:15:00', 'Nota fiscal em processamento'),
        (4, 4, '55', '1', '0012567',   '78901234567890123456799', '2023-04-05 11:30:00', 'Nota fiscal enviada para transporte'),
        (5, 5, '55', '1', '0016012',   '89012345678901233567890', '2023-05-12 12:45:00', 'Nota fiscal entregue ao cliente'),
        (6, 6, '55', '1', '0019456',   '90123456789012345778901', '2023-06-18 14:00:00', 'Nota fiscal em processamento'),
        (7, 7, '55', '1', '0022901',   '01234567890723456789012', '2023-07-23 15:15:00', 'Nota fiscal a caminho da entrega'),
        (8, 8, '55', '1', '0026345',   '12345678901234567890123', '2023-08-30 16:30:00', 'Nota fiscal entregue ao transportador'),
        (9, 9, '55', '1', '0029790',   '23456789012345678901234', '2023-09-05 17:45:00', 'Nota fiscal processada em processamento'),
        (10, 10, '55', '1', '0033234', '34567890123456789012345', '2023-10-08 19:00:00', 'Nota fiscal processada com sucesso'),
        (11, 11, '55', '1', '0036679', '45678901234567890123456', '2023-11-15 08:30:00', 'Nota fiscal cancelada'),
        (12, 12, '55', '1', '0040123', '56989012345678901234567', '2023-11-20 09:45:00', 'Nota fiscal cancelada'),
        (13, 13, '55', '1', '0043567', '27890123456789012345678', '2023-03-10 10:15:00', 'Nota fiscal em processamento'),
        (14, 14, '55', '1', '0047012', '78901234567890123456789', '2023-12-05 11:30:00', 'Nota fiscal enviada para transporte'),
        (15, 15, '55', '1', '0050456', '89012340678921234567890', '2023-12-12 12:45:00', 'Nota fiscal entregue ao cliente'),
        (16, 16, '55', '1', '0053901', '90123456789022345678901', '2023-06-18 14:00:00', 'Nota fiscal processada com sucesso'),
        (17, 17, '55', '1', '0057345', '01234562890123452789012', '2023-07-23 15:15:00', 'Nota fiscal a caminho da entrega'),
        (18, 18, '55', '1', '0060790', '12345672901234567890123', '2023-08-30 16:30:00', 'Nota fiscal entregue ao transportador'),
        (19, 19, '55', '1', '0064234', '23456789012345278901234', '2023-09-05 17:45:00', 'Nota fiscal em processamento'),
        (20, 20, '55', '1', '0067679', '34567890123456289012345', '2023-10-08 19:00:00', 'Nota fiscal processada com sucesso');
        '''
        cursor.execute(sql_inserir_dados_notas_fiscais)
        conexao.commit()

        print(f"""
        {40*'*'}
        DADOS DE NOTAS FISCAIS INSERIDOS COM SUCESSO
        {40*'*'}
        """)


        # INSERIDOS REGISTROS NA TABELA PEDIDOS Produtos 
        sql_inserir_dados_pedido_prduto = '''
        INSERT INTO nota_fiscal.pedidos_produtos 
        (pedidos_id, produtos_id, quantidade)
        VALUES
        (1, 1, 2),
        (1, 20, 5),
        (1, 11, 2),
        (1, 4, 3),
        (1, 2, 1),
        (2, 3, 3),
        (2, 4, 1),
        (2, 11, 2),
        (2, 10, 1),
        (3, 5, 1),
        (3, 6, 2),
        (4, 7, 1),
        (4, 8, 4),
        (5, 9, 2),
        (5, 10, 1),
        (6, 11, 3),
        (6, 12, 2),
        (7, 13, 1),
        (7, 14, 1),
        (8, 15, 5),
        (8, 16, 3),
        (9, 17, 2),
        (9, 18, 2),
        (10, 19, 1),
        (10, 20, 1),
        (11, 11, 2),
        (11, 2, 1),
        (12, 3, 3),
        (12, 14, 1),
        (13, 5, 1),
        (13, 16, 2),
        (14, 7, 1),
        (14, 18, 4),
        (15, 9, 2),
        (15, 10, 1),
        (16, 11, 3),
        (16, 12, 2),
        (17, 23, 1),
        (17, 14, 1),
        (18, 15, 5),
        (18, 16, 3),
        (19, 17, 2),
        (19, 18, 2),
        (20, 19, 1),
        (20, 20, 1);
        '''
        cursor.execute(sql_inserir_dados_pedido_prduto)
        conexao.commit()

        print(f"""
        {40*'*'}
        DADOS DE NOTAS FISCAIS INSERIDOS COM SUCESSO
        {40*'*'}
        """)

        # INSERIDOS REGISTROS NA TABELA FORNECEDORES PRODUTOS
        sql_inserir_dados_fornecedores_produto = '''
        INSERT INTO nota_fiscal.fornecedores_produtos 
        (fornecedores_id, produtos_id, quantidade)
        VALUES
        (1, 1, 100),
        (2, 2, 50),
        (3, 3, 200),
        (4, 4, 30),
        (5, 5, 80),
        (6, 6, 150),
        (7, 7, 40),
        (8, 8, 70),
        (9, 9, 120),
        (10, 10, 60),
        (1, 11, 100),
        (2, 12, 50),
        (3, 13, 200),
        (4, 14, 30),
        (5, 15, 80),
        (6, 16, 150),
        (7, 17, 40),
        (8, 18, 70),
        (9, 19, 120),
        (10, 20, 60),
        (1, 20, 100),
        (2, 21, 50),
        (3, 22, 200),
        (4, 23, 30),
        (5, 24, 80),
        (6, 25, 150),
        (7, 26, 40),
        (8, 27, 70),
        (9, 28, 120),
        (10, 30, 60);
        '''
        cursor.execute(sql_inserir_dados_fornecedores_produto)
        conexao.commit()

        print(f"""
        {40*'*'}
        DADOS DE FORNECEDORES PRODUTOS INSERIDOS COM SUCESSO
        {40*'*'}
        """)

except mysql.connector.Error as err:
    print(f'Erro ao conectar ao MySQL: {err}')

finally:
    # Fechar a Conexão ao Sair
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print('Conexão ao MySQL fechada.')


  










# # AQUI VAI UM CÓDIGO PARA FAZER UM LOOPING NA INSERSÃO DE DADOS
# acaba com essa repetição de conexão e cursor

#  


# ## Consultando os dados das tabelas

# # AQUI VAI UM MENU PARA ESCOLER QUAL TABELA QUER LER
# 
# tenta printar num formato legalzinho

#  
sql_consulta = "SELECT * FROM clientes"
cursor.execute(sql_consulta)


# Use "fetchall()" para leitura do banco
result = cursor.fetchall()

for dado in result:
    print(dado)

#  
sql_consulta_fornecedores = "SELECT * FROM fornecedores"
cursor.execute(sql_consulta_fornecedores)

result = cursor.fetchall()

for dado in result:
    print(dado)

#  
sql_consulta_pedidos = "SELECT * FROM pedidos"
cursor.execute(sql_consulta_pedidos)

result = cursor.fetchall()

for dado in result:
    print(dado)

#  
sql_consulta_notas_fiscais = "SELECT * FROM notas_fiscais"
cursor.execute(sql_consulta_notas_fiscais)

result = cursor.fetchall()

for dado in result:
    print(dado)

#  
sql_consulta_pedidos_produtos = "SELECT * FROM pedidos_produtos"
cursor.execute(sql_consulta_pedidos_produtos)

result = cursor.fetchall()

for dado in result:
    print(dado)

#  
sql_consulta_fornecedores_produtos = "SELECT * FROM fornecedores_produtos"
cursor.execute(sql_consulta_fornecedores_produtos)

result = cursor.fetchall()

for dado in result:
    print(dado)

# ## Atualizando dados nas tabelas

#  
sql_atualizacao_clientes = '''
UPDATE nota_fiscal.clientes
SET nome_completo = "MERCADINHO DE JOÃOZINHO"
WHERE id = 1;
'''
cursor.execute(sql_atualizacao_clientes)

result = cursor.fetchall()

for dado in result:
    print(dado)

#  


#  


#  
# SEMPRE FECHE A CONEXÃO COM O BANCO DE DADOS, é sério.

cursor.close()
conexao.close()

#  


