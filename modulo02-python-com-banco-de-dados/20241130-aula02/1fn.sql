/*
Primeira Forma Normal (1FN)

A 1FN define que uma tabela deve ter AS seguintes regras:
 * Cada coluna deve ter apenas valores atômicos ou indivisíveis, ou seja, 
valores não compostos.
 * A tabela deve ter pelo menos 1 coluna que seja chave primária.
 * Não podemos ter na tabela colunas multivaloradas, ou seja, mais de
um valor na mesma coluna.
*/

# Cria o banco de dados 20241130_modulo02_python caso ele não exista
CREATE DATABASE IF NOT EXISTS 20241130_modulo02_python;

# Define o banco de dados onde os comandos SQL serão executados
USE 20241130_modulo02_python;

# Criação da tabela tb_clientes
CREATE TABLE IF NOT EXISTS tb_clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    telefone VARCHAR(100) NOT NULL
);

# O comando DESC descreve a estrutura da tabela
DESC tb_clientes;

# Inserção de dados na tabela tb_clientes
INSERT INTO tb_clientes (nome, endereco, telefone) VALUES (
    "João da Silva",
    "Rua XV de Novembro, 1000, Centro, Blumenau, SC",
    "47923456789"
);
INSERT INTO tb_clientes (nome, endereco, telefone) VALUES (
    "Neide Carvalho",
    "Praça da Liberdade, 12, Liberdade, São Paulo, SP",
    "11957483902,11933334501"
);
INSERT INTO tb_clientes (nome, endereco, telefone) VALUES (
    "Maria Souza",
    "Rua dos Bandeirantes, 240, Centro, Pomerode, SC",
    "47992014544"
);

# Consulta a tabela tb_clientes
SELECT * FROM tb_clientes;

/*
 * A tabela tb_clientes não está na Primeira Forma Normal (1FN), pois:
 * A coluna 'endereco' não é indivisível (pode ser quebrada em outras colunas)
 * A coluna 'telefone' possui alguns registros multivalorados
*/

# Criando a tabela tb_clientes seguindo as regras da 1FN

# Vamos renomear a tabela fora das normas
RENAME TABLE tb_clientes TO tb_clientes_pre_1fn;

# Criar a tabela tb_clientes seguindo as regras da 1FN
CREATE TABLE IF NOT EXISTS tb_clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    tipo_logradouro VARCHAR(50) NOT NULL,
    logradouro VARCHAR(100) NOT NULL,
    numero VARCHAR(20) NOT NULL,
    bairro VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    uf CHAR(2) NOT NULL
);

DESC tb_clientes;

# Como a coluna telefone é multivalorada, precisamos criar uma
# nova tabela para armazenar esse tipo de informação

# Criação da tabela tb_telefones
CREATE TABLE IF NOT EXISTS tb_telefones(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES tb_clientes(id)
);

INSERT INTO tb_clientes(
    nome, tipo_logradouro, logradouro, numero, bairro, cidade, uf
) VALUES
("João da Silva", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC"),
("Neide Carvalho", "Praça", "da Liberdade", "12", "Liberdade", "São Paulo", "SP"),
("Maria Souza", "Rua", "dos Bandeirantes", "240", "Centro", "Pomerode", "SC");

SELECT * FROM tb_clientes;

INSERT INTO tb_telefones (cliente_id, telefone) VALUES
    (1, "47934985902"),
    (2, "11966739200"),
    (2, "11977728344"),
    (3, "47900982361");
SELECT * FROM tb_telefones;

# A linha abaixo não executará, pois irá acontecer um erro de chave estrangeira
# Não existe um cliente com id 1000 na tabela de clientes
INSERT INTO tb_telefones(cliente_id, telefone) VALUES
    (1000, "47944811095");
    
# Como as tabelas tb_clientes e tb_telefones estão relacionadas, podemos utilizar
# os joins para consultar informações das 2 tabelas ao mesmo tempo
SELECT tb_clientes.nome, tb_telefones.telefone
    FROM tb_clientes
    INNER JOIN tb_telefones
ON tb_clientes.id = tb_telefones.cliente_id;

# Inserindo cliente que não possui telefone
INSERT INTO tb_clientes(
    nome, tipo_logradouro, logradouro, numero, bairro, cidade, uf
) VALUES
    ("José Goulart", "Rua", "dos Caçadores", "4000", "Testo Central", "Pomerode", "SC");
SELECT * FROM tb_clientes;

# Dessa vez, utilizaremos apelidos (aliases) para as tabelas
SELECT tc.id, tc.nome, tt.telefone
    FROM tb_clientes tc
    INNER JOIN tb_telefones tt
ON tc.id = tt.cliente_id;