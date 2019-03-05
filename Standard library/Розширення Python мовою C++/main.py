# -*- coding: utf-8 -*-
"""
# Розширення Python мовою C++
Нижче наведено послідовність дій для створення мовою C++ Python-модуля `Extest`, який містить функцію `fac`, що повертає факторіал числа. Створення модулів розширення мовою C++ дозволяє вирішити проблему низької продуктивності Python.

1.Вихідний код модуля розширення мовою C++ (main.cpp):

```
int fac(int n) // рекурсивна функція, повертає факторіал
{
    if (n < 2) return(1);
    return (n)*fac(n-1);
}

#include "Python.h" // під’єднати файл Python.h
// функція повертає об’єкт Python типу int
static PyObject *Extest_fac(PyObject *self, PyObject *args)
{
    int num;
    // конвертує дане Python типу int в C++ типу int
    if (!PyArg_ParseTuple(args, "i", &num)) 
        return NULL;
    // конвертує дане C++ типу int в Python типу int
    return (PyObject*)Py_BuildValue("i", fac(num));
}

// масив методів, які експортує модуль
static PyMethodDef ExtestMethods[] =
{{ "fac", Extest_fac, METH_VARARGS }, { NULL, NULL },};

void initExtest() // функція ініціалізації модуля
{
    Py_InitModule("Extest", ExtestMethods);
}
```

2.Модуль Python, який створює і установлює модуль розширення за допомогою `distutils` (setup.py):

```
from distutils.core import setup, Extension
setup(name='Extest', ext_modules=[Extension('Extest', sources=['main.cpp'])])
```

3.В командному рядку введіть (для Python 2.5 необхідне установлене MS Visual C++ 2003):

    setup.py build
    setup.py install

4.Перевірка роботи модуля в Python:
"""
import Extest
Extest.fac(7) # 5040
