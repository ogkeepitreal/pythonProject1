with open('trimushketera.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = text.lower()
text = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
words = text.split()

total_words = len(words)
unique_words = set(words)

sorted_unique_words = sorted(unique_words)

with open('trimushketera_result.txt', 'w') as result_file:
    result_file.write(f'Количество слов: {total_words}\n')
    result_file.write(f'Уникальные слова: {len(sorted_unique_words)}\n')
    result_file.write('Уникальные слова по алфовиту:\n')
    for word in sorted_unique_words:
        result_file.write(word + '\n')

print('Сохранено в trimushketera_result.txt')