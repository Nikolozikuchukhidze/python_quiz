import requests
import json
import sqlite3

res = requests.get("https://jsonplaceholder.typicode.com/posts")

data = res.json()

#  1
status_code = res.status_code
text = res.text
headers = res.headers

print(status_code, headers, text)


# 2
with open("postebi.json", "w") as file:
    json.dump(data, file, indent=2)


# 3
for i in data:
    print(i["title"] + "\n" + i["body"] + "\n")


# 4
conn = sqlite3.connect("postebi.sqlite3")
cursor = conn.cursor()

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY, AUTOINCREMENT,
            userId INTEGER,
            title VARCHAR(255),
            body TEXT
) """
)

axali_data = []
for i in data:
    axali_data.append((i["userId"], i["title"], i["body"]))

cursor.executemany(
    "INSERT INTO posts (userId, title, body) VALUES (?, ?, ?)", axali_data
)
conn.commit()