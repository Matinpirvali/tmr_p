def science(scarf):
    roles = {
        "هشتم-شش-انگلیسی-صفحه-96": "نقش شما رضا هست(Reza)",
        "هشتم-پنج-انگلیسی-صفحه-82": "نقش شما مهسا هست(Mahsa)",
        "هشتم-چهار-انگلیسی-صفحه-64": "شما نقش پدرام را دارید (Pedram)",
        "هشتم-سه-انگلیسی-صفحه-50": "نقش شما نسرین هست(Nasrin)",
        "هشتم-دو-انگلیسی-صفحه-30": "نقش شما رکپشن هست(Receptionist)",
        "هشتم-یک-انگلیسی-صفحه-18": "نقش شما احمد هست(Ahmad)",
        "هفتم-شش-انگلیسی-صفحه-96": "نقش شما افشین هست(Afshin)",
        "هفتم-پنج-انگلیسی-صفحه-82": "نقش شما علی هست(Ali)",
        "هفتم-چهار-انگلیسی-صفحه-64": "نقش شما ابوالفضل هست(Abolfazl)",
        "هفتم-سه-انگلیسی-صفحه-50": "شما نقش سهیلا را دارید(Sohila)",
        "هفتم-دو-انگلیسی-صفحه-30": "شما نقش مریم را دارید(Maryam)",
        "هفتم-یک-انگلیسی-صفحه-18": "شما نقش محمد را دارید(Mohammad)"
    }
    
    for condition, answer in roles.items():
        if all(word in scarf for word in condition.split("-")):
            return answer

    return "هیچ نقشی برای شما تعیین نشده است."
