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