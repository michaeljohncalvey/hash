import math


def calculate_hash_collision_probability(n, k):
    """
    Calculate the probability of a hash collision for an n-bit hash function with k strings hashed.
    """
    prob_unique = 1.0
    N = 2**n

    for i in range(1, k):
        prob_unique = prob_unique * (N - (i - 1)) / N

    approx_prob = (k ** 2) / (2 * N)
    return (prob_unique, approx_prob)


def main():
    """
    Main function.
    """
    print("The probability of a hash collision is: ",
          calculate_hash_collision_probability(32, 200000))


if __name__ == "__main__":
    main()
