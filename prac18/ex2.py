import threading
import time
import random

def load_file(file_number):
    duration = random.randint(3, 5)
    print(f"Потік {file_number} почав завантаження (очікування {duration} сек)...")
    time.sleep(duration)
    print(f"Потік {file_number} завершив завантаження.")

threads = []
for i in range(1, 4):
    t = threading.Thread(target=load_file, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Усі потоки завершили завантаження.")
