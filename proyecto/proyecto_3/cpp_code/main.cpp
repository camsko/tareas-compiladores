#include "PyObject.hpp"
#include <iostream>

void pyPrint(PyObject obj) {
  switch (obj.type) {
  case INT:
    std::cout << obj.pyInt << std::endl;
    break;
  case FLOAT:
    std::cout << obj.pyFloat << std::endl;
    break;
  case BOOL:
    std::cout << obj.pyBool << std::endl;
    break;
  case STRING:
    std::cout << obj.pyString << std::endl;
    break;
  default:
    break;
  }
}

int main() {

  PyObject x;
  PyObject y;
  x = PyObject(5);
  y = PyObject(3.5);
  pyPrint(x * y);

  return 0;
}
