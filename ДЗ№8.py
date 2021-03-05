# Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов,
# хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
import numpy as np
from scipy import stats
stats.f_oneway

f = np.array([173, 175, 180, 178, 177, 185, 183, 182], dtype=np.float64)  # 8
x = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180], dtype=np.float64)  # 9
sh = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170], dtype=np.float64)  # 11

print(stats.f_oneway(f, x, sh))
# statistic=5.500053450812596, pvalue=0.010482206918698694
# Из таблицы назодим Fкрит = 2,95 сравниваем с 5,5,
# Так как фактическое значение отношения Фишера (5,5) больше критического (2,95),
# с вероятностью 95% отклоняем нулевую гипотезу