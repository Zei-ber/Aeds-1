import pygame

pygame.init()

TAM_BLOCO = 50
LARGURA = 10 * TAM_BLOCO
ALTURA = 10 * TAM_BLOCO
FPS = 60

# Cores
PRETO    = (0, 0, 0)
BRANCO   = (255, 255, 255)
AMARELO  = (255, 255, 0)
VERDE    = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL     = (0, 200, 255)
ROXO     = (100, 0, 255)
OURO     = (255, 215, 0)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tomb of the Mask - Estrelas")
clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 28)

vidas = 3
fase_atual = 0
jogador_x, jogador_y = 1, 1

# 0: caminho, 1: parede, 2: obstáculo, 3: fim, 4: estrela
fases = [
    [ # Fase 1
        [1,1,1,1,1,1,1,1,1,1],
        [1,0,4,0,0,0,0,0,3,1],
        [1,1,1,1,1,1,1,0,1,1],
        [1,0,0,0,0,0,1,0,1,1],
        [1,0,1,1,1,0,1,0,4,1],
        [1,0,1,2,1,0,1,1,0,1],
        [1,0,1,0,0,0,0,1,0,1],
        [1,0,1,1,1,1,4,1,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1],
    ],
    [ # Fase 2
        [1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,4,0,0,1],
        [1,1,1,1,1,1,1,1,4,1],
        [1,3,0,0,0,4,0,0,0,1],
        [1,1,0,0,0,1,1,1,1,1],
        [1,0,0,1,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,0,1],
        [1,0,1,0,4,0,0,1,0,1],
        [1,0,0,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1],
    ],
    [ # Fase 3
        [1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,4,0,1,1,1,1],
        [1,1,1,1,1,0,1,1,1,1],
        [1,0,0,4,1,0,0,1,1,1],
        [1,0,1,0,1,1,0,1,1,1],
        [1,0,1,0,0,0,0,1,3,1],
        [1,0,1,0,1,1,1,1,0,1],
        [1,4,0,0,0,4,0,1,0,1],
        [1,2,1,1,1,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1],
    ],
    [ # Fase 4
        [1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,1,0,3,1],
        [1,4,1,0,1,0,1,1,0,1],
        [1,0,0,0,1,0,4,1,0,1],
        [1,1,1,0,1,1,0,1,0,1],
        [1,0,1,2,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,0,1],
        [1,1,0,0,0,0,0,1,4,1],
        [1,0,1,1,2,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1],
    ],
    [ # Fase 5
        [1,1,1,1,1,1,1,1,1,1],
        [1,4,2,1,0,4,0,1,0,1],
        [1,0,1,1,1,1,0,1,0,1],
        [1,0,1,0,2,1,0,1,0,1],
        [1,0,1,0,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,1,0,1],
        [1,0,1,1,1,1,0,1,4,1],
        [1,0,0,0,0,1,0,0,0,1],
        [1,0,0,1,0,0,0,0,3,1],
        [1,1,1,1,1,1,1,1,1,1],
    ]
]

def contar_estrelas():
    return sum(row.count(4) for row in fases[fase_atual])

def desenhar_fase():
    fase = fases[fase_atual]
    for y in range(10):
        for x in range(10):
            celula = fase[y][x]
            if celula == 1:
                cor = PRETO
            elif celula == 0:
                cor = BRANCO
            elif celula == 2:
                cor = VERMELHO
            elif celula == 3:
                cor = ROXO
            elif celula == 4:
                cor = OURO
            pygame.draw.rect(tela, cor, (x*TAM_BLOCO, y*TAM_BLOCO, TAM_BLOCO, TAM_BLOCO))
    pygame.draw.rect(tela, AMARELO, (jogador_x*TAM_BLOCO, jogador_y*TAM_BLOCO, TAM_BLOCO, TAM_BLOCO))
    tela.blit(fonte.render(f"Fase {fase_atual+1}", True, VERDE), (10, 5))
    tela.blit(fonte.render(f"Vidas: {vidas}", True, AZUL), (LARGURA - 120, 5))
    tela.blit(fonte.render(f"Estrelas: {contar_estrelas()}", True, OURO), (LARGURA // 2 - 60, 5))

def mover(dx, dy):
    global jogador_x, jogador_y, vidas, fase_atual
    fase = fases[fase_atual]
    novo_x, novo_y = jogador_x, jogador_y
    while True:
        px, py = novo_x + dx, novo_y + dy
        if fase[py][px] == 1:
            break
        elif fase[py][px] == 2:
            vidas -= 1
            jogador_x, jogador_y = 1, 1
            return
        elif fase[py][px] == 4:
            fase[py][px] = 0
        elif fase[py][px] == 3:
            if contar_estrelas() == 0:
                fase_atual += 1
                if fase_atual >= len(fases):
                    fase_atual = 0
                jogador_x, jogador_y = 1, 1
                return
            else:
                break
        novo_x, novo_y = px, py
    jogador_x, jogador_y = novo_x, novo_y

# Loop principal
rodando = True
while rodando:
    tela.fill(PRETO)
    desenhar_fase()
    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                mover(-1, 0)
            elif evento.key == pygame.K_RIGHT:
                mover(1, 0)
            elif evento.key == pygame.K_UP:
                mover(0, -1)
            elif evento.key == pygame.K_DOWN:
                mover(0, 1)

    if vidas <= 0:
        tela.fill(PRETO)
        tela.blit(fonte.render("GAME OVER - Pressione qualquer tecla", True, VERMELHO), (50, ALTURA//2 - 20))
        pygame.display.update()
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    esperando = False
                    rodando = False
                elif evento.type == pygame.KEYDOWN:
                    vidas = 3
                    fase_atual = 0
                    jogador_x, jogador_y = 1, 1
                    esperando = False

    clock.tick(FPS)

pygame.quit()