import sys

m = int(sys.stdin.readline())
s = set()

for i in range(m):
  l = list(sys.stdin.readline().split())
  c = l[0]

  if c == 'add':
    s.add(int(l[1]))
  
  elif c == 'remove':
    try:
      s.remove(int(l[1]))
    except:
      pass
  
  elif c == 'check':
    if int(l[1]) in s:
        print(1)
    else:
      print(0)
  
  elif c == 'toggle':
    if int(l[1]) in s:
      s.remove(int(l[1]))
    else:
      s.add(int(l[1]))
  
  elif c == 'all':
    s = set([i for i in range(1,21)])
  
  else:
    s = set()