# 1- Hash e verificacao de senha com bcrypt
# 2- Geração do token JWT
# 3- Leitura e validacao do token vindo do cookie

from datetime import datetime, timedelta, timezone
from jose import JWSError, jwt
from passlib.context import CryptContext
from fastapi import Request, HTTPException, status
from dotenv import load_dotenv
import os 

#Carregar as variaveis de ambiente

load_dotenv()

SECRETY_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRACAO_MINUTOS = os.getenv("ACCESS_TOKEN_EXPIRACAO_MINUTOS")

#CryptContent
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função de senha

def hash_senha(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str):
    return pwd_context.verify(senha, senha_hash)

#Funções do token
def criar_token(data: dict):

    payload = data.copy()

    #define quando o token expira

    expira = datetime.now(timezone.utc) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRACAO_MINUTOS))
    payload.update({"exp": expira})

    #Criar o token
    token = jwt.encode(payload, SECRETY_KEY, algorithm=ALGORITHM)
    return token


def decodificar_token(token: str):
    payload = jwt.decode(token, SECRETY_KEY, algorithms=[ALGORITHM])
    return payload


#Dependencias do fastapi

def get_usuario_logado(request: Request):

    token  = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="NÃO AUTENTICADO"
        )
    try:
        payload = decodificar_token(token)
        email = payload.get("sub")

        if email is None:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalido"
        )

        return payload

    except JWSError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )
    
def get_usuario_opcional(request: Request):
    try:
        return get_usuario_logado(request)
    except HTTPException:
        return None