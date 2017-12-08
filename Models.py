def k_near_recommend(k1, k2, k3, man1, man2, man3, row,data):
    for i in range(1, row):
        if int(data[man1][i]) > 0 and int(data[man2][i]) > 0 and int(data[man3][i]) > 0:
            res = k1 * int(data[man1][i]) + k2 * int(data[man2][i]) + k3 * int(data[man3][i])
            if res >= 3:
                print(data[0][i])
    return