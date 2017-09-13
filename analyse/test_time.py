import time

t0 = time.mktime(time.strptime('2017-9-10', '%Y-%m-%d'))

t1 = time.mktime(time.strptime('2017-9-12', '%Y-%m-%d'))

if t1 + 1* 24 *3600 < t0:
    
    print('ok')