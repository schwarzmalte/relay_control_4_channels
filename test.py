import PySimpleGUI as sg

sg.theme('DarkAmber')  # Set the theme

layout = [[sg.Text('Hello, world!')], [sg.Button('OK')]]

window = sg.Window('My window', layout)  # Create the window

while True:
    event, values = window.read()  # Read events and values from the window
    if event == sg.WIN_CLOSED or event == 'OK':  # If user closes window or clicks OK button
        break

window.close()  # Close the window