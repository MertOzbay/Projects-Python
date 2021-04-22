from collections import Counter
import re

input_text = input("Please enter input text: ")
input_text = input_text.strip().lower()

bigram_list = []
for i in range(len(input_text)-1):
    bigram = input_text[i:i+2]
    if not re.search(r'\W', bigram): bigram_list.append(bigram)

bigram_count = Counter(bigram_list)
total = sum(item[1] for item in bigram_count.most_common())
print()
for i, item in enumerate(bigram_count.most_common(30)):
    print(str(i+1)+': '+ str(item[0])+', '+str(item[1]/total))

