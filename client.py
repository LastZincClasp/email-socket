import cal
import time

def main():
    c = cal.Lib()
    c.send("1", {"cmd": "print",
        "msg": "123321321123"})
    time.sleep(3)#防止误收刚才发出去的邮件，所以先等等
    while 1:
        a = c.recv()
        if a == {}:
            pass
        else:
            if a["2"]["cmd"] == "recv":
                print(a["2"]["msg"])
                break

if __name__ == "__main__":
    main()