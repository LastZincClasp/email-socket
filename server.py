import cal

def main():
    c = cal.Lib()
    while 1:
        a = c.recv()
        if a == {}:
            pass
        else:
            if a["1"]["cmd"] == "print":
                print(a["1"]["msg"])
                c.send("2", {"cmd": "recv",
                "msg": "SUCCESS"})
                break


if __name__ == "__main__":
    main()