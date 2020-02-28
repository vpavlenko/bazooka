import eng_to_ipa as ipa

html = open('source.txt').read()

replace_instructions = [
    # [('th', 'з'),],
    # [('sh', 'ш'),],
    # #[('r', 'р'),],
    # [('b', 'б'),],
    # [('v', 'в'),('w', 'в'),],
    # [('f', 'ф'),('ph', 'ф'),],
    # [('p', 'п'),],
    # # [('m', 'м'),],
    # [('d', 'д'),],
    # [('j', 'дж'),],
    # [('k', 'к'),('x', 'кс'),('l', 'л'),],
    # [('ng', 'н'),('n', 'н'),],
    # [],
    # [('and', 'и'),],
    # [('was', 'был'),],
    # [('his', 'его'),],
    # [('you', 'ты'),],
    # [('in', 'в'),],
    # [('her', 'её'),],
    # [('said', 'сказал'),],
    # [('magic', 'магия'),],
    [('ɛ', 'e'), ('oʊ', 'o'), ('ʊ', 'oo'), ('i', 'ee'), ('ŋ', 'ng'), ('ʧ', 'сh'), ('ð', 'dh'), ('θ', 'th'),
     ('ɑ', 'a'), ('æ', 'e'), ('ɪ', 'i'), ('ʃ', 'sh'), ('ˌ', ''), ('ˈ', ''), ('j', 'i'), ('ɔ', 'o')],
     [('ei', 'эй'), ('iu', 'ю'), ('z', 'з'), ('ai', 'ай'), ('p', 'п'), ('oi', 'ой'), ('f', 'ф'), ('m', 'м'),
     ('dh', 'з'), ('сh', 'ч'), ('ee', 'и'), ('k', 'к'), ('d', 'д'), ('sh', 'ш'), ('th', 'с'), ('s', 'с'), ('e', 'э'), ('oo', 'у'),
      ('ee', 'и'), ('ng', 'н'), ('i', 'ы'), ('ə', 'э'), ('r', 'р'), ('t', 'т'), ('b', 'б'), ('l', 'л'), ('n', 'н'), 
      ('w', 'в'), ('ʤ', 'дж'), ('v', 'в'), ('h', 'х'),  ('u', 'у'), ('g', 'г'), ],
      [(' прэфэсэр ', ' профессор '), (' зыс ', ' это '), (' энд ', ' и '), (' ай ', ' я '), (' зэт ', ' что '), (' ю ', ' ты '), ('', ''), ('', ''), 
      (' хи ', ' он '), (' джыст ', ' только '), (' лэтэр ', ' письмо '), (' сэд ', ' сказал '), (' май ', ' мой '), (' вэт ', ' что '),
       (' бэт ', ' но '), (' ыур ', ' наш '),
      (' ши ', ' она '), (' фэр ', ' для '), (' хaу ', ' как '), (' фрэм ', ' из '), (' лайк ', ' как '), (' oнли ', ' только '),
       (' лытэл ', ' маленький '), (' ивын ', ' даже '), ]
]

levels = [
    '''Every inch of wall space is covered by a bookcase. Each bookcase has six shelves, going almost to the ceiling. Some bookshelves are stacked to the brim with hardback books: science, maths, history, and everything else. Other shelves have two layers of paperback science fiction, with the back layer of books propped up on old tissue boxes or lengths of wood, so that you can see the back layer of books above the books in front. And it still isn't enough. Books are overflowing onto the tables and the sofas and making little heaps under the windows.''',
    '\n\n'.join(ipa.convert(paragraph) for paragraph in html.split('\n\n'))]

for replace_instruction in replace_instructions:
    new_level = levels[-1]
    for english_letter, russian_letter in replace_instruction:
        new_level = new_level.replace(english_letter, russian_letter)
    levels.append(new_level)

print('export const LEVELS = ', levels)
