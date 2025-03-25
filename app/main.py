from fastapi import FastAPI
import httpx

app = FastAPI()

TARGET_URL = "http://10.43.127.150"

@app.get("/comunicar")
def comunicar_con_typescript():
    try:
        respuesta = httpx.get(TARGET_URL)
        return {
            "mensaje_recibido": respuesta.json(),
            "origen": "Microservicio A (Python)"
        }
    except Exception as e:
        return {"error": str(e)}
