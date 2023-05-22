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

SSS()

input()