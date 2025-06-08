import threading
import random

numbers = [random.randint(1, 100) for _ in range(1000)]
partial_sums = [0] * 4

def compute_sum(part_index, data_slice):
    partial_sums[part_index] = sum(data_slice)

threads = []
chunk_size = len(numbers) // 4

for i in range(4):
    start = i * chunk_size
    end = start + chunk_size
    t = threading.Thread(target=compute_sum, args=(i, numbers[start:end]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

total = sum(partial_sums)
print(f"Загальна сума: {total}")
