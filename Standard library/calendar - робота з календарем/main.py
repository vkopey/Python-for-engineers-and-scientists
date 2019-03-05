#-*- coding: utf-8 -*-
"""
# calendar - робота з календарем
Функції для виведення календаря і роботи з ним. За замовчуванням першим днем тиждня є понеділок, а останнім - неділя.
"""
import calendar
c=calendar.Calendar(calendar.MONDAY) # календар (або calendar.Calendar())
print [d for d in c.itermonthdates(2016, 2)][:2] # ітератор на дні місяця datetime.date (цілі тиждні)
print calendar.weekday(2016, 2, 29) # день тиждня
print calendar.monthrange(2016, 2) # день тиждня першого дня місяця і кількість днів в місяці
calendar.TextCalendar(calendar.MONDAY).formatmonth(2016, 2) # повертає текстовий календар на місяць
calendar.LocaleTextCalendar(calendar.MONDAY,'Ukrainian_Ukraine').formatmonth(2016, 2) # повертає текстовий календар на місяць (українська мова)
calendar.HTMLCalendar(calendar.MONDAY).formatmonth(2016, 2) # повертає html календар на місяць
