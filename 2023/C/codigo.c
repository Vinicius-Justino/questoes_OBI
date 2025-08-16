#include <stdio.h>

int main(void) {
    int tamanho_entrada;
    scanf("%d", &tamanho_entrada);
    getchar();

    char letra_atual = getchar();
    int cont_letra = 1;
    for (char proxima_letra = getchar(); proxima_letra != '\n'; proxima_letra = getchar()) {
        if (proxima_letra == letra_atual) {
            cont_letra++;
        } else {
            printf("%d %c ", cont_letra, letra_atual);

            letra_atual = proxima_letra;
            cont_letra = 1;
        }
    }

    printf("%d %c\n", cont_letra, letra_atual);
    return 0;
}