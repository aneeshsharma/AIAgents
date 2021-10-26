import random

class Env:
    def __init__(self, pos: int, states: list):
        self.size = len(states)
        self.states = states
        self.bot = Bot(pos, self)

    def get(self, pos: int):
        return self.states[pos]

    def suck(self, pos: int):
        if self.states[pos] == 0:
            return False
        else:
            self.states[pos] = 0
            return True

    def cap(self, new_pos: int):
        if new_pos < 0:
            return 0
        elif new_pos > self.size - 1:
            return self.size - 1
        else:
            return new_pos

    def step(self):
        self.bot.step()

    def is_clean(self):
        return sum(self.states) == 0

    def __str__(self):
        s = ["+", "-", "-", "-"] * self.size + ["+"]
        s += ["\n"]
        s += ["|", " ", " ", " "] * self.size + ["|"]
        s += ["\n"]
        s += ["|", " ", " ", " "] * self.size + ["|"]
        s += ["\n"]
        s += ["+", "-", "-", "-"] * self.size + ["+"]

        for i in range(len(self.states)):
            if self.states[i] > 0:
                s[8 * self.size + 4 + 4*i + 2] = "#"

        s[4*self.size + 2 + 4*self.bot.pos + 2] = "B"

        return "".join(s)

    def display(self):
        s = ""
        s += f'Bot: {self.bot.pos}'
        s += f'Env: {self.states}'
        return s

class Bot:
    def __init__(self, pos: int, env: Env):
        self.pos = pos
        self.env = env
        self.score = 0

    def step(self):
        state = self.env.get(self.pos)
        if state > 0:
            if self.env.suck(self.pos):
                self.score += 1

        if random.random() > 0.5:
            self.move(1)
        else:
            self.move(-1)

    def move(self, direction: int):
        d = 0
        if direction < 0:
            d = -1
        elif direction > 0:
            d = 1

        new_pos = self.env.cap(self.pos + d)

        self.pos = new_pos

def permutation(states, size):
    if size <= 0:
        return [[]]
    l = []
    for s in states:
        for n in permutation(states, size - 1):
            x = [s]
            x.extend(n)
            l.append(x)
    return l

size = 2

env_states = permutation([0, 1], size)

envs = []

for i in [0, 1]:
    for states in env_states:
        envs.append(Env(i, [_ for _ in states]))

for i in range(len(envs)):
    env = envs[i]
    print("Scenario: ", i + 1)
    print("Initial state:")
    print(env)
    print("Simulating...")
    for j in range(1000):
        if env.is_clean():
            break
        env.step()

    print("Score: ", env.bot.score)
    print()
