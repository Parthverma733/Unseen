from fastapi import FastAPI

app = FastAPI(title="Hidden Destination API")


@app.get("/")
def root():
    return {"message": "Hidden Destination API running"}


@app.get("/health")
def health():
    return {"status": "ok"}