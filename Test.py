gamma = 0.9
x = 0.01
y = 0

R = [0, 0, 1, 10]
V = R
V_buffer = [0, 0, 0, 0]
all_transitions = [(1, 0, 1), (1, 0, 3), (2, 0, 0), (2, 0, 3), (3, 0, 0), (0, 1, 1), (0, 2, 2)]
epsilon = 0.0001

def get_P(s,a,s_prime):
    match s, a, s_prime:
        case 1, 0, 1:
            return 1-x
        case 1, 0, 3:
            return x
        case 2, 0, 0:
            return 1-y
        case 2, 0, 3:
            return y
        case 3, 0, 0:
            return 1
        case 0, 1, 1:
            return 1
        case 0, 2, 2:
            return 1

def get_Q(s, a):
    sum = 0
    for transition in all_transitions:
        if transition[0]==s and transition[1]==a:
            sum += get_P(s, a, transition[2]) * V[transition[2]]
    return gamma * sum + R[s]

def get_all_Q(s):
    Q_list = []
    for a in range(4):
        Q_list.append(get_Q(s, a))
    return Q_list

def test_epsilon():
    for s in range(4):
        if abs(V[s]-V_buffer[s]) > epsilon:
            return False
    return True

def get_pi_s(all_Q):
    max = 0
    max_index = 0
    for i in range(4):
        Q = all_Q[i]
        if Q > max:
            max = Q
            max_index = i
    return max_index

"""
Main loop
"""
while(True):
    pi = []
    for s in range(4):
        all_Q = get_all_Q(s)
        V_buffer[s] = max(all_Q)
        pi.append(get_pi_s(all_Q))
    if (test_epsilon()):
        break
    V = V_buffer.copy()
    print(f"V : V(S_0) = {V[0]}, V(S_1) = {V[1]}, V(S_2) = {V[2]}, V(S_3) = {V[3]}")
    print(f"pi : pi(S_0) = a{pi[0]}, pi(S_1) = a{pi[1]}, pi(S_2) = a{pi[2]}, pi(S_3) = a{pi[3]}")
print("-------------------------------------------")
print("----------------FINAL-RESULT---------------")
print("-------------------------------------------")
print(f"V : V(S_0) = {V[0]}, V(S_1) = {V[1]}, V(S_2) = {V[2]}, V(S_3) = {V[3]}")
print(f"pi : pi(S_0) = a{pi[0]}, pi(S_1) = a{pi[1]}, pi(S_2) = a{pi[2]}, pi(S_3) = a{pi[3]}")