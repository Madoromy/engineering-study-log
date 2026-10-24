from datetime import date

customer = {
    "nickname" : input("ニックネームを入力してください：").strip(),
    "birthday" : str(input("生年月日をYYYY-MM-DDの形で入力してください：").strip())
}

if customer["nickname"] == "":
    print("ニックネームの入力は必須です！")

else:
    print("=== 登録内容 ===")
    print("ニックネーム：", customer["nickname"])
    print("生年月日：", customer["birthday"])
    print("登録完了！")