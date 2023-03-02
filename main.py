import pygame

pygame.init()
pygame.font.init()

# Altera e largura da tela
SCREEN_W = 926
SCREEN_H = 450

# FPS
fps = pygame.time.Clock()

# Cria a tela
display = pygame.display.set_mode((SCREEN_W,SCREEN_H))

# Carrega as imagens da animação do personagem
imagesDino = [
    pygame.image.load('assets/user/user-1.png'),
    pygame.image.load('assets/user/user-2.png'),
    pygame.image.load('assets/user/user-3.png')
]

# Dino 
placar_dino = 0
speed_dino = 2
dino = imagesDino[0].get_rect(left=40, bottom=(SCREEN_H - 15))

# Informações do elemento de colisão 
elemento_img = pygame.image.load('assets/dormindo.png')
elemento = elemento_img.get_rect(left=SCREEN_W, bottom=(SCREEN_H - 15)) 
elemento_speed = 5


# Placar
font = pygame.font.Font(None, 50)
placar = font.render(str(placar_dino), True, "white")

# Background
bg_img = pygame.image.load('assets/bg.png')
bg_img = pygame.transform.scale(bg_img,(SCREEN_W,SCREEN_H))
speed = 2

loop = True

# Auxiliares
i = 0
img = 0
imgExibe = 0
cena = "menu"

# Fade
fade_img = pygame.Surface((1280, 720)).convert_alpha()
fade_img.fill("black")
fade_alpha = 255

# Game Over
gameover_img = pygame.image.load('assets/gameover.png')
logo = pygame.image.load('assets/dinos.png')
logo_img = logo.get_rect(center=[SCREEN_W / 2, SCREEN_H / 2])

pula = False
sobe = True

while loop: 
    # Eventos 
    for event in pygame.event.get():
        
        # Evento de fechar a janela
        if event.type == pygame.QUIT:
             loop = False
                
        # Evento de clique         
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and (cena == "gameover" or cena == "menu"):
                placar_dino = 0
                placar = font.render(str(placar_dino), True, "white")
                elemento.x = SCREEN_W
                cena = "jogo"
                fade_alpha = 255
                
            if event.key == pygame.K_SPACE and cena == "jogo" and pula == False	:
                pula = True
                sobe = True


    if cena == "jogo":
        img += speed_dino
        if img == 60:
            img = 0
        
        if img < 20:
            imgExibe = 0
        elif img < 40:
            imgExibe = 1
        else:
            imgExibe = 2
            
        elemento.x -= elemento_speed

        if elemento.x <= 0:
            placar_dino += 10
            placar = font.render(str(placar_dino), True, "white")
            elemento.x = SCREEN_W
            
        if placar_dino == 20:
            elemento_speed = 6
            speed = 5
            
        if placar_dino == 70:
            elemento_speed = 9
            speed = 4
            
        if placar_dino == 150:
            elemento_speed = 8
            
        if placar_dino == 390:
            elemento_speed = 11
            speed = 7
            
        if placar_dino == 500:
            elemento_speed = 15
            speed = 10
            
        if placar_dino == 1000:
            elemento_speed = 18
            speed = 15
            
        # Imagem de fundo 
        display.fill((0,0,0))
        display.blit(bg_img,(i,0))
        display.blit(bg_img,(SCREEN_W + i,0))
        
        if(i <= -SCREEN_W):
            display.blit(bg_img,(SCREEN_W + i,0))
            i = 0
        
        
        i -= speed
        
        # Colisao 
        if elemento.colliderect(dino):
            cena = "gameover"
        
        dinoPula = 0
        
        if pula:
            if sobe:
                if dino.y > 50:
                    dino.y -= 8
                else:
                    sobe = False
            else: 
                if dino.y < 200:
                    dino.y += 5
                else:
                    dino.y = 290
                    pula = False
            
            pygame.time.delay(10)
        
        
        # Adiciona o personagem na tela
        display.blit(imagesDino[imgExibe],dino)
        
        # Adiciona o elemento obstáculo na tela
        display.blit(elemento_img, elemento)
        
        # Adiciona o placar na tela
        display.blit(placar, (SCREEN_W / 2, 10))
        
    elif cena == "gameover":
        
        fade_alpha -= 2
        fade_img.set_alpha(fade_alpha)
        
        display.blit(gameover_img, [0, 0])
        display.blit(fade_img, [0, 0])
        
        if fade_alpha <= 0:
            texto = font.render("Pressione entrer para jogar", True, "white")
            display.blit(texto, [210, 188])
            
    elif cena == "menu":
        
        texto = font.render("Pressione entrer para jogar", True, "white")
        texto_rect = texto.get_rect(center=[(SCREEN_W / 2), (SCREEN_H / 2)  + 130])
        
        fade_alpha -= 2
        fade_img.set_alpha(fade_alpha)
        
        display.fill((0,0,0))
        display.blit(bg_img,(i,0))
        display.blit(logo, logo_img)
        display.blit(texto, texto_rect)
        display.blit(fade_img, [0, 0])
        
    
    fps.tick(60)
    pygame.display.update()
    