# -*- coding: utf-8 -*-
"""
# ctypes - виклик зовнішніх C-функцій
ctypes - це бібліотека для поступу до зовнішніх C-функцій, яка забезпечує сумісні з C типи даних і дозволяє виклик функцій з DLL або розподілюваних бібліотек Unix. Наступна С-функція `f` отримує три аргументи (змінну `n` та вказівники `x` і `A`) і повертає вказівник `B`. Зауважте, що функція змінює значення за адресами `x` і `A`.

```
#include <stdlib.h>
float* __declspec(dllexport) f(float* x, int n, float* A)
{
float *B = (float*)malloc(sizeof(float) * n);
int i;
for(i=0; i<n; i++)
    {B[i]=A[i]+*x; A[i]-=*x;}
*x=A[1]-A[0];
return B;
}
```

Для компіляції цього коду в бібліотеку DLL застосовано команди GCC 4.9.2 (tdm-1):

    mingw32-gcc.exe -O2 -c main.c -o main.o
    mingw32-gcc.exe -shared main.o -o mydll.dll -s

Тепер до бібліотеки mydll.dll можна звернутись з Python:
"""
from ctypes import *
mydll=cdll.LoadLibrary("mydll.dll") # завантажити бібліотеку DLL
float3 = c_float * 3 # тип масиву з 3 елем. С-сумісного типу float
A=float3(1, 2, 3) # масив
mydll.f.argtypes=[POINTER(c_float), c_int, float3] # типи аргументів
mydll.f.restype=POINTER(c_float) # тип результату
x=c_float(1) # змінна С-сумісного типу float 
B=mydll.f(x, 3, A) # виклик функції (x, A - вказівники)
# або B=mydll.f(byref(x), 3, A)
for a in A: print a, # вивести масив A
print '\n', B[0], B[1], B[2] # вивести масив B (але не B[3] !)
print x.value # значення змінної x
