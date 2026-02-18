use pyo3::prelude::*;

/// A simple function that adds two numbers
#[pyfunction]
fn add(a: i64, b: i64) -> i64 {
    a + b
}

/// A simple function that multiplies two numbers
#[pyfunction]
fn multiply(a: i64, b: i64) -> i64 {
    a * b
}

/// Sum numbers from 1 to n (Rust implementation)
#[pyfunction]
fn sum_range_rust(n: i64) -> i64 {
    (1..=n).sum()
}

/// Fibonacci number calculator (Rust implementation)
#[pyfunction]
fn fibonacci_rust(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let mut a = 0u64;
            let mut b = 1u64;
            for _ in 2..=n {
                let temp = a + b;
                a = b;
                b = temp;
            }
            b
        }
    }
}

/// A simple class to demonstrate PyO3 classes
#[pyclass]
struct Calculator {
    #[pyo3(get, set)]
    value: f64,
}

#[pymethods]
impl Calculator {
    #[new]
    fn new(value: f64) -> Self {
        Calculator { value }
    }

    fn add(&mut self, other: f64) -> f64 {
        self.value += other;
        self.value
    }

    fn multiply(&mut self, other: f64) -> f64 {
        self.value *= other;
        self.value
    }

    fn reset(&mut self) {
        self.value = 0.0;
    }
}

/// PyO3 Demo - A Python module implemented in Rust
#[pymodule]
fn pyo3_demo(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    m.add_function(wrap_pyfunction!(multiply, m)?)?;
    m.add_function(wrap_pyfunction!(sum_range_rust, m)?)?;
    m.add_function(wrap_pyfunction!(fibonacci_rust, m)?)?;
    m.add_class::<Calculator>()?;
    Ok(())
}
