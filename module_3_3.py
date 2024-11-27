#       Домашнее задание по уроку "Распаковка позиционных параметров"
#       Задача "Распаковка"
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(5, 'Hello', False)
print_params('Not',[3,2,1],23)
print_params(b = 25)
print_params(c = [1,2,3])

i=input('Для продолжения нажмите enter\n')
values_list=['Aaron',[3,2,1],3.65]
print_params(*values_list)

i=input('Для продолжения нажмите enter\n')
values_dict={ 'a': ['Оценки Johnny',5,3,3,5,4], 'b': 'Средняя оценка', 'c': 2.25 }
print_params(**values_dict)

i=input('Для продолжения нажмите enter\n')
values_list_2 = ['Евгений', 1971  ]
print_params(*values_list_2, 53)




