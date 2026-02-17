import matplotlib.pyplot as plt

import utils

# Данные
y = [utils.metraj_year(god=25, months=i) for i in range(1, 13)]
mount = ["Янв", "Фев", "Март", "Апр", "Май", "Июнь", "Июль", "Авг", "Сен", "Окт", "Ноя", "Дек"]
x = [f"{mount[i]}\n{y[i]:.0f}" for i in range(12)]

# Создание графика
fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(x, y, color="#9f2b68", edgecolor="white", width=0.8, align="center")
# Цвета

# Сохранение и отображение
plt.tight_layout()
plt.savefig("sine_plot.png", dpi=300, bbox_inches="tight")
plt.show()
