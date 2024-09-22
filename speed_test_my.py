import tkinter as tk
import speedtest as st


def insert_values(value):
    down_speed.delete(0, 'end')
    down_speed.insert(0, value)
    up_speed.delete(0, 'end')
    up_speed.insert(0, value)
    ping.delete(0, 'end')
    ping.insert(0, value)


def speed_test():
    test = st.Speedtest()
    down_speed.delete(0, 'end')
    down_speed.insert(0, round(test.download() / 10 ** 6, 2))
    up_speed.delete(0, 'end')
    up_speed.insert(0, round(test.upload() / 10 ** 6, 2))
    ping.delete(0, 'end')
    ping.insert(0, test.results.ping)


window = tk.Tk()
window.title('SpeedTest')
window.geometry('350x350')
window.configure(background='#FFE4C4')
window.resizable(False, False)
button_speed = tk.Button(window, text='Проверить скорость', width=30, height=5, command=speed_test, background='yellow')
button_speed.place(x=35, y=200)
down_speed = tk.Entry(window, width=15)
down_speed.place(x=210, y=75)
down_speed2 = tk.Label(window, text='Скорость загрузки Мб/сек:')
down_speed2.place(x=35, y=75)
up_speed = tk.Entry(window, width=15)
up_speed.place(x=210, y=100)
up_speed2 = tk.Label(window, text='Скорость передачи Мб/сек:')
up_speed2.place(x=35, y=100)
ping = tk.Entry(window, width=15)
ping.place(x=210, y=125)
ping2 = tk.Label(window, text='Пинг:')
ping2.place(x=35, y=125)
window.mainloop()
"""При запуске этого скрипта появляется окно, в котором можно проверить скорость загрузки/передачи данных и задержку (писал
прогу сам, а не спёр с инета). Здесь используются библиотеки speedtest и tkinter. 
  Первая нужна для проверки скорости через 
методы download(скорость загрузки), upload(скорость передачи данных) и results(проверка пинга, метод унаследован от 
класса Speedtest в самой библиотеке).
  Вторая библиотека нужна для создания окна, в котором будет выполняться программа, здесь использованы методы title(задаёт
название в строке заголовка), Button(создаёт виджет кнопки), Label(по сути просто создаёт поле с текстом), Entry(поле ввода/вывода
значений), place(задаёт расположение объекта), geometry(размер окна), configure(настройка окна, в данном случае просто поменял
цвет фона) и mainloop(вывести на экран при запуске само окно). 
 """
