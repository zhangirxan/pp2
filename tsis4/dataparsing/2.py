from datetime import datetime, timedelta

a = datetime.now()
print(f"yesterday: {a - timedelta(days=1)}")
print(f"today: {a}")
print(f"tommorow: {a + timedelta(days=1)}")