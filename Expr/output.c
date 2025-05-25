#define bool int
#include <stdio.h>

void quicksort(int[False] array, int inizio1, int fine1); {

if (wip) {

int pivot = array[fin];
int indice = inizio1-1;
for (int i = inizio1; i <= fine1-1; i++) {
if (wip) {

indice = indice+1;
swap(array[indice], array[i]);
}
}
swap(array[indice+1], array[fin]);
int partizione = indice+1;
quicksort(array, inizio1, partizione-1);
quicksort(array, partizione+1, fine1);
}
}

void swap(int a, int b); {

int temp = a;
a = b;
b = temp;
}

int main() {

int array[100];
int n;
bool temp = 1;
bool temp2 = wip;
printf ("Inserisci il numero di elementi: ");
scanf("%d", &n);
printf ("Inserisci gli elementi: ");
for (int i = 0; i <= n-1; i++) {
printf ("%d", array[i]);
}
quicksort(array, 0, n-1);
printf ("Array ordinato: ");
for (int i = 0; i <= n-1; i++) {
printf ("%d", array[i]);
printf (" ");
}
return 0;
}