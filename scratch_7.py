import multiprocessing
import datetime
import pandas as pd
import random  # To use random numbers
import time  # to use time functions like time.wait()
from multiprocessing import *  # for parallel processing
from tkinter import *  # to make the popup interface
import pandas as pd  # to use the exctracted csv file's data like the questioniers
from pynput.mouse import Listener
import logging
import socket
# ------------------------------------------------------------------------------------------------------------------------

logging.basicConfig(filename="mouse_log12.csv", level=logging.INFO, filemode="w+",
                    format='%(asctime)s.%(msecs)03d, %(message)s', datefmt='%Y-%m-%d,%H:%M:%S')

click_count = 0
movement = 0
temp = 0
scrolled = 0


def on_move(x, y):
    global movement
    movement += 1
    logging.info("movements {0}".format(movement))


def on_click(x, y, button, pressed):
    if pressed:
        global click_count
        click_count += 1
        logging.info("clicks {0}".format(click_count))


def countdown(t):
    while t > 0:
        t -= 1
        time.sleep(1)


def on_scroll(x, y, dx, dy):
    global scrolled
    scrolled += 1
    logging.info("scrolled {0}".format(scrolled))


def listening():
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()


# Your foo function
def solution_final(op1, df, x, q):
    if op1[0] == df[0]:
        q.put(1)
    else:
        q.put(-1)
    print("clicked")
    return x.destroy()


def popup(i, df, question, op1, op2, op3, op4, q,
          time_cut):  # function to create a popup box with options to be clicked
    print("popup")
    window = Tk()
    question_tab = Label(window, text=question, width=100, font=('ariel', 10, 'bold'),
                         anchor='w')
    question_tab.place(x=0, y=0)  # setting corrdinates for question buttons
    question_tab.bind('<Configure>', lambda e: question_tab.config(wraplength=question_tab.winfo_width()))
    question_tab.pack()
    opt1 = Button(window, text=op1, fg='blue',
                  command=lambda: solution_final(op1, df.iat[i, 2], window, q))  # inserting buttons as options
    opt1.place(x=0, y=50)  # setting corrdinates for options buttons
    opt1.pack()
    opt2 = Button(window, text=op2, fg='blue',
                  command=lambda: solution_final(op2, df.iat[i, 2], window, q))  # inserting buttons as options
    opt2.place(x=0, y=100)  # setting coordinates for options buttons
    opt2.pack()
    opt3 = Button(window, text=op3, fg='blue',
                  command=lambda: solution_final(op3, df.iat[i, 2], window, q))  # inserting buttons as options
    opt3.place(x=0, y=150)  # setting coordinates for options buttons
    opt3.pack()
    opt4 = Button(window, text=op4, fg='blue',
                  command=lambda: solution_final(op4, df.iat[i, 2], window, q))  # inserting buttons as options
    opt4.place(x=0, y=200)  # setting coordinates for options buttons
    opt4.pack()
    window.title('QUESTION NO.:')

    window.geometry("1000x400")  # setting popup window screen size
    window.mainloop()
    print("pop end")
    time_cut.put(datetime.datetime.now())


