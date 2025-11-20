import math

def calculate_lcm_gcd(X, Y):
    gcd = math.gcd(X, Y)
    lcm = (X * Y) // gcd
    return lcm, gcd

def main():
    try:
        T = int(input())
        for _ in range(T):
            X, Y = map(int, input().split())
            lcm, gcd = calculate_lcm_gcd(X, Y)
            print(f"LCM: {lcm}, GCD: {gcd}")
    except Exception as e:
        # In a real application, you'd log this error
        pass

if _name_ == "_main_":
    main
