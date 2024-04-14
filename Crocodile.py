def min_water_tap_openings(n, test_cases):
    results = []
    for i in range(n):
        h, c, k = test_cases[i]
        if k >= h:
            results.append(1)
        elif k <= c:
            results.append(-1)
        else:
            num_hot_tap_openings = (k - c) // (2 * c - h)
            
            temp = h + num_hot_tap_openings * (h - c)

            if temp >= k:
                 results.append(num_hot_tap_openings * 2 + 1)
            else:
                results.append(num_hot_tap_openings * 2 + 2) 
    return results


n = int(input("Enter the number of test cases: "))

test_cases = []
for i in range(n):
    h, c, k = map(int, input(f"Enter the values for test case {i+1} (hot water, cold water, desired temperature) ").split())
    test_cases.append([h, c, k])

output = min_water_tap_openings(n, test_cases)
for result in output:
    print(result)