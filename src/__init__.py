'''
JunQi game
'''
import pygame
from pathlib import Path

ROOT_PATH = Path(__file__)
IMAGES_PATH = ROOT_PATH / '..' / 'images'

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


class ChessError(Exception):
    pass


class Chess(pygame.sprite.Sprite):
    def __init__(self, level: int, team: str):
        self.level: int = level
        self.image = pygame.image.load(IMAGES_PATH / f'{team}_{level}.png')

    def __gt__(self, other):
        if not isinstance(other, Chess):
            raise TypeError
        
        if self.level == 10:
            return False
        
        elif self.level == 0 and other.level == 9:
            return True
        
        else:
            return self.level > other.level

    def __eq__(self, other):
        if not isinstance(other, Chess):
            raise TypeError
        
        return self.level == other.level or self.level == 10


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


def test():
    a = int(input('A >>> '))
    b = int(input('B >>> '))

    print('A > B: ', Chess(a, 'R') > Chess(b, 'B'))

    print('A == B: ', Chess(a, 'R') == Chess(b, 'B'))


if __name__ == "__main__":
    # main()
    while True:
        test()
