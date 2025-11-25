import pynput as py
keyboard = py.keyboard.Controller()
try :
    while True:
        count = 0

        def on_click(x, y, button, pressed):
            global click
            if pressed :
                if button == py.mouse.Button.left :
                    click = 1

        listener = py.mouse.Listener(on_click=on_click)
        entry = input("请输入轰炸内容:")
        times = int(input("请输入轰炸次数:"))
        f = 1/float(input("请输入轰炸频率:"))
        click = 0
        listener.start()

        while 1 :
            if click == 1 :
                keyboard.type(entry)
                keyboard.press(py.keyboard.Key.enter)
                count += 1
            if count == times :
                click = 0
                count = 0
                break

except TypeError :
    print("请输入有效数字")
    while True:
        click = 0
        count = 0


        def on_click(x, y, button, pressed):
            global click
            if pressed:
                if button == py.mouse.Button.left:
                    click = 1


        listener = py.mouse.Listener(on_click=on_click)
        entry = input("请输入轰炸内容:")
        times = int(input("请输入轰炸次数:"))
        f = 1 / float(input("请输入轰炸频率:"))
        listener.start()

        while 1:
            if click == 1:
                keyboard.type(entry)
                keyboard.press(py.keyboard.Key.enter)
                count += 1
            if count == times:
                break