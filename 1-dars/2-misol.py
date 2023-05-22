import threading
import time

def SSS():
    start_time = time.time()
    for i in range(10):
        time.sleep(1)
        print("Uxlanyapman...")
    end_time = time.time()
    print(f"Dastur boshlanish vaqti: {start_time}")
    print(f"Dastur tugash vaqti: {end_time}")
    print(f"Dastur bajarilish uchun sarflangan vaqt: {end_time - start_time} sekund")

t1 = threading.Thread(target=SSS)
t2 = threading.Thread(target=SSS)

t1.start()
t2.start()

t1.join()
t2.join()

SSS()

input()