print('Type the dates')

dates = []
for i in range(21):
    x = input().split('\n')
    dates.append(x)

new_dates = []
for i in dates:
    for j in i:
        day = j[8:10]
        new_date = day + '/02/2023' + j[10:]
        new_dates.append(new_date)

for i in new_dates:
    print(i)
