-- Active: 1733589803423@@127.0.0.1@3306@modulo02_python

/*
Níveis de relacionamento entre tabelas em um banco de dados

Podemos chamar de cardinalidade os níveis de relacionamento entre as tabelas de um banco de dados, ou seja, como se dão as relações entre essas tabelas.

Existem 3 tipos de relaciomentos possíveis entre 2 tabelas em um banco de dados, que são os seguintes:

1:1     Relacionamento Um para um
1:N     Relacionamento Um para muitos
N:N     Relacionamento Muitos para muitos

Entender como as tabelas(entidades) se relacionam é um passo fundamental na fase de modelagem dos dados da nossa aplicação. Relacionamentos mal definidos levam a perda de consistência e confiabilidade dos dados.

Para ilustrar esses tipos de relacionamentos, vamos montar um estrutura de tabelas que irá simular um sistema de posts e mensagens (estilo twitter). Para modelar essas tabelas, precisamos entender as regras desse negócio, que são as seguintes:

* Um usuário deverá ter as seguintes informações armazenadas:
    * Nome
    * Sobrenome
    * Data de nascimento
    * Email
    * Senha
Porém, para armazenar os dados do usuário, vamos dividir o que é dado pessoal e o que é dado de acesso ao sistema. Os dados pessoais são: nome, sobrenome e data de nascimento. Os dados de acesso são email e senha. Esses dados devem ser salvos em tabelas diferentes. Pra cada usuario, deve ter apenas 1 perfil, e vice-versa.
*/

CREATE DATABASE IF NOT EXISTS modulo02_python DEFAULT CHARACTER SET = 'utf8mb4';

USE modulo02_python;

-- Criação da tabela tb_usuarios, que irá armazenar os dados de acesso do usuário
CREATE TABLE IF NOT EXISTS tb_usuarios(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

-- Criação da tabela tb_perfis, que irá armazenar os dados pessoais do usuário
CREATE TABLE IF NOT EXISTS tb_perfis(
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    sobrenome VARCHAR(100),
    data_de_nascimento DATE NOT NULL,
    FOREIGN KEY(id) REFERENCES tb_usuarios(id)
);

-- Acima, definimos o id do perfil como chave primária e chave estrangeira ao mesmo tempo. Dessa maneira, conseguimos criar um relacionamento 1:1 entre as tabelas tb_usuarios e tb_perfis, pois não temos perfis com o mesmo id, e o id do perfil deve existir na tabela tb_usuarios

-- Criação de usuários
INSERT INTO tb_usuarios (email, senha) VALUES
    ("maria.silva@email.com", "123"),
    ("jose.soares@email.com", "123"),
    ("joao.ferreira@email.com", "123");

-- Criação dos perfis associados aos usuários
INSERT INTO tb_perfis (id, nome, sobrenome, data_de_nascimento) VALUES
    (1, "Maria", "Silva", "1999-05-17"),
    (2, "José", "Soares", "1983-12-03"),
    (3, "João", "Ferreira", "2000-08-12");

-- As seguintes instruções SQL não funcionarão

-- A instrução abaixo não funcionará, pois vamos tentar inserir um id que já existe na tabela de perfis. De acordo com as regras, devemos ter exatamente 1 perfil associado a 1 usuário
INSERT INTO tb_perfis (id, nome, sobrenome, data_de_nascimento) VALUES
    (2, "Barbara", "Correa", "1997-09-16");

-- Já a instrução abaixo não funcionará, pois vamos tentar inserir um id de perfil de um usuário que não existe na tabela de usuarios
INSERT INTO tb_perfis (id, nome, sobrenome, data_de_nascimento) VALUES
    (1000, "Thiago", "Carvalho", "1987-09-11");

/*

Continuando a modelagem das tabelas do nosso sistema de mensagens, vamos criar a tabela de postagens, que irá armazenar as postagens feitas pelos usuários. As regras para postagem são as seguintes:
    * Um usuário pode ter 0, 1 ou mais postagens salvas
    * Uma postagem pode ter apenas 1 autor, que será o usuário que fez a postagem
    * Precisamos armazenar as seguintes informações sobre a postagem:
        * id da postagem
        * id do autor da postagem
        * titulo da postagem
        * texto da postagem
        * data/hora de criação da postagem
*/

-- Criação da tabela tb_postagens, que irá armazenar os posts
CREATE TABLE IF NOT EXISTS tb_postagens(
    id INT AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    texto TEXT NOT NULL,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id, usuario_id),
    FOREIGN KEY (usuario_id) REFERENCES tb_usuarios(id)
);

