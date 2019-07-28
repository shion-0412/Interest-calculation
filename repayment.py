import sys

if len(sys.argv) == 1:
    print("error : Please type either argument, \"ganri\" or \"gankin\"")

elif sys.argv[1] == "gankin":
    prc = input("type the principal (yen): ")
    prc = int(prc)
    times = input("type the number of repayment: ")
    times = int(times)
    intr = input("type the interest rate (%): ")
    intr = float(intr) * 0.01
    ev_prc = prc / times
    tl_rep = 0
    cur_rm = prc
    print("time--repayment--interest--remains")
    for j in range(1, times+1):
        ev_intr = prc * intr * (1 - (j - 1) / times)
        ev_rep = ev_prc + ev_intr
        tl_rep = tl_rep + ev_rep
        cur_rm = cur_rm - ev_rep + ev_intr
        print('{:*>3}'.format(j) + "---" + '{:,}'.format(int(ev_rep)) + "--" + '{:,}'.format(int(ev_intr)) + "--" + '{:,}'.format(int(cur_rm)))
    print("Total repayment: " + '{:,}'.format(int(tl_rep)) + " yen.")
    tl_intr = tl_rep - prc
    print(" Total interest: " + '{:,}'.format(int(tl_intr)) + " yen.")
    sys.exit()

elif sys.argv[1] == "ganri":
    prc = input("type the principal (yen): ")
    prc = int(prc)
    times = input("type the number of repayment: ")
    times = int(times)
    intr = input("type the interest rate (%): ")
    intr = float(intr) * 0.01
    ev_rep = prc * intr * (1 + intr) ** times / (((1 + intr) ** times) - 1)
    tl_rep = 0
    cur_rm = prc
    print("time--repayment--interest--remains")
    for j in range(1, times+1):
        ev_intr = cur_rm * intr
        tl_rep = tl_rep + ev_rep
        cur_rm = cur_rm - ev_rep + ev_intr
        print('{:*>3}'.format(j) + "---" + '{:,}'.format(int(ev_rep)) + "--" + '{:,}'.format(int(ev_intr)) + "--" + '{:,}'.format(int(cur_rm)))
    print("Every repayment: " + '{:,}'.format(int(ev_rep)) + " yen.")
    print("Total repayment: " + '{:,}'.format(int(tl_rep)) + " yen.")
    tl_intr = tl_rep - prc
    print(" Total interest: " + '{:,}'.format(int(tl_intr)) + " yen.")
    sys.exit()

else:
    print("error : Please type correct argument, \"ganri\" or \"gankin\"")
