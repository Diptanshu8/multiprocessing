/* File : example.i */
%module example
%{
#include "example.h"
%}

extern void  run(PyObject *);

%include "example.h"

