# -*- coding: utf-8 -*-
"""
# Вбудовування інтерпретатора Python у C++ програму 
Нижче показано приклад програми мовою C++, яка має можливість звернення до інтерпретатора Python. Якщо використовується середовище розробки Code::Blocks 16.01 та компілятор GNU GCC Compiler, то в опціях проекту (Project build options) потрібно вказати шлях до заголовних файлів (Search directories) C:\\Python27\\include та під'єднати усі бібліотеки (Link libraries) з C:\\Python27\\libs. Якщо використовується середовище розробки Borland C++ Builder 6, то:

1. Виконайте конвертацію бібліотеки: `coff2omf.exe python27.lib python27_.lib`.
2. Скопіюйте python27_.lib в папку з проектом і переіменуйте його в python27.lib.
3. Виберіть меню Project/Options.../Directories та додайте в Include path C:\\Python27\\include
4. Додайте до проекту python27.lib та Python.h

```
#include "Python.h"    
main(int argc, char **argv)
{
Py_SetProgramName(argv[0]); // передає argv[0] інтерпретатору
Py_Initialize(); // ініціалізація інтерпретатора
// виконання команд Python (ніби модуль __main__)
PyRun_SimpleString("import time\n");
PyRun_SimpleString("print time.localtime(time.time())\n");
Py_Finalize(); // закінчення роботи інтерпретатора
}
```

"""
