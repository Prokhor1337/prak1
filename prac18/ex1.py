import threading
import time

def countdown():
    for i in range(10, 0, -1):
        print(f"Зворотний відлік: {i}")
        time.sleep(1)

thread = threading.Thread(target=countdown)
thread.start()
thread.join()
print("Зворотний відлік завершено.")
