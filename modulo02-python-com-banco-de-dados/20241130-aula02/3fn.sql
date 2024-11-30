/*
 * Terceira Forma Normal
 * 
 * Para uma tabela estar na 3FN, é necessário que:
 * -> Ela esteja na 2FN
 * -> Todas as colunas não chave da tabela dependem exclusivamente da chave primária.
 * Caso exista uma coluna não chave que dependa de outra coluna não chave,
 * temos uma dependência transitiva
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
CREATE TABLE IF NOT EXISTS tb_pedidos_produtos(
    pedido_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
    subtotal INT NOT NULL,
    PRIMARY KEY(pedido_id, produto_id),
    FOREIGN KEY(pedido_id) REFERENCES tb_pedidos(id),
    FOREIGN KEY(produto_id) REFERENCES tb_produtos(id)
);
DESC tb_pedidos_produtos;

INSERT INTO tb_pedidos_produtos(
    pedido_id, produto_id, quantidade, subtotal 
) VALUES
    (1, 1, 3, 267),
    (1, 2, 1, 9.90),
    (2, 3, 1, 14.90),
    (2, 4, 1, 79.90),
    (2, 1, 1, 89.90);
SELECT * FROM tb_pedidos_produtos tpp ;

/*
 * A coluna subtotal, apesar de depender de todas AS partes da chave primária,
 * também depende de uma coluna não chave, que é a quantidade. Nesse caso, devemos
 * remover essa coluna da tabela e a calcular NO momento de execução da consulta.
*/

-- O comando ALTER TABLE altera a estrutura de uma tabela
ALTER TABLE tb_pedidos_produtos DROP COLUMN subtotal;

-- Trazendo os dados das tabelas, calculando o subtotal
SELECT
    tpi.id,
    tpi.data_pedido,
    tpd.nome,
    tpd.valor_unitario,
    tpp.quantidade,
    -- Cálculo do subtotal.     
    tpd.valor_unitario * tpp.quantidade AS "subtotal"
FROM tb_pedidos tpi
INNER JOIN tb_pedidos_produtos tpp 
ON tpi.id = tpp.pedido_id
INNER JOIN tb_produtos tpd
ON tpp.produto_id = tpd.id;

-- Com isso, deixamos de ter uma coluna do subtotal, e calculamos diretamente na consulta