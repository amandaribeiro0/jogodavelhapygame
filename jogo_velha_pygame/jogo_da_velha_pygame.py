import pygame
import sys

pygame.init()

#Tela
tamanho = comprimento, altura = 600, 600
janela = pygame.display.set_mode(tamanho)

#Carrega imagens
xis = pygame.image.load("xiss.png")
bola = pygame.image.load("bola.png")
idosa = pygame.image.load("idosa2.png")
fogos = pygame.image.load("fogos2.png")

xis = pygame.transform.scale(xis, (100,100))
bola = pygame.transform.scale(bola,(100,100))
idosa = pygame.transform.scale(idosa,(500,500))
fogos = pygame.transform.scale(fogos,(400,400))


# cores:
preto = 0, 0, 0
branco = 255, 255, 255
vermelho = 255, 0, 0
verde = 0, 255, 0
azul = 0, 0, 255
ciano = 27, 242, 213
rosa = 203, 7, 118
roxo = 158, 151, 255
roxo2 = 74, 50, 155
verdeagua = 38, 209, 175
roxo3 = 175, 163, 222
rosa2 = 223,143,204

cores = [preto, branco, vermelho, verde, azul, ciano, rosa, roxo, roxo2, verdeagua, roxo3, rosa2]

vez = 'X'
rodada = 0
vencedor1 = ''

jogo = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'], ]

#Pos quadrantes
quadrante_linha = [50 , 250, 450]
quadrante_coluna = [50, 250, 450]

#Preenche a janela (0: preto - 1: branco - 2: vermelho - 3: verde - 4:azul - 5:ciano - 6:rosa - 7:roxo - 8:roxo2 - 9:verde água - 10:roxo3 - 11:rosa2)
janela.fill(cores[11]) 

#Desenha o jogo da velha
def desenha_quadro():
    pygame.draw.line(janela, preto, (200,0),(200,600),15)
    pygame.draw.line(janela, preto, (400,0),(400,600),15)
    pygame.draw.line(janela, preto, (0,200),(600,200),15)
    pygame.draw.line(janela, preto, (0,400),(600,400),15)


#Função para inserir imagem X ou O
def faz_jogada_bola(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    
    if (jogo[index_coluna][index_linha] == '_'):
        janela.blit(bola,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        jogo[index_coluna][index_linha] = 'O'
        return True
    else:
        print('Posição ocupada')
        return False


def faz_jogada_xis(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)

    if (jogo[index_coluna][index_linha] == '_'):
        janela.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        jogo[index_coluna][index_linha] = 'X'
        return True

    else:
        print('Posição ocupada')
        return False
    
####################################################

def ganhou1():
    vencedor = ''
    
    #Linhas
    if (jogo[0][0]== "X") and (jogo[0][1]== "X") and (jogo[0][2]== "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, branco,(0,100), [600,100], 15)
        janela.blit(fogos,(100,100))
        vencedor = 'X'
    if (jogo[1][0] == "X") and (jogo[1][1]== "X") and (jogo[1][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, branco, (0, 300), (600, 300), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'X'
    if (jogo[2][0] == "X") and (jogo[2][1] == "X") and(jogo[2][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, branco, (0, 500), (600, 500), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'X'

    #Coluna   
    if (jogo[0][0] == "X") and (jogo[1][0] == "X") and(jogo[2][0] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, branco, (100, 0), (100, 600), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'X'
    if (jogo[0][1] == "X") and (jogo[1][1] == "X") and(jogo[2][1] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, branco, (300, 0), (300, 600), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'X'
    if (jogo[0][2] == "X") and (jogo[1][2] == "X") and(jogo[2][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, branco, (500, 0), (500, 600), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'X'

    #Diagonal
    if (jogo[0][0] == "X") and (jogo[1][1] == "X") and (jogo[2][2] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, branco, (0, 0), (600, 600), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'X'
    if (jogo[0][2] == "X") and (jogo[1][1] == "X") and (jogo[2][0] == "X"):
        print ("JOGADOR X GANHOU!!!")
        pygame.draw.line(janela, branco, (0, 600), (600, 0), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'X'    
    return vencedor

def ganhou2():
    vencedor = ''
    #Linhas
    if (jogo[0][0]== "O") and (jogo[0][1]== "O") and (jogo[0][2]== "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, branco,(0,100), [600,100], 15)
        janela.blit(fogos,(100,100))
        vencedor = 'O'
    if (jogo[1][0] == "O") and (jogo[1][1]== "O") and (jogo[1][2] == "O"):
        print ("JOGADOR 1 GANHOU!!!")
        pygame.draw.line(janela, branco, (0, 300), (600, 300), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'O'
    if (jogo[2][0] == "O") and (jogo[2][1] == "O") and(jogo[2][2] == "O"):
        print ("JOGADOR 1 GANHOU!!!")
        pygame.draw.line(janela, branco, (0, 500), (600, 500), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'O'

    #Coluna   
    if (jogo[0][0] == "O") and (jogo[1][0] == "O") and(jogo[2][0] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, branco, (100, 0), (100, 600), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'O'
    if (jogo[0][1] == "O") and (jogo[1][1] == "O") and(jogo[2][1] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, branco, (300, 0), (300, 600), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'O'
    if (jogo[0][2] == "O") and (jogo[1][2] == "O") and(jogo[2][2] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, branco, (500, 0), (500, 600), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'O'

    #Diagonal
    if (jogo[0][0] == "O") and (jogo[1][1] == "O") and (jogo[2][2] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, branco, (0, 0), (600, 600), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'O'
    if (jogo[0][2] == "O") and (jogo[1][1] == "O") and (jogo[2][0] == "O"):
        print ("JOGADOR O GANHOU!!!")
        pygame.draw.line(janela, branco, (0, 600), (600, 0), 15)
        janela.blit(fogos,(100,100))
        vencedor = 'O'    
    return vencedor


#####################################################################################

while True:
    desenha_quadro()

    
    #Verifica eventos na janela do jogo
    for event in pygame.event.get():
        #Se for pressionado o fechar da janela o jogo é encerrado
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
                        
    #Verifica vez de cada jogador
            if (vez=='X'):
                print("Vez de X")
                fez_jogada = faz_jogada_xis(click_pos)
                vencedor1= ganhou1()
                if (fez_jogada == True):
                    vez='O'
                    rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'X'
                    
                
            elif (vez=='O'):
                print("Vez de O")
                fez_jogada = faz_jogada_bola(click_pos)
                vencedor1= ganhou2()
                if (fez_jogada == True):
                    vez = 'X'
                    rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'O'
                    
    pygame.display.flip() #Atualiza a janela

    #Verifica se há vencedores ou não
    if (rodada>=9) and (vencedor1==''):
        print("VELHA!")
        janela.fill(cores[11]) 
        janela.blit(idosa,(80,30))
        pygame.display.flip() #Atualiza a janela
        print(jogo)
        break
    
    elif (vencedor1!=''):
        print ('finish')
        print(jogo)
        break
