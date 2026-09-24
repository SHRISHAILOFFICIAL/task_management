from fastapi import FastAPI

app =FastAPI(
    title="My FastAPI Application",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to my FastAPI application!"
    }

# app.listen(8003);