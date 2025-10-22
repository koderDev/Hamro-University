#include <iostream>
#include <string>

int main() {
    std::cout << "Enter your name: ";
    std::string name;
    std::getline(std::cin, name);

    if (name.empty()) {
        std::cout << "Hello, mysterious stranger!" << std::endl;
    } else {
        std::cout << "Hello, " << name << "!" << std::endl;
    }

    return 0;
}
