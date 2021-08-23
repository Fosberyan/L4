from sys import argv


def zp():
    try:
        time, money, kpi = map(float, argv[1:])
        print(f"<Баблосики> - {time * money + kpi}")
    except ValueError:
        print("Ведите в следующим прядке дни -> зп день -> премия")


zp()
