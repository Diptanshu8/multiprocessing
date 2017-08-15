/* File : example.c */

#include "example.h"


void run(PyObject * reporter) {
    const char * s = "123abc";
    assert ( PyFunction_Check(reporter) );
    PyObject* args = PyTuple_Pack(1, PyString_FromString(s));
    PyObject_CallObject((PyObject*)reporter, args);
}

