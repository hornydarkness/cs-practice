import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    valid_records = read_valid(lines)
    
    non_empty = [line for line in lines if line.strip()]
    skipped_count = len(non_empty) - len(valid_records)
    
    averages = average_by_city(valid_records)
    best = warmest_city(valid_records)
    
    print(len(valid_records))
    print(skipped_count)
    if best:
        print(f"{averages[best]:.1f}")
    else:
        print("0.0")

if __name__ == "__main__":
    main()