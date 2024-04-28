def main(N, M, P, C, D, rudolphPosition, santaList):
    directions8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    directions4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    santas = {santa[0]: tuple(santa[1:]) for santa in santaList}
    santaScores = {santa[0]: tuple(santa[1:]) for santa in santaList}
    knockedOut = set()
    stunned = dict()

    def updateStunned(turn):
        removes = [s for s in stunned if turn > stunned[s]]
        for remove in removes:
            del stunned[remove]

    def findClosestSanta():
        MAX = int(1e9)
        closest, minDist = None, MAX
        for santa, position in santas.items():
            if santa not in knockedOut:
                currentDist = dist(rudolphPosition, position)
                if currentDist < minDist:
                    closest, minDist = position, currentDist
        return closest, minDist

    def moveRudolph():
        closestSanta, minDist = findClosestSanta()
        if closestSanta:
            pass

    def dist(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    for turn in range(1, M+1):
        updateStunned(turn)
        moveRudolph()



if __name__ == '__main__':
    N, M, P, C, D = map(int, input().split())
    Rr, Rc = map(int, input().split())
    rudolphPosition = [Rr, Rc]
    santaList = list()
    for _ in range(P):
        santaList.append(list(map(int, input().split())))

    main(N, M, P, C, D, rudolphPosition, santaList)