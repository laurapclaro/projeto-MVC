# instale o requirements.txt
# iniciar o alembic - python -m alembic init migrations

# gerar a migration 
# python -m alembic revision --autogenerate -m "Criar tabela usuarios"

# Como rodar o codigo:
python -m uvicorn app.main:app --reload