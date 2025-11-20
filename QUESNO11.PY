def calculate_duration(SH, SM, EH, EM):
    start_time = SH * 60 + SM
    end_time = EH * 60 + EM
    duration = end_time - start_time
    hours = duration // 60
    minutes = duration % 60
    return f"{hours} hours {minutes} minutes"

def main():
    try:
        N = int(input())
        for _ in range(N):
            SH, SM, EH, EM = map(int, input().split())
            print(calculate_duration(SH, SM, EH, EM))
    except Exception as e:
        # In a real application, you'd log this error
        pass

if _name_ == "_main_":
    main()
