subject = input("今日の勉強科目は？：")
minute = int(input("勉強時間は何分？："))
yesterday = int(input("昨日の勉強時間は何分？："))

total = minute + yesterday

print("今日の勉強科目：", subject)
print("勉強時間：", minute, "分")
print("昨日の勉強時間：", yesterday, "分")
print("合計勉強時間：", total, "分")

if total >= 60:
    print("目標達成！🎉")
elif total >= 30:
    print("あと少し！💪")
else:
    print("まずは30分をめざそう！🌱")