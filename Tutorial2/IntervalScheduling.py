Intervals = [[1,2],[1.3,2],[1.5,3],[2,5],[1,5],[2,2.5]]

    

def schedule(intervals: list):
    intervals.sort(key = lambda x: x[1])
    schedule = []
    for I in intervals:
        if schedule == []:
            schedule.append(I)
        elif I[0] >= schedule[-1][1]:
            schedule.append(I)
    return schedule

print(schedule(Intervals))

def partition(intervals: list):
    intervals.sort(key= lambda x:x[0])
    intervals.append("end")
    partition = {}
    p = 0
    j = 0
    while intervals[j] != "end":
        if j == 0:
            partition[p] = [intervals[j]]
        elif intervals[j][0] >= intervals[j-1][1]:
            partition[p].append(intervals[j])
        else:
            p += 1
            partition[p] = []
            partition[p].append(intervals[j])
        j += 1
    return partition
        
print(partition(Intervals))
