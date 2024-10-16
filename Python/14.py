import numpy as np
import matplotlib.pyplot as plt

# پارامتر
a = 1  # می‌توانید مقدار دلخواهی برای a قرار دهید

# تعریف دامنه t (محور زمان)
t = np.linspace(0, 10, 1000)  # از 0 تا 10 با 1000 نقطه

# تعریف تابع f(t)
def f(t):
    return a * np.exp(-t)

# تعریف تابع واحد u(t)
def u(t):
    return np.where(t >= 0, 1, 0)

# تعریف f3(t) = f(t-1) * u(t)
f3_t = f(t - 1) * u(t)

# محاسبه مشتق f3(t)
f3_derivative = np.gradient(f3_t, t)

# محاسبه انتگرال f3(t)
f3_integral = np.cumsum(f3_t) * (t[1] - t[0])  # استفاده از روش انتگرال‌گیری عددی

# رسم توابع
plt.figure(figsize=(15, 8))

# رسم f3(t)
plt.subplot(3, 1, 1)
plt.plot(t, f3_t, label='f3(t) = f(t-1)u(t)', color='blue')
plt.xlabel('t')
plt.ylabel('f3(t)')
plt.title('Signal f3(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.legend()

# رسم مشتق f3(t)
plt.subplot(3, 1, 2)
plt.plot(t, f3_derivative, label="f3'(t)", color='orange')
plt.xlabel('t')
plt.ylabel("f3'(t)")
plt.title('Derivative of f3(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.legend()

# رسم انتگرال f3(t)
plt.subplot(3, 1, 3)
plt.plot(t, f3_integral, label='∫f3(t) dt', color='green')
plt.xlabel('t')
plt.ylabel('∫f3(t) dt')
plt.title('Integral of f3(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
