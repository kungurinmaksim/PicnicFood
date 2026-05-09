from tkinter import  *
from random import  *
from  pickle import  dump, load

def menu_create(canvas):
    offset = 0
    for menu_option in menu_options:
        option_id = canvas.create_text(350, 150+ offset, anchor=CENTER, font=('Arial', '25'), text=menu_option, fill='black')
        menu_option_id.append(option_id)
        offset += 50
        canvas.itemconfig(window_id_m, state='hidden')
        canvas.itemconfig(window_id_k, state='hidden')
    menu_update()

def key_press(event):
    if menu_mode:
        menu_controller(event)
    else:
        #print("game mode")
        key_handler(event)

def menu_controller(event):
    if event.keycode == KEY_UP:
        menu_up()
    elif event.keycode == KEY_UP_s:
        menu_up()
    elif event.keycode == KEY_DOWN:
        menu_down()
    elif event.keycode == KEY_DOWN_s:
        menu_down()
    elif event.keycode == KEY_ENTER:
        menu_enter()

def menu_down():
    global menu_current_index
    menu_current_index += 1
    if menu_current_index > len(menu_options) - 1 :
        menu_current_index = len(menu_options) - 1
    menu_update()

def menu_up():
    global menu_current_index
    menu_current_index -= 1
    if menu_current_index < 0 :
        menu_current_index = 0
    menu_update()

def menu_enter():

    if menu_current_index == 0:
        game_new()
    elif menu_current_index == 1:
        game_new_hide()
    elif menu_current_index == 2:
        game_new_red()
    elif menu_current_index == 3:
        game_new_ha()
    elif menu_current_index == 4:
        game_exit()

def menu_clear():
    for menu_index in range(len(menu_option_id)):
        canvas.itemconfig(menu_option_id[menu_index], state='hidden')

def menu_update():
    for menu_index in range(len(menu_option_id)):
        element_id = menu_option_id[menu_index]
        if menu_mode:
            canvas.itemconfig(element_id, state ='normal')
            if menu_index == menu_current_index:
                canvas.itemconfig(menu_option_id[menu_index], fill='blue')
            else:
                canvas.itemconfig(menu_option_id[menu_index], fill='black')
        else:
            canvas.itemconfig(element_id, state ='hidden')

def game_new():
    global menu_mode  , speed_n ,speed_v, i , g , p , l
    print('Начинаем лёгкую игру')
    canvas.itemconfig(window_id_m, state='normal')
    canvas.itemconfig(window_id_k, state='normal')
    menu_clear()
    menu_mode = False
    speed_n = 12
    speed_v = 4
    i = 3
    g = 1
    p = 0
    l = 0
    animate_frame()
    #move_actor()
    move_morkovka()
    colision_morkovka()
    move_bird()
    colision_bird()

def game_new_hide():
    global menu_mode  , speed_n ,speed_v, i , g , p , l
    print('Начинаем нормальную игру')
    canvas.itemconfig(window_id_m, state='normal')
    canvas.itemconfig(window_id_k, state='normal')
    menu_clear()
    menu_mode = False
    speed_n = 10
    speed_v = 3
    i = 5
    g = 1.1
    p = 1
    l = 0
    #update()
    #move_actor()
    animate_frame()
    # move_actor()
    move_morkovka()
    #colision_morkovka()
    move_bird()
    colision_bird()

def game_new_red():
    global menu_mode , speed_n ,speed_v, i , g , p , l
    print('Начинаем сложную  игру')
    canvas.itemconfig(window_id_m, state='normal')
    canvas.itemconfig(window_id_k, state='normal')
    menu_clear()
    menu_mode = False
    speed_n = 8
    speed_v = 2
    i = 6
    g = 1.4
    p = 0
    l = 0
    animate_frame()
    # move_actor()
    move_morkovka()
    colision_morkovka()
    move_bird()
    colision_bird()

def game_new_ha():
    global menu_mode  , speed_n ,speed_v , i , g , p , l
    print('Начинаем невозможную игру')
    canvas.itemconfig(window_id_m, state='normal')
    canvas.itemconfig(window_id_k, state='normal')
    menu_clear()
    menu_mode = False
    speed_n = 1
    speed_v = 10
    i = 100
    g = 2.2
    p = 1
    l = 1
    animate_frame()
    # move_actor()
    move_morkovka()
    colision_morkovka()
    move_bird()
    colision_bird()

