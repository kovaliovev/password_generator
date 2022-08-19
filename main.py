from random import sample


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
doubtful_symbols = 'il1Lo0O'
chairs = ''

pass_count = int(input('Введите желанное количество паролей \n'))
while pass_count < 1:
    pass_count = int(input('Введите допустимое количество паролей \n'))

pass_len = int(input('Введите желанную длину паролей \n'))
while pass_len < 1:
    pass_len = int(input('Введите допустимую длину паролей \n'))

digits_include = input('Желаете генерировать в пароле цифры? (да/нет) \n')
lowercase_letters_include = input('Желаете генерировать в пароле прописные буквы? (да/нет) \n')
uppercase_letters_include = input('Желаете генерировать в пароле заглавные буквы? (да/нет) \n')
punctuation_include = input('Желаете генерировать в пароле знаки пунктуации? (да/нет) \n')
doubtful_symbols_include = input('Желаете убрать из пароля неоднозначные символы? (il1Lo0O) (да/нет) \n')
agreement = ['lf', 'l', 'да', 'д']

if digits_include in agreement:
    chairs += digits
if lowercase_letters_include in agreement:
    chairs += lowercase_letters
if uppercase_letters_include in agreement:
    chairs += uppercase_letters
if punctuation_include in agreement:
    chairs += punctuation
if doubtful_symbols_include in agreement:
    s = []
    s.extend(chairs)
    chairs = ''.join([i for i in s if i not in 'il1Lo0O'])

def password_generate(symb, leng):
    return sample(symb, leng)

while len(chairs) < pass_len:
    chairs = chairs * 2
for _ in range(pass_count):
    print(''.join(password_generate(chairs, pass_len)))

print(input()) #exit
