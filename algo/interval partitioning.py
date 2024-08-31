def interval_partitioning(intervals):

    intervals.sort(key=lambda x: x[0])
    print(intervals)
    print(intervals[-1][1])
    resources = []

    for interval in intervals:
        placed = False
        for resource in resources:
            print("resource",resource, end = ' ')
            if resource[-1][1] <= interval[0]:
                print("add")
                print(interval)
                resource.append(interval)
                placed = True
                break

        if not placed:
            print("new")
            print(interval)
            resources.append([interval])

    return resources


intervals = [(0, 3), (1, 4), (4, 7), (8, 11), (9, 11), (2, 7), (6, 10), (7, 12), (5, 9)]
resources = interval_partitioning(intervals)
print(f"Number of resources needed: {len(resources)}")
for i, resource in enumerate(resources, 1):
    print(f"Resource {i}: {resource}")
