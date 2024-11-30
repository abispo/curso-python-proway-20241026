/*
 * Terceira Forma Normal
 * 
 * Para uma tabela estar na 3FN, é necessário que:
 * -> Ela esteja na 2FN
 * -> Todas as colunas não chave da tabela dependem exclusivamente da chave primária (dependência transitiva)
 * 
 */

# Cria o banco de dados 20241130_modulo02_python caso ele não exista
CREATE DATABASE IF NOT EXISTS 20241130_modulo02_python;

# Define o banco de dados onde os comandos SQL serão executados
USE 20241130_modulo02_python;

CREATE TABLE IF NOT EXISTS tb_pedidos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    data_pedido DATETIME NOT NULL,
    observacoes VARCHAR(200) NULL
);
DESC tb_pedidos;
INSERT INTO tb_pedidos (data_pedido, observacoes) VALUES
    ("2024-10-11 12:42:52", NULL),
    ("2024-10-12 14:04:23", "primeira compra");
SELECT * FROM tb_pedidos tp ;

CREATE TABLE IF NOT EXISTS tb_produtos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    valor_unitario FLOAT NOT NULL
);
DESC tb_produtos;
INSERT INTO tb_produtos (nome, valor_unitario) VALUES 
    ("Mochila do Naruto", 89),
    ("Caneta de Gatinho", 9.90),
    ("Caneca do Sasuke", 14.90),
    ("Mouse Gamer do Seu Madruga", 79.90),
    ("Gravata", 10);
SELECT * FROM tb_produtos tp ;

# Crição da tabela que irá relacionar os pedidos com os produtos

