import warnings

warnings.filterwarnings("ignore")

import math
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, FuncFormatter


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def compute_pi(n):
    theta = 2 * math.pi / n
    side_length = 2 * math.sin(theta / 2)
    perimeter = n * side_length
    pi_approx = perimeter / 2
    return pi_approx


n_list = [3, 4, 6, 8, 16, 32, 64, 128, 256, 512, 1024]
pi_list = [compute_pi(n) for n in n_list]


print("单元数n\tπ近似计算值")
print("-" * 30)
for n, pi_val in zip(n_list, pi_list):
    print(f"{n}\t\t{pi_val:.8f}")


plt.figure(figsize=(10, 6), dpi=100)


plt.plot(n_list, pi_list, 'o-', color='#1f77b4', linewidth=2, markersize=5)

plt.axhline(y=math.pi, color='red', linestyle='--', label='理论真实π')

plt.xscale('log', base=10)
ax = plt.gca()


ax.set_yscale('log')

def log_formatter(x, pos):
    exp = math.floor(math.log10(x))
    return r'$10^{%d}$' % exp

ax.xaxis.set_major_locator(LogLocator(base=10, subs=(1.0,)))
ax.yaxis.set_major_locator(LogLocator(base=10, subs=(1.0,)))
ax.xaxis.set_major_formatter(FuncFormatter(log_formatter))
ax.yaxis.set_major_formatter(FuncFormatter(log_formatter))


plt.xlabel('离散划分单元数量 n')
plt.ylabel('圆周率 π 近似求解值')
plt.title('有限元离散近似：圆周率收敛特性曲线')


plt.grid(True, alpha=0.3, which="both")

plt.tight_layout()
plt.show()