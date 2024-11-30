/*
 * Segunda Forma Normal (2FN)
 * 
 * Para uma tabela estar na 2FN, é necessário que:
 * -> Ela esteja na 1FN
 * -> Todas as colunas não-chave da tabela devem depender inteiramente de todas as
 * partes da chave primária. Chamamos isso de Dependência Funcional Total.
 */

# Cria o banco de dados 20241130_modulo02_python caso ele não exista
CREATE DATABASE IF NOT EXISTS 20241130_modulo02_python;

# Define o banco de dados onde os comandos SQL serão executados
USE 20241130_modulo02_python;

# Criação da tabela tb_controle_servico. Essa tabela terá uma chave primária
# composta, ou seja, uma chave primária criada a partir de 2 colunas ou mais.
CREATE TABLE IF NOT EXISTS tb_controle_servico(
    id INT AUTO_INCREMENT,
    servico_id INT NOT NULL,
    servico VARCHAR(100) NOT NULL,
    valor_hora FLOAT,
    total_horas INT NOT NULL,
    PRIMARY KEY(id, servico_id)
);

DESC tb_controle_servico;

INSERT INTO tb_controle_servico(servico_id, servico, valor_hora, total_horas)
VALUES
    (1, "Manutenção de PC", 80, 6),
    (1, "Manutenção de PC", 80, 10),
    (2, "Desenvolvimento de Site", 150, 10),
    (3, "Configuração de Servidor", 100, 3),
    (4, "Aulas de Programação Java", 60, 8);
SELECT * FROM tb_controle_servico tcs ;

/*
 * No caso acima, a tabela tb_controle_servico está na 1FN, pois possui uma
 * chave primária, não possui colunas multivaloradas e não possui colunas com
 * valores compostos.
 * Porém, ela não está na 2FN pois as colunas servico_id e valor_hora dependem apenas
 * de um lado da chave primária, que é a coluna servico_id. A coluna total_horas
 * depende de todas as partes da chave, pois irá associar o id do registro de
 * serviço com o serviço que foi realizado.
 * Nesse caso, o ideal é remover as colunas que dependem de apenas um lado da
 * chave primária, e criarmos novas tabelas. Além disso, vamos criar uma chave
 * estrangeira na tabela tb_controle_servico que irá referenciar essa nova
 * tabela.
 */


