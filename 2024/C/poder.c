#include <stdio.h>

#define VIZINHO 1
#define CONQUISTADO 2
#define Y 0
#define X 1
#define HEROI_VIVO 1
#define VISITADO 1

typedef unsigned long int poder;

const char DIRECOES[4][2] = {
    {-1, 0}, // norte
    {0, 1},  // leste
    {1, 0},  // sul
    {0, -1}  // oeste
};

int main(void) {
    int linhas, colunas;
    scanf("%d %d", &linhas, &colunas);

    unsigned int tabuleiro[linhas][colunas];
    for (int linha = 0; linha < linhas; linha++) {
        for (int coluna = 0; coluna < colunas; coluna++) {
            scanf("%u", &tabuleiro[linha][coluna]);
        }
    }

    for (int heroi_y = 0; heroi_y < linhas; heroi_y++) {
        for (int heroi_x = 0; heroi_x < colunas; heroi_x++) {
            poder poder_heroi = tabuleiro[heroi_y][heroi_x];
            
            // lembra onde estao todos os vizinhos do terreno que o heroi ja conquistou
            char vizinhanca[linhas][colunas];
            int quantidade_vizinhos = 0;
            for (int linha = 0; linha < linhas; linha++) {
                for (int coluna = 0; coluna < colunas; coluna++) {
                    vizinhanca[linha][coluna] = !VIZINHO;
                }
            }

            for (char i = 0; i < 4; i++) {
                char vizinho_x = heroi_x + DIRECOES[i][X];
                char vizinho_y = heroi_y + DIRECOES[i][Y];

                if (0 <= vizinho_x && vizinho_x < colunas && 0 <= vizinho_y && vizinho_y < linhas) {
                    vizinhanca[vizinho_y][vizinho_x] = VIZINHO;
                    quantidade_vizinhos++;
                }
            }
            vizinhanca[heroi_y][heroi_x] = CONQUISTADO;

            while (HEROI_VIVO) {
                // procura o vizinho mais fraco dentre todos os vizinhos do heroi
                poder vizinho_mais_fraco = poder_heroi + 1;
                int posicao_mais_fraco[2] = {0, 0};

                char caminho[linhas][colunas];
                for (int linha = 0; linha < linhas; linha++) {
                    for (int coluna = 0; coluna < colunas; coluna++) {
                        caminho[linha][coluna] = !VISITADO;
                    }
                }
                caminho[heroi_y][heroi_x] = VISITADO;

                // anda em espiral partindo da posicao do heroi
                int casa_atual[2] = {heroi_y, heroi_x};
                char direcao_caminhada = 0, proxima_direcao = 1;
                int vizinhos_visitados = 0;

                while (vizinhos_visitados < quantidade_vizinhos) {
                    casa_atual[X] += DIRECOES[direcao_caminhada][X];
                    casa_atual[Y] += DIRECOES[direcao_caminhada][Y];

                    // vira em sentido horario se saiu do tabuleiro ou se a proxima casa naquele sentindo nao foi visitada ainda
                    if (!(0 <= casa_atual[X] && casa_atual[X] < colunas && 0 <= casa_atual[Y] && casa_atual[Y] < linhas)) {
                        casa_atual[X] -= DIRECOES[direcao_caminhada][X];
                        casa_atual[Y] -= DIRECOES[direcao_caminhada][Y];

                        direcao_caminhada = proxima_direcao;
                        proxima_direcao = (proxima_direcao + 1) % 4;
                        continue;
                    }

                    char casa_adjascente[2] = {casa_atual[Y] + DIRECOES[proxima_direcao][Y], casa_atual[X] + DIRECOES[proxima_direcao][X]};
                    if (0 <= casa_adjascente[X] && casa_adjascente[X] < colunas && 0 <= casa_adjascente[Y] && casa_adjascente[Y] < linhas) {
                        if (caminho[casa_adjascente[Y]][casa_adjascente[X]] != VISITADO) {
                            direcao_caminhada = proxima_direcao;
                            proxima_direcao = (proxima_direcao + 1) % 4;
                        }
                    }

                    if (caminho[casa_atual[Y]][casa_atual[X]] == VISITADO) {
                        continue;
                    }
                    
                    caminho[casa_atual[Y]][casa_atual[X]] = VISITADO;
                    if (vizinhanca[casa_atual[Y]][casa_atual[X]] != VIZINHO) {
                        continue;
                    }

                    vizinhos_visitados++;
                    if (tabuleiro[casa_atual[Y]][casa_atual[X]] < vizinho_mais_fraco) {
                        vizinho_mais_fraco = tabuleiro[casa_atual[Y]][casa_atual[X]];
                        posicao_mais_fraco[X] = casa_atual[X];
                        posicao_mais_fraco[Y] = casa_atual[Y];
                    }
                }

                if (vizinho_mais_fraco > poder_heroi) {
                    break;
                }

                // o heroi derrota o vizinho mais fraco, conquista o seu territorio e passa a ser vizinho de todos os vizinhos dele
                poder_heroi += vizinho_mais_fraco;

                vizinhanca[posicao_mais_fraco[Y]][posicao_mais_fraco[X]] = CONQUISTADO;
                quantidade_vizinhos--;

                for (char i = 0; i < 4; i++) {
                    char vizinho_x = posicao_mais_fraco[X] + DIRECOES[i][X];
                    char vizinho_y = posicao_mais_fraco[Y] + DIRECOES[i][Y];

                    if (vizinhanca[vizinho_y][vizinho_x] != !VIZINHO) {
                        continue;
                    } else if (0 <= vizinho_x && vizinho_x < colunas && 0 <= vizinho_y && vizinho_y < linhas) {
                        vizinhanca[vizinho_y][vizinho_x] = VIZINHO;
                        quantidade_vizinhos++;
                    }
                }

                if (quantidade_vizinhos == 0) {
                    break;
                }
            }

            printf("%lu%c", poder_heroi, ((heroi_x == colunas - 1) ? '\n' : ' '));
        }
    }

    return 0;
}