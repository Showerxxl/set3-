import numpy as np
import matplotlib.pyplot as plt

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def in_circle(x, y, circle):

    return (x - circle.x) ** 2 + (y - circle.y) ** 2 <= circle.r ** 2

def monte_carlo_area(circle1, circle2, circle3, num_points):
    x_min = min(circle1.x - circle1.r, circle2.x - circle2.r, circle3.x - circle3.r)
    x_max = max(circle1.x + circle1.r, circle2.x + circle2.r, circle3.x + circle3.r)
    y_min = min(circle1.y - circle1.r, circle2.y - circle2.r, circle3.y - circle3.r)
    y_max = max(circle1.y + circle1.r, circle2.y + circle2.r, circle3.y + circle3.r)
    area_box = (x_max - x_min) * (y_max - y_min)


    cnt = 0
    for _ in range(num_points):
        x = np.random.uniform(x_min, x_max)
        y = np.random.uniform(y_min, y_max)
        if in_circle(x, y, circle1) and in_circle(x, y, circle2) and in_circle(x, y, circle3):
            cnt += 1


    estimated_area = (cnt / num_points) * area_box
    return estimated_area


circle1 = Circle(1.0, 1.0, 1.0)
circle2 = Circle(1.5, 2.0, np.sqrt(5) / 2)
circle3 = Circle(2, 1.5, np.sqrt(5) / 2)


N_values = range(100, 100001, 500)
estimated_areas = []
relative_errors = []


precise_area = monte_carlo_area(circle1, circle2, circle3, 1000000)


for N in N_values:
    estimated_area = monte_carlo_area(circle1, circle2, circle3, N)
    estimated_areas.append(estimated_area)


    relative_error = abs(estimated_area - precise_area) / precise_area
    relative_errors.append(relative_error)


plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(N_values, estimated_areas, label="Площадь", color="blue")
plt.xlabel("Количество точек")
plt.ylabel("Площадь")
plt.title("График 1: Оценка площади по количеству точек")
plt.legend()
plt.grid()

# График относительной ошибки в зависимости от числа точек N
plt.subplot(1, 2, 2)
plt.plot(N_values, relative_errors, label="Отклонение", color="red")
plt.xlabel("Количество точек")
plt.ylabel("Погрешность")
plt.title("График 2: Отклонение от точного значения")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
plt.show()

