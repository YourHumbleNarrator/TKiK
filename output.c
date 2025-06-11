#define bool int
#include <stdio.h>

void quicksort(int array[], int inizio1, int fine1) {
	if (inizio1 < fine1) {
		int pivot = array[fin];
		int indice = inizio1-1;
		for (int i = inizio1; i <= fine1-1; i++) {
			if (array[i] < pivot) {
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

void swap(int a, int b) {
	int temp = a;
	a = b;
	b = temp;
}

int main() {
	int array[100];
	int n;
	printf("Inserisci il numero di elementi: ");
	scanf("%d", &n);
	for (int i = 0; i <= n-1; i++) {
		scanf("%d", &array[i]);
	}
	quicksort(array, 0, n-1);
	for (int i = 0; i <= n-1; i++) {
		printf("%d", array[i]);
		printf(" ");
	}
	return 0;
}
