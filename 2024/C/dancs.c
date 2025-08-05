#include <stdio.h>

#define TROCA_LINHA 'L'
#define TROCA_COLUNA 'C'

int main(void) {
    int linhas, colunas, passos;
    scanf("%d %d %d", &linhas, &colunas, &passos);

    int pista[linhas][colunas];
    for (int linha = 0; linha < linhas; linha++) {
        for (int coluna = 0; coluna < colunas; coluna++) {
            pista[linha][coluna] = linha * colunas + coluna + 1;
        }
    }

    for (int passo = 0; passo < passos; passo++) {
        char comando;
        int origem, destino;
        getchar();
        scanf("%c %d %d", &comando, &origem, &destino);
        origem--;
        destino--;

        if (comando == TROCA_LINHA) {
            for (int coluna = 0; coluna < colunas; coluna++) {
                int buffer = pista[destino][coluna];

                pista[destino][coluna] = pista[origem][coluna];
                pista[origem][coluna] = buffer;
            }
        } else if (comando == TROCA_COLUNA) {
            for (int linha = 0; linha < linhas; linha++) {
                int buffer = pista[linha][destino];

                pista[linha][destino] = pista[linha][origem];
                pista[linha][origem] = buffer;
            }   
        }
    }

    for (int linha = 0; linha < linhas; linha++) {
        for (int coluna = 0; coluna < colunas; coluna++) {
            printf("%d", pista[linha][coluna]);
            putchar((coluna == colunas - 1) ? '\n' : ' ');
        }
    }

    return 0;
}