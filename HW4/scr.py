import numpy as np

def pearson_correlation(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(np.square(x))
    sum_y_squared = np.sum(np.square(y))
    product_sum = np.sum(np.multiply(x, y))

    numerator = (n * product_sum) - (sum_x * sum_y)
    denominator = np.sqrt(((n * sum_x_squared) - np.square(sum_x)) * ((n * sum_y_squared) - np.square(sum_y)))

    correlation = numerator / denominator

    return correlation

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = pearson_correlation(x, y)
print("Корреляция Пирсона =", correlation)