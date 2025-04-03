import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Variáveis dos elementos do jogo
raquete_largura, raquete_altura = 10, 100
bola_tamanho = 15

raquete_esquerda = pygame.Rect(30, altura // 2 - raquete_altura // 2, raquete_largura, raquete_altura)
raquete_direita = pygame.Rect(largura - 40, altura // 2 - raquete_altura // 2, raquete_largura, raquete_altura)
bola = pygame.Rect(largura // 2, altura // 2, bola_tamanho, bola_tamanho)

velocidade_raquete = 5
velocidade_bola_x = 4
velocidade_bola_y = 4

# Pontuação
pontos_esquerda = 0
pontos_direita = 0
pontos_para_vencer = 10

# Fonte para o placar
fonte = pygame.font.Font(None, 74)

# Função para desenhar os elementos
def desenhar():
    tela.fill(preto)
    pygame.draw.rect(tela, branco, raquete_esquerda)
    pygame.draw.rect(tela, branco, raquete_direita)
    pygame.draw.ellipse(tela, branco, bola)
    pygame.draw.aaline(tela, branco, (largura // 2, 0), (largura // 2, altura))

    # Desenhar o placar
    texto_esquerda = fonte.render(str(pontos_esquerda), True, branco)
    texto_direita = fonte.render(str(pontos_direita), True, branco)
    tela.blit(texto_esquerda, (largura // 4, 20))
    tela.blit(texto_direita, (3 * largura // 4, 20))

# Loop principal
relogio = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controle das raquetes
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete_esquerda.top > 0:
        raquete_esquerda.y -= velocidade_raquete
    if teclas[pygame.K_s] and raquete_esquerda.bottom < altura:
        raquete_esquerda.y += velocidade_raquete
    if teclas[pygame.K_UP] and raquete_direita.top > 0:
        raquete_direita.y -= velocidade_raquete
    if teclas[pygame.K_DOWN] and raquete_direita.bottom < altura:
        raquete_direita.y += velocidade_raquete

    # Movimento da bola
    bola.x += velocidade_bola_x
    bola.y += velocidade_bola_y

    # Colisão com as bordas
    if bola.top <= 0 or bola.bottom >= altura:
        velocidade_bola_y *= -1

    # Pontuação e reinício da bola
    if bola.left <= 0:
        pontos_direita += 1
        bola.x, bola.y = largura // 2, altura // 2
        velocidade_bola_x *= -1
    if bola.right >= largura:
        pontos_esquerda += 1
        bola.x, bola.y = largura // 2, altura // 2
        velocidade_bola_x *= -1

    # Colisão com as raquetes
    if bola.colliderect(raquete_esquerda) or bola.colliderect(raquete_direita):
        velocidade_bola_x *= -1

    # Verificar condição de vitória
    if pontos_esquerda >= pontos_para_vencer:
        print("Jogador da esquerda venceu!")
        pygame.quit()
        sys.exit()
    if pontos_direita >= pontos_para_vencer:
        print("Jogador da direita venceu!")
        pygame.quit()
        sys.exit()

    desenhar()
    pygame.display.flip()
    relogio.tick(60)
