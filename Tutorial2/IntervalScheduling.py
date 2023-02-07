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
    partition = []
    p = 0
    for i in range(len(intervals)):
        Ii = intervals[i]
        for j in range(i):
            Ij = intervals[j]
            if Ii[0] >= Ij[1]:
                partition.append(partition[j])
                break
        else:
            p += 1
            partition.append(p)
    partition_dict = dict(zip(partition,intervals))
    return partition_dict
        
print(partition(Intervals))
