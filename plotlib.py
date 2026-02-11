import matplotlib.pyplot as plt
import numpy as np
from run import *

# Данные
y = [metraj_year(year=25, month=i) for i in range(1, 13)]
x = np.arange(len(y))

# Создание графика
fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(x, y, color='#9f2b68', edgecolor='white', width=0.8, align='edge')
# Цвета

# Сохранение и отображение
plt.tight_layout()
plt.savefig('sine_plot.png', dpi=300, bbox_inches='tight')
plt.show()