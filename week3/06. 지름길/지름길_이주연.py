import collections

n, d = map(int, input().split())
dict = collections.defaultdict(list) # dict[key(end)] = {[val(start), val(short_value)], ... }
dp = [0 for _ in range(d+1)] # save min_dis

# save short_cut information
for i in range(n):
    s, e, m = map(int, input().split())
    dict[e].append([s, m])
# calculate dp

for i in range(d+1):
    dp[i] = dp[i - 1] + 1
    if i in dict:
        for s, v in dict[i]:
            dp[i] = min(dp[i], dp[s]+v)
print(dp[d]-1)

