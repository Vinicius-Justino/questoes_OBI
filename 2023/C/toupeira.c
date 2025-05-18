#include <stdio.h>

int main(void) {
    int saloes, tuneis;
    scanf("%d %d\n", &saloes, &tuneis);

    typedef struct vertice {
        int vizinhanca[saloes - 1];
        int grau;
    } salao;

    salao mapa[saloes];
    for (int i = 0; i < saloes; i++) {
        mapa[i].grau = 0;
    }

    for (int i = 0; i < tuneis; i++) {
        int origem, destino;
        scanf("%d %d\n", &origem, &destino);
        origem--;
        destino--;

        mapa[origem].vizinhanca[mapa[origem].grau] = destino;
        mapa[origem].grau++;

        mapa[destino].vizinhanca[mapa[destino].grau] = origem;
        mapa[destino].grau++;
    }

    int caminhos, cont_caminhos_validos = 0;
    scanf("%d\n", &caminhos);
    for (int i = 0; i < caminhos; i++) {
        int tamanho_passeio;
        scanf("%d ", &tamanho_passeio);

        int salao_atual;
        char separador, caminho_valido = 1;

        scanf("%d%c", &salao_atual, &separador);
        salao_atual--;
        while (separador != '\n') {
            int prox_salao;
            scanf("%d%c", &prox_salao, &separador);
            prox_salao--;

            if (!caminho_valido) {
                continue;
            }

            char eh_vizinho = 0;
            for (int j = 0; !eh_vizinho && (j < mapa[salao_atual].grau); j++) {
                eh_vizinho = (prox_salao == mapa[salao_atual].vizinhanca[j]);
            }

            caminho_valido = eh_vizinho;
            salao_atual = prox_salao;
        }

        cont_caminhos_validos += caminho_valido;
    }

    printf("%d\n", cont_caminhos_validos);
    return 0;
}