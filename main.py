#!/usr/bin/env python3
"""
Demo script using the pyo3_demo Rust module
"""

import pyo3_demo

def main():
    print("=== PyO3 Demo ===\n")
    
    # Test simple functions
    print("Testing functions:")
    result = pyo3_demo.add(5, 3)
    print(f"  add(5, 3) = {result}")
    
    result = pyo3_demo.multiply(4, 7)
    print(f"  multiply(4, 7) = {result}")
    
    # Test the Calculator class
    print("\nTesting Calculator class:")
    calc = pyo3_demo.Calculator(10.0)
    print(f"  Initial value: {calc.value}")
    
    calc.add(5.0)
    print(f"  After add(5.0): {calc.value}")
    
    calc.multiply(2.0)
    print(f"  After multiply(2.0): {calc.value}")
    
    calc.reset()
    print(f"  After reset(): {calc.value}")

if __name__ == "__main__":
    main()
