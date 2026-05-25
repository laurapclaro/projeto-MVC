# Tabela de produtos AAPM
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200), unique=True, index=True)
    descricao = Column(String)
    preco = Column(Float, nullable=False, default=0.0)
    estoque_atual = Column(Integer, nullable=False, default=0)
    ativo = Column(Boolean, default=True)

    # Relacionamento
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="produtos")

    imagem_path = Column(String(255), nullable=True)

    categoria_id = Column(Integer, ForeignKey("categorias.id", ondelete="SET NULL"), nullable=True)
    categoria = relationship("Categoria", back_populates="produtos")

    #metodo
    @property
    def imagem_url(self):
        if self.imagem_path:
            return f"/static/imagens/{self.imagem_path}"
        else:
            return "/static/img/produto-placeholder.png"