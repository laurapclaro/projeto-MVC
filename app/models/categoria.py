#Tabels de categorias
from  sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
from sqlalchemy.orm import relationship

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    ativo = Column(Boolean, default=True)

    # Relacionamento
    # lazy="select" - Carrega os produtos relacionados somente quando necessário (lazy loading)
    produtos = relationship("Produto", back_populates="categoria", lazy="select")
    