html = open('source.html').read()

replace_instructions = [
    # [('th', 'з'),],
    # [('sh', 'ш'),],
    # #[('r', 'р'),],
    # [('b', 'б'),],
    # [('v', 'в'),('w', 'в'),],
    # [('f', 'ф'),('ph', 'ф'),],
    # # [('p', 'п'),],
    # # [('m', 'м'),],
    # [('d', 'д'),],
    # [('j', 'дж'),],
    # [('k', 'к'),('x', 'кс'),('l', 'л'),],
    # [('ng', 'н'),('n', 'н'),],
    [],
    [('and', 'и'),],
    [('was', 'был'),],
    [('his', 'его'),],
    [('you', 'ты'),],
    [('in', 'в'),],
    [('her', 'её'),],
    [('said', 'сказал'),],
    [('magic', 'магия'),],
]

levels = [html]

for replace_instruction in replace_instructions:
    new_level = levels[-1]
    for english_letter, russian_letter in replace_instruction:
        new_level = new_level.replace(english_letter, russian_letter)
    levels.append(new_level)

print('export const LEVELS = ', levels)
