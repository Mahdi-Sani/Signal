import numpy as np
import matplotlib.pyplot as plt

# تعریف دامنه n (محور گسسته)
n = np.arange(0, 50, 1)  # از 0 تا 50 با گام 1 (اعداد صحیح)
x_n = np.cos((8 * np.pi / 31) * n)  # سیگنال x[n] = cos(8π/31 * n)

# رسم سیگنال گسسته
plt.figure()
plt.stem(n, x_n)  
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[n] = cos(8π/31 * n)')
plt.grid(True)
plt.show()
