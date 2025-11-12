import schedule
import time
import os

def organizar():
    os.system("uv run movendo.py")

schedule.every().day.at("08:12").do(organizar)

while True:
    schedule.run_pending()
    time.sleep(60)
