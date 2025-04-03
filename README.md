. Bibliotecas e Configurações Iniciais
python
import pygame
import sys
pygame: Uma biblioteca especializada em desenvolvimento de jogos. Ela fornece funções para trabalhar com gráficos, sons, e entrada de usuários.

sys: Usada para encerrar o jogo quando necessário.

Depois disso, inicializamos o Pygame:

python
pygame.init()
Este comando prepara a biblioteca para que possamos usá-la.

2. Definição da Janela
python
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")
Aqui, criamos a janela do jogo com dimensões 800x600 pixels e definimos o título "Pong".

3. Definição das Cores
python
preto = (0, 0, 0)
branco = (255, 255, 255)
Usamos o formato RGB para representar as cores. O fundo será preto e os elementos do jogo serão desenhados na cor branca.

4. Definição dos Objetos do Jogo
python
raquete_esquerda = pygame.Rect(30, altura // 2 - 50, 10, 100)
raquete_direita = pygame.Rect(largura - 40, altura // 2 - 50, 10, 100)
bola = pygame.Rect(largura // 2, altura // 2, 15, 15)
pygame.Rect: Cria retângulos que representam os objetos do jogo.

As raquetes têm 10px de largura e 100px de altura.

A bola é um quadrado de 15px.

5. Variáveis de Controle
python
velocidade_raquete = 5
velocidade_bola_x = 4
velocidade_bola_y = 4
velocidade_raquete: Define a velocidade com que as raquetes podem se mover.

velocidade_bola_x e velocidade_bola_y: Representam as velocidades horizontais e verticais da bola, respectivamente.

6. Pontuação e Condição de Vitória
python
pontos_esquerda = 0
pontos_direita = 0
pontos_para_vencer = 10
pontos_esquerda e pontos_direita: Armazenam os pontos de cada jogador.

pontos_para_vencer: Define quantos pontos são necessários para vencer o jogo.

7. Função desenhar()
python
def desenhar():
    tela.fill(preto)
    pygame.draw.rect(tela, branco, raquete_esquerda)
    pygame.draw.rect(tela, branco, raquete_direita)
    pygame.draw.ellipse(tela, branco, bola)
    pygame.draw.aaline(tela, branco, (largura // 2, 0), (largura // 2, altura))
    texto_esquerda = fonte.render(str(pontos_esquerda), True, branco)
    texto_direita = fonte.render(str(pontos_direita), True, branco)
    tela.blit(texto_esquerda, (largura // 4, 20))
    tela.blit(texto_direita, (3 * largura // 4, 20))
tela.fill(preto): Preenche o fundo da janela com a cor preta.

pygame.draw.rect: Desenha as raquetes.

pygame.draw.ellipse: Desenha a bola.

pygame.draw.aaline: Desenha uma linha divisória no centro da tela.

tela.blit: Exibe o placar na tela.

8. Movimentação das Raquetes
python
if teclas[pygame.K_w] and raquete_esquerda.top > 0:
    raquete_esquerda.y -= velocidade_raquete
if teclas[pygame.K_s] and raquete_esquerda.bottom < altura:
    raquete_esquerda.y += velocidade_raquete
Usamos as teclas W e S para mover a raquete da esquerda.

As teclas SETAS PARA CIMA e PARA BAIXO controlam a raquete da direita.

9. Movimento e Colisões da Bola
python
bola.x += velocidade_bola_x
bola.y += velocidade_bola_y
A posição da bola é atualizada com base na velocidade.

Quando a bola toca o topo ou a base da janela:

python
if bola.top <= 0 or bola.bottom >= altura:
    velocidade_bola_y *= -1
A velocidade vertical da bola é invertida.

Quando a bola ultrapassa um dos lados, o adversário ganha pontos:

python
if bola.left <= 0:
    pontos_direita += 1
if bola.right >= largura:
    pontos_esquerda += 1
Quando a bola colide com uma das raquetes:

python
if bola.colliderect(raquete_esquerda) or bola.colliderect(raquete_direita):
    velocidade_bola_x *= -1
A velocidade horizontal da bola é invertida.

10. Verificação de Condição de Vitória
python
if pontos_esquerda >= pontos_para_vencer:
    print("Jogador da esquerda venceu!")
    pygame.quit()
    sys.exit()
if pontos_direita >= pontos_para_vencer:
    print("Jogador da direita venceu!")
    pygame.quit()
    sys.exit()
Aqui, o jogo verifica se algum jogador alcançou a pontuação necessária para vencer. Caso isso aconteça, o jogo termina e uma mensagem é exibida no console.

11. Atualização da Tela
python
desenhar()
pygame.display.flip()
desenhar(): Atualiza os elementos visuais do jogo.

pygame.display.flip(): Renderiza a nova imagem na tela.
