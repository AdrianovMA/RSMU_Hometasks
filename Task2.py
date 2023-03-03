
# Задача 2
# 1. Найдите пакет http, с помощью функции help изучите модули, из которых он состоит.
# 2. Импортируйте модуль client из пакета http.
# 3. Воспользуйтесь функционалом импортированного модуля:
#     1. Создайте HTTP соединение по адресу www.google.com
#     2. Отправьте GET запрос по адресу выше
#     3. Проверьте ответ на отправленный запрос

import http
import http.client


connection = http.client.HTTPConnection('www.google.com')
connection.request('GET', '/')
res = connection.getresponse()
print(res.status, res.reason)
