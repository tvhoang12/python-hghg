def minimum_time_to_print(N, X, Y, Z):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        dp[i] = min(dp[i], dp[i - 1] + X)  # Thực hiện thao tác insert
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + Z)  # Thực hiện thao tác copying

    for i in range(1, N + 1):
        if i < N:
            dp[i + 1] = min(dp[i + 1], dp[i] + X)  # Thực hiện thao tác insert
        if i * 2 <= N:
            dp[i * 2] = min(dp[i * 2], dp[i] + Y)  # Thực hiện thao tác delete

    return dp[N]

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X, Y, Z = map(int, input().split())
        result = minimum_time_to_print(N, X, Y, Z)
        print(result)

if __name__ == "__main__":
    main()
