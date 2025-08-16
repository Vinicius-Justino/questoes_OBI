#include <stdio.h>

int main(void) {
    int tamanho_sequencia;
    scanf("%d", &tamanho_sequencia);

    int sequencia[tamanho_sequencia];
    int inicio_intervalo = 0, final_intervalo = 0, maior_intervalo = 0;
    for (int i = 0; i < tamanho_sequencia; i++) {
        int numero;
        scanf("%d", &numero);

        sequencia[i] = numero;

        for (int j = inicio_intervalo; j <= final_intervalo; j++) {
            if (sequencia[j] == numero) {
                int tamanho_intervalo = final_intervalo - inicio_intervalo + 1;
                maior_intervalo = (tamanho_intervalo > maior_intervalo) ? tamanho_intervalo : maior_intervalo;

                inicio_intervalo = j + 1;
                break;
            }
        }

        final_intervalo = i;
    }

    int tamanho_intervalo = final_intervalo - inicio_intervalo + 1;
    maior_intervalo = (tamanho_intervalo > maior_intervalo) ? tamanho_intervalo : maior_intervalo;

    printf("%d\n", maior_intervalo);
    return 0;
}