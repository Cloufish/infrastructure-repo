from fastapi import FastAPI
import torch

app = FastAPI()

@app.get("/gpu-test")
def gpu_test():
    if not torch.cuda.is_available():
        return {"error": "No GPU available"}
    
    return {"gpu": torch.cuda.get_device_name(0)}

# Run it with command: uvicorn main:app --host 0.0.0.0 --port 8000
# TODO: Develop this script for n8n use
