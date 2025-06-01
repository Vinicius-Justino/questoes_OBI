#include <stdio.h>

#define CONSTRUCAO 1
#define CONSULTA 2

typedef struct elo {
    int cidades[2];
    unsigned int peso;
} estrada;

unsigned long long int soma_distancias;
char caminho_encontrado;
void caminha(estrada obra[], int quantidade_estradas, int caminho[], int tamanho_caminho, unsigned long long int distancia_percorrida, int destino);

int main(void) {
    int quantidade_cidades, tamanho_lista;
    scanf("%d %d", &quantidade_cidades, &tamanho_lista);

    estrada obra[quantidade_cidades - 1];
    int quantidade_estradas = 0;
    for (int linha = 0; linha < tamanho_lista; linha++) {
        int tarefa;
        scanf("%d", &tarefa);

        if (tarefa == CONSTRUCAO) {
            int origem, destino, tamanho;
            scanf("%d %d %d", &origem, &destino, &tamanho);

            obra[quantidade_estradas].cidades[0] = origem;
            obra[quantidade_estradas].cidades[1] = destino;
            obra[quantidade_estradas].peso = tamanho;
            quantidade_estradas++;

        } else if (tarefa == CONSULTA) {
            int componente[quantidade_cidades];
            int tamanho_componente = 1, primeira_cidade;
            scanf("%d", &primeira_cidade);

            componente[0] = primeira_cidade;
            for (int cidade = 0; cidade < tamanho_componente; cidade++) {
                for (int estrada_atual = 0; estrada_atual < quantidade_estradas; estrada_atual++) {
                    int vizinho;
                    if (componente[cidade] == obra[estrada_atual].cidades[0]) {
                        vizinho = obra[estrada_atual].cidades[1];
                    } else if (componente[cidade] == obra[estrada_atual].cidades[1]) {
                        vizinho = obra[estrada_atual].cidades[0];
                    } else {
                        continue;
                    }

                    char vizinho_dentro_componente = 0;
                    for (int i = 0; !vizinho_dentro_componente && i < tamanho_componente; i++) {
                        vizinho_dentro_componente = (vizinho == componente[i]);
                    }

                    if (!vizinho_dentro_componente) {
                        componente[tamanho_componente] = vizinho;
                        tamanho_componente++;
                    }
                }
            }

            soma_distancias = 0;
            for (int i = 1; i < tamanho_componente; i++) {
                for (int j = 0; j < i; j++) {
                    int origem = componente[i], destino = componente[j];
                    int caminho[tamanho_componente];

                    caminho[0] = origem;
                    caminho_encontrado = 0;
                    caminha(obra, quantidade_estradas, caminho, 1, 0, destino);
                }
            }

            printf("%llu\n", soma_distancias);
        }
    }

    return 0;
}

void caminha(estrada obra[], int quantidade_estradas, int caminho[], int tamanho_caminho, unsigned long long int distancia_percorrida, int destino) {
    int cidade_atual = caminho[tamanho_caminho - 1];
    if (cidade_atual == destino) {
        soma_distancias += distancia_percorrida;
        caminho_encontrado = 1;
    }

    for (int estrada_atual = 0; !caminho_encontrado && estrada_atual < quantidade_estradas; estrada_atual++) {
        int vizinho;
        if (cidade_atual == obra[estrada_atual].cidades[0]) {
            vizinho = obra[estrada_atual].cidades[1];
        } else if (cidade_atual == obra[estrada_atual].cidades[1]) {
            vizinho = obra[estrada_atual].cidades[0];
        } else {
            continue;
        }

        char vizinho_participa_caminho = 0;
        for (int i = 0; !vizinho_participa_caminho && i < tamanho_caminho; i++) {
            vizinho_participa_caminho = (vizinho == caminho[i]);
        }

        if (!vizinho_participa_caminho) {
            caminho[tamanho_caminho] = vizinho;
            caminha(obra, quantidade_estradas, caminho, tamanho_caminho + 1, distancia_percorrida + obra[estrada_atual].peso, destino);
        }
    }
}