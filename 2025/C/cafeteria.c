#include <stdio.h>

int main(void) {
    int min_leite, max_leite, volume_copo, dose_cafe;
    scanf("%d\n%d\n%d\n%d", &min_leite, &max_leite, &volume_copo, &dose_cafe);
    
    int maximo_cafe = (volume_copo - min_leite);
    if (maximo_cafe % dose_cafe == 0) {
        printf("S\n");
        return 0;
    }
    
    int menor_quantidade_leite_possivel = min_leite + (maximo_cafe % dose_cafe);
    if (menor_quantidade_leite_possivel <= max_leite) {
        printf("S\n");
    } else {
        printf("N\n");
        return 0;
    }

    return 0;
}