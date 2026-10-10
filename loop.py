count = 1
subject_count = int(input("今日の勉強した科目数を教えて！："))
total = 0

while count <= subject_count:
    subject = input("勉強した科目は？：")   
    minute = int(input(f"{count}回目の勉強時間は何分？"))
    total = minute + total
    count = count + 1

print("合計勉強時間：", total, "分")   