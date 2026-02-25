import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    alice_w = alice_b = 0
    bob_w = bob_b = 0

    i = 1
    turn = 0  # 0 = Alice, 1 = Bob
    card_index = 0  # 0-based (even = white, odd = black)

    while n > 0:
        take = min(i, n)

        # count whites and blacks in this segment
        white = (take + (card_index % 2 == 0)) // 2
        black = take - white

        if turn == 0:
            alice_w += white
            alice_b += black
        else:
            bob_w += white
            bob_b += black

        n -= take
        card_index += take

        i += 1

        # change turn every two steps
        if (i - 1) % 2 == 1:
            turn ^= 1

    print(alice_w, alice_b, bob_w, bob_b)