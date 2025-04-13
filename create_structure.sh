# Create directory structure
mkdir -p options_pricing/{src,tests,docs}

# Create key files
touch options_pricing/src/{pricing_models.py,greeks_calculator.py,main.py}
touch options_pricing/tests/{test_pricing_models.py,test_greeks_calculator.py}
touch options_pricing/README.md