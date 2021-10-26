class Node:
    def __init__(self, state, action, turn: int):
        self.state = state
        self.turn = turn
        self.action = action
        self.child = []
        self.best = -1
        self.score = 0

    def add_child(self, child):
        self.child.append(child)

    def set_best(self, best: int):
        self.best = best

    def set_score(self, score: int):
        self.score = score

    def print_route(self):
        print(self.state)
        if len(self.child) > 0:
            self.child[self.best].print_route()
        else:
            print("Wins: ", -self.turn)

    def print_tree(self):
        print(self.state)
        for c in self.child:
            c.print_tree()


def generate_tree(root: Node):
    if root.state == (0, 0):
        root.set_score(-root.turn)
        return
    l_max = root.state[0]
    r_max = root.state[1]

    if root.turn == 1:
        next_turn = -1
    else:
        next_turn = 1

    for i in range(1, l_max + 1):
        new_state = (root.state[0] - i, root.state[1])
        c = Node(new_state, (-i, 0), next_turn)
        generate_tree(c)
        root.add_child(c)

    for i in range(1, r_max + 1):
        new_state = (root.state[0], root.state[1] - i)
        c = Node(new_state, (0, -i), next_turn)
        generate_tree(c)
        root.add_child(c)

    if root.turn == 1:
        maxc = root.child[0].score
        maxi = 0
        for i, c in enumerate(root.child):
            if c.score > maxc:
                maxc = c.score
                maxi = i
        root.set_best(maxi)
        root.set_score(maxc)
    elif root.turn == -1:
        minc = root.child[0].score
        mini = 0
        for i, c in enumerate(root.child):
            if c.score < minc:
                minc = c.score
                mini = i
        root.set_best(mini)
        root.set_score(minc)

class Agent:
    def __init__(self, turn: int, human=False):
        self.turn = turn
        self.human = human

    def is_turn(self, turn: int):
        return self.turn == turn

    def play(self, tree: Node):
        if not self.human:
            return tree.child[tree.best].action
        else:
            while True:
                try:
                    choice = input("Your Action (n 0) or (0 n): ")
                    choice = choice.split()
                    choice = [int(i) for i in choice]
                    if choice[0] > 0 and choice[1] > 0:
                        raise Exception("Invalid")
                    elif choice[0] == 0 and choice[1] == 0:
                        raise Exception("Invalid")
                    elif choice[0] < 0 or choice[1] < 0:
                        raise Exception("Invalid")
                    return (-choice[0], -choice[1])
                except Exception:
                    print("Invalid input!")


start = input("Enter starting state: ")
start = start.split()
start = [int(i) for i in start]

a1 = Agent(1)
a2 = Agent(-1)

root = Node((start[0], start[1]), (0, 0), 1)

generate_tree(root)

state = (start[0], start[1])

while state != (0, 0):
    print("\nState:", state)
    if a1.is_turn(root.turn):
        action = a1.play(root)
        for c in root.child:
            if action == c.action:
                print("Player 1 plays", action)
                root = c
                state = (c.state[0], c.state[1])
    elif a2.is_turn(root.turn):
        action = a2.play(root)
        for c in root.child:
            if action == c.action:
                print("Player 2 plays", action)
                root = c
                state = (c.state[0], c.state[1])

if root.turn == 1:
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")
