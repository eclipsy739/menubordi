!pip install gspread oauth2client

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

try:
    sheet = client.open("Учебная таблица").sheet1
    data = sheet.get_all_values()
    print(data)
except gspread.SpreadsheetNotFound:
    print("Spreadsheet 'Учебная таблица' not found or not accessible by the service account.")

