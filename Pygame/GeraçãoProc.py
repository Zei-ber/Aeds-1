import pygame
import random

pygame.init()

TAM_BLOCO = 40
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

# Tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tomb of the Mask - Procedural com Fim")
clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 28)

# Estado do jogo
fase_atual = 0
vidas = 3
jogador_x, jogador_y = 1, 1
fases = []

def gerar_fase_procedural(largura=10, altura=10, dificuldade=1):
    fase = [[1]*largura for _ in range(altura)]
    x, y = 1, 1
    fase[y][x] = 0
    caminho = [(x, y)]
    direcoes = [(1,0), (0,1), (-1,0), (0,-1)]

    for _ in range(60 + dificuldade * 5):
        dx, dy = random.choice(direcoes)
        nx, ny = x + dx, y + dy
        if 1 <= nx < largura-1 and 1 <= ny < altura-1:
            x, y = nx, ny
            if random.random() < 0.15 + dificuldade * 0.02:
                fase[y][x] = 2  # obstáculo letal
            else:
                fase[y][x] = 0
            caminho.append((x, y))

    # Marcar o fim do caminho como linha de chegada (valor 3)
    if caminho:
        fim_x, fim_y = caminho[-1]
        fase[fim_y][fim_x] = 3
    return fase

def nova_fase():
    global jogador_x, jogador_y
    dificuldade = fase_atual + 1
    fases.append(gerar_fase_procedural(dificuldade=dificuldade))
    jogador_x, jogador_y = 1, 1

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
            pygame.draw.rect(tela, cor, (x*TAM_BLOCO, y*TAM_BLOCO, TAM_BLOCO, TAM_BLOCO))
    pygame.draw.rect(tela, AMARELO, (jogador_x*TAM_BLOCO, jogador_y*TAM_BLOCO, TAM_BLOCO, TAM_BLOCO))
    tela.blit(fonte.render(f"Fase {fase_atual+1}", True, VERDE), (10, 5))
    tela.blit(fonte.render(f"Vidas: {vidas}", True, AZUL), (LARGURA - 120, 5))

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
        elif fase[py][px] == 3:
            fase_atual += 1
            nova_fase()
            return
        novo_x, novo_y = px, py
    jogador_x, jogador_y = novo_x, novo_y

# Iniciar 1ª fase
nova_fase()

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
                    fases.clear()
                    nova_fase()
                    esperando = False

    clock.tick(FPS)

pygame.quit()