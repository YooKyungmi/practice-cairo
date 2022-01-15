import pygame
from PIL import Image, ImageDraw
import numpy as np


def pilImageToSurface(pilImage):     # pillow -> pygame 사진 변환
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode)


pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

img = Image.open("2.jpg").convert("RGB")
height, width = img.size   # 사진 원으로 자르기
lum_img = Image.new('L', [height, width], 0)

draw = ImageDraw.Draw(lum_img)
draw.pieslice([(0, 0), (height, width)], 0, 360,
              fill=255, outline="white")   # 검은색 바탕에 하얀색 원을 그려서 비트연산으로 원으로 자름
img_arr = np.array(img)
lum_img_arr = np.array(lum_img)
final_img_arr = np.dstack((img_arr, lum_img_arr))
final_image = Image.fromarray(final_img_arr)  # 비트연산
final_image.show()  # pillow로 출력

pygameSurface = pilImageToSurface(final_image)    # pygame으로 출력

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    window.blit(pygameSurface, pygameSurface.get_rect(center=(250, 250)))
    pygame.display.flip()
