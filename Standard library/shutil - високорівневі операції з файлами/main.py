# -*- coding: utf-8 -*-
"""
# shutil - високорівневі операції з файлами
Модуль shutil містить високорівневі функції для операцій з файлами (копіювання, переміщення, архівування).
"""
import os, shutil
os.mkdir('tmp'); os.mkdir('tmp/tmp2') # створити каталоги
shutil.copyfile('main.py', 'tmp/tmp2/main.py') # копіювати файл
shutil.move('tmp/tmp2', '.') # перемістити каталог в поточний
shutil.copytree('tmp2', 'tmp3') # копіювати каталог
print shutil.make_archive('tmp/test_archive.zip', 'zip', base_dir='tmp2') # архівувати каталог
