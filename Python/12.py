import numpy as np
import matplotlib.pyplot as plt

# تعریف دامنه t (محور زمان)
t = np.linspace(0, 10, 1000)  # از 0 تا 10 با 1000 نقطه

# تعریف تابع x(t)
x_t = np.sin(t)  # تابع x(t) را به عنوان سینوس تعریف کردیم

# تعریف تابع واحد u(t-2)
def u(t):
    return np.where(t >= 2, 1, 0)

# تعریف سیگنال y(t) = x(t) * u(t-2)
y_t = x_t * u(t - 2)

# رسم سیگنال
plt.figure()
plt.plot(t, y_t, label='y(t) = x(t)u(t - 2)', color='blue')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Signal y(t)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.axvline(0, color='black', lw=0.5, ls='--')  # خط عمودی صفر
plt.grid(True)
plt.legend()
plt.show()
