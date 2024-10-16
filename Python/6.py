import numpy as np
import matplotlib.pyplot as plt

# تعریف دامنه n (محور گسسته)
n = np.arange(0, 50, 1)  # از 0 تا 50 با گام 1 (اعداد صحیح)

# تعریف سیگنال مختلط x[n] = e^(j2n) + e^(j3n)
x_n = np.exp(1j * 2 * n) + np.exp(1j * 3 * n)

# استخراج قسمت حقیقی و موهومی
real_part = np.real(x_n)
imaginary_part = np.imag(x_n)

# رسم قسمت حقیقی سیگنال
plt.figure()
plt.stem(n, real_part, label='Real Part', basefmt=" ")
plt.stem(n, imaginary_part, label='Imaginary Part', basefmt=" ", linefmt='--', markerfmt='o')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[n] = e^(j2n) + e^(j3n)')
plt.legend()
plt.grid(True)
plt.show()
