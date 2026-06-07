import random
import matplotlib.pyplot as plt

T = 0
O = 1
C = 2

state = T
theta = 0.7

history = []

def instability():
    return random.random()

def transition(state):
    i = instability()

    if i > theta:
        return C

    if state == T:
        return O
    elif state == O:
        return T
    elif state == C:
        return random.choice([T, O])

for t in range(100):
    history.append(state)
    state = transition(state)

# 转换成可视化数据
x = list(range(len(history)))
y = history

plt.figure(figsize=(10,4))
plt.plot(x, y, drawstyle="steps-post")
plt.yticks([0,1,2], ["T", "O", "∅"])
plt.title("Σ-Φ-C Cognitive State Dynamics")
plt.xlabel("Time")
plt.ylabel("State")
plt.show()
