def mean(values_list):
    return (round(sum([v[0] for v in values_list])/len(values_list), 2), round(sum([v[1] for v in values_list])/len(values_list), 2))