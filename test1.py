bad_words = ['дурак', 'козёл']
mes = 'Иван Сидоров - дурак'
if any(map(lambda x: x in bad_words, mes.split())):
    print('Вы забанены')