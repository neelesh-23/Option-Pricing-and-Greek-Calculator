# Options Pricing & Greeks Calculation

This Python project implements core options pricing models and calculates risk sensitivities (Greeks) for financial derivatives. It also demonstrates simulations for exotic options and conducts sensitivity analysis.

## 📈 Features
- Black-Scholes pricing model
- Binomial Tree pricing model
- Greeks calculation (Delta, Gamma, Vega, Theta, Rho)
- Exotic options: Barrier, Digital, Range Accrual (simplified)
- Sensitivity analysis over time (Delta, Theta)
- Visual plots for Greek behavior

## 📂 Project Structure
```
├── options_pricing_greeks.py    # Core logic for pricing and greeks
├── main.py                      # Script to run and test features
├── README.md                    # Project documentation
├── requirements.txt             # Dependencies
```

## 🚀 Getting Started
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/options-pricing-greeks.git
cd options-pricing-greeks
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the main script
```bash
python main.py
```

## 🧠 Usage Example
```python
from options_pricing_greeks import black_scholes_price, greeks
price = black_scholes_price(100, 100, 1, 0.05, 0.2, 'call')
greek_vals = greeks(100, 100, 1, 0.05, 0.2)
```

## 📊 Output Example
- Option prices printed in console
- Plot showing Delta and Theta over time

## 📚 References
- Hull, J. C. *Options, Futures, and Other Derivatives*
- [Black-Scholes Model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)
- [Binomial Option Pricing](https://en.wikipedia.org/wiki/Binomial_options_pricing_model)

---

Made with ❤️ for finance and data science.

