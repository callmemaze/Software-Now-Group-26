"""
    Checks if the the total count of prime numbers found
        • the smallest and largest prime number in the range
        • the sum of all prime numbers found
"""
def find_all_prime_numbers(user_input: str) -> str:
    prime_no=[]

    for x in range(2, user_input + 1):
        is_prime = True
        for y in range (2, int(x**0.5) + 1):
            if x % y == 0:
                is_prime = False
                break

        if is_prime:
            prime_no.append(x)

    if not prime_no:
        return "No prime numbers found."
    
    Result=""
    Result += "Total prime numbers found: "+" ".join(map(str, prime_no)) + "\n"
    Result += "Total primes found: " + str(len(prime_no)) + "\n"
    Result += "Largest prime: " + str(max(prime_no)) + "\n"
    Result += "Smallest prime: " + str(min(prime_no)) + "\n"
    Result += "Sum of all primes: " + str(sum(prime_no))
   
    return Result

if __name__ == "__main__":
    user_input = int(input("Enter a number (between 2 to max 100): "))

    if user_input > 100:
        print("Please enter a number less than or equal to 100.")
    else:
        print(find_all_prime_numbers(user_input))
