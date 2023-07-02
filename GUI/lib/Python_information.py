from tkinter import ttk
from tkinter import *
from customtkinter import *

def science(scarf):
    print(1)
    Answer = 0
    Answer2 = 0
    global n
    if "back" == scarf or "Back" == scarf:
        n= 0

    if n==0:
        ##################################درس شش انگلیسی صفحه 96 نهم#######################################
        if "هشتم" in scarf and "درس" in scarf and "شش" in scarf and "انگلیسي" in scarf and "صفحه" in scarf and "96" in scarf or ("هشتم" and "درس" and "شش" and "انگلیسی" and "صفحه" and "نود و شش") in scarf or ("هشتم" and "درس" and "6" and "انگلیسی" and "صفحه" and "96") in scarf:
            Answer2="نقش شما رضا هست(Reza)"
            n=149
        ###################################درس پنج انگلیسی صفحه 82 نهم########################################
        if "هشتم" in scarf and "درس" in scarf and "پنج" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "82" in scarf or ("هشتم" and "درس" and "پنج" and "انگلیسی" and "صفحه" and "هشتاد و دو") in scarf or ("هشتم" and "درس" and "5" and "انگلیسی" and "صفحه" and "82") in scarf:
            Answer2="نقش شما مهسا هست(Mahsa)"
            n=140
        ############################################درس چهار انگلیسی صفحه 64 نهم########################################
        if "هشتم" in scarf and "درس" in scarf and "چهار" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "64" in scarf or ("هشتم" and "درس" and "چهار" and "انگلیسی" and "صفحه" and "شصت و چهار") in scarf or ("هشتم" and "درس" and "4" and "انگلیسی" and "صفحه" and "64") in scarf:
            Answer2="شما نقش پدرام را دارید (Pedram)"
            n=131
        ##############################درس سه انگلیسی صفحه 50 نهم######################################
        if "هشتم" in scarf and "درس" in scarf and "سه" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "50" in scarf or ("هشتم" and "درس" and "سه" and "انگلیسی" and "صفحه" and "پنجاه") in scarf or ("هشتم" and "درس" and "3" and "انگلیسی" and "صفحه" and "50") in scarf:
            Answer2="نقش شما نسرین هست(Nasrin)"
            n=123
        ############################################درس دو انگلیسی صفحه 30 نهم#######################################
        if "هشتم" in scarf and "درس" in scarf and "دو" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "30" in scarf or ("هشتم" and "درس" and "دو" and "انگلیسی" and "صفحه" and "سی") in scarf or ("هشتم" and "درس" and "2" and "انگلیسی" and "صفحه" and "30") in scarf:
            Answer2="نقش شما رکپشن هست(Receptionist)"
            n=116
        ##################################درس یک انگلیسی صفحه 18 نهم#######################################
        if "هشتم" in scarf and "درس" in scarf and "یک" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "16" in scarf or ("هشتم" and "درس" and "یک" and "انگلیسی" and "صفحه" and "هجدهم") in scarf or ("هشتم" and "درس" and "1" and "انگلیسی" and "صفحه" and "18") in scarf:
            Answer2="نقش شما احسان هست(Ehsan)"
            n=108
        #
        ##############################درس هفت انگلیسی صفحه 54 هشتم#######################################
        if "هشتم" in scarf and "درس" in scarf and "هفت" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "54" in scarf or ("هشتم" and "درس" and "هفت" and "انگلیسی" and "صفحه" and "پنجاه و چهار") in scarf or ("هشتم" and "درس" and "7" and "انگلیسی" and "صفحه" and "54") in scarf:
            Answer2="شما نقش زهرا را دارید"
            n=48
        ###################################درس شش انگلیسی صفحه 48 هشتم#######################################
        if "هشتم" in scarf and "درس" in scarf and "شش" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "48" in scarf or ("هشتم" and "درس" and "شش" and "انگلیسی" and "صفحه" and "چهل و هشت") in scarf or ("هشتم" and "درس" and "6" and "انگلیسی" and "صفحه" and "48") in scarf:
            Answer2="شما نقش حمید را دارید(Hamid)"
            n=56
        ##################################درس پنج انگلیسی صفحه 42 هشتم########################################
        if "هشتم" in scarf and "درس" in scarf and "پنج" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "42" in scarf or ("هشتم" and "درس" and "پنج" and "انگلیسی" and "صفحه" and "چهل و دو") in scarf or ("هشتم" and "درس" and "5" and "انگلیسی" and "صفحه" and "42") in scarf:
            Answer2="نقش شما مرتضی ست (Morteza)"
            n=67
        #################################درس چهار انگلیسی صفحه 34 هشت########################################
        if "هشتم" in scarf and "درس" in scarf and "چهار" "" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "34" in scarf or ("هشتم" and "درس" and "چهار" and "انگلیسی" and "صفحه" and "سی و چهار") in scarf or ("هشتم" and "درس" and "4" and "انگلیسی" and "صفحه" and "34") in scarf:
            Answer2="نقش شما دانش آموز هست(Student)"
            n=77
        ###############################درس سه انگلیسی صفحه 26 هشتم########################################
        if "هشتم" in scarf and "درس" in scarf and "سه" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "26" in scarf or ("هشتم" and "درس" and "سه" and "انگلیسی" and "صفحه" and "بیست و شش") in scarf or ("هشتم" and "درس" and "3" and "انگلیسی" and "صفحه" and "26") in scarf:
            Answer2="نقش شما سارا است (sara)"
            n=84
        ##########################درس دو انگلیسی صفحه 18 هشتم########################################
        if "هشتم" in scarf and "درس" in scarf and "دو" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "18" in scarf or ("هشتم" and "درس" and "دو" and "انگلیسی" and "صفحه" and "هجده") in scarf or ("هشتم" and "درس" and "2" and "انگلیسی" and "صفحه" and "18") in scarf:
            Answer2="نقش شما معلم هست (Teacher)"
            n=92
        ###############################درس یک انگلیسی صفحه 12 هشتم########################################
        if "هشتم" in scarf and "درس" in scarf and "یک" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "12" in scarf or ("هشتم" and "درس" and "یک" and "انگلیسی" and "صفحه" and "دوازده") in scarf or ("هشتم" and "درس" and "1" and "انگلیسی" and "صفحه" and "12") in scarf:
            Answer="نقش شما سام هست (sam)"
            n=101
        #############################درس هشت انگلیسی صفحه 42 هفتم########################################
        elif "هفتم" in scarf and "درس" in scarf and "هشت" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "42" in scarf or ("هفتم" and "درس" and "هشت" and "انگلیسی" and "صفحه" and "چهل و دو") in scarf or ("هفتم" and "درس" and "8" and "انگلیسی" and "صفحه" and "42") in scarf:
            Answer2="Lok,it`s enough.I`m hungry.How about you."
            n=45
        ####################################درس هفت انگلیسی صفحه38#######################################
        if "هفتم" in scarf and "درس" in scarf and "هفت" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "38" in scarf or ("هفتم" and "درس" and "هفت" and "انگلیسی" and "صفحه" and "سی و هشت") in scarf or ("هفتم" and "هفت" and "7" and "انگلیسی" and "صفحه" and "38") in scarf:
            Answer2="Ali`s not well.I`m going to visit him today.Are you coming with me?"
            n=39
        #########################پرسش درس شش انگلیسی صفحه 32 هفتم#######################################
        if "هفتم" in scarf and "درس" in scarf and "شش" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "32" in scarf or ("هفتم" and "درس" and "شش" and "انگلیسی" and "صفحه" and "سی و دو") in scarf or ("هفتم" and "درس" and "6" and "انگلیسی" and "صفحه" and "32") in scarf:
            Answer2="Mom,where are you?"
            n=33
        ###############################پرسش درس پنج انگلیسی 5 صفحه 28 هفتم#######################################
        if "هفتم" in scarf and "درس" in scarf and "پنج" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "28" in scarf or ("هفتم" and "درس" and "پنج" and "انگلیسی" and "صفحه" and "بیست و هشت") in scarf or ("هفتم" and "درس" and "5" and "انگلیسی" and "صفحه" and "28") in scarf:
            Answer2="Is that your English theacher?"
            n=29
        ######################پرسش درس یک انگلیسی صفحه 8 هفتم ######################################
        if "هفتم" in scarf and "درس" in scarf and "یک" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "8" in scarf or ("هفتم" and "درس" and "یک" and "انگلیسی" and "صفحه" and "هشت") in scarf or ("هفتم" and "درس" and "1" and "انگلیسی" and "صفحه" and "8") in scarf:
            Answer2="Hi,class!"
            n=23
        #######################پرسش درس دو انگلیسی صفحه 10 هفتم#####################################
        if "هفتم" in scarf and "درس" in scarf and "دو" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "10" in scarf or ("هفتم" and "درس" and "دو" and "انگلیسی" and "صفحه" and "ده") in scarf or ("هفتم" and "درس" and "2" and "انگلیسی" and "صفحه" and "10") in scarf:
            Answer2= "Who is that boy?"
            n=16
        ######################################پرسش درس سه انگیلیسی صفحه 16 هفتم######################
        if "هفتم" in scarf and "درس" in scarf and "سه" in scarf and "انگلیسی" in scarf and "صفحه" in scarf and "16" in scarf or ("هفتم" and "درس" and "سه" and "انگلیسی" and "صفحه" and "شانزده") in scarf or ("هفتم" and "درس" and "3" and "انگلیسی" and "صفحه" and "16") in scarf:
            Answer2="Nargess,when is your birthday?"
            n=12

        ##################### پرسش درس چهار انگلیسی هفتم صفحه 22##############
        elif "هفتم" in scarf and "درس" in scarf and "چهار" in scarf and "انگلیسي" in scarf and "صفحه" in scarf and "22" in scarf or ("هفتم"and "درس" and "چهار" and "انگلیسی" and "صفحه" and "بیست و دو") in scarf or ("هفتم" and "درس" and "4" and "انگلیسی" and "صفحه" and "22") in scarf:
            Answer2= "Nice picture! Is that your father?"
            n = 4

        #######################################سوال درس یک علوم هفتم#################################

        elif ("درس" and "یک" and "علوم" and "هفتم") in scarf or ("درس" and "1" and "علوم" and "هفتم") in scarf:
            Answer2="بهترین راه مطالعه ی درستی یا نادرستی پیش بینی, طراحی و انجام ..... و برسی نتایج آن است"
            n=9
    elif n !=0:
        #######################################ادامه درس ها###############
        if n ==4:
            #شروع درس چهار#####################
            if ("Yes, he is."or "Yes, he`s.") != scarf:
                Answer="Yes, he is."
            n=n+1
        elif n==5:
            Answer2="How old is he?"
            n=n+1
        elif n==6:
            if "38." != scarf:
                Answer='38.'
            n=n+1
        elif n==7:
            Answer2="What`s his jop?"
            n=n+1
        elif n==8:
            if ("He`s a mechanic." or "He is a mechanic.") != scarf:
                Answer="He`s a mechanic."
            n=n+1
        elif n==9:
            Answer2="And your mother?"
            n=n+1
        elif n==10:
            if (("She`s 35, She is a houswife.") or ("She is 35, She is a housewife.") or ("She is 35, She`s a housewife.")) != scarf:
                Answer="She`s 35. She is a housewife."
            n=0
            ####################################پایان درس چهار انگلیسی صفحه 22################################
        elif n==12:
            if "It`s in Mehr." !=scarf or "It is in Mehr." != scarf:
                Answer="It`s in Mehr."
            n=n+1
        elif n==13:
            Answer2="Really? How old are you now?"
            n=n+1
        elif n==14:
            if ("I`m 12." or "I am 12.") !=scarf:
                Answer="I`m 12."
            n=n+1
        elif n==15:
            Answer2="What about you, Tahereh?"
            n=0
            ########################################پایان درس سه انگلیسی صفحه 16##################################

        elif n==16:
            if ("That`s Erfan. He`s our new classmate."or "That`s Erfan. He is our new classmate." or "That is Erfan. He`s our new classmate." or "That is Erfan. He is our new classmate.") != scarf:
                Answer="That`s Erfan. He`s our new classmate."
            n=n+1
        elif n==17:
            Answer2="Let`s talk to him."
            n=n+1
        elif n==18:
            if "Hi, Erfan. This is Ali." !=scarf:
                Answer="Hi, Erfan. This is Ali."
            n=n+1
        elif n==19:
            Answer2="Nice to meet you, Erfan."
            n=n+1
        elif n==20:
            if "Nice to meet you, too." !=scarf:
                Answer="Nice to meet you, too."
            n=n+1
        elif n==21:
            Answer2="Welcom to our school."
            n=n+1
        elif n==22:
            if "Thank you." !=scarf:
                Answer="Thank you."
            n=0
            #####################################پایان درس دو انگلیسی صفحه 10 هفتم#################################
        elif n==23:
            if "Hello, Teacher." != scarf:
                Answer = "Hello, Teacher."
            n = n + 1
        elif n==24:
            Answer2 = "Thank you, sit down, please. I`m your English teacher. My name is Ahmad Karimi. now, you tell me your names. What`s your name?"
            n = n + 1
        elif n == 25:
            if "My name is Ali Mohammadi." != scarf:
                Answer = "My name is Ali mohammadi."
            n = n + 1
        elif n == 26:
            Answer2 = "How are you, Ali?"
            n = n + 1
        elif n == 27:
            if "Fine, thank you." != scarf:
                Answer = "Fine, thank you."
            n = n + 1
        elif n == 28:
            Answer2 = "And what`s your name?"
            n = 0
        ###################################پایان درس یک انگلیسی صفحه 6 هفتم #########################################
        elif n == 29:
            if ("No, my English teacher is the tall man. He`s wearing a gray suit. He`s over there." or "No, my English teacher is the tall man. He is wearing a gray suit. He`s over there." or "No, my English teacher is the tall man. He`s wearing a gray suit. He is over there." or "No, my English teacher is the tall man. He is wearing a gray suit. He is over there.") != scarf:
                Answer = "No, my English teacher is the tall man. He`s wearing a gray suit. He`s over there."
            n = n + 1
        elif n == 30:
            Answer2 = "And which one is your math teacher?"
            n = n + 1
        elif n == 31:
            if ("He`s wearing a blue suit and a white shirt." or "He is wearing a blue suit and a white shirt.") != scarf:
                Answer = "He`s wearing a blue suit and a white shirt."
            n = n + 1
        elif n == 32:
            Answer2 = "Let`s meet your English teacher first."
            n = 0
            ################################### پایان درس پنج انگلیسی صفحه 28 هفتم####################################
        elif n == 33:
            if ("I`m in the kitchen." or "I am in the kitchen."):
                Answer = "I`m in the kitchen."
            n = n + 1
        elif n == 34:
            Answer2 = "Hello. where`s Dad?"
            n = n + 1
        elif n == 35:
            if "In the garage." != scarf:
                Answer = "In the garage."
            n = n + 1
        elif n == 36:
            Answer2 = "What`s he doing? I`m so hungry."
            n = n + 1
        elif n == 37:
            if ("Ok, wash your hands and come for lunch. I`ll call Dad; he`s fixing the car." or "Ok, wash your hands and come for lunch. I`ll call Dad; he is fixing the car."or "Ok, wash your hands and come for lunch. I will call Dad; he`s fixing the car." or "Ok, wash your hands and come for lunch. I will call Dad; he is fixing the car.") != scarf:
                Answer = "Ok, wash your hands and come for lunch. I`ll call Dad; he`s fixing the car."
            n = n + 1
        elif n == 38:
            Answer2 = "Ok."
            n = 0
        ######################################پایان درس ۶ انگلیسی صفحه 32 هفتم########################################
        elif n == 39:
            if "What time are you going?" != scarf:
                Answer = "What time are you going?"
            n = n + 1
        elif n == 40:
            Answer2 = "Around 5 in the afternoon."
            n = n + 1
        elif n == 41:
            if ("I`m not sure I can, but I`ll try. What`s his address?" or "I`m not sure I can, but I`ll try. What is his address?" or "I am not sure I can, but I`ll try. What`s his address?" or "I am not sure I can, but I`ll try. What is his address?"or "I`m not sure I can, but I will try. What`s his address?" or "I`m not sure I can, but I`ll try. What is his address?" or "I am not sure I can, but I will try. What`s his address?" or "I am not sure I can, but I will try. What is his address?") != scarf:
                Answer = "I`m not sure I can, but I`ll try.What`s his address?"
            n = n + 1
        elif n == 42:
            Answer2="5 Azadi Street."
            n = n + 1
        elif n == 43:
            if "Call me before you go. My phone number is 586-2144." != scarf:
                Answer = "Call me before you go. My phone number is 586-2144"
            n = n + 1
        elif n == 44:
            Answer2 = "Ok, bye."
            n = 0
        #######################################پایان درس هفت انگلیسی صفحه 38 هفتم####################################
        elif n == 45:
            if ("Me,too. Let`s have some cake and milk."or "Me,too. Let is have some cake and milk.") != scarf:
                Answer = "Me,too. Let`s have some cake and milk."
            n = n + 1
        elif n == 46:
            Answer2 = "Sounds good, but I`d like some tea with my cake. That`s my favorite!"
            n = n + 1
        elif n == 47:
            if ("Ok, let`s go to the kitchen. Mom?" or "Ok, let`s go to the kitchen. Mom?")!= scarf:
                Answer = "Ok, let`s go to the kitchen. Mom?"
            n=0
        #######################################پایان درس هشت انگلیسی صفحه 42 هفتم##################################
        elif n==48:
            Answer2="Do you have any hobbies, Zahra?"
        elif n==49:
            if "Yes, I do. I watch movies as a hobby."!=scarf:
                Answer="Yes, I do. I watch movies as a hobby."
            n=n+1
        elif n==50:
            Answer2="Interesting! How about you, Samira?"
            n=n+1
        elif n==51:
            Answer2="Well, I love reading."
            n=n+1
        elif n==52:
            if "Really? What sort of things do you read?"!=scarf:
                Answer="Really? What sort of things do you read?"
            n=n+1
        elif n==53:
            Answer2="Books, magazines, sports news on the Net, and sometimes poems."
            n=n+1
        elif n==54:
            if "And how about you, Mrs. Emami?" !=scarf:
                Answer="And how about you, Mrs. Emami?"
            n=n+1
        elif n==55:
            Answer2="Actually, I don’t have any hobbies. But I usually go to the gym in my free time."
            n=0
            ###########################پایان درس هفت انگلیسی صفحه 54 هشتم##############################
        elif n==56:
            Answer2="Where are you from, Hamid?"
            n=n+1
        elif n==57:
            if "Ghez-ghal’eh."!=scarf:
                Answer="Ghez-ghal’eh."
            n=n+1
        elif n==58:
            Answer2="Where is it?"
            n=n+1
        elif n==59:
            if ("It’s a village in West Azarbaijan, near the city of Khoy."or "It is a village in West Azarbaijan, near the city of Khoy.")!=scarf:
                Answer="It’s a village in West Azarbaijan, near the city of Khoy."
            n=n+1
        elif n==60:
            Answer2="What’s it like?"
            n=n+1
        elif n==61:
            if ("It’s a mountain village with many trees and flowers. It’s famous for its sunflower fields." or "It’s a mountain village with many trees and flowers. It is famous for its sunflower fields."or "It is a mountain village with many trees and flowers. It’s famous for its sunflower fields." or "It is a mountain village with many trees and flowers. It is famous for its sunflower fields.")!=scarf:
                Answer="It’s a mountain village with many trees and flowers. It’s famous for its sunflower fields."
            n=n+1
        elif n==62:
            Answer2="What’s the people’s job?"
            n=n+1
        elif n==63:
            if "They work on farms and raise animals."!= scarf:
                Answer="They work on farms and raise animals."
            n=n+1
        elif n==64:
            Answer2="What about the weather?"
            n=n+1
        elif n==65:
            if "There’s a lot of wind in summer, fall and winter.It’s very cold from Aban to Farvardin." or "There is a lot of wind in summer, fall and winter.It’s very cold from Aban to Farvardin." or "There’s a lot of wind in summer, fall and winter.It is very cold from Aban to Farvardin." or "There is a lot of wind in summer, fall and winter.It is very cold from Aban to Farvardin.":
                Answer="There’s a lot of wind in summer, fall and winter.It’s very cold from Aban to Farvardin."
            n=n+1
        elif n==66:
            Answer2="It sounds to be a very interesting place."
            n=0
        ##############################پایان درس شش انگلیسی صفحه 48 هشتم#########################################
        elif n==67:
            Answer2="Morteza, tell me about Isfahan. Where is it?"
            n=n+1
        elif n==68:
            if "Well, Isfahan’s an old city in the center of Iran." !=scarf:
                Answer="Well, Isfahan’s an old city in the center of Iran."
            n=n+1
        elif n==69:
            Answer2="What’s it like?"
            n=n+1
        elif n==70:
            if ("It’s a big and clean city." or "It is a big and clean city.")!=scarf:
                Answer=("It’s a big and clean city.")
            n=n+1
        elif n==71:
            Answer2="Any famous buildings?"
            n=n+1
        elif n==72:
            if "Yes, many. Actually, Isfahan is very famous for its mosques and palaces."!=scarf:
                Answer="Yes, many. Actually, Isfahan is very famous for its mosques and palaces."
            n=n+1
        elif n==73:
            Answer2="Are there any museums?"
            n=n+1
        elif n==74:
            if "Yes, some great ones."!=scarf:
                Answer="Yes, some great ones."
            n=n+1
        elif n==75:
            Answer="I should see the city soon."
            n=n+1
        elif n==76:
            Answer2="Sure, and we can have special food downtown."
            n=0
        #####################پایان درس پنج انگلیسی صفحه 42 هشتم#######################################
        elif n==77:
            Answer2="Are you OK?"
            n=n+1
        elif n==78:
            if ("No, I’m not. I have a headache." or "No, I am not. I have a headache.")!=scarf:
                Answer="No, I’m not. I have a headache."
            n=n+1
        elif n==79:
            Answer2="Oh, you have sore eyes, too. You should go home and rest."
            n=n+1
        elif n==80:
            if "Yes, but we have one more class." !=scarf:
                Answer="Yes, but we have one more class."
            n=n+1
        elif n==81:
            Answer2="Don’t worry. I’ll talk to your teacher."
            n=n+1
        elif n==82:
            if "Thanks for your help."!=scarf:
                Answer="Thanks for your help."
            n=n+1
        elif n==83:
            Answer2="Let’s go to the office and call your parents first. Class, be quiet! I’ll be back in a minute."
            n=0
        ###############################پایان درس چهار انگلیسی صفحه 34 هشتم####################################
        elif n==84:
            Answer2="Wow! Your drawing is very good."
            n=n+1
        elif n==85:
            if "Thanks. Can you draw?"!=scarf:
                Answer="Thanks. Can you draw?"
            n=n+1
        elif n==86:
            Answer2="No, I’m not good at drawing. But I can take good photos."
            n=n+1
        elif n==87:
            if ("Really? Can I see your photos?"!=scarf)!=scarf:
                Answer="Really? Can I see your photos?"
            n=n+1
        elif n==88:
            Answer2="Why not? Come to my house this afternoon."
            n=n+1
        elif n==89:
            if ("Oh, I can not make it today. How about Thursday afternoon?"or "Oh, I can’t make it today. How about Thursday afternoon?"!=scarf):
                Answer="Oh, I can’t make it today. How about Thursday afternoon?"
            n=n+1
        elif n==90:
            Answer2="That’s fine. You can bring your drawing book, too."
            n=n+1
        elif n==91:
            if "Sure."!=scarf:
                Answer="Sure."
            n=0
        ###########################پایان درس سه انگلیسی صفحه 26 هشتم#####################################
        elif n==92:
            if "What do you do in the afternoons, Reihaneh?"!=scarf:
                Answer="What do you do in the afternoons, Reihaneh?"
            n=n+1
        elif n==93:
            Answer2="Well, I go to the gym on Sundays and Tuesdays."
            n=n+1
        elif n==94:
            if "How about Friday mornings?"!=scarf:
                Answer="How about Friday mornings?"
            n=n+1
        elif n==95:
            Answer2="I stay at home and relax. Why?"
            n=n+1
        elif n==96:
            if "You know, Shiva is not very good at English. Can you help her?"!= scarf:
                Answer="You know, Shiva is not very good at English. Can you help her?"
            n=n+1
        elif n==97:
            Answer2="Oh, sure."
            n=n+1
        elif n==98:
            if "That sounds great! When can you start?"!=scarf:
                Answer="That sounds great! When can you start?"
            n=n+1
        elif n==99:
            Answer2="This Wednesday afternoon."
            n=n+1
        elif n==100:
            if ("That’s fine. Thank you. I’ll let her know." or "That’s fine. Thank you. I will let her know." or "That is fine. Thank you. I will let her know.")!=scarf:
                Answer="That’s fine. Thank you. I’ll let her know."
            n=0
        #####################################پایان درس دو انگلیسی صفحه 18 هشتم####################################
        elif n==101:
            Answer2="Mr. Chaychi, this is my cousin Sam. He speaks French, English, and a little Persian."
            n=n+1
        elif n==102:
            Answer2="Oh, nice to meet you, Sam."
            n=n+1
        elif n==103:
            if "Nice to meet you, too."!=scarf:
                Answer="Nice to meet you, too."
            n=n+1
        elif n==104:
            Answer2="Are you from Iran?"
            n=n+1
        elif n==105:
            if "Yes, I’m originally Iranian, but I live in France." or "Yes, I am originally Iranian, but I live in France."!=scarf:
                Answer="Yes, I’m originally Iranian, but I live in France."
            n=n+1
        elif n==106:
            Answer2="Welcome to our class. How do you like it in Iran?"
            n=n+1
        elif n==107:
            if ("Iran is great! I love it. It’s a beautiful country."or "Iran is great! I love it. It is a beautiful country.")!= scarf:
                Answer="Iran is great! I love it. It’s a beautiful country."
            n=0
        ################################پایان درس یک انگلیسی صفحه 12 هشتم#####################################
        elif n==108:
            if "Who is your best friend at school?"!=scarf:
                Answer="Who is your best friend at school?"
            n=n+1
        elif n==109:
            Answer2="Reza."
            n=n+1
        elif n==110:
            if ("What’s he like?"or "What is he like?")!=scarf:
                Answer="What’s he like?"
            n=n+1
        elif n==111:
            Answer2="Oh, he is really great! He’s clever and kind."
            n=n+1
        elif n==112:
            if "Is he hard-working too?"!=scarf:
                Answer="Is he hard-working too?"
            n=n+1
        elif n==113:
            Answer2="Yes! And he’s always very helpful."
            n=n+1
        elif n==114:
            if "How?"!=scarf:
                Answer="How?"
            n=n+1
        elif n==115:
            Answer2="He always helps me with my lessons."
            n=0
        ######################################پایان درس یک انگلیسی صفحه 18 نهم#####################################
        elif n==116:
            if "Welcome to our hotel sir, how can I help you?"!=scarf:
                Answer="Welcome to our hotel sir, how can I help you?"
            n=n+1
        elif n==117:
            Answer2="My name is Paul Kress.I’m from Germany. I have a reservation here."
            n=n+1
        elif n==118:
            if "I see! Are you staying here for two nights?"!=scarf:
                Answer="I see! Are you staying here for two nights?"
            n=n+1
        elif n==119:
            Answer2="Yes, my wife and I are visiting Tehran for three days."
            n=n+1
        elif n==120:
            if "Where is she now? I need to check her passport."!=scarf:
                Answer="Where is she now? I need to check her passport."
            n=n+1
        elif n==121:
            Answer2="She’s standing over there, by the gift shop. Here is her passport."
            n=n+1
        elif n==122:
            if ("Thank you. This is your key. It’s room 213. Hope you enjoy your stay in Tehran." or "Thank you. This is your key. It is room 213. Hope you enjoy your stay in Tehran.")!=scarf:
                Answer="Thank you. This is your key. It’s room 213. Hope you enjoy your stay in Tehran."
            n=0
        ######################################پایان درس دو انگلیسی صفحه 30 نهم#####################################
        elif n==123:
            Answer2="I just love New Year holidays!"
            n=n+1
        elif n==124:
            if ("Oh, yes, me too. It’s really great." or "Oh, yes, me too. It is really great.")!=scarf:
                Answer="Oh, yes, me too. It’s really great."
            n=n+1
        elif n==125:
            Answer2="We normally visit our relatives in Norooz. It’s fun!"
            n=n+1
        elif n==126:
            if "Do you get New Year gifts too?"!=scarf:
                Answer="Do you get New Year gifts too?"
            n=n+1
        elif n==127:
            Answer2="Sure! We usually get money. I really like it."
            n=n+1
        elif n==128:
            if "Well…, We always go to my grandparents’ houses."!=scarf:
                Answer="Well…, We always go to my grandparents’ houses."
            n=n+1
        elif n==129:
            Answer2="That’s nice! Does your grandmother cook the New Year meal?"
            n=n+1
        elif n==130:
            if "Actually, she doesn’t. My mother makes it."!=scarf:
                Answer="Actually, she doesn’t. My mother makes it."
            n=0
        ############################پایان درس سه انگلیسی صفحه 50 نهم####################################
        elif n==131:
            Answer2="Excuse me sir! Can you help me please?"
            n=n+1
        elif n==132:
            if "What can I do for you?"!=scarf:
                Answer="What can I do for you?"
            n=n+1
        elif n==133:
            Answer2="I want a postcard, an envelope and a stamp."
            n=n+1
        elif n==134:
            if "Umm…, you can get them from a post office."!=scarf:
                Answer="Umm…, you can get them from a post office."
            n=n+1
        elif n==135:
            Answer2="Where is the post office?"
            n=n+1
        elif n==136:
            if "Actually it’s near here. It’s just round the corner." or "Actually it is near here. It’s just round the corner." or "Actually it’s near here. It is just round the corner." or "Actually it is near here. It is just round the corner."!=scarf:
                Answer="Actually it’s near here. It’s just round the corner."
            n=n+1
        elif n==137:
            Answer2="Good! Thank you. What time does it open?"
            n=n+1
        elif n==138:
            if"It opens at 8." !=scarf:
                Answer="It opens at 8."
            n=n+1
        elif n==139:
            Answer2="Thanks a lot!"
            n=0
        #########################################پایان درس چهار انگلیسی صفحه 64 هشتم##################################
        elif n==140:
            Answer2="Did you enjoy your weekend?"
            n=n+1
        elif n==141:
            if "Yes, it was wonderful! I attended Fajr International Film Festival."!=scarf:
                Answer="Yes, it was wonderful ! I attended Fajr International Film Festival."
            n=n+1
        elif n==142:
            Answer2="Really? I am also interested in its events and movies."
            n=n+1
        elif n==143:
            if "Oh, did you watch the reports on TV last night?"!=scarf:
                Answer="Oh, did you watch the reports on TV last night?"
            n=n+1
        elif n==144:
            Answer2="Yes, I did, but I like to read about them."
            n=n+1
        elif n==145:
            if "Well, you can surf its website if you like. There are many interesting things there."!=scarf:
                Answer="Well, you can surf its website if you like. There are many interesting things there."
            n=n+1
        elif n==146:
            Answer2="That’s great! Could you please give me the website address?"
            n=n+1
        elif n==147:
            if "Why not! Just a moment. Umm… I just texted it."!=scarf:
                Answer="Why not! Just a moment. Umm… I just texted it."
            n=n+1
        elif n==148:
            Answer2="Thanks a lot."
            n=0
        ##################################پایان درس پنج انگلیسی صفحه 82 نهم#################################
        elif n==149:
            if "We plan to go to the lake. Do you want to come?"!=scarf:
                Answer="We plan to go to the lake. Do you want to come?"
            n=n+1
        elif n==150:
            Answer2="I don’t think so. I don’t like school trips. Last summer I fell and broke my leg."
            n=n+1
        elif n==151:
            if "It sometimes happens. I twisted my ankle last winter. I stayed home for two weeks!"!=scarf:
                Answer="It sometimes happens. I twisted my ankle last winter. I stayed home for two weeks!"
            n=n+1
        elif n==152:
            Answer2="That’s too bad! I didn’t know that."
            n=n+1
        elif n==153:
            if "Yeah…, but after that, I participated in Helal-e-Ahmar frst aid classes. I learned how to take care of myself."!=scarf:
                Answer="Yeah…, but after that, I participated in Helal-e-Ahmar frst aid classes. I learned how to take care of myself."
            n=n+1
        elif n==154:
            Answer2="I like that. Can you give me some advice?"
            n=n+1
        elif n==155:
            if "Sure!"!=scarf:
                Answer="Sure!"
            n = 0
        ################################پایان درس شش انگلیسی صفحه 96 نهم################################

    print(Answer)
    print(Answer2)
    if Answer != 0:
        print(Answer)
        home = CTk()
        home.title('TMR_P')
        home.geometry('600x600')
        home.resizable(width=False, height=False)

        # BOT Aseets
        frame_bot = CTkFrame(home)
        frame_bot.pack(padx=10, pady=12, fill=X)

        bot_tit_lb = CTkLabel(frame_bot, text=Answer, font=('Roboto', 25), corner_radius=0)
        bot_tit_lb.pack(padx=12, pady=12, side=TOP)

        Answer = 0
        home.mainloop()

    if Answer2!=0:
        home = CTk()
        home.title('TMR_P')
        home.geometry('600x600')
        home.resizable(width=False, height=False)

        # BOT Aseets
        frame_bot = CTkFrame(home)
        frame_bot.pack(padx=10, pady=12, fill=X)

        bot_lb = CTkLabel(frame_bot, text=Answer2, font=('Roboto', 20), corner_radius=0)
        bot_lb.pack(padx=12, pady=12, side=LEFT)


        Answer2 = 0
        home.mainloop()
