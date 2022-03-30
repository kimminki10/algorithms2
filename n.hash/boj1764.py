import sys
input = sys.stdin.readline


N, M = map(int, input().split())

heard = { input().strip() for _ in range(N) }
seen = { input().strip() for _ in range(M) }

heard_and_seen = heard.intersection(seen)

print(len(heard_and_seen))
for r in sorted(heard_and_seen):
    print(r)