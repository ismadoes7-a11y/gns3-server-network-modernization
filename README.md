# PortManager

A small, concurrency-safe port allocator and validation helper for network-heavy applications.

This repo intentionally keeps the scope narrow: the first PR fixes the real issues in the port allocator path without changing the wider networking stack.

## Features
- thread-safe port reservation
- correct end-of-range handling
- validation for invalid ranges and occupied ports
- TCP/UDP allocation helpers
- a benchmark script to measure allocation behavior

## Running tests

```bash
python -m pytest -q
```

## Running the benchmark

```bash
python benchmarks/benchmark_port_manager.py
```
