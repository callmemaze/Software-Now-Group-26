"""
Prime Number Analyzer 

Finds all prime numbers up to a user-defined limit (max 100)
and displays key statistics.

Group Name: Sydney Group 26
Group Members:
Dipesh Shrestha - S394865
Aryan Shrestha - S396160
Priyanka Shakya - S396306
Nahida Aktar - S391730

"""

from math import isqrt


def get_limit() -> int:
    """Get a valid integer input between 0 and 100."""
    while True:
        try:
            value = int(input("Enter a number (1–100): "))
            if 1 <= value <= 100:
                return value
            print("❌ Error: Number must be between 1 and 100.")
        except ValueError:
            print("❌ Error: Please enter a valid integer.")


def sieve_primes(limit: int) -> list[int]:
    """
    Generate prime numbers using the Sieve of Eratosthenes.
    More efficient and professional than basic checking.
    """
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            for multiple in range(i * i, limit + 1, i):
                sieve[multiple] = False

    return [i for i, is_prime in enumerate(sieve) if is_prime]

def calculate_statistics(primes: list[int]) -> dict:
    """Return statistics as a dictionary for clarity."""
    return {
        "count": len(primes),
        "smallest": primes[0] if primes else None,
        "largest": primes[-1] if primes else None,
        "sum": sum(primes)
    }

def display_results(primes: list[int]) -> None:
    """Display results in a clean, formatted output."""
    stats = calculate_statistics(primes)

    print("\n📊 Prime Number Analysis")
    print("=" * 45)

    primes_str = " ".join(map(str, primes)) if primes else "None"
    print(f"{'Prime numbers found:':<25} {primes_str}")
    print(f"{'Total primes found:':<25} {stats['count']}")
    print(f"{'Smallest prime:':<25} {stats['smallest'] if stats['smallest'] is not None else 'N/A'}")
    print(f"{'Largest prime:':<25} {stats['largest'] if stats['largest'] is not None else 'N/A'}")
    print(f"{'Sum of all primes:':<25} {stats['sum']}")


if __name__ == "__main__":
    limit = get_limit()
    primes = sieve_primes(limit)
    display_results(primes)