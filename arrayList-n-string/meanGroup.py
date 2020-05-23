def meanGroup(a):
    dict = {}
    output = []
    mean_order = []
    for i in range(len(a)):
        sum = 0
        for j in range(len(a[i])):
            sum += a[i][j]
        mean = sum/len(a[i])
        if mean not in dict.keys():
            dict[mean] = [i]
        else:
            dict[mean].append(i)
        if mean not in mean_order:
            mean_order.append(mean)
    for i in range(len(mean_order)):
        output.append(dict[mean_order[i]])
    return output

a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]

print(meanGroup(a))