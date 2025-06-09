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

long int add(long int a, long int b) {
	long int result = a+b;
	return result;
}

short int subtract(short int a, short int b) {
	short int result = a-b;
	return result;
}

float multiply(float a, float b) {
	float result = a*b;
	return result;
}

double divide(double a, double b) {
	double result = a/b;
	return result;
}

double divideByTwo(double a) {
	double result = a/2;
	return result;
}

void printSymbols(int a, char b, char c) {
	for (int i = 0; i <= b; i++) {
		if (i%2 == 0) {
			printf("%c", b);
		}
		else {
			printf("%c", c);
		}
	}
}

void printEvenNumbersUpTo18() {
	for (int i = 0; i <= 100; i++) {
		if (i%2 == 1) {
			continue;
		}
		else {
			printf("%d", i);
		}
	}
}

int main() {
	int array[100];
	int n;
	bool temp = 1;
	bool temp2 = (3 > 2) || (2 < 3);
	printf("Inserisci il numero di elementi: ");
	scanf("%d", &n);
	printf("Inserisci gli elementi: ");
	for (int i = 0; i <= n-1; i++) {
		printf("%d", array[i]);
	}
	quicksort(array, 0, n-1);
	printf("Array ordinato: ");
	for (int i = 0; i <= n-1; i++) {
		printf("%d", array[i]);
		printf(" ");
	}
	int i = 10;
	while (i < 14) {
		long int additionResult = add(60,i);
		printf("%li", additionResult);
		short int subtractionResult = subtract(60,i);
		printf("%hi", subtractionResult);
		float multiplicationResult = multiply(60,i);
		printf("%f", multiplicationResult);
		double divisionResult = divide(60,i);
		printf("%lf", divisionResult);
		i = i+1;
	}
	char symbol;
	scanf("%c", &symbol);
	if (symbol == '#') {
		printf("You chose the # symbol :D");
	}
	else {
		printf("%c", symbol);
	}
	return 0;
}
