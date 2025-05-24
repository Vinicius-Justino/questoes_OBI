#include <stdio.h>

#define MORTO 0

typedef struct personagem {
    int poder;
    int bonus;
} fada;

int main(void) {
    int quantidade_monstros, quantidade_fadas;
    scanf("%d", &quantidade_monstros);
    scanf("%d", &quantidade_fadas);

    int monstros[quantidade_monstros];
    for (int i = 0; i < quantidade_monstros; i++) {
        scanf("%d", &monstros[i]);
    }

    

    fada fadas[quantidade_fadas];
    for (int i = 0; i < quantidade_fadas; i++) {
        scanf("%d", &fadas[i].poder);
    }

    for (int i = 0; i < quantidade_fadas; i++) {
        scanf("%d", &fadas[i].bonus);
    }

    int melhor_fada = 0, monstros_derrotados = 0;
    do {
        for (int i = 0; i < quantidade_fadas; i++) {
            if (fadas[i].poder > fadas[melhor_fada].poder) {
                melhor_fada = i;
            }
        }

        while (fadas[melhor_fada].bonus > 0){
            char melhor_monstro_derrotavel = 0;
            for (int i = 1; i < quantidade_monstros; i++) {
                if (monstros[i] < monstros[melhor_monstro_derrotavel]) {
                    continue;
                } else if (monstros[i] >= fadas[melhor_fada].poder) {
                    continue;
                }

                melhor_monstro_derrotavel = i;
            }

            if (monstros[melhor_monstro_derrotavel] == MORTO) {
                break;
            } else if (monstros[melhor_monstro_derrotavel] >= fadas[melhor_fada].poder) {
                break;
            }

            monstros[melhor_monstro_derrotavel] = MORTO;
            monstros_derrotados++;
            fadas[melhor_fada].bonus--;
        }

        fadas[melhor_fada].poder = MORTO;
    } while (fadas[melhor_fada].bonus == 0);

    printf("%d\n", monstros_derrotados);
    return 0;
}