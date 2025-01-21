from collections import defaultdict

def max_fruit(n, fruits):
    max_length = 0
    left = 0
    fruit_count = defaultdict(int)
    unique_fruits = 0

    for right in range(n):
        if fruit_count[fruits[right]] == 0:
            unique_fruits += 1
        fruit_count[fruits[right]] += 1

        while unique_fruits > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                unique_fruits -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

n = int(input().strip())
fruits = list(map(int, input().strip().split()))
print(max_fruit(n, fruits))