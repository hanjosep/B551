import sys

# run the file in cmd line: 
# python yahtzee.py 1 2 3
# returns suggestion of which roll to do,
# along with the expected value from doing that roll.
# if not written in this format: play the game itself and the game will suggest which move to do.
def score(lst):
    # return 25 if lst[0] == lst[1] and lst[1] == lst[2] else sum(lst)

    scr = 0
    if lst[0] == lst[1] and lst[1] == lst[2]:
        scr = 25
    else:
        scr = sum(lst)
    return scr


def evaluate_game(glist, roll):
    (oa,ob,oc) = glist
    
    (rea,reb,rec) = ([],[],[])
    if "a" in roll:
        for i in range(1,7):
            rea.append([i,ob,oc])
    if 'b' in roll:
        if rea != []:
            for g in rea:
                for i in range(1,7):
                    reb.append([g[0],i,g[2]])
        else:
            for i in range(1,7):
                reb.append([oa,i,oc])
    if 'c' in roll:
        if len(rea)+len(reb) > 0:
            for g in rea:
                for i in range(1,7):
                    rec.append([g[0],g[1],i])
            for g in reb:
                for i in range(1,7):
                    rec.append([g[0],g[1],i])
        else:
            for i in range(1,7):
                rec.append([oa,ob,i])
    scores = []
    if len(rec) > len(reb):
        for r in rec:
            scores.append(score(r))
    elif len(reb)>len(rea):
        scores = []
        for r in reb:
            scores.append(score(r))
    else:
        for r in rea:
            
            scores.append(score(r))
    return sum(scores)/len(scores)

def eval_full(game):
    null = score(game)
    a = evaluate_game(game,'a')
    b = evaluate_game(game,'b')
    c = evaluate_game(game,'c')
    ab = evaluate_game(game,'ab')
    bc = evaluate_game(game,'bc')
    ac = evaluate_game(game,'ac')
    abc = evaluate_game(game,'abc')
    lst = [float(null),a,b,c,ab,bc,ac,abc]
    max_value = max(lst)
    max_index = lst.index(max_value)
    if max_index == 0:
        print('no reroll')
    if max_index == 1:
        print('a')
    if max_index == 2:
        print('b')
    if max_index == 3:
        print('c')
    if max_index == 4:
        print('ab')
    if max_index == 5:
        print('bc')
    if max_index == 6:
        print('ac')
    if max_index == 7:
        print('abc')
    # print(max(lst))

    return max(lst)
import random
def roll():
    return random.randint(1,6)

# play the game:
if __name__ == "__main__":
    try:
        r = [int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])]
    except:
        print('no list made: making random roll')

        r = [roll(),roll(),roll()]
    print('you rolled: ', r)
    
    print(eval_full(r))
