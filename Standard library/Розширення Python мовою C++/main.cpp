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
