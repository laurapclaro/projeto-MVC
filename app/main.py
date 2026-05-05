from fastapi import FastAPI, Request, Depends, 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI(title="Sistema Estoque")

#Configurar o fastapi para servir os arquivos estaticos (CSS, JS, Imagens)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

#Incluie os routers dos controles

app.include_router(auth_controller.router)
