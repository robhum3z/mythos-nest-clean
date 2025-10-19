from __future__ import print_function
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

CLIENT_FILE = "client_secret.json"   # same file you just downloaded
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
creds = flow.run_local_server(port=0)

with open("token.json", "w") as f:
    f.write(creds.to_json())

print("\n✅ Token saved as token.json — open it and copy the JSON into Render as NEST_TOKEN_JSON.")
