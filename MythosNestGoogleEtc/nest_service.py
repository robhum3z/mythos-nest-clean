from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

app = FastAPI(title="Mythos Nest", version="0.4.0")

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
TOKEN_PATH = "token.json"
CLIENT_SECRET_PATH = "client_secret.json"
NEST_FOLDER_ID = os.getenv("NEST_FOLDER_ID", "")

def get_drive_service():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    return build("drive", "v3", credentials=creds)

@app.get("/health")
def health():
    return {"status": "nest-ok"}

@app.get("/index")
def list_docs():
    """List all PDFs in the specified Nest folder."""
    try:
        service = get_drive_service()
        query = f"'{NEST_FOLDER_ID}' in parents and mimeType='application/pdf' and trashed=false"
        results = service.files().list(q=query, fields="files(id, name)").execute()
        files = results.get("files", [])
        return {"docs_indexed": len(files), "files": files}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/search")
def search_docs(q: str = Query(..., description="Search query text")):
    """Search for PDFs by filename within the Nest folder."""
    try:
        service = get_drive_service()
        query = f"'{NEST_FOLDER_ID}' in parents and name contains '{q}' and mimeType='application/pdf' and trashed=false"
        results = service.files().list(q=query, fields="files(id, name)").execute()
        files = results.get("files", [])
        return {"query": q, "results": files, "count": len(files)}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
