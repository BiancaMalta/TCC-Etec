from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .routes.movieRoutes import router as movieRoutes
from .routes.avaliacoesRoutes import router as avaliacoesRoutes  # Importe a nova rota

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}

# Inclui as rotas de filmes
app.include_router(movieRoutes, prefix="/api")
# Inclui as rotas de avaliações
app.include_router(avaliacoesRoutes, prefix="/api/avaliacoes")

# Função para configurar o tratamento de erros
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "An error occurred.", "detail": str(exc)},
    )

# Rodar a aplicação com: uvicorn api.main:app --reload
