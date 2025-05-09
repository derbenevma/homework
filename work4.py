# s = input()
# counter = 0
# N_words = []
# for n, i in enumerate(s):
#     if i == 'н':
#         if counter == 0:
#             N_words.append([n])
#         counter += 1
#     elif i != 'н' and counter > 0:
#         N_words[-1].append(counter)
#         counter = 0
# else:
#     if counter > 0:
#         N_words[-1].append(counter)
# N_words = sorted(N_words, key=lambda x: x[1], reverse=True)
# t = '!' * N_words[0][1]
# s = s[:N_words[0][0]] + t + s[N_words[0][0]+N_words[0][1]+1:]
# print(s)
# print(f'количество н: {N_words[0][1]}')
# # Задача 2
# s = input() 
# print(s[s.index('(')+1:s.index(')')])
# Задача 3
# import re

# def words_starting_a_ending_ya(text):

#   words = re.findall(r'\b[аА][а-яА-Я]*я\b', text)
#   return words

# text = "Абстракция авария аллея Абракадабра Банальная история"
# result = words_starting_a_ending_ya(text)
# print(f"Слова, начинающиеся на а и заканчивающиеся на я {result}")
