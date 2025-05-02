#include <stdio.h>

int main(void) {
    int quantidade_pocoes, variedade_minima;
    scanf("%d %d", &quantidade_pocoes, &variedade_minima);

    int prateleira[quantidade_pocoes];
    for (int espaco = 0; espaco < quantidade_pocoes; espaco++) {
        scanf("%d", &prateleira[espaco]);
    }

    int cont_maneiras = 0;
    for (int tamanho_segmento = variedade_minima; tamanho_segmento <= quantidade_pocoes; tamanho_segmento++) {
        for (int inicio_segmento = 0; inicio_segmento <= (quantidade_pocoes - tamanho_segmento); inicio_segmento++) {
            int pocoes_diferentes[tamanho_segmento];
            int variedade = 0;
            for (int i = 0; i < tamanho_segmento; i++) {
                int pocao_diferente = 1;
                for (int pocao = 0; pocao < variedade && pocao_diferente; pocao++) {
                    pocao_diferente = (prateleira[inicio_segmento + i] != pocoes_diferentes[pocao]);
                }

                if (pocao_diferente) {
                    pocoes_diferentes[variedade] = prateleira[inicio_segmento + i];
                    variedade++;
                }
            }

            cont_maneiras += (variedade >= variedade_minima);
        }
    }

    printf("%d\n", cont_maneiras);
    return 0;
}