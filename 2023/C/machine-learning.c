#include <stdio.h>
#include <string.h>

#define IGUAL 0

typedef struct secao {
    char identificador[21];
    char palavras[100][21];
    char quantidade_palavras;
} topico;

int main(void) {
    int quantidade_topicos;
    scanf("%d", &quantidade_topicos);
    getchar();

    topico dicionario[quantidade_topicos];
    int cont_palavras_relacionadas[quantidade_topicos];
    for (int t = 0; t < quantidade_topicos; t++) {
        scanf("%s %d ", &dicionario[t].identificador, &dicionario[t].quantidade_palavras);
        cont_palavras_relacionadas[t] = 0;

        for (int p = 0; p < dicionario[t].quantidade_palavras; p++) {
            scanf("%s", &dicionario[t].palavras[p]);
        }
    }

    int tamanho_entrada;
    scanf("%d", &tamanho_entrada);
    getchar();

    for (int i = 0; i < tamanho_entrada; i++) {
        char palavra[21];
        scanf("%s", palavra);

        char topico_encontrado = 0;
        for (int t = 0; !topico_encontrado && t < quantidade_topicos; t++) {
            for (int p = 0; !topico_encontrado && p < dicionario[t].quantidade_palavras; p++) {
                topico_encontrado = (strcmp(palavra, dicionario[t].palavras[p]) == IGUAL);
            }

            if (topico_encontrado) {
                cont_palavras_relacionadas[t]++;
            }
        }
    }

    int topico_principal = 0;
    int max_palavras_relacionadas = cont_palavras_relacionadas[0];
    for (int t = 0; t < quantidade_topicos; t++) {
        if (cont_palavras_relacionadas[t] < max_palavras_relacionadas) {
            continue;
        } else if (cont_palavras_relacionadas[t] > max_palavras_relacionadas) {
            topico_principal = t;
            max_palavras_relacionadas = cont_palavras_relacionadas[t];
            continue;
        }

        if (strcmp(dicionario[topico_principal].identificador, dicionario[t].identificador) > 0) {
            topico_principal = t;
            max_palavras_relacionadas = cont_palavras_relacionadas[t];
        }
    }

    printf("%s\n", dicionario[topico_principal].identificador);
    return 0;
}