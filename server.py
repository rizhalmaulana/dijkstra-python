# Import untuk membuat server
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Import algoritma
from main import fetchAllNodes, shortestPath, shortestPathtoAllNode, checkDistanceMap

# Inisialisasi server
app = FastAPI()

# Mengatur supaya server bisa diakses dari mana saja
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Daftar URL dari server
@app.get("/list")
def list():
    return fetchAllNodes()

@app.get("/path")
def shortest_path(start: int, end: int):
    return shortestPath(start, end)

@app.get("/distance")
def check_distance(start: int, end: int):
    return checkDistanceMap(start, end)

@app.get("/dinsos")
def dinsos():
    return shortestPathtoAllNode()

if __name__ == '__main__':
    uvicorn.run(app, host="192.168.32.228", port=8005)