######################################
# Opening Comments
# Author: Nathaniel Edwards
# 3/4/21
# Book Assignment
#######################################

import PySimpleGUI as sg

class book:
    def __init__(self, title, description, condition, pagenum):
        self.title = title
        self.description = description
        self.condition = condition
        self.pagenum = pagenum

    def getCondition (self):
        return self.condition

    def getTitle(self):
        return self.title

    def getPagenum(self):
        return int(self.pagenum)




BookNum = 0
Valid = False

Conditions = ['', 'New', 'Like New', 'Ok', 'Poor', 'Very Poor']
PageNumbers = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
layout = [[sg.Text('Book Name:', relief='sunken', font=('Any', 13), size=(17,1), enable_events=True, key='-Text-'),
          sg.InputText('', size=(50,1), enable_events=True, key = '-title-')],
          [sg.Text('Book Description:', relief='sunken', font=('Any', 13), size=(17,1), enable_events=True, key='-Text2-'),
           sg.MLine('', size=(47,10), enable_events=True, key='-description-')],
          [sg.Text('Book Condition:', relief='sunken', font=('Any', 13), size=(17,1), enable_events=True, key='-Text3-'),
           sg.Combo(Conditions, size=(48,1), readonly=True, enable_events=True, key='-condition-')],
          [sg.Text('Book Page Number:', relief='sunken', font=('Any', 13), size=(17,1), enable_events=True, key='-Text4-'),
           sg.InputText('', size=(42, 1), enable_events=True, key='-pagenum-'),
           sg.Button('submit', bind_return_key=True, disabled=True, key='-submit-')],
          [sg.HorizontalSeparator()],
          [sg.Text('Total book num', relief='sunken', font=('Any', 13), size=(17,1), enable_events=True, key='-Text5-'),
           sg.InputText('', size=(10,1), readonly=True, key='-TotalBooks-'),
           sg.Button('Get books', key='-AllBooksButton-')],
          [sg.Text('Book condition num', relief='sunken', font=('Any', 13), size=(17, 1), enable_events=True, key='-Text6-'),
           sg.Combo(Conditions, size=(10,1), readonly=True, enable_events=True, key='-ConditionSearch-'),
           sg.InputText('', size=(10, 1), readonly=True, key='-ConditionNum-'),
           sg.Button('Get books', key='-ConditionButton-')],
          [sg.Text('Book Page Num', relief='sunken', font=('Any', 13), size=(17, 1), enable_events=True, key='-Text7-'),
           sg.Combo(PageNumbers, size=(10,1), readonly=True, enable_events=True, key='-GreaterPages-'),
           sg.InputText('', size=(10, 1), readonly=True, key='-GreatPageNum-'),
           sg.Button('Get books', key='-PageNumButton-')]]

window = sg.Window('Book input window', layout, resizable=True, finalize=True)
#Main code

booklist = []
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        window.close()
        break
    elif event == '-submit-':
        Title = window['-title-'].get()
        Description = window['-description-'].get()
        Condition = window['-condition-'].get()
        PageNum = window['-pagenum-'].get()
        if not PageNum.isdigit():
            sg.popup('Please only enter Digits')
            window['-pagenum-'].update('')
        else:
            Book = book(Title, Description, Condition, PageNum)
            booklist.append(Book)
            BookNum = BookNum + 1
            window['-TotalBooks-'].update(BookNum)
            window['-title-'].update('')
            window['-description-'].update('')
            window['-condition-'].update('')
            window['-pagenum-'].update('')
            window['-submit-'].update(disabled=True)
    elif event == '-title-':
        if Valid:
            window['-submit-'].update(disabled=False)
        else:
            window['-submit-'].update(disabled=True)
        if values['-title-'] == '':
            Valid = False
        elif values['-description-'] == '':
            Valid = False
        elif values['-condition-'] == '':
            Valid = False
        elif values['-pagenum-'] == '':
            Valid = False
        else:
            Valid = True
    elif event == '-description-':
        if Valid:
            window['-submit-'].update(disabled=False)
        else:
            window['-submit-'].update(disabled=True)
        if values['-title-'] == '':
            Valid = False
        elif values['-description-'] == '':
            Valid = False
        elif values['-condition-'] == '':
            Valid = False
        elif values['-pagenum-'] == '':
            Valid = False
        else:
            Valid = True
    elif event == '-condition-':
        if Valid:
            window['-submit-'].update(disabled=False)
        else:
            window['-submit-'].update(disabled=True)
        if values['-title-'] == '':
            Valid = False
        elif values['-description-'] == '':
            Valid = False
        elif values['-condition-'] == '':
            Valid = False
        elif values['-pagenum-'] == '':
            Valid = False
        else:
            Valid = True
    elif event == '-pagenum-':
        if Valid:
            window['-submit-'].update(disabled=False)
        else:
            window['-submit-'].update(disabled=True)
        if values['-title-'] == '':
            Valid = False
        elif values['-description-'] == '':
            Valid = False
        elif values['-condition-'] == '':
            Valid = False
        elif values['-pagenum-'] == '':
            Valid = False
        else:
            Valid = True
    elif event == '-AllBooksButton-':
        BookList = []
        for Books in booklist:
            BookList.append(Books.getTitle())
        sg.popup_scrolled(BookList)
    elif event == '-ConditionSearch-':
        conditionList = []
        for Books in booklist:
            if Books.getCondition() == values['-ConditionSearch-']:
                conditionList.append(Books.getTitle())
        ConditionNum = len(conditionList)
        window['-ConditionNum-'].update(ConditionNum)
    elif event == '-ConditionButton-':
        conditionlist = []
        for Books in booklist:
            if Books.getCondition() == values['-ConditionSearch-']:
                conditionlist.append(Books.getTitle())
        sg.popup_scrolled(conditionlist)
    elif event == '-GreaterPages-':
        NumList = []
        for Books in booklist:
            if Books.getPagenum() >= values['-GreaterPages-']:
                NumList.append(Books.getTitle())
        BookPageNumber = len(NumList)
        window['-GreatPageNum-'].update(BookPageNumber)
    elif event == '-PageNumButton-':
        numlist = []
        for Books in booklist:
            if Books.getPagenum() >= values['-GreaterPages-']:
                numlist.append(Books.getTitle())
        sg.popup_scrolled(numlist)