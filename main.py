# main.py
from options_pricing_greeks import (
    black_scholes_price,
    binomial_option_price,
    greeks,
    digital_option_price,
    barrier_option_price,
    range_accrual_price,
    sensitivity_analysis
)

import matplotlib.pyplot as plt

if __name__ == "__main__":
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2

    print("--- Vanilla Options ---")
    print("Black-Scholes Call Price:", black_scholes_price(S, K, T, r, sigma, 'call'))
    print("Binomial Put Price:", binomial_option_price(S, K, T, r, sigma, option_type='put'))
    print("Greeks:", greeks(S, K, T, r, sigma))

    print("\n--- Exotic Options ---")
    print("Digital Call Option Price:", digital_option_price(S, K, T, r, sigma))
    print("Barrier Option (Placeholder):", barrier_option_price(S, K, 120, T, r, sigma))
    print("Range Accrual Option (95-105):", range_accrual_price(S, 95, 105, T, r, sigma))

    print("\n--- Sensitivity Analysis ---")
    days, deltas, thetas = sensitivity_analysis(S, K, T, r, sigma)
    plt.plot(days, deltas, label='Delta')
    plt.plot(days, thetas, label='Theta')
    plt.xlabel("Days to Maturity")
    plt.ylabel("Value")
    plt.title("Sensitivity of Delta and Theta over Time")
    plt.legend()
    plt.grid(True)
    plt.show()
