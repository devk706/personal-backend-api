from datetime import datetime, timezone
from typing import Optional

from fastapi import FastAPI, Query
import psutil

app = FastAPI(title="Personal Backend API")


@app.get("/")
def root():
    return {"message": "Personal Backend API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/time")
def get_time():
    return {"server_time": datetime.now(timezone.utc).isoformat()}


@app.get("/status")
def status():
    return {
        "service": "personal-backend-api",
        "state": "online",
    }


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/search")
def search(q: str = "nothing"):
    return {"query": q}


@app.get("/greet")
def greet(
    name: str = Query(default="Guest", min_length=3),
    age: Optional[int] = Query(default=None, ge=0),
):
    if age is not None:
        return {"message": f"Hello {name}, you are {age} years old."}
    return {"message": f"Hello {name}"} 

@app.get("/system/cpu")
def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return {"cpu_usage_percent": cpu_percent}