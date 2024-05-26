def longest_mountain(heights, left, right):
    max_length = 0
    n = len(heights)
    
    for i in range(left + 1, right):
        
        if heights[i - 1] < heights[i] > heights[i + 1]:
            l = i
            r = i
            
           
            while l > left and heights[l - 1] < heights[l]:
                l -= 1
            
            
            while r < right and heights[r + 1] < heights[r]:
                r += 1
            
          
            max_length = max(max_length, r - l + 1)
    
    return max_length
def solve(heights, queries):
    results = []
    for left, right in queries:
        results.append(longest_mountain(heights, left, right))
    return results

if __name__ == "__main__":
    n = int(input())
    heights = [int(x) for x in input().split()]
    q = int(input())
    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append((l - 1, r - 1))  

    results = solve(heights, queries)
    for result in results:
        print(result)
        


