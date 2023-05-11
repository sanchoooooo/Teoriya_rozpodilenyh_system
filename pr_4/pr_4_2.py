from multiprocessing import Pool
import time

def calculate_row_products(row1, row2):
    n = len(row1)
    products = []
    for i in range(n):
        product = 0
        # Обчислення добутку елементів двох рядків
        for k in range(n):
            product += row1[k] * row2[n-k-1]
        products.append(product)
    return products

def count_negative_products(matrix):
    n = len(matrix)
    with Pool() as pool:
        results = []
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    continue
                # Застосування функції calculate_row_products до пари рядків
                results.append(pool.apply_async(calculate_row_products, (matrix[i], matrix[j])))
        total_negative = 0
        for result in results:
            # Обчислення кількості від'ємних добутків у парі рядків
            products = result.get()
            negative_products = sum(1 for p in products if p < 0)
            total_negative += negative_products
        return total_negative

# Приклад використання
if __name__ == '__main__':
    matrix = [
        [6, 1, 3],
        [-4, 5, -9],
        [7, -8, 2]
    ]
    start_time = time.time()
    negative_pairs_count = count_negative_products(matrix)
    end_time = time.time()
    print(f"Кількість від'ємних добутків: {negative_pairs_count}")
    print(f"Час виконання: {end_time - start_time} секунд")