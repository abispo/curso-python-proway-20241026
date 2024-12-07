-- Active: 1733589803423@@127.0.0.1@3306
CREATE DATABASE IF NOT EXISTS modulo02_exercicios_relacionamentos
    DEFAULT CHARACTER SET = 'utf8mb4';

USE modulo02_exercicios_relacionamentos;

-- Exercício 1
CREATE TABLE IF NOT EXISTS tb_livros(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    isbn CHAR(13) NOT NULL
);

INSERT INTO tb_livros(nome, autor, isbn) VALUES
    ("A Sociedade do Anel", "J.R.R Tolkien", "5930985721943"),
    ("A cor que caiu do espaço", "H.P. Lovecraft", "1830222748375"),
    ("O caminho do feiticeiro", "Steve Jackson", "1993499046128");

SELECT * FROM tb_livros;

CREATE TABLE IF NOT EXISTS tb_detalhes_livros(
    id INT PRIMARY KEY NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    numero_de_paginas SMALLINT NOT NULL,
    ano_de_lancamento DATE NOT NULL,
    FOREIGN KEY (id) REFERENCES tb_livros(id)
);

INSERT INTO tb_detalhes_livros(id, categoria, numero_de_paginas, ano_de_lancamento) VALUES
    (1, "Fantasia", 600, "1950-01-01"),
    (2, "Horror Cósmico", 300, "1930-01-01"),
    (3, "RPG", 180, "1970-01-01");

SELECT tl.nome, tl.autor, tdl.categoria
    FROM tb_livros tl
    INNER JOIN tb_detalhes_livros tdl
    ON tl.id = tdl.id;

-- ------------------------------------------------------------

-- Exercício 4
CREATE TABLE IF NOT EXISTS tb_usuarios(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_de_nascimento DATE NOT NULL,
    genero_favorito VARCHAR(50)
);

INSERT INTO tb_usuarios(nome, data_de_nascimento, genero_favorito) VALUES
    ("Maria da Silva", "1977-07-29", "Rock"),
    ("João das Neves", "1993-02-15", "Reggae"),
    ("Bruna Aparecida", "2000-01-22", "POP");

CREATE TABLE IF NOT EXISTS tb_playlists(
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    nome VARCHAR(200) NOT NULL,
    observacoes VARCHAR(200) NULL,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(usuario_id) REFERENCES tb_usuarios(id)
);

INSERT INTO tb_playlists(usuario_id, nome) VALUES(
    1, "Rock clássico anos 1980"
);
INSERT INTO tb_playlists(usuario_id, nome, observacoes) VALUES
    (2, "Coleção Bob Marley", "Coleção Som livre");

INSERT INTO tb_playlists(usuario_id, nome) VALUES
    (3, "Madonna, Lady Gaga e Cyndi Lauper");

INSERT INTO tb_playlists(usuario_id, nome) VALUES
    (2, "Root songs 1980");

SELECT * FROM tb_playlists;

SELECT tb_usuarios.nome, tb_playlists.nome
    FROM tb_usuarios
    INNER JOIN tb_playlists
    ON tb_usuarios.id = tb_playlists.id;