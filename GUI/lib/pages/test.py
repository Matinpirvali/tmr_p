m=1
nm=0
l=0
n=0
Answer2=0
zog93=0
fard54=0
Analis=0

def i(scarf):
    print(12)
    global Answer2
    global fard54
    global zog93
    global m
    global nm
    global l
    global n
    global Analis
    if "n" in scarf:
        n=168
        l=1
        m=1
        print(4566)
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

            line_m = lines[m-1]
            line_zog93=lines[zog93-1]

            line_fard54=lines[fard54-1]


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
                m+=1
            elif scarf ==book[line_fard54]:
                print(456)
                Answer2="صحیح است"
                m+=1
                zog93+=2
                fard54+=2
            elif 1==1:
                print(456)

                import nltk
                from nltk.tokenize import word_tokenize
                from nltk.corpus import stopwords
                from nltk.stem import WordNetLemmatizer
                from sklearn.feature_extraction.text import TfidfVectorizer
                from sklearn.metrics.pairwise import cosine_similarity

                # دانلود داده‌های ضروری
                nltk.download('punkt')
                nltk.download('wordnet')
                nltk.download('stopwords')

                # تعریف توابع پردازش زبان طبیعی
                def preprocess_text(text):
                    # توکن‌بندی متن
                    tokens = word_tokenize(text.lower())

                    # حذف کلمات پرتکرار
                    stop_words = set(stopwords.words('english'))
                    tokens = [token for token in tokens if token not in stop_words]

                    # لماتیزاسیون
                    lemmatizer = WordNetLemmatizer()
                    tokens = [lemmatizer.lemmatize(token) for token in tokens]

                    return ' '.join(tokens)

                # تعریف داده‌های آموزشی
                training_data = [
                    "نظریه عمومی نسبی این است که جرم و انرژی فضا و زمان را انعطاف‌پذیر می‌کند.",
                    "نظریه داروین درباره تکامل و انتخاب طبیعی می‌باشد.",
                    "نظریه کوانتومی به تفسیر رفتار میکروسکوپی ذرات می‌پردازد."
                ]

                # پیش‌پردازش داده‌های آموزشی
                preprocessed_training_data = [preprocess_text(data) for data in training_data]

                # استخراج ویژگی‌ها با استفاده از TF-IDF
                vectorizer = TfidfVectorizer()
                tfidf_matrix = vectorizer.fit_transform(preprocessed_training_data)

                # مثالی از اجرای بات

                user_question =scarf

                # پیش‌پردازش سوال کاربر
                preprocessed_question = preprocess_text(user_question)

                # استخراج ویژگی‌های سوال کاربر با استفاده از TF-IDF
                tfidf_question = vectorizer.transform([preprocessed_question])

                # محاسبه شباهت کیسنی بین سوال کاربر و داده‌های آموزشی
                similarity_scores = cosine_similarity(tfidf_question, tfidf_matrix)[0]

                # پیدا کردن داده‌های آموزشی با بیشترین شباهت
                max_similarity_index = similarity_scores.argmax()

                # نمایش پاسخ
                if similarity_scores[max_similarity_index] > 0:
                    answer = training_data[max_similarity_index]
                    print("پاسخ: " + answer)
                else:
                    print("متأسفم، نمی‌توانم به این سوال پاسخ دهم.")

                print(4655455555555)
                if Analis==Answer2:
                    print(456556)
                    Answer2=("این هم می تواند درست باشد ولی جواب کتابی تر مساوی هست با:",Analis)
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
    scarf=input(",mmmmm")
    i(scarf)