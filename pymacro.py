from pynput.mouse import Listener, Controller, Button
import keyboard
import time, sys

events = []
pressed = set()


def on_click(x, y, button, pressed):
    if pressed:
        events.append({"x": x, "y": y, "button": button, "time": time.time()})


def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


def end(queue, mouse_listener):

    print("CALLED!")
    print("Stopping muis listener")
    mouse_listener.stop()
    qx = 0
    ex = 0
    ret_list = []
    print(queue)
    while True:
        if(qx == len(queue) and ex < len(events)):
            ret_list.append((events[ex], events[ex]["time"]))
            ex += 1
        elif(qx < len(queue) and ex == len(events)):
            if queue[qx].event_type == 'down':
                ret_list.append((queue[qx].name, queue[qx].time))
            qx += 1
        elif qx == len(queue) and ex == len(events):
            break
        else:
            if queue[qx].time < events[ex]["time"]:
                if queue[qx].event_type == 'down':
                    ret_list.append((queue[qx].name,  queue[qx].time))
                qx += 1
            elif queue[qx].time > events[ex]["time"]:
                ret_list.append((events[ex], events[ex]["time"]))
                ex += 1

    ret_list.pop()

    tb = ret_list[0][1]
    for i in range(len(ret_list)):
        temp = ret_list[i][1]
        interaction = "click" if "button" in ret_list[i][0] else "key"
        if interaction == "click":
            ret_list[i] = ({"x": ret_list[i][0]["x"],
                            "y": ret_list[i][0]["y"],
                            "button": "left" if ret_list[i][0]["button"] == Button.left else "right"},
                           (ret_list[i][1] - tb), interaction)
        else:
            ret_list[i] = (ret_list[i][0], (ret_list[i][1] - tb), interaction)
        tb = temp

    with open("log.txt", "w") as f:
        f.write(str(ret_list))


def main():
    
    # Create a mouse listener
    mouse_listener = Listener(on_click=on_click, on_scroll=on_scroll)
    keyboard.start_recording()

    mouse_listener.start()
    keyboard.wait('f9')
    end(keyboard.stop_recording(), mouse_listener)


if __name__ == '__main__':
    main()
