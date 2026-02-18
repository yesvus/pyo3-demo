#!/usr/bin/env python3
"""
Benchmark comparing Rust (PyO3) vs Pure Python performance
"""

import time
import pyo3_demo

# Pure Python implementations
def sum_range_python(n):
    return sum(range(1, n + 1))

def fibonacci_python(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def benchmark(name, func, *args, iterations=1):
    """Run a function multiple times and measure execution time"""
    start = time.perf_counter()
    result = None
    for _ in range(iterations):
        result = func(*args)
    elapsed = time.perf_counter() - start
    return result, elapsed

def main():
    print("=" * 60)
    print("🦀 Rust (PyO3) vs 🐍 Pure Python Benchmark")
    print("=" * 60)
    
    # Test 1: Sum range
    print("\n📊 Test 1: Sum numbers from 1 to 10,000,000")
    n = 10_000_000
    
    result_py, time_py = benchmark("Python", sum_range_python, n)
    result_rs, time_rs = benchmark("Rust", pyo3_demo.sum_range_rust, n)
    
    print(f"  Python: {time_py:.4f}s (result: {result_py})")
    print(f"  Rust:   {time_rs:.4f}s (result: {result_rs})")
    print(f"  🚀 Speedup: {time_py/time_rs:.1f}x faster")
    
    # Test 2: Fibonacci
    print("\n📊 Test 2: Calculate Fibonacci(50) - 1,000,000 times")
    n = 50
    iterations = 1_000_000
    
    result_py, time_py = benchmark("Python", fibonacci_python, n, iterations=iterations)
    result_rs, time_rs = benchmark("Rust", pyo3_demo.fibonacci_rust, n, iterations=iterations)
    
    print(f"  Python: {time_py:.4f}s")
    print(f"  Rust:   {time_rs:.4f}s")
    print(f"  🚀 Speedup: {time_py/time_rs:.1f}x faster")
    
    print("\n" + "=" * 60)
    print("💡 Rust is much faster for CPU-intensive operations!")
    print("=" * 60)

if __name__ == "__main__":
    main()
