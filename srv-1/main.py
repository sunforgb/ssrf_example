from fastapi import FastAPI, Request, status
import httpx
from fastapi.responses import JSONResponse, HTMLResponse
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "srv-1"}

@app.get("/external-data/", response_class=HTMLResponse)
async def fetch_external_data(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text

@app.get("/admin")
async def read_admin(request: Request):
    if request.client.host == '127.0.0.1':
        return {"admin": "password"}
    else:
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"message": "forbidden for non local users"})