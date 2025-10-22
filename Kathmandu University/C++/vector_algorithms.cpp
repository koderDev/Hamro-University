#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

void print_vector(const std::vector<int>& values, const std::string& label) {
    std::cout << label << ": ";
    for (int v : values) {
        std::cout << v << ' ';
    }
    std::cout << '\n';
}

int main() {
    std::vector<int> numbers{5, 1, 9, 3, 7, 2, 8};

    print_vector(numbers, "Original");

    const int sum = std::accumulate(numbers.begin(), numbers.end(), 0);
    std::cout << "Sum: " << sum << '\n';

    const bool has_even = std::any_of(numbers.begin(), numbers.end(), [](int v) { return v % 2 == 0; });
    std::cout << "Contains even number: " << (has_even ? "yes" : "no") << '\n';

    std::vector<int> sorted = numbers;
    std::sort(sorted.begin(), sorted.end());
    print_vector(sorted, "Sorted");

    std::vector<int> evens;
    std::copy_if(numbers.begin(), numbers.end(), std::back_inserter(evens), [](int v) { return v % 2 == 0; });
    print_vector(evens, "Even elements");

    std::vector<int> squared(numbers.size());
    std::transform(numbers.begin(), numbers.end(), squared.begin(), [](int v) { return v * v; });
    print_vector(squared, "Squared");

    return 0;
}
