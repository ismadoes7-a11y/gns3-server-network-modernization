import time
from concurrent.futures import ThreadPoolExecutor

from port_manager import PortManager


def benchmark_allocations(num_threads=32, allocations=200):
    manager = PortManager(console_host="127.0.0.1", console_port_range=(44000, 44500))
    start = time.perf_counter()

    def allocate(_):
        return manager.get_free_tcp_port()

    with ThreadPoolExecutor(max_workers=num_threads) as pool:
        ports = list(pool.map(allocate, range(allocations)))

    elapsed = time.perf_counter() - start
    unique_count = len(set(ports))
    print(f"allocated {unique_count} unique TCP ports across {allocations} requests in {elapsed:.4f}s")


if __name__ == "__main__":
    benchmark_allocations()
