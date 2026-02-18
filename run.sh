#!/bin/bash
# Build and run the PyO3 demo

echo "🦀 Building Rust module with PyO3..."
source venv/bin/activate
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 maturin develop

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Build successful! Running demo..."
    echo ""
    python main.py
else
    echo "❌ Build failed"
    exit 1
fi
