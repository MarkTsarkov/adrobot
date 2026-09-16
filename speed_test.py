import sys
import time
import urllib.request

DEFAULT_URL = "https://fastly.picsum.photos/id/545/5000/5000.jpg?hmac=g9yRBtkYttctwBksi8hIIdmvVD_X31keNm1_jfm5hkE"
NUM_REQUESTS = 10


def measure(url, n=NUM_REQUESTS):
    times = []
    speeds = []
    total_bytes = 0
    for i in range(n):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        start = time.perf_counter()
        with urllib.request.urlopen(req) as response:
            data = response.read()
        elapsed = time.perf_counter() - start
        mb = len(data) / (1024 * 1024)
        speed = mb / elapsed
        times.append(elapsed)
        speeds.append(speed)
        total_bytes += len(data)
        print(f"Запрос {i + 1}/{n}: {elapsed:.3f} c, {mb:.2f} МБ, {speed:.2f} МБ/с")
    return times, speeds, total_bytes


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL

    times, speeds, total_bytes = measure(url)

    avg_time = sum(times) / len(times)
    avg_speed = sum(speeds) / len(speeds)
    total_mb = total_bytes / (1024 * 1024)

    print()
    print(f"Среднее время запроса: {avg_time:.3f} c")
    print(f"Объём скачанных данных: {total_mb:.2f} МБ")
    print(f"Средняя скорость: {avg_speed:.2f} МБ/с")


if __name__ == "__main__":
    main()
