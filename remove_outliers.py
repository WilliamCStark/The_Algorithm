file = open('delta_v_time.csv')
times = list()
vals = list()
for line in file:
    line = line.split(',')
    times.append(float(line[0]))
    vals.append(float(line[1]))
file.close()
vals = sorted(vals)
q1 = vals[int(len(vals) / 4)]
q3 = vals[int(3*len(vals)/4)]
iqr = q3 - q1
min_outlier = q1 - 1.5*iqr
max_outlier = q3 + 1.5*iqr
new_vals = list()
file = open('delta_v_time.csv', 'w')
for i in range(len(vals)):
    if not(vals[i] > max_outlier or vals[i] < min_outlier):
        file.write(str(times[i]) + ',' + str(vals[i]) + '\n')
file.close()