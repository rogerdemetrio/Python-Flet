from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///bancoCadastro.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Tabela Produto
class Produto(Base):
    __tablename__ = "tbproduto"
    id = Column(Integer, primary_key=True)
    nm_prod = Column(String(50))
    vl_prod = Column(Float())
    desc_prod = Column(String(100))
    marca = Column(String(50))

# Tabela Pessoa
class Pessoa(Base):
    __tablename__ = "tbpessoa"
    id = Column(Integer, primary_key=True)
    nm_pessoa = Column(String(50))
    sob_pessoa = Column(String(100))

# Tabela Pesquisa
class Pesquisa(Base):
    __tablename__ = "tbpesquisa"
    id = Column(Integer, primary_key=True)
    nome_conc = Column(String(50))
    vl_conc = Column(Float())
    marca_conc = Column(String(50))
    dias_conc = Column(String(50))
    obs = Column(String(200))

Base.metadata.create_all(engine)