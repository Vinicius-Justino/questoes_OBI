#include <stdio.h>

int main(void) {
    int quantidade_refeicoes, max_calorias;
    scanf("%d %d", &quantidade_refeicoes, &max_calorias);

    int calorias_consumidas = 0;
    for (int lasanha = 0; lasanha < quantidade_refeicoes; lasanha++) {
        int proteina, gordura, carboidrato;
        scanf("%d %d %d", &proteina, &gordura, &carboidrato);

        calorias_consumidas += 4 * proteina + 9 * gordura * 4 * carboidrato;
    }

    printf("%d\n", (max_calorias - calorias_consumidas));
    return 0;
}