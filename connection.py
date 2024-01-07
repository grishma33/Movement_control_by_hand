import subprocess,bluetooth,pyautogui
import pydirectinput,time
passkey="1234"
subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)
status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(("00:18:91:D7:D1:53",1))
while 1:
    x=sock.recv(1024)
    x=x.decode()
    if x=="w":
        pydirectinput.keyDown("w")
        time.sleep(0.6)
        pydirectinput.keyUp("w")
    elif x=="a":
        pydirectinput.keyDown("a")
        time.sleep(0.6)
        pydirectinput.keyUp("a")
    elif x=="s":
        pydirectinput.keyDown("s")
        time.sleep(0.6)
        pydirectinput.keyUp("s")
    elif x=="d":
        pydirectinput.keyDown("d")
        time.sleep(0.6)
        pydirectinput.keyUp("d")
    elif x=="q":
        pydirectinput.keyDown("w")
        pydirectinput.keyDown("a")
        time.sleep(0.6)
        pydirectinput.keyUp("a")
        pydirectinput.keyUp("w")
    elif x=="e":
        pydirectinput.keyDown("w")
        pydirectinput.keyDown("d")
        time.sleep(0.6)
        pydirectinput.keyUp("d")
        pydirectinput.keyUp("w")
    elif x=="c":
        pydirectinput.keyDown("s")
        pydirectinput.keyDown("d")
        time.sleep(0.6)
        pydirectinput.keyUp("d")
        pydirectinput.keyUp("s")
    elif x=="z":
        pydirectinput.keyDown("s")
        pydirectinput.keyDown("a")
        time.sleep(0.6)
        pydirectinput.keyUp("a")
        pydirectinput.keyUp("s")
