import numpy as np
import matplotlib.pyplot as plt

# پارامتر
a = 1  # می‌توانید مقدار دلخواهی برای a قرار دهید

# تعریف دامنه t (محور زمان)
t = np.linspace(0, 10, 1000)  # از 0 تا 10 با 1000 نقطه

# تعریف تابع f(t)
def f(t):
    return a * np.exp(-t)

# تعریف تابع واحد u(t-1)
def u(t):
    return np.where(t >= 0, 1, 0)

# تعریف f4(t) = f(t-1) * u(t-1)
f4_t = f(t - 1) * u(t - 1)

# محاسبه مشتق f4(t)
f4_derivative = np.gradient(f4_t, t)

# محاسبه انتگرال f4(t)
f4_integral = np.cumsum(f4_t) * (t[1] - t[0])  # استفاده از روش انتگرال‌گیری عددی

# رسم توابع
plt.figure(figsize=(15, 8))

# رسم f4(t)
plt.subplot(3, 1, 1)
plt.plot(t, f4_t, label='f4(t) = f(t-1)u(t-1)', color='blue')
plt.xlabel('t')
plt.ylabel('f4(t)')
plt.title('Signal f4(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.legend()

# رسم مشتق f4(t)
plt.subplot(3, 1, 2)
plt.plot(t, f4_derivative, label="f4'(t)", color='orange')
plt.xlabel('t')
plt.ylabel("f4'(t)")
plt.title('Derivative of f4(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.legend()

# رسم انتگرال f4(t)
plt.subplot(3, 1, 3)
plt.plot(t, f4_integral, label='∫f4(t) dt', color='green')
plt.xlabel('t')
plt.ylabel('∫f4(t) dt')
plt.title('Integral of f4(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
