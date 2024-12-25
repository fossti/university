import pymorphy3
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='en')
morph_analyzer = pymorphy3.MorphAnalyzer()

word_count = {}

with open('dialogue', encoding='utf-8') as file:
    lines = file.read().splitlines()

for line in lines:
    words_in_line = line.split()
    for word in words_in_line:
        normalized_word = morph_analyzer.parse(word)[0].normal_form
        word_count[normalized_word] = word_count.get(normalized_word, 0) + 1

with open('result', 'w', encoding='utf-8') as result_file:
    result_file.write('Исходное слово | Перевод | Количество упоминаний\n')
    for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
        translated_word = translator.translate(word)
        result_file.write(f'{word} | {translated_word} | {count}\n')
