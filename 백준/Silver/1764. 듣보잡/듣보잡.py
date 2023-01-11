n, m = map(int, input().split())
n_lst = set()
for i in range(n):
    n_lst.add(input())

m_lst = set()
for i in range(m):
    m_lst.add(input())

print_lst = sorted(list(n_lst & m_lst))

print(len(print_lst))
for i in print_lst:
    print(i)