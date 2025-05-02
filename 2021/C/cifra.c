#include <stdio.h>

int main(void) {
    char palavra[31];
    scanf("%s", palavra);

    char vogais[6] = "aeiou";
    for (int letra = 0; palavra[letra] != '\0'; letra++) {
        int eh_vogal = 0;
        for (int vogal = 0; vogal < 5; vogal++) {
            if (vogais[vogal] == palavra[letra]) {
                eh_vogal = 1;
                break;
            }
        }

        putchar(palavra[letra]);
        if (eh_vogal) {  
            continue;
        }

        int menor_distancia = palavra[letra] - 'a';
        char vogal_mais_proxima = 'a';
        for (int vogal = 0; vogal < 5; vogal++) {
            int distancia = palavra[letra] - vogais[vogal];
            if (distancia < 0) {
                distancia *= -1;
            }

            if (distancia < menor_distancia) {
                menor_distancia = distancia;
                vogal_mais_proxima = vogais[vogal];
            }
        }

        putchar(vogal_mais_proxima);

        char consoantes[21] = "bcdfghjklmnpqrstvxzz";
        for (int consoante = 0; consoante < 21; consoante++) {
            if (consoantes[consoante] == palavra[letra]) {
                putchar(consoantes[consoante + 1]);
                break;
            }
        }
    }

    putchar('\n');
    return 0;
}