from guizero import *

txt_home_win = None
txt_visitors_win = None


def score(team, team_win):
    goals = int(team.value)
    team.value = goals + 1
    team_win.value = team.value


def clear(team1, team2):
    team1.value = 0
    team2.value = 0
    txt_home_win.value = 0
    txt_visitors_win.value = 0


def main():
    global txt_home_win, txt_visitors_win

    app = App(title='Score Board Console', height=250, width=280, layout='grid')
    win = Window(app, title='Score Board', height=120, width=280, layout='grid')

    # Outdoor board
    Text(win, text=' ' * 20, size=6, grid=[0, 0])

    Text(win, text='BLUE HENS LACROSSE', color='blue', grid=[1, 1, 3, 1])

    Text(win, size=6, grid=[0, 2])

    Text(win, text='HOME', color='green', grid=[1, 3])
    txt_home_win = Text(win, text='0', color='green', grid=[1, 4])
    Text(win, size=4, grid=[1, 5])

    Text(win, text='VISITORS', color='red', grid=[3, 3])
    txt_visitors_win = Text(win, text='0', color='red', grid=[3, 4])
    Text(win, size=4, grid=[3, 5])

    # Console
    Text(app, text=' ' * 20, size=6, grid=[0, 0])

    Text(app, text='BLUE HENS LACROSSE', color='blue', grid=[1, 1, 3, 1])

    Text(app, size=6, grid=[0, 2])

    Text(app, text='HOME', color='green', grid=[1, 3])
    txt_home = Text(app, text='0', color='green', grid=[1, 4])
    Text(app, size=4, grid=[1, 5])
    btn_home = PushButton(app, text='SCORE',
                          command=score, args=[txt_home, txt_home_win], grid=[1, 6])
    btn_home.bg = 'green'

    Text(app, text='VISITORS', color='red', grid=[3, 3])
    txt_visitors = Text(app, text='0', color='red', grid=[3, 4])
    Text(app, size=4, grid=[3, 5])
    btn_visitors = PushButton(app, text='SCORE',
                              command=score, args=[txt_visitors, txt_visitors_win], grid=[3, 6])
    btn_visitors.bg = 'red'

    Text(app, grid=[0, 7])

    PushButton(app, text='CLEAR ALL', command=clear, args=[txt_home, txt_visitors],
               grid=[1, 8, 3, 1])

    app.display()


main()
