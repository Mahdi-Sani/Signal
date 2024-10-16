import numpy as np
import matplotlib.pyplot as plt

# تعریف تابع پله u[n]
def u(n):
    return np.where(n >= 0, 1, 0)

# تعریف h2[n] = u[n] - u[n-2]
def h2(n):
    return u(n) - u(n-2)

# تعریف h1[n] به صورت دلخواه، فرض کنید این یک فیلتر میان‌نگذر است
def h1(n):
    return np.where((n >= 0) & (n <= 4), 1, 0)  # یک فیلتر ساده برای مثال

# سیگنال ورودی x[n]
def x(n):
    return np.sin(0.1 * np.pi * n)  # برای مثال، یک سیگنال سینوسی

# اندازه n و ایجاد آرایه n
n = np.arange(-10, 20)

# محاسبه h1[n]، h2[n] و سیگنال نهایی y[n]
h1_n = h1(n)
h2_n = h2(n)

# خروجی h1[n] * x[n]
h1_output = np.convolve(x(n), h1_n, mode='same')

# خروجی h2[n] * h1_output
y_n = np.convolve(h1_output, h2_n, mode='same')

# رسم نتایج
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(n, x(n), marker='o')
plt.title("ورودی x[n]")

plt.subplot(3, 1, 2)
plt.plot(n, h1_output, marker='o')
plt.title("خروجی h1[n]")

plt.subplot(3, 1, 3)
plt.plot(n, y_n, marker='o')
plt.title("خروجی نهایی y[n]")

plt.tight_layout()
plt.show()
