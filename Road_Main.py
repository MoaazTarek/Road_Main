import itertools
crew_id_1 = [4, 5, 1, 4, 2]   
job_id_1 = [4, 4, 7, 9, 10]
comb = []
crew_id_1_per = itertools.permutations(crew_id_1, len(job_id_1))
for each_permutation in crew_id_1_per:
    zipped = zip(each_permutation, job_id_1)
    comb.append(list(zipped))    
#print(comb)
dist_lst = []
for i in comb:
    distance = 0
    for x,y in i:
        distance = distance + abs(x-y)
    dist_lst.append(distance)
min_dist = min(dist_lst)
min_distribution = comb[dist_lst.index(min_dist)]   
print(min_dist)
print(min_distribution)     
