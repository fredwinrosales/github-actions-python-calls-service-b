from fastapi import FastAPI
import httpx

app = FastAPI()

TARGET_URL = "http://typescript-api-service"

@app.get("/comunicar")
def comunicar_con_typescript():
    try:
        respuesta = httpx.get(TARGET_URL)
        return {
            "mensaje_recibido": respuesta.json(),
            "origen": "python-api-calls-service-b",
            "destino": TARGET_URL
        }
    except Exception as e:
        return {"error": str(e)}
