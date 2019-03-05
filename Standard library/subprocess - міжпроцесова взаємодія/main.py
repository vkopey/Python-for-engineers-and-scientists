# -*- coding: utf-8 -*-
"""
# subprocess - міжпроцесова взаємодія
## main.py - модуль клієнта
Міжпроцесова взаємодія (англ. IPC) - це обмін даними між процесами. Як правило реалізується засобами ОС. До методів IPC належать: файли, неіменовані і іменовані канали, черги повідомлень, сигнали, спільна пам'ять, сокети і файли, що відображаються в пам'ять. В прикладі створюється канал між стандартними потоками введення/виведення/помилок (stdin/stdout/stderr) процесів. Цей модуль створює новий процес server.py, відсилає йому дані на stdin та отримує дані з його stdout.
"""
import subprocess, pickle
data=['A','B','C'] # дані
s = pickle.dumps(data) # серіалізувати список в рядок
s=s.encode("string_escape") # перетворити в рядковий літерал Python (без "\n")
p=subprocess.Popen(["python", "server.py"],stdin = subprocess.PIPE, stdout= subprocess.PIPE, stderr= subprocess.PIPE) # створити процес
stdout, stderr = p.communicate(input=s) # надіслати дані в stdin, отримати дані з stdout, чекати завершення процесу
s=stdout.decode("string_escape") # перетворити з рядкового літералу Python
print pickle.loads(s) # перетворити в список
