import matplotlib.pyplot as plt
import utils

# Данные
god = 2024
months = ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
values = [utils.metraj_year(god=int(str(god)[-2:]), months=i) for i in range(1, 13)]

# График
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(months, values, color='#4FC3F7', edgecolor='black', linewidth=0.5)

# Текст ВНУТРИ, в верхней части столбца
for bar, val in zip(bars, values):
    x = bar.get_x() + bar.get_width() / 2
    # y — 85% от высоты столбца (можно регулировать: 0.8–0.95)
    y = bar.get_height() * 0.9

    label = f"{val:,}".replace(",", " ")  # → "2 114", "3 112"

    ax.text(
        x, y,
        label,
        ha='center',  # по центру по X
        va='top',  # прижать текст к точке сверху → будет внутри, у верха
        fontsize=10,
        fontweight='bold',
        color='white',
        # Опционально: лёгкий фон для лучшей читаемости
        bbox=dict(
            facecolor='none',  # прозрачный фон (оставьте как есть)
            edgecolor='none',
            pad=0.2
        )
    )

# Оформление
ax.set_title(f'Метраж на {god} год', fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sine_plot.png", dpi=300, bbox_inches="tight")
plt.show()
