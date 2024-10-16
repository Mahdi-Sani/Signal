import numpy as np
import matplotlib.pyplot as plt

# تعریف دامنه t (محور زمان)
t = np.arange(0, 10, 0.01)  # از 0 تا 10 با گام 0.01

# تعریف سیگنال مختلط x(t) = e^(j2t) + e^(j3t)
x_t = np.exp(1j * 2 * t) + np.exp(1j * 3 * t)

# استخراج قسمت حقیقی و موهومی
real_part = np.real(x_t)
imaginary_part = np.imag(x_t)

# رسم قسمت حقیقی سیگنال
plt.figure()
plt.plot(t, real_part, label='Real Part')
plt.plot(t, imaginary_part, label='Imaginary Part', linestyle='--')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t) = e^(j2t) + e^(j3t)')
plt.legend()
plt.grid(True)
plt.show()
