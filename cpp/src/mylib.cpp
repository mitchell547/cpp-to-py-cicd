#include <vector>
#include <numeric>
#include <cstdint>

#ifdef __linux__ 
	#define __declspec(v)
#endif

extern "C" __declspec(dllexport) int32_t sum_of_array(const int32_t* arr, size_t n) {
    std::vector<int32_t> v(arr, arr + n);
    int32_t sum = std::accumulate(std::begin(v), std::end(v), 0);
    return sum;
}
