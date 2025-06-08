#include <stdio.h>

#define NAO_VIZINHO 0
#define VIZINHO 1

int quantidade_cidades;
char caminho_encontrado = 0;
void encontra_caminho(size_t N, char mapa[][N], int caminho[], int destino, int indice_cidade_atual);

int main(void) {
    int variedade_frutas;
    scanf("%d %d", &quantidade_cidades, &variedade_frutas);

    char mapa[quantidade_cidades][quantidade_cidades];
    for (int origem = 0; origem < quantidade_cidades; origem++) {
        for (int destino = 0; destino < quantidade_cidades; destino++) {
            mapa[origem][destino] = NAO_VIZINHO;
        }
    }

    for (int i = 1; i < quantidade_cidades; i++) {
        int origem, destino;
        scanf("%d %d", &origem, &destino);
        origem--;
        destino--;

        mapa[origem][destino] = VIZINHO;
        mapa[destino][origem] = VIZINHO;
    }

    char mercados[quantidade_cidades][variedade_frutas];
    for (int cidade = 0; cidade < quantidade_cidades; cidade++) {
        for (int tipo_fruta = 0; tipo_fruta < variedade_frutas; tipo_fruta++) {
            int estado;
            scanf("%d", &estado);

            mercados[cidade][tipo_fruta] = estado;
        }
    }

    int quantidade_viagens;
    scanf("%d", &quantidade_viagens);

    for (int viagem = 0; viagem < quantidade_viagens; viagem++) {
        int origem, destino;
        scanf("%d %d", &origem, &destino);
        origem--;
        destino--;

        int caminho[quantidade_cidades];
        caminho[0] = origem;
        caminho_encontrado = 0;
        encontra_caminho(quantidade_cidades, mapa, caminho, destino, 0);

        int carrinho_compras[variedade_frutas];
        for (int tipo_fruta = 0; tipo_fruta < variedade_frutas; tipo_fruta++) {
            carrinho_compras[tipo_fruta] = 0;
        }

        for (int i = 0; 1; i++) {
            int cidade_atual = caminho[i];

            for (int tipo_fruta = 0; tipo_fruta < variedade_frutas; tipo_fruta++) {
                carrinho_compras[tipo_fruta] += mercados[cidade_atual][tipo_fruta];
            }

            if (cidade_atual == destino) {
                break;
            }
        }

        int variedade_compra = 0;
        for (int tipo_fruta = 0; tipo_fruta < variedade_frutas; tipo_fruta++) {
            variedade_compra += carrinho_compras[tipo_fruta] % 2;
        }

        printf("%d\n", variedade_compra);
    }
}

void encontra_caminho(size_t N, char mapa[][N], int caminho[], int destino, int indice_cidade_atual) {
    int cidade_atual = caminho[indice_cidade_atual];
    if (cidade_atual == destino) {
        caminho_encontrado = 1;
        return;
    }

    for (int cidade = 0; !caminho_encontrado && cidade < quantidade_cidades; cidade++) {
        if (mapa[cidade_atual][cidade] == NAO_VIZINHO) {
            continue;
        }

        int cidade_no_caminho = 0;
        for (int i = 0; !cidade_no_caminho && i < indice_cidade_atual; i++) {
            cidade_no_caminho = (cidade == caminho[i]);
        }

        if (!cidade_no_caminho) {
            caminho[indice_cidade_atual + 1] = cidade;
            encontra_caminho(N, mapa, caminho, destino, indice_cidade_atual + 1);
        }
    }
}