# TODO  Напишите функцию count_letters

from collections import Counter
def count_letters(text):
    filtered_text = [char.lower() for char in text if char.isalpha()]
    return Counter(filtered_text)
def calculate_frequency(letter_count, total_letters):
    return {letter: count / total_letters for letter, count in letter_count.items()}

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
letter_count = count_letters(main_str)

total_letters = sum(letter_count.values())

letter_frequency = calculate_frequency(letter_count, total_letters)

for letter, frequency in sorted(letter_frequency.items()):
    print(f"{letter}: {frequency:.4f}")

# TODO Напишите функцию calculate_frequency

# TODO Распечатайте в столбик букву и её частоту в тексте
