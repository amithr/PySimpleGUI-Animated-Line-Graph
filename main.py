import PySimpleGUI as sg
from random import randint

GRAPH_SIZE = (400,200)
GRAPH_STEP_SIZE = 5

sg.change_look_and_feel('LightGreen')
# Graph element(canvas_size, graph_bottom_left, graph_top_right)
layout = [  [sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key='-GRAPH-', background_color='lightblue'),],
            [sg.Text('Milliseconds per sample:', size=(20,1)),
             sg.Slider((0,30), default_value=15, orientation='h', key='-DELAY-')],
            [sg.Text('Pixels per sample:', size=(20,1)),
             sg.Slider((1,30), default_value=GRAPH_STEP_SIZE, orientation='h', key='-STEP-SIZE-')],
            [sg.Button('Exit')]]

window = sg.Window('Animated Line Graph Example', layout)

delay = x = lastx = lasty = 0
while True:                             # Event Loop
    # Each graph movement is happening in the span of the delay (in milliseconds)
    event, values = window.read(timeout=delay)
    if event in (None, 'Exit'):
        break
    step_size, delay = values['-STEP-SIZE-'], values['-DELAY-']
    y = randint(0,GRAPH_SIZE[1])        # get random y coordinate for graph
    if x < GRAPH_SIZE[0]:               # if still drawing initial width of graph, meaning less than 400
        # Draw line from initial lastx, lasty, to current
        window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
    else:
                                       # finished drawing full graph width so move each time to make room
        # Effectively move current graph backwards, so that earlier drawn part is out of view
        print(step_size)
        print(x)
        window['-GRAPH-'].Move(-step_size, 0)
        # Once graph has been moved backwards, draw new line from last (x, y) coordinate
        window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
        # Reduce x by step size to move graph forward 
        # (basically, keep x will have the step size added to it later, so this keeps it the same)
        x -= step_size
        print(x)
    lastx, lasty = x, y
    # Move graph forward or keep at same place depending on position
    x += step_size
window.close()