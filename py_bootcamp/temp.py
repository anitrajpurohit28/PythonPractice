txt = """5m 42s
2m 28s
3m 35s
3m 38s
1m 26s
1m 49s
2m 47s
1m 25s
3m 20s
3m 15s
1m 16s
1m 22s
3m 40s
2m 30s
4m 42s
2m 21s
1m 1s
4m 54s
1m 5s
6m 53s
2m 26s
54s
2m 31s
3m 5s
5m 4s
1m 5s
1m 51s
1m 30s
5m 50s
2m 6s
2m 54s
2m 15s
2m 8s
2m 0s
49s
4m 24s
2m 17s
2m 38s
6m 2s
1m 49s
5m 27s
3m 39s
4m 1s
7m 26s
7m 26s
3m 3s
1m 48s
1m 30s
2m 52s
59s
1m 51s
2m 26s
2m 30s
1m 43s
2m 10s
2m 41s
5m 42s
10m 31s
3m 6s
5m 46s
2m 54s
1m 43s
5m 21s
2m 0s
3m 35s
1m 14s
54s
2m 54s
12m 46s
3m 41s
4m 18s
1m 39s
3m 27s
1m 46s
41s
1m 58s
2m 43s
1m 37s
2m 24s
58s
58s
1m 47s
1m 46s
3m 36s
3m 50s
1m 44s
2m 34s
1m 7s
2m 44s
1m 17s
3m 45s
1m 44s
1m 57s
2m 32s
1m 50s
1m 16s
1m 39s
2m 10s
1m 28s
5m 6s
1m 19s
5m 18s
2m 18s
2m 26s
2m 40s
2m 36s
3m 21s
1m 37s
4m 30s
1m 10s
2m 2s
43s
4m 22s
2m 0s
3m 3s
3m 55s
5m 30s
1m 4s
2m 48s
4m 1s
4m 34s
3m 56s
3m 20s
4m 27s
2m 37s
3m 43s
1m 21s
1m 38s
6m 4s
2m 4s
2m 45s
2m 10s
2m 47s
1m 11s
1m 43s
2m 16s
58s
4m 41s
2m 46s
1m 16s
2m 56s
3m 41s
3m 5s
5m 7s
2m 59s
4m 25s
11m 35s
1m 55s"""

# import re
#
# for line in txt.split('\n'):
#     res = re.sub(r'(?P<min>\d+)*m* *(?P<sec>\d+)*s',r'\g<min>.\g<sec>', line)
#     print(res)

txt2 = """58s,
11m 35s,
1m 55s,
43s,
56s
"""
import re

for line in txt.split('\n'):
    #print(line, end='\t')
    res = re.search(r'(?:(\d+)m )*(?:(\d+)s)*', line)
    sec = 0
    if res.group(1):
        sec += int(res.group(1))*60
    if res.group(2):
        sec += int(res.group(2))
    print(sec)
