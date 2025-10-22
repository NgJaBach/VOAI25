import math

n = int(input())
nums = list(map(int, input().split()))

# Mean
mean = sum(nums) / n

# Median
nums_sorted = sorted(nums)

if n % 2 == 0:
    median = (nums_sorted[n // 2 - 1] + nums_sorted[n // 2]) / 2
else:
    median = nums_sorted[n // 2]

# Mode
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1 # Create new key if none
    
max_freq = max(freq.values())
modes = [k for k, v in freq.items() if v == max_freq]
mode = min(modes)

# SD
std = math.sqrt(sum((x - mean) ** 2 for x in nums) / n)

# Confidence
z = 1.96
margin_error = z * std / math.sqrt(n)
lwb = mean - margin_error
upb = mean + margin_error

print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)
print(f"{std:.1f}")
print(f"{lwb:.1f} {upb:.1f}")