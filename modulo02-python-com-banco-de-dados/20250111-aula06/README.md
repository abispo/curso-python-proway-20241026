SQLAlchemy

SQLAlchemy é um ORM (Object Relational Mapper/Mapeador Objeto Relacional) para Python. Em um ORM, as chamadas da linguagem são "traduzidas" para chamadas SQL.

# Desafios

1. Criar a model `Postagem`. Essa model terá os seguintes atributos:
    | nome       | tipo | observações                        
    |------------|------|------------------------------------|
    | id         | int  | chave primária, auto incremento    |
    | usuario_id | int  | chave estrangeira para usuarios.id |
    | titulo     | str  | varchar(100) not null              |
    | texto      | str  | text not null                      |
`Usuario` terá uma relação 1:N com `Postagem` 

2. Criar a model `Categoria`. Essa model terá os seguintes atributos:
    | nome       | tipo | observações                        
    |------------|------|------------------------------------|
    | id         | int  | chave primária, auto incremento    |
    | nome       | str  | varchar(100) not null              |

3. Criar a model `postagens_categorias`. Essa model será a representação da tabela associativa entre `Postagem` e `Categoria`. Essa model terá a seguinte estrutura:
    | nome         | tipo | observações                        
    |--------------|------|------------------------------------------------------|
    | postagem_id  | int  | chave primária, chave estrangeira para postagens.id  |
    | categoria_id | int  | chave primária, chave estrangeira para categorias.id |

No caso da tabela associativa, a sua estrutura não precisa ser igual as outras. Utilize a classe `Table` para criá-la. Você pode seguir a documentação em https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#setting-bi-directional-many-to-many

4. Criar a model `Comentario`, que terá a seguinte estrutura:
    | nome         | tipo | observações                        
    |--------------|------|------------------------------------------------------|
    | id           | int  | chave primária, auto incremento                      |
    | postagem_id  | int  | chave estrangeira para postagens.id                  |
    | usuario_id   | int  | chave estrangeira para usuarios.id                   |
    | texto        | str  | varchar(200) NOT NULL

Observações:
* Para os nomes das tabelas, utilize o padrão que foi utilizado para `Usuario` e `Perfil`. Por exemplo, a tabela associada a model `Postagem` se chamará `postagens`.
* Para cada model, crie os atributos do tipo `relationship` correspondentes.
* Crie as estruturas restantes de gerenciamento. Ou seja, crie funções para selecionar, inserir, atualizar e apagar os registros. Tente também adicionar a opção do usuário selecionar passando algum parâmetro, por exemplo, selecionar um usuário a partir do e-mail.