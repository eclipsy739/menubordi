import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Настройка доступа
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Открываем таблицу и нужный лист
sheet = client.open("Учебная таблица").sheet1

# Пример данных для добавления
new_data = ["Андрей", "Запись", "2025-06-05"]

# Добавление новой строки
sheet.append_row(new_data)

print("✅ Данные успешно записаны!")