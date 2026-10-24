import sqlite3
import uuid

customer = {
    "uid" : str(uuid.uuid4()),
    "nickname" : input("ニックネームを入力してください：").strip(),
    "birthday" : input("生年月日を入力してください：").strip()
}

connection = sqlite3.connect("customers.db")
connection.execute("""
CREATE TABLE IF NOT EXISTS customers(
    uid TEXT PRIMARY KEY NOT NULL,
    nickname TEXT NOT NULL,
    birthday TEXT NOT NULL
)
""")

if customer["nickname"] == "":
    print ("⚠️エラー：ニックネームは必須です！")
else:
    connection.execute(
        "INSERT INTO customers (uid, nickname,birthday) VALUES(?, ?, ?)",
        (customer["uid"], customer["nickname"], customer["birthday"])
    )
    connection.commit()
    columns = connection.execute("PRAGMA table_info(customers)").fetchall()

    print ("=== 顧客登録システム ===")
    nicknames = connection.execute(
         "SELECT nickname FROM customers"
    ).fetchall()
    print("ニックネーム：", nicknames)
    birth_date = connection.execute(
        "SELECT birthday FROM customers"
    ).fetchall()
    print("生年月日：", birth_date)
    print("登録完了！")

connection.close()