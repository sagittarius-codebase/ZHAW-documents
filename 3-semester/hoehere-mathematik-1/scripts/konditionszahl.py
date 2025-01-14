import numpy as np

def get_derivative(f, x, epsilon=1e-6):
    return (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)

def konditionszahl(f, x):
    f_x = f(x)
    f_prime_x = get_derivative(f, x)
    return abs(f_prime_x) * abs(x) / abs(f_x)


# replace with your values:
x_value = 0.0000000001
f_x = lambda x: np.sin(x)


k_value = konditionszahl(f_x, x_value)
print(f'Die Konditionszahl K bei x = {x_value}: {k_value}')