import multiprocessing
import time
#source:https://realpython.com/python-concurrency/#how-to-speed-up-a-cpu-bound-program

def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)

def find_sums2(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)




if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(40)]
    tipo=2

    start_time = time.time()
    if tipo==1:
        print("Sin procesamiento paralelo")
        find_sums(numbers)
    else:
        print("Con procesamiento paralelo")
        find_sums2(numbers)

    duration = time.time() - start_time
    print(f"Duración {duration} segundos")