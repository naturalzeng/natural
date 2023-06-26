import pyautogui

import time


# pyautogui.mouseInfo()


# time.sleep(2)  # 留一点切换页面时间
# im = pyautogui.screenshot()  # 截取整个屏幕
# om = im.crop(
#     (2198, 651, 2305, 679))  # 根据截取的屏幕仅截取“带赞的手势图片”，用pyautogui.mouseInfo()获取图片的位置(1127,756,1146,775)，这里截取区域用到了Pillow
# om.save(r"E:\images\2.png")  # 将图片保存供pyautogui.locateOnScreen（）使用


def zan():
    # time.sleep(1)  # 这个可以用来防止操作过快
    # left, top, width, height = pyautogui.locateOnScreen(r"E:\images\quiz.png", region=(1980, 33, 2519, 993))
    # try:
    #     center = pyautogui.center((left, top, width, height))
    #     pyautogui
    #     pyautogui.click(center)
    # except TypeError:
    #     print("not found")
    # print('进入答题页面')
    #
    # time.sleep(5)
    # left, top, width, height = pyautogui.locateOnScreen(r"E:\images\zhangpeng.png", region=(1980, 33, 2519, 993))
    # center = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    # pyautogui.click(center)
    #
    # time.sleep(5)
    # left, top, width, height = pyautogui.locateOnScreen(r"E:\images\a.png", region=(1980, 33, 2519, 993))
    # center = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    # pyautogui.click(center)
    #
    # time.sleep(5)
    # left, top, width, height = pyautogui.locateOnScreen(r"E:\images\next.png", region=(1980, 33, 2519, 993))
    # center = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    # pyautogui.click(center)

    # time.sleep(5)
    # left, top, width, height = pyautogui.locateOnScreen(r"E:\images\next.png", region=(1980, 33, 2519, 993))
    # print(left)
    # print(top)
    # print(width)
    # print(height)
    # center = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    # pyautogui.click(center)

    pyautogui.moveTo(2246, 491, duration=0.25)
    pyautogui.scroll(-500)


# zan()

def click_image(image):
    while 1 == 1:
        try:
            left, top, width, height = pyautogui.locateOnScreen(image, region=(1980, 33, 2519, 993))
            center = pyautogui.center((left, top, width, height))
            print('找到' + image)
            pyautogui.click(center)
            time.sleep(0.3)
            break
        except TypeError:
            print('重试' + image)
            pyautogui.moveTo(2246, 491, duration=0.25)
            pyautogui.scroll(-500)
            if "a.png" in image:
                time.sleep(3)
                try:
                    left, top, width, height = pyautogui.locateOnScreen(r"E:\images\next.png", region=(1980, 33, 2519, 993))
                    center = pyautogui.center((left, top, width, height))
                    print('找到' + image)
                    pyautogui.click(center)
                except TypeError:
                    print('not found a.png')
            time.sleep(0.3)


click_image(r"E:\images\quiz.png")
click_image(r"E:\images\zhangpeng.png")
while 1 == 1:
    click_image(r"E:\images\a.png")
    click_image(r"E:\images\submit.png")
    click_image(r"E:\images\next.png")
