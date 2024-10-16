import numpy as np
import matplotlib.pyplot as plt

# تعریف دامنه t (محور زمان)
t = np.arange(0, 10, 0.01)  # از 0 تا 10 با گام 0.01
x_t = np.cos((1/6) * t)     # تعریف سیگنال

# رسم سیگنال
plt.figure()
plt.plot(t, x_t)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t) = cos(1/6 * t)')
plt.grid(True)
plt.show()
