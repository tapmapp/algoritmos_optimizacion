def torres_hanoy(N, desde, hasta):
    if N == 1:
        print("Llevar desde " + str(desde) + " hasta " + str(hasta))
    else:
        torres_hanoy(N - 1, desde, 6 - desde - hasta)
        print("Llevar desde " + str(desde) + " hasta " + str(hasta))
        torres_hanoy(N - 1, No(desde, hasta), hasta)

torres_hanoy(4, 1, 3)