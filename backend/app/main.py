
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# --------------------------------------------------
# 1. Create the FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="VerwaltungsAI API",
    description=(
        "AI-assisted administrative document processing "
        "with human review and transparent audit trails."
    ),
    version="0.1.0",
)


# --------------------------------------------------
# 2. Configure CORS for local frontend development
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# --------------------------------------------------
# 3. Root endpoint
# --------------------------------------------------

@app.get("/", tags=["System"])
def root():
    return {
        "message": "Welcome to VerwaltungsAI",
        "docs": "/docs",
        "health": "/health",
    }


# --------------------------------------------------
# 4. Health-check endpoint
# --------------------------------------------------

@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "healthy",
        "service": "verwaltungsai-api",
        "version": "0.1.0",
    }


# --------------------------------------------------
# 5. API information endpoint
# --------------------------------------------------

@app.get("/api/v1", tags=["System"])
def api_information():
    return {
        "name": "VerwaltungsAI",
        "description": "AI-assisted administrative document processing",
        "version": "0.1.0",
        "decision_policy": (
            "Human review required for administrative decisions"
        ),
    }
