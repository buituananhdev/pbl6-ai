from fastapi import FastAPI, Request, Body
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.recommendations import get_recommendations_fuzzy

app = FastAPI(
    title="PBL6",
    debug=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/v1", include_in_schema=False)
async def healthcheck(request: Request) -> JSONResponse:
    return JSONResponse(content={"status": "ok"})

@app.post("/v1/recommendations", include_in_schema=False)
async def get_movie_recommendations(request: Request, title: str = Body(...)) -> JSONResponse:
    result = get_recommendations_fuzzy(title)
    return JSONResponse(content=result)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
