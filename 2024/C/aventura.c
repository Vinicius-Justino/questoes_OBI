#include <stdio.h>

#define MOVA 'M'
#define GIRE 'G'

#define NORTE 0
#define LESTE 1
#define SUL 2
#define OESTE 3

int main(void) {
    int quantidade_instrucoes;
    scanf("%d", &quantidade_instrucoes);

    int coordenadas[2] = {0, 0};
    char direcao = NORTE;
    for (int i = 0; i < quantidade_instrucoes; i++) {
        getchar();
        char acao = getchar();
        if (acao == MOVA) {
            int passos;
            scanf("%d", &passos);

            coordenadas[(direcao == NORTE || direcao == SUL)] += passos * (1 - 2 * (direcao == OESTE || direcao == SUL));
        } else {
            int graus;
            scanf("%d", &graus);

            direcao = (direcao + (graus / 90)) % 4;
        }
    }

    printf("%d %d\n", coordenadas[0], coordenadas[1]);
}