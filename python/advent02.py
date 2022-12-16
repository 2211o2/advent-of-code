import sys

points = {
    'win':  6,
    'draw': 3,
    'loss': 0,
}

hands = {
    'X': 1,     # rock
    'Y': 2,     # paper
    'Z': 3      # scissors
}

# part one
rounds = {
   # O P : outcome
    'A X': "draw",
    'A Z': "loss",
    'A Y': "win",
    'B X': "loss",
    'B Y': "draw",
    'B Z': "win",
    'C X': "win",
    'C Y': "loss",
    'C Z': "draw"
}

# part two
# deffo a cleaner way to do this but idgaf
strategies = {
    # Desired outcome: { Opponent: Required round } 
    'X': {             # lose
        'A': 'A Z',
        'B': 'B X',
        'C': 'C Y'
    },
    'Y': {            # draw
        'A': 'A X',
        'B': 'B Y',
        'C': 'C Z'
    },
    'Z': {            # win
        'A': 'A Y',
        'B': 'B Z',
        'C': 'C X'
    }
}

def main():
    with open(sys.path[0] + '/../inputs/input02') as file:
        lines = file.readlines()

    score1 = first_strategy(lines)      # part one
    score2 = second_strategy(lines)     # part two
    
    print("Score 1: ", score1,
    "      Score 2: ", score2)

def first_strategy(lines):
    score = 0

    for l in lines:
        score += points[ rounds[l.split("\n")[0]] ]
        score += hands[l.strip()[-1]]

        print("Round ", l.split("\n")[0],
        "      Outcome points:", points[rounds[l.split("\n")[0]]],
        "      Hand points:", hands[l.strip()[-1]])

    return score

# reuses code from part 1 but also idgaf enough
def second_strategy(lines):
    score = 0

    for l in lines:
        rnd = strategies[ l.strip()[-1] ][ l.split()[0] ]
        score += points[ rounds[rnd] ]
        score += hands[ rnd.strip()[-1] ]
        
        print("Round ", rnd,
        "      Outcome points:", points[rounds[rnd]],
        "      Hand points:", hands[rnd.strip()[-1]])

    return score

if __name__ == '__main__':
    main()