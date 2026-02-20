'''
JunQi game
'''
import pygame

CHESS_LEVEL: dict[int, str] = {
    0: '工兵',
    1: '排长',
    2: '连长',
    3: '营长',
    4: '团长',
    5: '旅长',
    6: '师长',
    7: '军长',
    8: '司令',
    9: '地雷',
    10: '炸弹',
    -1: '军旗',
}


class Chess(pygame.sprite.Sprite):
    def __init__(self, level: int, team:str):
        self.level: int = level
        self.image = pygame.image.load(f'{team}-{level}.png')

def main():
    pygame.init()
    screen = pygame.display.set_mode((720, 900))
    pygame.display.set_caption('JunQi')
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
