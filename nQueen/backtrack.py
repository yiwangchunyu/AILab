global N  # 皇后个数
# global x  # 当前解
global SUM  # 当前已找到的可行方案数
# N = 4
SUM = 0


def print_solution(x):
    fo = open("backtrack_" + str(N) + ".txt", "a")
    fo.write("(")
    for i in range(len(x) - 1):
        fo.write(str(x[i]) + ",")
    fo.write(str(x[len(x) - 1]) + ")" + "\n")
    fo.close()


def is_safe(k):
    for i in range(k):
        if (x[i] == x[k]) or (abs(x[i] - x[k]) == (k - i)):
            return False
    return True


def backtrack(t):
    if t >= N:
        global SUM
        SUM += 1
        print_solution(x)
    else:
        for i in range(N):
            x[t] = i
            if is_safe(t):
                backtrack(t + 1)


if __name__ == "__main__":
    for k in range(4, 50):
        global N
        N = k

        x = [0 for i in range(N)]
        backtrack(0)
        print("sum =" + str(SUM))
        fo = open("backtrack_" + str(N) + ".txt", "a")
        fo.write("sum =" + str(SUM) + "\n")
        fo.close()

        SUM = 0


