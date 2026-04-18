import math
import time

# Your friend's algorithm: O(n²) - Bubble Sort style
def friend_algorithm(arr):
    n = len(arr)
    instructions = 0
    # Simulating n² operations
    for i in range(n):
        for j in range(n):
            instructions += 1  # Each comparison counts
    return instructions

# Your algorithm: O(n log n) - Merge Sort style
def your_algorithm(arr):
    n = len(arr)
    instructions = 0
    # Simulating n log n operations
    for i in range(n):
        instructions += 1
    # Additional log n factor
    instructions = instructions * math.log2(n) * 50
    return int(instructions)

# Calculate actual time
def calculate_time(instructions, computer_speed):
    return instructions / computer_speed

# Test with different sizes
sizes = [1000, 10000, 100000, 1000000]
friend_speed = 1_000_000_000  # 1 billion/sec
your_speed = 10_000_000        # 10 million/sec

print("="*70)
print(f"{'n':<10} {'Friend Time':<20} {'Your Time':<20} {'Winner':<15}")
print("="*70)

for n in sizes:
    # Friend's calculation
    friend_instr = 2 * n * n
    friend_time = friend_instr / friend_speed
    
    # Your calculation
    your_instr = int(50 * n * math.log2(n))
    your_time = your_instr / your_speed
    
    winner = "YOU" if your_time < friend_time else "Friend"
    print(f"{n:<10} {friend_time:>8.2f}s       {your_time:>8.2f}s       {winner:>10}")