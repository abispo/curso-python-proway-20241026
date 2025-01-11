from datetime import date
from typing import List

from sqlalchemy import Integer, String, ForeignKey, Date, Text, Column, Table, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import Base

import datetime

postagens_categorias = Table(
    "postagens_categorias",
    Base.metadata,
    Column("postagem_id", ForeignKey("postagens.id"), primary_key=True),
    Column("categoria_id", ForeignKey("categorias.id"), primary_key=True)
)

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

    # Abaixo criamos um atributo do tipo relationship. Esse tipo de atributo serve para carregar automaticamente o(s) objeto(s) relacionado(s) a essa model. Nesse caso, o atributo perfil vai carregar o objeto Perfil associado ao objeto Usuario.
    perfil: Mapped["Perfil"] = relationship(back_populates="usuario")

    # O parâmetro uselist=True indica que esse atributo irá retornar uma lista de objetos Perfil associados ao objeto Usuario atual. Caso o usuário não tenha feito postagens, será retornada uma lista vazia.
    postagens: Mapped["Postagem"] = relationship(back_populates="usuario", uselist=True)

    def __repr__(self) -> str:
        return f"<Usuario {self.email}>"


class Perfil(Base):

    __tablename__ = "perfis"

    id: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    sobrenome: Mapped[str] = mapped_column(String(100), nullable=False)
    data_de_nascimento: Mapped[date] = mapped_column(Date, nullable=True)

    criado_em: Mapped[DateTime] = mapped_column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC)
    )
    atualizado_em: Mapped[DateTime] = mapped_column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC)
    )

    usuario: Mapped["Usuario"] = relationship(back_populates="perfil")

    def __repr__(self) -> str:
        return f"<Perfil '{self.nome} {self.sobrenome}'>"


class Postagem(Base):

    __tablename__ = "postagens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    usuario_id: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"), nullable=False)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    texto: Mapped[str] = mapped_column(Text, nullable=False)
    
    usuario: Mapped["Usuario"] = relationship(back_populates="postagens")

    categorias: Mapped[List["Categoria"]] = relationship(secondary=postagens_categorias, back_populates="postagens")

    def __repr__(self):
        return f"<Postagem({self.id}) '{self.titulo}'>"
    

class Categoria(Base):

    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    postagens: Mapped[List["Postagem"]] = relationship(secondary=postagens_categorias, back_populates="categorias")

    def __repr__(self):
        return f"<Categoria({self.id}) '{self.nome}'>"