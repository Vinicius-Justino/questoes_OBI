#include <stdio.h>

int main(void) {
    int escola, mercado, loja;
    scanf("%d\n%d\n%d", &escola, &mercado, &loja);

    int rua[3] = {escola, mercado, loja};
    int menor = escola, maior = escola;
    for (char predio = 0; predio < 3; predio++) {
        menor = (rua[predio] < menor) ? rua[predio] : menor;
        maior = (rua[predio] > maior) ? rua[predio] : maior;
    }

    printf("%d\n", (maior - menor) * 2);
}