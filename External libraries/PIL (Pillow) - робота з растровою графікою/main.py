# -*- coding: utf-8 -*-
"""
# PIL (Pillow) - робота з растровою графікою
Pillow 4.2.1 (Python Imaging Library) - це бібліотека для роботи з растровою графікою (http://pillow.readthedocs.io). Підтримує велику кількість форматів, їх конвертацію, різні операції з зображенням. 
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
image = Image.new('RGBA', (50, 40), (0, 0, 0, 0)) # зображення з заданою колірною моделлю, розміром і фоном
draw = ImageDraw.Draw(image) # простий інтерфейс для 2D рисування
fnt = ImageFont.truetype(r'c:\Windows\Fonts\times.ttf', 28) # шрифт
draw.text((5, 5), "PIL", font=fnt, fill=(0,255,0,255)) # рисувати текст в заданих координатах
image2=image.rotate(20) # повернути на 20 градусів
image2=image2.filter(ImageFilter.SMOOTH) # згладити зображення
image=Image.alpha_composite(image,image2) # об'єднати
image = image.crop([1, 1, 49, 39]) # обрізати
image.convert('RGB') # конвертувати в модель RGB
#image.save("pil.png") # зберегти
image.show() # показати у зовнішній програмі
"""
![](fig.png)

Рисунок - Растровий рисунок
"""
