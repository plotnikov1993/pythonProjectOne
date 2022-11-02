import Control as c

print('Выберите Калькулятор:\n\t 1. Рациональный\n\t 2. Комплексный\n')

calc = input('Тип калькулятора №')
if calc == '1':
    c.button_click_rac()
if calc == '2':
    c.button_click_complex()