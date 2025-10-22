#include <algorithm>
#include <iostream>
#include <random>
#include <vector>

void selection_sort(std::vector<int>& data) {
    const std::size_t n = data.size();
    for (std::size_t i = 0; i < n; ++i) {
        std::size_t min_idx = i;
        for (std::size_t j = i + 1; j < n; ++j) {
            if (data[j] < data[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(data[i], data[min_idx]);
    }
}

int main() {
    std::vector<int> values(10);
    std::mt19937 rng(std::random_device{}());
    std::uniform_int_distribution<int> dist(0, 99);

    for (int& value : values) {
        value = dist(rng);
    }

    std::vector<int> std_sorted = values;
    std::vector<int> selection_sorted = values;

    std::sort(std_sorted.begin(), std_sorted.end());
    selection_sort(selection_sorted);

    std::cout << "Original: ";
    for (int v : values) {
        std::cout << v << ' ';
    }
    std::cout << "\nstd::sort: ";
    for (int v : std_sorted) {
        std::cout << v << ' ';
    }
    std::cout << "\nSelection sort: ";
    for (int v : selection_sorted) {
        std::cout << v << ' ';
    }
    std::cout << '\n';

    return 0;
}
