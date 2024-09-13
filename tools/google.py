# References
# https://developers.google.com/calendar/api/quickstart/python?hl=it

import datetime
import os.path
from langchain.agents import Tool
from langchain_core.tools import tool
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

TOKEN_PATH=r"C:\Users\ELAFACRB1\Codice\GitHub\langchain-rag-agent-chatbot\creds\token.json"
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
now=datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time

@tool
def get_calendar_events(num_events: int) -> dict:
    """Prende gli ultimi n eventi da Google Calendar

    Args:
        num_events: numero di eventi da ritornare
    """
    creds=None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
        service = build("calendar", "v3", credentials=creds)
        events_result = (
                service.events()
                .list(
                    calendarId="primary",
                    timeMin=now,
                    maxResults=num_events,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
        events = events_result.get("items", [])
        return events
