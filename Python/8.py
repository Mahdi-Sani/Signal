import numpy as np
import matplotlib.pyplot as plt

# تعریف دامنه t (محور زمان)
t = np.linspace(-1, 3, 1000)  # از -1 تا 3 با 1000 نقطه

# تعریف تابع واحد u(t)
def u(t):
    return np.where(t >= 0, 1, 0)

# تعریف سیگنال x(t) = u(t) - u(t - 2)
x_t = u(t) - u(t - 2)

# رسم سیگنال
plt.figure()
plt.plot(t, x_t, label='x(t) = u(t) - u(t - 2)', color='blue')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Signal x(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.ylim(-0.2, 1.2)  # تنظیم محدوده محور عمودی
plt.legend()
plt.show()
