from datetime import datetime

p = 1.02030239239

b = '%.1f' % p

print(b)

t = datetime.strptime('2018-9-8', '%Y-%m-%d').strftime('%Y-%m-%d')

print(t)