def game_exit():
    print('Выходим из игры')
    exit()

def animate_frame(frame=0):
    canvas.itemconfigure(actor,image= photos[frame])
    canvas.after(50 , animate_frame, (frame + 1) % len(photos))

def colision(x):
    position = canvas.coords(actor)
    left = position[0]
    right = position[0] + actor
    return left < x < right

def colision_morkovka():
    global c , y_m , x_m, x, y
    if x_m +25 >= x and x_m + 25 <= x + 100 and y_m + 50 >= y:
        c = True
        return True
    else:
        False


def update():
    global vx , photos, gameower
    if not gameower:
        return
    x = canvas.coords(actor)[0] + vx
    if x < 0:
        x = 0
        vx = -vx
        photos = [PhotoImage(file=f'ресурсы/зайка{i}_f.png') for i in range(1, 9)]
    if x > game_with - 100:
        x = game_with - 100
        vx = -vx
        photos = [PhotoImage(file=f'ресурсы/зайка{i}_g.png') for i in range(1, 9)]
    canvas.moveto(actor, x, y)
    canvas.after(10, update)

def rabbit_eat():
    global s
    s = s + 1
    canvas.itemconfig(text_eat, text=f'еды в корзине: {s}')
    canvas.itemconfig(text_end, text=f'конец игры.Еды собрано :{s}')

def move_actor():
    if gameower:
        return
    global x,vx,speed,photos
    x += vx
    if x < 0:
         x = 0
         vx = -vx
         photos = [PhotoImage(file=f'ресурсы/зайка{i}_f.png') for i in range(1, 9)]
    if x > game_with - 100:
         x = game_with - 100
         vx = -vx
         photos = [PhotoImage(file=f'ресурсы/зайка{i}_g.png') for i in range(1, 9)]
    canvas.coords(actor , x , y)
    canvas.after(speed , move_actor)

def move_morkovka():
    global y_m, speed_nб, gameower

    global vx_m , i
    if menu_mode:
        return
    if gameower:
        return

    y_m += vx_m
    if colision_morkovka():
        vx_m *= 1.1
        vx_m  = min(i, vx_m)
        home_morkovka()
        rabbit_eat()
    if y_m+ 50 > game_height:
        home_morkovka()
    canvas.coords(window_id_m , x_m , y_m)
    canvas.after(speed_n , move_morkovka)

def home_morkovka():
    global  game_height , y_m , x_m , game_with , e ,window_pictures_m
    if l >-1 and l<1 :
        e = randint(1, 2)
        window_pictures_m = PhotoImage(file=f'ресурсы/morkovka_{e}.png')
        canvas.itemconfigure(window_id_m, image=window_pictures_m)
    x_m = randint(1 , game_with-50)
    y_m = 0

def rabbit_i():
    global f
    f = f - 1
    if f < 5 and f>3 :
        canvas.itemconfig(text_i, text= f'жизни:♥ ♥ ♥ ♥ *')
    if f < 4 and f>2 :
        canvas.itemconfig(text_i, text= f'жизни:♥ ♥ ♥ * *')
    if f < 3 and f>1 :
        canvas.itemconfig(text_i, text= f'жизни:♥ ♥ * * *')
    if f < 2 and f>0 :
        canvas.itemconfig(text_i, text= f'жизни:♥ * * * *')
    if f < 1 and f>-1 :
        canvas.itemconfig(text_i, state='hidden')
        canvas.itemconfig(text_end, state='normal')
        game_over()

def game_over():
    global gameower
    gameower = True
    canvas.itemconfig(window_id_m, state='hidden')
    canvas.itemconfig(window_id_k, state='hidden')
    save_game()
    canvas.after(4000, game_new_return)
    update()

def game_new_return():
    canvas.itemconfig(text_end, state='hidden')
    canvas.itemconfig(text_i, state='normal')
    global gameower , menu_mode , f , s, speed_n ,speed_v , i , g , p , l , i , j , speed , b
    f = 5
    s = 0
    i = 5
    g = 1.1
    j = 0
    p = 0
    b = 0
    speed = 3
    speed_n = 10
    speed_v = 3
    canvas.itemconfig(text_i, text= f'жизни:♥ ♥ ♥ ♥ ♥')
    canvas.itemconfig(text_eat, text=f'еды в корзине: {s}')
    gameower = False
    menu_mode = True
    menu_update()
    load_game()
    move_actor()



