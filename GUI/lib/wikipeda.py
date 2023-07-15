import wikipedia

entry_value = input(': ')
answer_value = wikipedia.summary(entry_value)
print(answer_value)