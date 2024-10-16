import numpy as np
import matplotlib.pyplot as plt

# پارامتر
a = 1  # می‌توانید مقدار دلخواهی برای a قرار دهید

# تعریف دامنه t (محور زمان)
t = np.linspace(0, 10, 1000)  # از 0 تا 10 با 1000 نقطه

# تعریف تابع f(t)
def f(t):
    return a * np.exp(-t)

# تعریف تابع واحد u(t-2)
def u(t):
    return np.where(t >= 0, 1, 0)

# تعریف f2(t) = f(t-1) * u(t-2)
f2_t = f(t - 1) * u(t - 2)

# محاسبه مشتق f2(t)
f2_derivative = np.gradient(f2_t, t)

# محاسبه انتگرال f2(t)
f2_integral = np.cumsum(f2_t) * (t[1] - t[0])  # استفاده از روش انتگرال‌گیری عددی

# رسم توابع
plt.figure(figsize=(15, 8))

# رسم f2(t)
plt.subplot(3, 1, 1)
plt.plot(t, f2_t, label='f2(t) = f(t-1)u(t-2)', color='blue')
plt.xlabel('t')
plt.ylabel('f2(t)')
plt.title('Signal f2(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.legend()

# رسم مشتق f2(t)
plt.subplot(3, 1, 2)
plt.plot(t, f2_derivative, label="f2'(t)", color='orange')
plt.xlabel('t')
plt.ylabel("f2'(t)")
plt.title('Derivative of f2(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.legend()

# رسم انتگرال f2(t)
plt.subplot(3, 1, 3)
plt.plot(t, f2_integral, label='∫f2(t) dt', color='green')
plt.xlabel('t')
plt.ylabel('∫f2(t) dt')
plt.title('Integral of f2(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
