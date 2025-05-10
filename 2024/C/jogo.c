#include <stdio.h>

#define VIVO 1
#define MORTO 0

int main(void) {
    int tamanho_matriz, geracoes;
    scanf("%d %d\n", &tamanho_matriz, &geracoes);

    char presente[tamanho_matriz][tamanho_matriz];
    char futuro[tamanho_matriz][tamanho_matriz];
    for (char linha = 0; linha < tamanho_matriz; linha++) {
        for (char coluna = 0; coluna < tamanho_matriz; coluna++) {
            presente[linha][coluna] = getchar() - '0';
        }

        getchar();
    }

    for (char geracao = 0; geracao < geracoes; geracao++) {
        for (char linha = 0; linha < tamanho_matriz; linha++) {
            for (char coluna = 0; coluna < tamanho_matriz; coluna++) {
                char celula_viva = presente[linha][coluna];
                char vizinhos = 0;
    
                for (char mod_linha = -1; mod_linha <= 1; mod_linha++) {
                    char linha_vizinho = linha + mod_linha;
    
                    for (char mod_coluna = -1; mod_coluna <= 1; mod_coluna++) {
                        char coluna_vizinho = coluna + mod_coluna;
    
                        if (!((0 <= linha_vizinho && linha_vizinho < tamanho_matriz) && (0 <= coluna_vizinho && coluna_vizinho < tamanho_matriz))) {
                            continue;
                        } else if (mod_coluna == 0 && mod_linha == 0) {
                            continue;
                        }
    
                        vizinhos += presente[linha_vizinho][coluna_vizinho];
                    }
                }
    
                if (!celula_viva && vizinhos == 3) {
                    futuro[linha][coluna] = VIVO;
                } else if (celula_viva && (vizinhos == 2 || vizinhos == 3)) {
                    futuro[linha][coluna] = VIVO;
                } else {
                    futuro[linha][coluna] = MORTO;
                }
            }
        }

        for (char linha = 0; linha < tamanho_matriz; linha++) {
            for (char coluna = 0; coluna < tamanho_matriz; coluna++) {
                presente[linha][coluna] = futuro[linha][coluna];
            }
        }
    }
    
    for (char linha = 0; linha < tamanho_matriz; linha++) {
        for (char coluna = 0; coluna < tamanho_matriz; coluna++) {
            putchar(presente[linha][coluna] + '0');
        }

        putchar('\n');
    }

    return 0;
}