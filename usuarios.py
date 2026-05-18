from app.database import Session, engine, Base
from app.models.usuario import Usuario
from app.auth import hash_senha

usuarios = [
    {
        "nome": "admin",
        "email": "admin@teste.com",
        "senha": "admin@1234",
        "role": "admin"
    },
    {
        "nome": "Gabriel",
        "email": "gabriel@teste.com",
        "senha": "admin@1234",
        "role": "admin"
    }

]
def criar_usuario():
    db = Session()

    try:
        for usuario in usuarios:
            existente = db.query(Usuario).filter_by(email=usuario["email"]).first()

            if existente:
                print(f"Já existe esse email: {usuario["email"]} no banco.")
                continue
            else:
                novo_usuario = Usuario(
                    nome = usuario["nome"],
                    email = usuario["email"],
                    senha_hash = hash_senha(usuario["senha"]),
                    role = usuario["role"],


                )
                db.add(novo_usuario)

        db.commit()
        print(F"Usuarios cadastrados com sucesso!")
        
    except Exception as erro:
        db.rollback()
        print(erro)
    finally:
        db.close()

criar_usuario()