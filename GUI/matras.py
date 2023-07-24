Analis=0
def Analis(scarf):
    global Analis
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    from test import Answer2
    # دانلود داده‌های ضروری
    print(45)
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('stopwords')

    print(44454)
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
        "سوال کردن و تلاش برای یافتن جواب، مهمترین نکته در علم است",
        " دانشی است که از طریق کنجکاوری و با روش های کسب تجربه، آزمایش و حواس پنجگانه بدست می آید",
        "سد کرخه، بزرگترین سد خاکی – رسی خاورمیانه شش داروی جدید زیست فناوری ایرانی پهپاد پرنده هدایت پذیر از راه دور (ساخت ایران) بنیانا اولین گوساله شبیه سازی شده در خاورمیانه"
    ]

    # پیش‌پردازش داده‌های آموزشی
    preprocessed_training_data = [preprocess_text(data) for data in training_data]

    # استخراج ویژگی‌ها با استفاده از TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_training_data)

    # مثالی از اجرای بات



    # پیش‌پردازش سوال کاربر
    preprocessed_question = preprocess_text(scarf)

    # استخراج ویژگی‌های سوال کاربر با استفاده از TF-IDF
    tfidf_question = vectorizer.transform([preprocessed_question])

    # محاسبه شباهت کیسنی بین سوال کاربر و داده‌های آموزشی
    similarity_scores = cosine_similarity(tfidf_question, tfidf_matrix)[0]

    # پیدا کردن داده‌های آموزشی با بیشترین شباهت
    max_similarity_index = similarity_scores.argmax()

    # نمایش پاسخ
    if similarity_scores[max_similarity_index] > 0:
        Analis= training_data[max_similarity_index]
        print("پاسخ: " + Analis)

    else:
        print("متأسفم، نمی‌توانم به این سوال پاسخ دهم.")
