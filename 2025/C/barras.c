#include <stdio.h>

int main(void) {
    int quantidade_brinquedos;
    scanf("%d", &quantidade_brinquedos);

    int avaliacoes[quantidade_brinquedos];
    int altura_grafico = -1;
    for (int i = 0; i < quantidade_brinquedos; i++) {
        int avaliacao;
        scanf("%d", &avaliacao);

        avaliacoes[i] = avaliacao;
        altura_grafico = (avaliacao > altura_grafico) ? avaliacao : altura_grafico;
    }

    for (int nivel = altura_grafico; nivel > 0; nivel--) {
        char linha_saida[2 * quantidade_brinquedos];

        for (int i = 0; i < quantidade_brinquedos; i++) {
            linha_saida[2 * i] = (avaliacoes[i] >= nivel) ? '1' : '0';
            linha_saida[(2 * i) + 1] = (i == quantidade_brinquedos - 1) ? '\0' : ' ';
        }

        printf("%s\n", linha_saida);
    }

    return 0;
}