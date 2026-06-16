# Google Docs Export Setup

FairFlow exports mitigation reports to Google Docs. For local demos with a Gmail account, use OAuth so documents are created in your own Drive. Service accounts often cannot create Docs because they do not have personal Drive storage quota.

## Recommended Local Setup: User OAuth

1. Open Google Cloud Console and select your project.
2. Enable these APIs:
   - Google Docs API
   - Google Drive API
3. Go to APIs & Services -> OAuth consent screen.
4. Configure the consent screen for External testing if needed.
5. Add your Google account as a test user.
6. Go to APIs & Services -> Credentials.
7. Click Create Credentials -> OAuth client ID.
8. Choose Desktop app.
9. Download the JSON file and save it as:

```text
backend/google_oauth_client_secret.json
```

10. Install dependencies and run the local OAuth setup script:

```bash
cd FairFlow-AI
backend/.venv/bin/pip install -r backend/requirements.txt
backend/.venv/bin/python scripts/google_docs_oauth_setup.py
```

11. Sign in with the Google account where you want exported Docs to appear.
12. The script writes:

```text
backend/google_oauth_token.json
```

Both OAuth files are ignored by git.

Use this in `backend/.env`:

```env
GOOGLE_DOCS_ENABLED=true
GOOGLE_OAUTH_TOKEN_JSON=google_oauth_token.json
GOOGLE_DOCS_PUBLIC_SHARE=true
```

## Alternative: Service Account

1. Open Google Cloud Console and select your project.
2. Enable these APIs:
   - Google Docs API
   - Google Drive API
3. Create a service account:
   - IAM & Admin -> Service Accounts -> Create service account
   - Name: `fairflow-docs-exporter`
4. Open the service account, go to Keys, and create a JSON key.
5. Save that JSON file locally as:

```text
backend/google_service_account.json
```

This file is ignored by git and should never be committed.

## Local Env

Use this in `backend/.env`:

```env
GOOGLE_DOCS_ENABLED=true
GOOGLE_SERVICE_ACCOUNT_JSON=google_service_account.json
GOOGLE_DOCS_PUBLIC_SHARE=true
```

Restart the backend after adding the file.

## Deployed Env

If the deployment platform cannot mount files, put the full JSON contents in:

```env
GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT={...full service account json...}
```

Keep `GOOGLE_DOCS_ENABLED=true`.
