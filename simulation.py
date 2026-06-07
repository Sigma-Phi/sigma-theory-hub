import random

# 三个状态
T = "GENERATION"
O = "CORRECTION"
C = "COLLAPSE"

# 初始状态
state = T

# 参数
theta = 0.7  # 失稳阈值

def instability():
    return random.random()

def transition(state):
    i = instability()

    # ∅：失稳
    if i > theta:
        return C

    # 状态切换逻辑
    if state == T:
        return O
    elif state == O:
        return T
    elif state == C:
        # collapse 后重启
        return random.choice([T, O])

# 模拟运行
for t in range(20):
    print(t, state)
    state = transition(state)
