def ack(m, n):
    """Return result of Ackermann function."""
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    if m < 0 or n < 0:
        return none

wiki = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 5, 7, 9, 11, 5, 13, 29, 61, 125]

my_list = []

if __name__ == "__main__":
    for i in range(4):
        for j in range(5):
            my_list.append(ack(i, j))

    if wiki == my_list:
        print(u"All Tests Pass")

