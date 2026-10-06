from fastapi import FastAPI

app = FastAPI(title="VISIONPAY API")


@app.get("/")
def root():
    return {"message": "VISIONPAY Backend is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}