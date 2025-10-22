#include <iostream>
#include <limits>

void clear_stdin() {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

double evaluate(double a, double b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return b != 0.0 ? a / b : std::numeric_limits<double>::quiet_NaN();
        default: return std::numeric_limits<double>::quiet_NaN();
    }
}

int main() {
    std::cout << "Simple Calculator (type q to quit)" << std::endl;

    while (true) {
        double lhs = 0.0;
        double rhs = 0.0;
        char op = 0;

        std::cout << "Enter expression (e.g., 3 + 4): ";
        if (!(std::cin >> lhs)) {
            char c;
            std::cin.clear();
            std::cin >> c;
            if (c == 'q' || c == 'Q') {
                std::cout << "Goodbye!" << std::endl;
                break;
            }
            std::cout << "Invalid input, try again." << std::endl;
            clear_stdin();
            continue;
        }

        std::cin >> op >> rhs;
        if (!std::cin) {
            std::cout << "Invalid expression, try again." << std::endl;
            clear_stdin();
            continue;
        }

        const double result = evaluate(lhs, rhs, op);
        if (result != result) { // NaN check
            std::cout << "Operation failed (possible division by zero or unknown operator)." << std::endl;
        } else {
            std::cout << "Result: " << result << std::endl;
        }
    }

    return 0;
}
