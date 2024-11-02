import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та меж інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(f, a, b, n=100000):
    x_random = np.random.uniform(a, b, n)  # Генерація випадкових точок у діапазоні [a, b]
    y_random = f(x_random)                 # Обчислення значень функції в цих точках
    integral = (b - a) * np.mean(y_random)  # Інтеграл як середнє значення * діапазон
    return integral

# Обчислення інтегралу методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b)
print(f"Інтеграл (метод Монте-Карло): {monte_carlo_result}")

# Обчислення точного значення інтегралу за допомогою функції quad
quad_result, error = spi.quad(f, a, b)
print(f"Інтеграл (функція quad): {quad_result} з помилкою {error}")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
