def distanceToStar(neighbors, star_space, starting_space, visited=None):
    visited = [] if visited is None else visited
    if starting_space != star_space:
        distance = 0
        current_space = starting_space
    else:
        distance = 1
        current_space = neighbors[starting_space]
    looking = True
    while looking is True and current_space != star_space:
        if current_space in visited:
            distance -= 1
            looking = False
        else:
            visited.insert(0, current_space)
            if isinstance(current_space, list):
                min_junction_dist = float("inf")
                for x in current_space:
                    choice_distance = distanceToStar(neighbors, star_space, x, visited)
                    if choice_distance < min_junction_dist:
                        min_junction_dist = choice_distance
                distance += min_junction_dist
            else:
                current_space = neighbors[current_space]
                if (current_space != star_space):
                    distance += 1
    return distance


neighbors = [1, 2, 3, 4, [5, 20], 6, 7, 8, 9,
             10, 11, 12, 13, 14, 15, 16, 17,
             18, 19, 0, 21, 22, 23, 14]
star_positions = [3, 6, 9, 12, 15, 18]
junctions = []
for x in range(0, len(neighbors)):
    if isinstance(neighbors[x], list):
        junctions.append(x)

# neighbors = [1, 2, 3, [4, 7], 5, 6, 0, [8, 9], 9, 0]  # hard
# neighbors = [1, 2, 3, [4, 5], 6, 1, 0]  # medium
# neighbors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # easy
# neighbors = [1, 2, 3, 4, 0]  # v easy

dist = []
ddddist = []
for x in star_positions:
    for y in range(0, len(neighbors)):
        dist.append(distanceToStar(neighbors, x, y))
    ddddist.append(dist)
    dist = []

for x in range(len(ddddist)):
    raise("junctions contains a list of all addresses of junctions, use it to pick the shortest path for a junction space (which should have a distances of zero)")
    print(f"{ddddist[x]}")
