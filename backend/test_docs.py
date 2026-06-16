import sys
import os
sys.path.append(os.getcwd())
from google_docs_service import get_google_services
from googleapiclient.errors import HttpError
try:
    docs, drive, err = get_google_services()
    if err:
        print("Error getting services:", err)
    else:
        print("Got services!")
        try:
            doc = docs.documents().create(body={"title": "Test FairFlow Doc"}).execute()
            print("Created doc successfully:", doc["documentId"])
        except HttpError as e:
            print("HttpError creating doc:")
            print(e.content.decode('utf-8'))
        except Exception as e:
            print("Other error:", e)
except Exception as e:
    print("Failed:", e)
