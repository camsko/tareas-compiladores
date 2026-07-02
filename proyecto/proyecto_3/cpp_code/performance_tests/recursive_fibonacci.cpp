#include <iostream>

int fibonacci(int n) {
    if (n <= 1)
        return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    for (int i = 1; i <= 50; i++) {
        std::cout << "Fib(" << i << ") = " << fibonacci(i) << std::endl;
    }
    return 0;
}