-- Inserir postagens feitas por maria.silva@email.com
INSERT INTO tb_postagens(usuario_id, titulo, texto) VALUES
    (1, "A linguagem Python", "A linguagem Python é simples."),
    (1, "A linguagem Java", "A linguagem Java é robusta.");

-- Inserir postagem feita por jose.soares@email.com
INSERT INTO tb_postagens(usuario_id, titulo, texto) VALUES
    (2, "A linguagem PHP", "PHP é muito utilizada na WEB.");

-- Retornar as postagens feitas por maria.silva@email.com
SELECT tu.email, tp.titulo, tp.texto
    FROM tb_usuarios tu
    INNER JOIN tb_postagens tp
    ON tu.id = tp.usuario_id
    AND tu.id = 1;

-- Mostrar os usuários que ainda não fizeram nenhuma postagem
-- SELECT tu.email, tp.id, tp.usuario_id from tb_usuarios tu
--     LEFT JOIN tb_postagens tp
--     ON tu.id = tp.usuario_id
--     and tp.id IS NULL;


/*
    Para cada postagem que for feita, podemos definir categorias para essa postagem. Por exemplo: A postagem "A linguagem Python" pode fazer parte das categorias "programacao", "python", "2024" e etc. Assim como podemos filtrar postagens de acordo com uma dada categoria. Por exemplo, podemos trazer todas as postagens que façam parta da categoria "bancodedados".

    Ou seja, vamos criar um relacionamento entre as entidades Postagem e Categoria. Para a categoria, precisamos apenas do seu nome.
*/

-- Criação da tabela de categorias
CREATE TABLE IF NOT EXISTS tb_categorias(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

INSERT INTO tb_categorias(nome) VALUES
    ("programacao"),
    ("python"),
    ("java"),
    ("php"),
    ("proway"),
    ("2024"),
    ("sql"),
    ("arduino"),
    ("powerbi"),
    ("linux");

-- Nesse caso, teremos uma relação de N:N (Muitos para muitos) entre as tabelas tb_postagens e tb_categorias. Quando temos esse tipo de relacionamento, sobre obrigados a criar uma outra tabela, que chamaremos de tabela associativa. Essa tabela será responsável por associar as postagens com as categorias. Vamos criar a tabela tb_postagens_categorias

CREATE TABLE IF NOT EXISTS tb_postagens_categorias(
    postagem_id INT NOT NULL,
    categoria_id INT NOT NULL,
    PRIMARY KEY(postagem_id, categoria_id),
    FOREIGN KEY(postagem_id) REFERENCES tb_postagens(id),
    FOREIGN KEY(categoria_id) REFERENCES tb_categorias(id)
);

-- Associar algumas categorias às postagens
INSERT INTO tb_postagens_categorias(postagem_id, categoria_id) VALUES
    (1, 1),
    (1, 2),
    (1, 5),
    (1, 6),
    (2, 1),
    (2, 3),
    (2, 5),
    (2, 6);

-- A consulta abaixo trás todas as postagens onde exista a categoria 'java' associada.
SELECT tp.titulo, tc.nome
    FROM tb_postagens tp
    INNER JOIN tb_postagens_categorias tpc
    ON tp.id = tpc.postagem_id
    INNER JOIN tb_categorias tc
    ON tpc.categoria_id = tc.id
    WHERE tc.nome = 'java';

-- Como vimos acima, quando temos um relacionamento N:N, para mantermos a confiabilidade e a otimização dos dados nas tabelas, criamos uma outra tabela que chamamos de tabela associativa, que irá associar os dados das tabelas A e B.

-- Desafio: Temos que criar uma estrutura para armazenar os comentários que podem ser feitos em cada postagem. Cada comentário terá um id, o id do usuário que fez esse comentário, e o texto do comentário. Crie a tabela para armazenamento e também o(s) relacionamento(s) necessário(s).
CREATE TABLE IF NOT EXISTS tb_comentarios(
    id INT PRIMARY KEY AUTO_INCREMENT,
    postagem_id int NOT NULL,
    usuario_id INT NOT NULL,
    texto VARCHAR(200) NOT NULL,
    FOREIGN KEY(postagem_id) REFERENCES tb_postagens(id),
    FOREIGN KEY(usuario_id) REFERENCES tb_usuarios(id)
);