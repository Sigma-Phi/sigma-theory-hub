# Σ-Φ-C 理论核心（数学形式化）

## 1. 系统定义

C = ⟨S, Δ, I⟩

S ∈ {T, O, ∅}

---

## 2. 状态转移

S_{t+1} ~ P(S | S_t, I_t)

---

## 3. 失稳函数

定义：

p_c = σ(I(S_t) - θ)

σ(x) = 1 / (1 + e^{-x})

---

## 4. 转移概率

P(∅ | S_t) = p_c

P(O | T) = 1 - p_c  
P(T | O) = 1 - p_c  

---

## 5. ∅状态定义

∅ = reconfiguration state

P(S_{t+1} | ∅) = Uniform({T, O})

---

## 6. 熵

H(S) = - Σ P(S_t) log P(S_t)
