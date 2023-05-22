import multiprocessing
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

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=SSS)
    p2 = multiprocessing.Process(target=SSS)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Dastur foydalangan CPU lar soni: {multiprocessing.cpu_count()}")

SSS()
input()