#include <iostream>
    #include "cpp_code/PyObject.hpp"

    using namespace std;

    int main() {
    PyObject x;
PyObject y;
PyObject z;
PyObject a;
PyObject b;
PyObject c;
PyObject d;
PyObject e;
PyObject f;
PyObject g;
x = PyObject(4);
y = PyObject(3);
z = PyObject(2);
a = x + PyObject(1);
b = a - PyObject(2);
c = b / PyObject(1);
d = c * PyObject(3);
e = PyObject(true);
f = PyObject("Hola");
g = PyObject(3.14);
if ((x == PyObject(4)) && ((z <= PyObject(3)) || (y <= PyObject(5)))) {
std::cout << PyObject(false) << std::endl;
}
else if (x == PyObject(5)) {
std::cout << PyObject(false) << std::endl;
}
else {
std::cout << PyObject(true) << std::endl;
}
while (x > PyObject(4)) {
std::cout << PyObject(true) << std::endl;
}
for (PyObject i : z) {
std::cout << i << std::endl;
}
for (PyObject i = PyObject(2); i < PyObject(10); i++) {
std::cout << i << std::endl;
}
if (((a >= d) || (b <= PyObject(2))) && ((c != b) || (d < PyObject(10)))) {
std::cout << PyObject(true) << std::endl;
}
else if (!e) {
std::cout << PyObject(false) << std::endl;
}
else {
std::cout << PyObject(true) << std::endl;
}

    return 0;
    }
    