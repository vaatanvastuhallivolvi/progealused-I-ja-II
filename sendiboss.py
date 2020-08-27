print("Kui soovite avaldada, siis palju on Teil eurosente: ")
sendid = int(input())

mündiäss = sendid // 100
jääk = sendid % 100

if sendid == 100:
    print("1 euro")
elif sendid > 1 and jääk == 0:
    print(str(mündiäss) + " eurot ")
elif sendid == 1:
    print("1 sent")
elif sendid < 100 and sendid > 1:
    print(str(sendid) + " senti")
elif sendid < 199 and sendid > 99 and jääk < 2:
    print(str(mündiäss) + " euro ja " + "1 sent")
elif sendid > 199 and jääk < 2:
    print(str(mündiäss) + " eurot ja " + "1 sent")
elif sendid > 199 and jääk > 1:
    print(str(mündiäss) + " eurot ja " + str(jääk) + " senti")
elif sendid < 200 and sendid > 99:
    print(str(mündiäss) + " euro ja " + str(jääk) + " senti")
else:
    print("Oled rahatu õilishing.")