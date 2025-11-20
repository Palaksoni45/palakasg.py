def max_lemon_cakes(N):
    return max(N % A for A in range(1, N))

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(max_lemon_cakes(N))

if _name_ == "_main_":
    main()
