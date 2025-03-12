'''Задача 3. Преобразование времени'''

time_seconds = input('Введите кол-во секунд: ')

hour = int(time_seconds) // 3600
minutes = int(time_seconds) % 3600 // 60
seconds = int(time_seconds) % 3600 % 60

print('Время в формате "часы:минуты:секунды": ' + str(hour) + ':' + str(minutes) + ':' + str(seconds))