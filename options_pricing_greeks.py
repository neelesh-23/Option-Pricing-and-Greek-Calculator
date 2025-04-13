import numpy as np
from scipy.stats import norm

# ----------------------------
# Black-Scholes Model
# ----------------------------
def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return price

# ----------------------------
# Binomial Model
# ----------------------------
def binomial_option_price(S, K, T, r, sigma, N=100, option_type='call'):
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    prices = np.zeros(N + 1)
    for i in range(N + 1):
        prices[i] = S * (u ** (N - i)) * (d ** i)

    values = np.zeros(N + 1)
    for i in range(N + 1):
        if option_type == 'call':
            values[i] = max(prices[i] - K, 0)
        else:
            values[i] = max(K - prices[i], 0)

    for j in range(N - 1, -1, -1):
        for i in range(j + 1):
            values[i] = np.exp(-r * dt) * (p * values[i] + (1 - p) * values[i + 1])

    return values[0]

# ----------------------------
# Greeks Calculation
# ----------------------------
def greeks(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)
    theta = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2)
    rho = K * T * np.exp(-r * T) * norm.cdf(d2)

    return {
        'Delta': delta,
        'Gamma': gamma,
        'Vega': vega / 100,  # per 1% change
        'Theta': theta / 365,  # per day
        'Rho': rho / 100  # per 1% change
    }

# ----------------------------
# Exotic Options - Stubs
# ----------------------------
def digital_option_price(S, K, T, r, sigma, option_type='call'):
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    if option_type == 'call':
        return np.exp(-r * T) * norm.cdf(d2)
    else:
        return np.exp(-r * T) * norm.cdf(-d2)

def barrier_option_price(S, K, H, T, r, sigma, option_type='call', barrier_type='up-and-out'):
    # Placeholder for barrier logic (complex logic depending on barrier type)
    return 'Barrier Option Pricing Logic Placeholder'

def range_accrual_price(S, K_low, K_high, T, r, sigma):
    # Simulate average payoff between strike bounds (simplified version)
    num_steps = 1000
    dt = T / num_steps
    accrual = 0
    for _ in range(num_steps):
        ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * np.random.normal())
        if K_low <= ST <= K_high:
            accrual += 1
    return (accrual / num_steps) * np.exp(-r * T)

# ----------------------------
# Sensitivity Analysis
# ----------------------------
def sensitivity_analysis(S, K, T, r, sigma):
    days = np.linspace(1, int(T * 365), 100)
    deltas = []
    thetas = []

    for d in days:
        t = d / 365
        g = greeks(S, K, t, r, sigma)
        deltas.append(g['Delta'])
        thetas.append(g['Theta'])

    return days, deltas, thetas

# Example usage (uncomment to run directly)
# if __name__ == '__main__':
#     S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
#     print("Black-Scholes Call:", black_scholes_price(S, K, T, r, sigma, 'call'))
#     print("Binomial Put:", binomial_option_price(S, K, T, r, sigma, option_type='put'))
#     print("Greeks:", greeks(S, K, T, r, sigma))
#     print("Digital Option:", digital_option_price(S, K, T, r, sigma))
#     print("Range Accrual Option:", range_accrual_price(S, 95, 105, T, r, sigma))