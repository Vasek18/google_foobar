def solution(entrances, exits, path):
    entranceRoomsNumber = len(entrances)
    exitRoomsNumber = len(exits)
    roomsNumber = len(path)

    savedBunniesCount = 0

    for roomNumber in range(roomsNumber):
        if roomNumber in entrances: 
            continue
        if roomNumber in exits: 
            continue

        corridorToRoomCapacity = 0                             
        for entrance in entrances:
            corridorToRoomCapacity += path[entrance][roomNumber]

        roomCapacity = sum(path[roomNumber])
        
        savedBunniesCount += min(roomCapacity, corridorToRoomCapacity)

    return savedBunniesCount