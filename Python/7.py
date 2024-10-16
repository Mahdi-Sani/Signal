import numpy as np
import matplotlib.pyplot as plt

# تعریف دامنه t (محور زمان)
t = np.linspace(-2, 2, 1000)  # از -2 تا 2 با 1000 نقطه

# تعریف T
T = 1

# تعریف تابع واحد u(t)
def u(t):
    return np.where(t >= 0, 1, 0)

# تعریف سیگنال x(t) = u(t + T/2) - u(t - T/2)
x_t = u(t + T/2) - u(t - T/2)

# رسم سیگنال
plt.figure()
plt.plot(t, x_t, label='x(t) = u(t + T/2) - u(t - T/2)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Signal x(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.ylim(-0.2, 1.2)  # تنظیم محدوده محور عمودی
plt.legend()
plt.show()
