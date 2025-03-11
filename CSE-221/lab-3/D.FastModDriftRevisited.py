def solve():
    T = int(input())  # Number of test cases
    for _ in range(T):
        a, n, m = map(int, input().split())
        
        # Calculate the sum of the first n integers modulo m
        sum_n = (n * (n + 1) // 2) % m
        
        # Calculate the final result modulo m
        result = (a * sum_n) % m
        
        print(result)

# Run the function
solve()
