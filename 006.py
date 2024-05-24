import pygame
import random
import os
import time
import tkinter as daan
import threading
import queue

# 初始化Pygame
pygame.init()

# 设置窗口尺寸
WIDTH, HEIGHT = 1438, 807
WIN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Dice Roller")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

dice_images = [pygame.image.load(f'{i}.png') for i in range(1, 7)]

def roll_dice():
    a = 0
    my_list = [[0 for _ in range(5)] for _ in range(305)]
    for m in range(1, 7):
        for n in range(1, 7):
            for o in range(1, 7):
                for p in range(1, 7):
                    for q in range(1, 7):
                        if m + n + o + p + q == 12:
                            my_list[a] = [m, n, o, p, q]
                            a += 1
    d = Dice()
    while True:
        arr = my_list[d.fun()]
        if d.judge(arr) == 2:
            break
    return arr


def func(root, entry, q, time_star):
    sum_ = entry.get()
    time_f = time.time()
    sum_time = time_f-time_star
    with open('expe.txt', 'a') as f:
        f.write(f'{sum_}    ')
        f.write(f'{sum_time}\n')
    root.quit()
    q.put('done')


def run_tkinter(q, time_star):
    root = daan.Tk()
    entry = daan.Entry(root)
    entry.pack()
    b = daan.Button(root, text="完成", command=lambda: func(root, entry, q, time_star))
    b.pack()
    root.mainloop()


def update_dice_image(WIN, current_index, dice_images1, last_switch_time, image_switch_time, cout):
    if cout == 7:
        return 1, 2
    current_time = pygame.time.get_ticks()
    if current_time - last_switch_time > image_switch_time:
        current_index = (current_index + 1) % len(dice_images1)
        last_switch_time = current_time
        WIN.fill(WHITE)
        WIN.blit(dice_images1[current_index], (485, 100))
        pygame.display.flip()
    return current_index, last_switch_time


def draw(dice_value, count, time_star, q):
    WIN.fill(WHITE)
    fnt_obj = pygame.font.Font('./fonts/Dengl.ttf', 18)
    fnt_name1 = fnt_obj.render('第', True, 'red')
    fnt_surf = fnt_obj.render(str(count), True, 'red')
    fnt_name2 = fnt_obj.render('次', True, 'red')
    WIN.blit(fnt_name1, (0, 0))
    WIN.blit(fnt_surf, (20, 0))
    WIN.blit(fnt_name2, (30, 0))
    dice_image = dice_images[dice_value - 1]
    WIN.blit(dice_image, (485, 100))
    pygame.display.update()
    if count == 5:
        threading.Thread(target=run_tkinter, args=(q, time_star)).start()

def screen():
    background = pygame.image.load('background2.png')
    WIN.blit(background, (0, 0))
    pygame.display.update()


def main():
    current_index = 0
    last_switch_time = 0
    image_switch_time = 100
    dice_images1 = []
    clock = pygame.time.Clock()
    dice_folder = "./dict/"
    for i in range(1, 7):
        dice_image = pygame.image.load(os.path.join(dice_folder, f"{i}.png")).convert_alpha()
        dice_images1.append(dice_image)
    run = True
    cout = 0
    dice_value_index = 0
    arr1 = roll_dice()
    screen()

    q = queue.Queue()

    while run:
        i = 10
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                with open('expe.txt', 'a') as f:
                    f.write('分界线\n')
            elif cout == 6:
                cout = 0
                time_star = time.time()
                arr1 = roll_dice()
                screen()

            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE and cout == 0:
                        time_star = time.time()
                while i:
                    current_index, last_switch_time = update_dice_image(WIN, current_index, dice_images1, last_switch_time, image_switch_time, cout)
                    pygame.time.delay(50)
                    i -= 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    cout += 1
                    draw(arr1[dice_value_index], cout, time_star, q)
                    dice_value_index = (dice_value_index + 1) % len(arr1)

        # 检查队列是否有消息
        try:
            msg = q.get_nowait()
            if msg == 'done':
                cout += 1
        except queue.Empty:
            pass

    pygame.quit()


class Dice:
    def __init__(self):
        self.num1 = None

    def fun(self):
        self.num1 = random.randint(0, 304)
        return self.num1

    @staticmethod
    def judge(my_list):
        for z in range(0, 3):
            for e in range(z + 1, 4):
                for k in range(e + 1, 5):
                    if my_list[z] == my_list[e] and my_list[z] == my_list[k]:
                        return 1
        return 2


if __name__ == "__main__":
    main()