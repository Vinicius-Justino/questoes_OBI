#include <stdio.h>

#define VALOR_MAXIMO 1000000007

int main(void) {
    int passos = 0;
    scanf("%d", &passos);

    unsigned int tesouras_passo = 1;
    unsigned int tinta_gasta = 0;
    for (int passo = 1; passo <= passos; passo++) {
        if (passo % 2 == 0) {
            tesouras_passo *= 2;
            tesouras_passo %= VALOR_MAXIMO;
        }

        tinta_gasta += (2 * tesouras_passo) - 1;
        tinta_gasta %= VALOR_MAXIMO;
    }

    printf("%d\n", tinta_gasta);
    return 0;
}