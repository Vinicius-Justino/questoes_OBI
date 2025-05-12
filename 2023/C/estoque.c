#include <stdio.h>

int main(void) {
    int tipos, tamanhos;
    scanf("%d %d", &tipos, &tamanhos);

    char estoque[tipos][tamanhos];
    for (int tipo = 0; tipo < tipos; tipo++) {
        for(int tamanho = 0; tamanho < tamanhos; tamanho++) {
            scanf("%d", &estoque[tipo][tamanho]);
        }
    }

    int pedidos;
    scanf("%d", &pedidos);

    int pedidos_efetivados = 0;
    for (int pedido = 0; pedido < pedidos; pedido++) {
        int tipo, tamanho;
        scanf("%d %d", &tipo, &tamanho);
        tipo--;
        tamanho--;

        if (estoque[tipo][tamanho] > 0) {
            estoque[tipo][tamanho]--;
            pedidos_efetivados++;
        }
    }

    printf("%d\n", pedidos_efetivados);
    return 0;
}