def record_setting(li, r, w, m):
    tot_movement = 0
    tot_clicks = 0
    tot_scroll = 0

    count = []
    df = pd.read_csv("mouse_log12.csv")
    df.columns = ["Date", "Time", "actions"]
    df.drop(["Date"], axis=1, inplace=True)
    print(len(df))
    df = df.iloc[::-1]
    track = 0
    for i in range(0, len(df)):
        if "scrolled" in df.iat[i, 1]:
            count.append(df.iat[i, 1])
            track += 1
            break
    for j in range(0, len(df)):
        if "movements" in df.iat[j, 1]:
            count.append(df.iat[j, 1])
            track += 1
            break
    for k in range(0, len(df)):
        if "clicks" in df.iat[k, 1]:
            count.append(df.iat[k, 1])
            track += 1
            break
    for i in range(0, track):
        if i == 2:
            tot_clicks = int((count[i])[7:])
        if i == 1:
            tot_movement = int((count[i])[11:])

        if i == 0:
            tot_scroll = int((count[i])[9:])
    print("Overall mouse record:")
    print("Total_movements: ",tot_movement,"Total_clicks: ", tot_clicks,"Total_scrols: ", tot_scroll)
    tot_pop_movement = 0
    tot_pop_clicks = 0
    tot_pop_scroll = 0

    for l in range(0, len(df)):
        if df.iat[l, 0] >= li[0].strftime("%H:%M:%S.%f") or df.iat[l, 0] <= li[0].strftime("%H:%M:%S.%f"):
            if "scrolled" in df.iat[l, 1]:
                tot_pop_scroll += 1
            elif "movements" in df.iat[l, 1]:
                tot_pop_movement += 1
            elif "clicks" in df.iat[l, 1]:
                tot_pop_clicks += 1
        elif df.iat[l, 0] >= li[2].strftime("%H:%M:%S.%f") or df.iat[l, 0] <= li[3].strftime("%H:%M:%S.%f"):
            if "scrolled" in df.iat[l, 1]:
                tot_pop_scroll += 1
            elif "movements" in df.iat[l, 1]:
                tot_pop_movement += 1
            elif "clicks" in df.iat[l, 1]:
                tot_pop_clicks += 1
        elif df.iat[l, 0] >= li[4].strftime("%H:%M:%S.%f") or df.iat[l, 0] <= li[5].strftime("%H:%M:%S.%f"):
            if "scrolled" in df.iat[l, 1]:
                tot_pop_scroll += 1
            elif "movements" in df.iat[l, 1]:
                tot_pop_movement += 1
            elif "clicks" in df.iat[l, 1]:
                tot_pop_clicks += 1
    print("Overall mouse record during popups:")
    print("total_movements: ",tot_pop_movement,"total_clicks:", tot_pop_clicks, "total_scrolls: ",tot_pop_scroll)
    ret_clicks = 0
    ret_scrolls = 0
    if tot_clicks != 0:
        ret_clicks = (tot_pop_clicks / tot_clicks) * 100
    if tot_scroll != 0:
        ret_scrolls = (tot_pop_scroll / tot_scroll) * 100
    accur = (r / (r + w)) * 100
    miss_fact = (m / (r + w + m)) * 100
    return ret_clicks, ret_scrolls, accur, miss_fact



def foo():
    identity = input("Enter User id")
    result = []
    time_seg = []
    print("start")
    print(datetime.datetime.now())
    df = pd.read_csv("C:\\Users\\SHIVAM SINGH NEGI\\PycharmProjects\\studen_activness_system\\final2.csv")
    df = df.sample(n=3, replace=False)
    p0 = multiprocessing.Process(target=listening, args=())
    p0.start()
    p1 = multiprocessing.Process(target=countdown, args=(20,))
    p1.start()
    lock = Lock()
    q = multiprocessing.Queue()
    time_cut = multiprocessing.Queue()
    for i in range(0, len(df)):
        ran_time = random.randint(1, 2)
        print("running:", i)
        time.sleep(ran_time)
        que = df.iat[i, 1]
        op1 = df.iat[i, 3]
        op2 = df.iat[i, 4]
        op3 = df.iat[i, 5]
        op4 = df.iat[i, 6]
        print(que, op1, op2, op3, op4)
        lock.acquire()
        time_cut.put(datetime.datetime.now())
        p = multiprocessing.Process(target=popup, args=(i, df, que, op1, op2, op3, op4, q, time_cut))
        p.start()  # Wait 10 seconds for foo
        time.sleep(5)
        p.terminate()
        print("pop termnate")
        time_cut.put(datetime.datetime.now())
        if time_cut.qsize() % 2 != 0:
            print("2 entries")
            time_cut.get()
        lock.release()
    p1.join()
    while not q.empty():
        result.append(q.get())
    print("Queue is now empty!")
    print("option out")
    print("timeout")
    p0.terminate()
    print(datetime.datetime.now())
    print("Printing the time stamp")
    while not time_cut.empty():
        time_seg.append(time_cut.get())
    return result, time_seg, identity


# ------------------------------------------------------------------------------------------------------------------------

def records_making(time_seg):
    df = pd.read_csv("mouse_log12.csv")


if __name__ == '__main__':
    result, time_seg, user = foo()

    print(user)
    print(result)
    print(time_seg)
    # ---------------------------------------------------------------------------------------------------------------------
    right = 0
    wrong = 0
    missed = 0
    for i in result:
        if i < 0:
            wrong += 1
        if i > 0:
            right += 1
    missed = 6 - (wrong + right)  #taking 6 as the model is made for 6 questions but we are only for testing purpose using 3 popups only
    # ---------------------------------------------------------------------------------------------------------------------
    ef_clicks,ef_scroll,acc_ans,miss_que=record_setting(time_seg, right, wrong, missed)
    print("user: ",user,"Effective clicks: ", ef_clicks,"Effective scrolls: ",ef_scroll,"\n","accuracy: ",acc_ans,"Missed questions: ",miss_que)
    s = socket.socket()
    s.connect(('localhost', 12345))
    str = "{0},{1},{2},{3},{4}".format(user,acc_ans,miss_que,ef_clicks,ef_scroll)  #user/rollnumber,Accuracy,Missed,Clicks,Scrolls
    s.send(str.encode());
    print("N:", s.recv(1024).decode())
    s.close()