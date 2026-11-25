import time
import random
import sys
import math
import base64

_K = b"spongebob"
_B = "MCQ6LRw2UjY9QCM7OzdEJiAf"
_U = "GwQbHhRfTUAWGh4WGxUJTAwNHl9dCwMLEhUUGA=="


def slow_print(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def progress(label, steps=30, speed=0.06):
    for i in range(steps + 1):
        pct = int(i / steps * 100)
        bar = "#" * i + "-" * (steps - i)
        sys.stdout.write(f"\r{label:<32} [{bar}] {pct:3d}%")
        sys.stdout.flush()
        time.sleep(speed + random.random() * 0.04)
    print()


def fake_matrix(n):
    m = [[random.uniform(-1, 1) for _ in range(n)] for _ in range(n)]
    total = 0.0
    for row in m:
        for v in row:
            total += math.sin(v) * math.cos(v ** 2)
    return total


def eigen_stuff():
    vals = []
    for i in range(8):
        v = fake_matrix(12)
        vals.append(v)
        slow_print(f"  lambda_{i} = {v:+.8f}", 0.008)
        time.sleep(0.15)
    return vals


def hash_chain(rounds):
    h = 0xCBF29CE484222325
    for i in range(rounds):
        h ^= random.getrandbits(64)
        h = (h * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF
        if i % 40000 == 0:
            sys.stdout.write(f"\r  entropy pool: {h:016x}")
            sys.stdout.flush()
    print()
    return h


def reveal(blob):
    raw = base64.b64decode(blob)
    return "".join(chr(b ^ _K[i % len(_K)]) for i, b in enumerate(raw))


def ask_route():
    while True:
        slow_print("Would you rather (1) do the long route or (2) Get the flag ? : ", 0.03)
        choice = input("> ").strip()
        if choice in ("1", "2"):
            return choice
        print("Invalid choice, enter 1 or 2.")


def main():
    if ask_route() == "2":
        print()
        slow_print(reveal(_B))
        return

    print()
    slow_print("Initializing Bikini Bottom")
    time.sleep(1)
    slow_print("Allocating tensor workspace (2048 x 2048 x 64)")
    progress("Loading kernel modules")
    progress("Calibrating flux capacitors", 25, 0.05)

    slow_print("\nComputing eigenvalue decomposition:")
    eigen_stuff()

    slow_print("\nRunning stochastic hash convergence...")
    hash_chain(400000)

    progress("Normalizing probability field", 35, 0.07)
    progress("Resolving 14,882 dependency nodes", 40, 0.05)

    slow_print("\nResidual error: {:.3e}".format(random.uniform(1e-9, 9e-9)))
    slow_print("Convergence achieved after {} iterations".format(random.randint(8000, 9999)))
    time.sleep(1.2)

    progress("Decrypting final payload", 20, 0.12)

    print()
    slow_print("=" * 67)
    slow_print("  RESULT READY")
    slow_print("  " + reveal(_U))
    slow_print("=" * 67)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\naborted")
