#!/usr/bin/python

from fastapi import FastAPI
from routers import dragonball, dragonballz, dragonballgt, dragonballsuper, dragons
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=[""],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Rouuters
app.include_router(dragonball.router)
app.include_router(dragonballz.router)
app.include_router(dragonballgt.router)
app.include_router(dragonballsuper.router)
app.include_router(dragons.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    html_address = "./static/public/index.html"
    return FileResponse(html_address,status_code=200)

@app.get("/documentacion", response_class=HTMLResponse)
async def root():
    html_address = "./static/public/documentacion.html"
    return FileResponse(html_address,status_code=200)
    
@app.get("/url")
async def url():
    return {"Gracias":"Por usar esta api"}

#Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc