import PySimpleGUI as sg
import datetime

dt = datetime.datetime.now()
ev, honap, nap, ora, perc = dt.year, dt.month, dt.day, dt.hour, dt.minute 
datum = f'{ev}-{honap}-{nap}'

with open('orvosok.txt', 'r', encoding='UTF-8-sig') as f:
    orvosok=[sor.strip() for sor in f]
    
with open('elojegyzes.txt', 'r',) as f:
    elojegyzesek=[sor.strip().split(';') for sor in f]
    

col1=[
    [sg.Text()],
    [sg.Text('dátum:',size=(10,1)),       sg.Input(key='dátum')],
    [sg.Text('óra:',size=(10,1)),         sg.Slider(key='óra',orientation='horizontal', range=(8,20), tick_interval=2,default_value=ora)],
    [sg.Text('perc:',size=(10,1)),        sg.Radio('00','perc',default=(0<perc<20)), sg.Radio('20','perc', default=(0<perc<20)), sg.Radio('40','perc',default=(0<perc<20))],
    [sg.Text('Név:',size=(10,1)),         sg.Input(key='Név')],
    [sg.Text('Telefon:',size=(10,1)),     sg.Input(key='Telefon')],
    [sg.Button('Ment'), sg.Button('Keres')]
      
]

col2=[
    [sg.Text('Orvosok:')],
    [sg.Listbox(orvosok,key='Orvosok',size=(10,14))],
    
    ]
col3=[
    [sg.Text('Előjegyzések:')],
    [sg.Listbox(  elojegyzesek, key='Előjegyzések', size=(50,14))],
    [sg.Button('Töröl')]
    
    ]


layout=[[sg.Column(col1),sg.Column(col2),sg.Column(col3),]]

window=sg.Window('Rendelő előjegyzés', layout,default_button_element_size=(15,1), font='Helvetica 14',auto_size_buttons=False)
window.read(100)
window['dátum'].update(datum)

while True:
    event,values=window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Ment':
        datum=values['dátum']
        ora=values['óra']
        nev=values['Név']
        print
        telefon=values['Telefon']
        orvos=values['Orvosok']
        sor=f'{datum};{ora};{nev};{telefon};{orvos}'
        print(sor)
        with open('elojegyzes.txt','w') as f:
            print(sor, file=f)
            
    if event == 'Töröl':
        elöjegyzes=values['Előjegyzések']
        index=elojegyzesek.index(elojegyzes[0])
        elojegyzesek.pop(index)
        window['Előjegyzések'].update(elojegyzesek)
        
        with open('elojegyzesek.txt','w') as f:
            break
    