def colision_bird():
    global v , y_k , x_k
    if x_k +25 >= x and x_k + 25 <= x + 100 and y_k + 50 >= y:
        v = True
        return True
    else:
        False

def move_bird():
    if menu_mode:
        return
    if gameower:
        return
    global y_k , speed_v , b , vx_k
    y_k += vx_k
    if colision_bird():
        home_bird()
        rabbit_i()
    if y_k+ 50 > game_height:
        home_bird()
        b = b + 1
        if b >2:
            vx_k *= g
            vx_k = min(5, vx_k)
            b = 0
    canvas.coords(window_id_k , x_k , y_k)
    canvas.after(speed_v , move_bird)

def home_bird():
    global  game_height , y_k , x_k , game_with
    x_k = randint(1 , game_with-50)
    y_k = 0

def key_handler(event):
    if menu_mode:
        return
    if gameower:
        return
    key_a = 65
    key_d = 68
    key_a_t = 39
    key_b_t = 37
    if event.keycode == key_a or event.keycode == key_b_t:
        left()
    elif event.keycode == key_d or event.keycode == key_a_t:
        right()

def left():
    global vx , photos
    vx = -1
    photos = [PhotoImage(file=f'ресурсы/зайка{i}_g.png') for i in range(1, 9)]

def right():
    global vx, photos
    vx = 1
    photos = [PhotoImage(file=f'ресурсы/зайка{i}_f.png') for i in range(1, 9)]

def save_game():
    if p > -1 and p <1 :
        global s
        if s >j:
            r = s
            data = r
            with open('save.dat', 'wb') as f:
                dump(data, f)

def load_game():
    global j , s
    with open('save.dat', 'rb') as f:
        f.seek(0)
        data = load(f)
        j = data
        canvas.itemconfig(text_i_r, text=f'рекорд :{j}')


game_with = 700
game_height = 500
x= 0
y= 301
vx = 1
speed = 3
y_m = y_k = 0
vx_m =vx_k = 1
x_m = x_k = game_with//2-25
speed_n = 10
speed_v = 3
c = False
v = False
s = 0
f = 5
i = 5
g = 1.1
j = 0
p = 0
menu_current_index = 3
menu_option_id = []
KEY_UP = 87
KEY_DOWN = 83
KEY_ENTER = 13
KEY_UP_s = 38
KEY_DOWN_s = 40
gameower = False
menu_mode = True
b = 0
l = 0
e = 1
menu_options =['Сложность: лёгкая.', 'Сложность: дача.','Сложность: что-то сложненько.','Сложность: продуктовый склад. ','Выход']

window = Tk()
window.title('Беги!!!')
window.resizable(width= False, height=False)
canvas = Canvas(window, width=game_with, height=game_height, background='white')
canvas.pack()
window_pictures = PhotoImage(file='ресурсы/images.png')
window_id = canvas.create_image(-50, 0, image=window_pictures, anchor='nw')
text_eat = canvas.create_text(game_with , 10, fill = 'yellow', font = 'Times 25 bold', text = f'еды в корзине: {s}', anchor= NE)
text_i = canvas.create_text(game_with//2 + 37 , 10, fill = 'red', font = 'Times 25 bold', text = f'жизни:♥ ♥ ♥ ♥ ♥', anchor= NE)
text_end = canvas.create_text(game_with//2 +250  ,game_height//2 , fill = 'red', font = 'Times 30 bold', text = f'конец игры.Еды собрано :{s}', anchor= NE)
text_i_r = canvas.create_text(game_height-300 , 450, fill = 'red', font = 'Times 25 bold', text = f'рекорд :{j}', anchor= NE)
photos = [PhotoImage(file=f'ресурсы/зайка{i}_f.png')for i in range(1,9)]
actor = canvas.create_image(0,301, image = photos[0],anchor = 'nw')
window_pictures_m = PhotoImage(file=f'ресурсы/morkovka_{e}.png')
window_id_m = canvas.create_image(x_m, 0, image=window_pictures_m, anchor='nw')
window_pictures_k = PhotoImage(file='ресурсы/коршун.png')
window_id_k = canvas.create_image(x_k, 0, image=window_pictures_k, anchor='nw')
canvas.itemconfig(text_end, state='hidden')
load_game()
animate_frame()
move_actor()
menu_create(canvas)
window.bind('<Key>', key_press)
window.mainloop()
#430