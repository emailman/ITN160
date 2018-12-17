from guizero import *


def score(team):
    goals = int(team.value)
    team.value = goals + 1


def clear(team1, team2):
    team1.value = 0
    team2.value = 0


def main():
    app = App(title='Score Board', height=250, width=250, layout='grid')

    Text(app, text=' ' * 14, size=6, grid=[0, 0])

    Text(app, text='BLUE HENS LACROSSE', color='blue', grid=[1, 1, 3, 1])

    Text(app, size=6, grid=[0, 2])

    Text(app, text='HOME', color='green', grid=[1, 3])
    txt_home = Text(app, text='0', color='green', grid=[1, 4])
    Text(app, size=4, grid=[1, 5])
    btn_home = PushButton(app, text='SCORE',
                          command=score, args=[txt_home], grid=[1, 6])
    btn_home.bg = 'green'

    Text(app, text='VISITORS', color='red', grid=[3, 3])
    txt_visitors = Text(app, text='0', color='red', grid=[3, 4])
    Text(app, size=4, grid=[3, 5])
    btn_visitors = PushButton(app, text='SCORE',
                              command=score, args=[txt_visitors], grid=[3, 6])
    btn_visitors.bg = 'red'

    Text(app, grid=[0, 7])

    PushButton(app, text='CLEAR ALL', command=clear, args=[txt_home, txt_visitors],
               grid=[1, 8, 3, 1])

    app.display()


main()
