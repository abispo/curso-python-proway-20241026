
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from config import Base

# Aqui criamos a model Usuario. O termo model refere-se a classes que serão mapeadas para tabelas no banco de dados. No nosso caso, sempre que quisermos criar uma model, obrigatoriamente devemos herdar de Base
class Usuario(Base):

    # O atributo __tablename__ define o nome que a tabela mapeada terá no banco de dados. Se esse atributo for omitido, o nome da tabela terá o mesmo nome da classe
    __tablename__ = "usuarios"

    # Abaixo criamos os atributos da model, que serão mapeados como as colunas da tabela. A principal diferença para as versões 1.* do SQLAlchemy, é que aqui estamos utilizando recursos de type hint do Python, o que é recomendável para a versão 2.* do SQLAlchemy

    # Será criada na tabela uma coluna de nome id, do tipo int, que será chave primária e auto incremento
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    # Será criada uma coluna de nome email, do tipo varchar(100), que não aceita valores nulos
    email: Mapped[str] = mapped_column(String(100), nullable=False)

    # Será criada uma coluna de nome senha, do tipo varchar(100), que não aceita valores nulos
    senha: Mapped[str] = mapped_column(String(100), nullable=False)
