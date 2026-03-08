import pymongo 
from datetime import datetime, timedelta
import random

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["funel_db"]["lead_events"]
db.delete_many({})

stages = ["Lead", "Qualified", "Approved", "Converted"]
print("Seeding data spread across the last 30 days...")
for _ in range(500):
    l_id = f"UID-{random.randint(1000, 9999)}"
    random_days_ago = random.randint(0, 30)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    timestamp = datetime.now() - timedelta(days=random_days_ago)
    timestamp = timestamp.replace(hour=random_hour, minute=random_minute)
    depth = random.choices([0, 1, 2, 3], weights=[40, 30, 20, 10])[0]
    for i in range(depth + 1):
        db.insert_one({
            "lead_id": l_id, 
            "stage": stages[i], 
            "timestamp": timestamp
        })
print(f"Successfully seeded 500 leads in 'funel_db'.")