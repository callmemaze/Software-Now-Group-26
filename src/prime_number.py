"""
    Checks if the the total count of prime numbers found
        • the smallest and largest prime number in the range
        • the sum of all prime numbers found
"""
def find_all_prime_numbers(user_input: str) -> str:


   
   
 return "True"

if __name__ == "__main__":
    user_input = int(input("Enter a number (max 100): "))

    if user_input > 100:
        print("Please enter a number less than or equal to 100.")
    else:
        find_all_prime_numbers(user_input)