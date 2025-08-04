#include <stdio.h>

int main(void) {
    int tamanho_lista, quantidade_perguntas;
    scanf("%d %d", &tamanho_lista, &quantidade_perguntas);

    char lista[tamanho_lista];
    for (int i = 0; i < tamanho_lista; i++) {
        int digito;
        scanf("%d", &digito);

        lista[i] = digito;
    }

    for (int pergunta = 0; pergunta < quantidade_perguntas; pergunta++) {
        int inicio, fim;
        scanf("%d %d", &inicio, &fim);

        int potencial_intervalo = 0;
        for (int i = inicio - 1; i < fim; i++) {
            potencial_intervalo += lista[i] * 11 * (fim - inicio);
        }

        printf("%d\n", potencial_intervalo);
    }

    return 0;
}