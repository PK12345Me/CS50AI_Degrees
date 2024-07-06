def shortest_path(actor, target):
    frontier = []
    frontier.append((None, actor))
    explored_actor = set()

    path_tracker = {actor: (None, None)}

    while frontier:  # helps remove extra line of code:

        path_tracker[actor] = (None, None)
        # if len(frontier)==0:
        # return Exception("no path")

        node = frontier[0][1]

        frontier = frontier[1:]

        if node == target:
            path = []

            current = node
            while current is not None:
                node, film = path_tracker[current]  # its a dict with unique keys
                # it generates node variable which is used later *

                if film is not None:  # there might be some in the dict - why?
                    path.append((film, current))
                    # and first element in path_tracker will be added last **
                    # this last item to be added is the first movie our main(starting) actor has done

                current = node
                # * this is where the 'node' variable is being used, to reiterate the loop
                # and traverse the path_tracker variable

            path.reverse()
            # this converts the last element(first movie of starting actor) as first

            return path
            # break

        neighbors = neighbors_for_person(node)
        explored_actor.add(node)

        for film, star in neighbors:
            if star not in explored_actor and not any(
                star == item[1] for item in frontier
            ):
                path_tracker[star] = (node, film)
                frontier.append((film, star))

    return None
