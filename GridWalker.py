"""
Hello,

I am fully aware that this code is a little rough. First time with Python.
Remember that my goal is functionality, not style or even good code.
"""

# Given an array of neighbors,
# return the shortest path to star given a starting position


def distanceToStar(neighbors, star_space, starting_space, visited=None):
    # initialize an empty array of visited spaces
    # (unless there's already a visited list)
    visited = [] if visited is None else visited

    # If the starting space is the star, the player is actually
    # in front of the star, so scoot them forward

    # if starting_space != star_space:
    #     distance = 0
    #     current_space = starting_space
    # else:
    #     distance = 1
    #     current_space = neighbors[starting_space]
    distance = 0
    current_space = starting_space
    looking = True
    while looking is True and current_space != star_space:
        if current_space in visited:
            # If we've already visited this space, we bail out
            # Mario party boards are monodirectional (thank god)
            # So we know a visited space means we're good to stop looking
            distance -= 1
            looking = False
        else:
            # Add this space to our visited spaces
            visited.insert(0, current_space)

            if isinstance(current_space, list):
                # We've hit a junction! We need to find the shortest path
                # for a player on this junction
                min_junction_dist = float("inf")
                # Make the current distance infinity so anything is smaller
                for x in current_space:
                    # Recurse with every option of the junction as our starting space,
                    # keeping our visited spaces array so we don't loop forever
                    choice_distance = distanceToStar(
                        neighbors, star_space, x, visited)
                    if choice_distance < min_junction_dist:
                        # find the shortest junction option distance
                        min_junction_dist = choice_distance
                distance += min_junction_dist
            else:
                # scoot forward
                # if current_space is the star_space, the while loop will break
                current_space = neighbors[current_space]
                if (current_space != star_space):
                    distance += 1
    # return the distance traveled required to find the star
    return distance


# neighbors = [1, 2, 3, 4, [5, 20],
#              6, 7, 8, 9, 10,
#              11, 12, 13, 14,
#              15, 16, 17, 18,
#              19, 0, 21, 22, 23,
#              14]
star_positions = [16, 12, 21, 27, 32, 41]
# checked spaces [16, 12, x21x, ]

neighbors = [1, 2, 3, 4, [5, 21, 25], 5, 6, [8, 15], 9, 10,
             11, 12, 13, 14, 0, 16, 17, 18, 19, 20, 9, 22, 23,
             24, 6, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, [37, 40],
             38, 39, 22, 41, 42, 43, 44, 45, 46, 36]

for x in range(len(neighbors)):
    print(f"neighbors[{x}] = {neighbors[x]}")

junctions = []
for x in range(0, len(neighbors)):
    if isinstance(neighbors[x], list):
        junctions.append(x)

dist = []
ddddist = []
for x in star_positions:
    for y in range(0, len(neighbors)):
        dist.append(distanceToStar(neighbors, x, y))
    ddddist.append(dist)
    dist = []

shortest_paths = [[0] * len(junctions) for i in range(len(star_positions))]
for x in range(len(ddddist)):
    print(f"{ddddist[x]} {len(ddddist[x]) = }")

    # ddddist is an array of an array of distances
    # the index of the first level is tied to the array of star_positions
    # the index of the second level is the space's distance to the star given the star_position
    # so ddddist[0][0] is the distance to the star for the first space when the star is in its first position
    for junction in junctions:
        shortest_choice = 0
        for option in range(0, len(neighbors[junction])):
            # Sorry about this
            # Remember how ddddist works above
            # junction is the address of the junctions, option is between 0 and the number of options at the current junction
            # so if the current junction option's distance is lower than the current shortest_choice's distance, store that
            # shortest_choice is NOT A DISTANCE! it's an array index
            # I am also confused by it
            if ddddist[x][neighbors[junction][option]] < ddddist[x][neighbors[junction][shortest_choice]]:
                shortest_choice = option
        shortest_paths[x][junctions.index(junction)] = shortest_choice


print(f"{shortest_paths}")

for stars in range(len(ddddist)):
    for junction in range(len(junctions)):
        print(f"When the star is at {star_positions[stars]}, "
              f"the fastest choice at junction {junction} (located at {junctions[junction]}) "
              f"is {shortest_paths[stars][junction]}, to {neighbors[junctions[junction]][shortest_paths[stars][junction]]}")

raise("doesn't work with the real world. Might be because it's labeled wrong")
raise("shortest_paths is the intended output")

"""
https://csacademy.com/app/graph_editor/
0,1, 2, 3, 4, [5, 21, 25], 5, 6, 7, [8,15], 9, 10, 11, 12, 13, 14, 0,
16, 17, 18, 19, 20, 9, 22, 22, 23, 24, 6, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, [37, 40],
38, 39, 22, 41, 42, 43, 44, 45, 46, 36]


"""


"""
strn = ""
for x in ddddist:
    strn += "["
    for u in x:
        strn += str(0) + str(u) if u < 10 else str(u)
        strn += ", "
    strn += "],\n"
print(f"{strn}")

addresses = "["
for x in range(0, len(neighbors)):
    addresses += str(0) if x < 10 else ""
    addresses += str(x) + ", "
addresses += "]"
print(f"{addresses}")
"""
