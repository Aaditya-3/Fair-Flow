import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
]

def main():
    if not os.path.exists("google_oauth_client_secret.json"):
        print("Error: google_oauth_client_secret.json not found in backend directory.")
        return

    flow = InstalledAppFlow.from_client_secrets_file(
        "google_oauth_client_secret.json", SCOPES
    )
    creds = flow.run_local_server(port=0)

    with open("google_oauth_token.json", "w") as token:
        token.write(creds.to_json())
    
    print("\nSUCCESS! Saved google_oauth_token.json.")
    print("You can now export Google Docs from the FairFlow AI frontend!")

if __name__ == "__main__":
    main()
