import PySimpleGUI as sg
import arduino

layout = [
    [sg.Text('Enter the port (e.g. COM4):'), sg.Input(key='-INPUT-'),sg.Button('Set')],
    [sg.Button('Diode 1',key='-1-'), sg.Button('Diode 2',key='-2-'), sg.Button('Diode 3',key='-3-'), sg.Button('Diode 4',key='-4-'), sg.Button('OFF',key = '-OFF-')],
    [sg.Text("Arduino says:", size=(0, 1), key='OUTPUT')],
    [sg.Button('Close')]
]

message = "" #string to Arduino

window = sg.Window('Arduino Switch Control', layout)


event, values = window.read()

def default_button_color():
    window['-1-'].update(button_color=('white', 'red'))
    window['-2-'].update(button_color=('white', 'red'))
    window['-3-'].update(button_color=('white', 'red'))
    window['-4-'].update(button_color=('white', 'red'))
    window['-OFF-'].update(button_color=('white', 'green'))

def execute_diode(message,key,ard):
        default_button_color()
        window[key].update(button_color=('white', 'green'))
        window['-OFF-'].update(button_color=('white', 'red'))
        answer = ard.query(message)
        window['OUTPUT'].update(value=answer)
    
connected = False

while True:
    event, values = window.read()
    if not connected:
        ard = arduino.Arduino(values['-INPUT-'])
        connected = True
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    elif event == 'Set':
        default_button_color()
        answer = ard.read()
        window['OUTPUT'].update(value=answer)
    elif event == '-1-':
        message = "1"
        execute_diode(message, event, ard)
    elif event == '-2-':
        message = "2"
        execute_diode(message, event, ard)
    elif event == '-3-':
        message = "3"
        execute_diode(message, event, ard)
    elif event == '-4-':
        message = "4"
        execute_diode(message, event,ard)
    elif event == '-OFF-':
        message = "OFF"
        execute_diode(message, event, ard)
        default_button_color()

window.close()

