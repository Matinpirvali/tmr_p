m=1
nm=0
l=0
n=0
Answer2=0
zog93=0
fard54=0
from matras import Analis
def i(scarf):
    print(12)
    global Answer2
    global fard54
    global zog93
    global m
    global nm
    global l
    global n
    if "n" in scarf:
        n=168
        l=1
        m=1
        zog93 = 2
        fard54 = 1
    if n==168:
        print(n)
        if m==21:
            print(nm)
            l=0

        if l!=0:
            print(45)
            # باز کردن فایل و خواندن خط‌ها
            with open('information.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # استخراج خط دوم (در صورت وجود)
            if len(lines) >= 2:
                line_m = lines[m-1]
                line_zog93=lines[zog93-1]

                line_fard54=lines[fard54-1]

            else:
                line2 = "خط دوم در فایل وجود ندارد."
            book={
                line_fard54:line_zog93
            }


            my_list=["فرضیه چیست","کاوشگری چیست","نظریه چیست"]
            Answer2=line_m
            print(Answer2)
            nm+=1
            if nm%2!=0:
                print(44)
                kl=1+8
            elif scarf ==book[line_fard54]:
                print(456)
                Answer2="صحیح است"
                m+=1
                zog93+=2
                fard54+=2
            elif 1==1:
                print(456)

                Analis(scarf)
                print(4655455555555)
                if Analis==Answer2:
                    print(456556)
                    Answer2=("این هم می تواند درست باشد ولی جواب کتابی تر مساوی هست با:",Answer2)
                    nm+=1
                    zog93 += 2
                    fard54 += 2
                else:
                    print(555555555)
                    Answer2=("نادرست دوست عزیز,جواب درست :",Answer2)
                    m+=1
                    zog93 += 2
                    fard54 += 2
            print(Answer2)
while True:
    print("hk")
    scarf=input("")
    i(scarf)