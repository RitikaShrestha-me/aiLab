from math import inf

alpha, beta = -inf, inf
nodeIndex = 0
Depth = 3
Children = 2

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == Depth:
        return values[nodeIndex] #if explored depth is equal to max Depth return the node

    if maximizingPlayer: #for maximizing the player
        best = -inf 
        for i in range(0, Children):
            if alpha < beta:
                val = alphabeta(depth + 1, nodeIndex * Children +
                                i, False, values, alpha, beta) #calculate the value
                best = max(val, best)
                alpha = max(alpha, best)
                print("depth: ", depth)
                print(f'value: {val} alpha: {alpha} beta: {beta}')
        return best
    else: #for minimizing the player.
        best = inf
        for i in range(0, Children):
            if alpha < beta:
                val = alphabeta(depth+1, nodeIndex*Children +
                            i, True, values, alpha, beta) # calculate the value
                best = min(val, best)
                beta = min(beta, best)
                print("depth: ", depth)
                print(f'value: {val} alpha: {alpha} beta: {beta}')
        return best

if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]  # depth 3, child 2
    print("The optimal value is:", alphabeta(
        0, nodeIndex, True, values, alpha, beta))