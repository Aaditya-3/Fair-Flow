from __future__ import annotations

from pathlib import Path
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
]


ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
CLIENT_SECRETS = BACKEND / "google_oauth_client_secret.json"
TOKEN = BACKEND / "google_oauth_token.json"


def main() -> None:
    if not CLIENT_SECRETS.exists():
        raise SystemExit(
            "Missing backend/google_oauth_client_secret.json. "
            "Download an OAuth Desktop client JSON from Google Cloud and place it there."
        )

    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRETS), SCOPES)
    callback: dict[str, str] = {}

    def app(environ, start_response):
        params = parse_qs(environ.get("QUERY_STRING", ""))
        if "code" in params:
            callback["code"] = params["code"][0]
            body = b"FairFlow Google Docs authorization complete. You can close this tab."
            start_response("200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(body)))])
            return [body]
        callback["error"] = params.get("error", ["Missing OAuth code"])[0]
        body = f"FairFlow authorization failed: {callback['error']}".encode("utf-8")
        start_response("400 Bad Request", [("Content-Type", "text/plain"), ("Content-Length", str(len(body)))])
        return [body]

    with make_server("127.0.0.1", 0, app) as server:
        port = server.server_port
        flow.redirect_uri = f"http://localhost:{port}/"
        auth_url, _ = flow.authorization_url(
            access_type="offline",
            include_granted_scopes="true",
            prompt="consent",
        )
        print("Open this URL to authorize FairFlow Google Docs export:", flush=True)
        print(auth_url, flush=True)
        while "code" not in callback and "error" not in callback:
            server.handle_request()

    if "error" in callback:
        raise SystemExit(callback["error"])

    flow.fetch_token(code=callback["code"])
    credentials = flow.credentials
    TOKEN.write_text(credentials.to_json(), encoding="utf-8")
    print(f"Saved OAuth token to {TOKEN}")


if __name__ == "__main__":
    main()
