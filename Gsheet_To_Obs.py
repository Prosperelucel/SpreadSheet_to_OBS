import gspread
from obswebsocket import obsws, requests, events
import PySimpleGUI as sg
import time
import configparser
import threading
import os
import sys
abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

current_state = "Init"
config = configparser.ConfigParser()
config.read('config.ini')
url = config['DEFAULT']['url']
timer_refresh = float(config['DEFAULT']['timer_refresh'])
max_row = int(config['DEFAULT']['max_row'])

col_list = []

host = config['DEFAULT']['obswebsocket_ip']
port = config['DEFAULT']['obswebsocket_port']
password = config['DEFAULT']['obswebsocket_pw']

ws = obsws(host, port, password)

def ConnectObs():
    global current_state
    try:
        ws.connect()
    except Exception as e:
        print(e)
        current_state = e

def Scan_Gsheet(url):
    global current_state
    try:
        gc = gspread.service_account(filename='service_account.json')
        sh = gc.open_by_url(url)
        worksheet = sh.worksheet("Feuille 1")
        col_list = worksheet.col_values(1)
        return col_list

    except Exception as e:
        current_state = e
        print(e)

def Main_Loop():
    global window
    global layout
    global col_list
    global current_state
    ConnectObs()
    while True:
        try:
            current_state = "Scanning..."
            col_list = Scan_Gsheet(url)
            for i in range(1, max_row):
                window[str(i) + "_ROW"].update(col_list[i - 1])
                ws.call(requests.SetTextGDIPlusProperties(source=str(i)+"_TXT", text=str(col_list[i-1])))
                print('Sending : ' + str(col_list[i-1]))
            time.sleep(timer_refresh)
            if thread_stop:
                current_state = "Stop"
                break
        except Exception as e:
            print(e)
            current_state = e
            break

if __name__ == "__main__":

    sg.theme('DarkBrown1')
    layout = [
        [sg.Frame('Status :', layout=[
            [
                sg.T(current_state, key='_STATE_', size=(25, 1))
            ]]),

         sg.Button('Start', key='_START_'), sg.Button('Stop', key='_STOP_', disabled=True)
         ],
        [sg.T("Scan Url: "), sg.Input(key='_URL_', default_text=url)],
        [sg.T("SpreadSheet =============================================> OBS")]
    ]
    layout += [
                [sg.Text(f'{i}. '), sg.In(size=(50,1),key=f"{i}_ROW"),sg.Text('=>'),sg.In(default_text=f"{i}_TXT",key=f"{i}_SOURCE",size=(10,1))] for i in range(1,max_row)
               ]

    window = sg.Window('SpreadSheet To OBS', layout, keep_on_top=True, auto_size_text=True)

    while True:
        event, values = window.read(timeout=1000)
        window['_STATE_'].update(current_state)

        if event == sg.WIN_CLOSED or event == 'Exit':
            thread_stop = True
            break
        if event == '_START_':
            window['_START_'].update(disabled=True)
            window['_STOP_'].update(disabled=False)
            t = threading.Thread(target=Main_Loop, args=())
            t.start()
            thread_stop = False
        if event == '_STOP_':
            window['_START_'].update(disabled=False)
            window['_STOP_'].update(disabled=True)
            thread_stop = True