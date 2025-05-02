#include <stdio.h>

int main(void) {
    int meses_vida;
    scanf("%d", &meses_vida);

    if (meses_vida <= 5) {
        int alturas_infancia[5] = {1, 2, 4, 5, 7};
        printf("%d", alturas_infancia[meses_vida - 1]);
    } else {
        int altura_fase_adulta = 7 + (meses_vida - 5) * 6;
        printf("%d", altura_fase_adulta);
    }

    return 0;
}