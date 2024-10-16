import numpy as np
import matplotlib.pyplot as plt

# تعریف دامنه n (محور گسسته)
n = np.arange(0, 6, 1)  # از 0 تا 5

# تعریف تابع واحد گسسته u[n]
def u(n):
    return np.where(n >= 0, 1, 0)

# تعریف سیگنال x[n] = u[n] - u[n - 3]
x_n = u(n) - u(n - 3)

# رسم سیگنال
plt.figure()
plt.stem(n, x_n, basefmt=" ", linefmt='b-', markerfmt='bo', label='x[n] = u[n] - u[n - 3]')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Signal x[n]')
plt.axhline(0, color='black', lw=0.5, ls='--')  # خط افقی صفر
plt.grid(True)
plt.ylim(-0.2, 1.2)  # تنظیم محدوده محور عمودی
plt.legend()
plt.show()
