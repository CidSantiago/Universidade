#include <stdio.h>
#include <stdlib.h>
#include <string.h>

union FloatingPoint32IEEE754 {
	struct {
		unsigned int mantissa : 23;
		unsigned int exponent : 8;
		unsigned int sign : 1;
	} raw;
	float f;
} number32;

union FloatingPoint64IEEE754 {
	struct {
		unsigned long long int mantissa : 52;
		unsigned long long int exponent : 11;
		unsigned long long int sign : 1;
	} raw;
	double f;
} number64;

int main() {
	number32.f = -6.8;
	number64.f = -6.8;
	char temp[10][65];
	itoa(number32.raw.mantissa,temp[0],2);
	itoa(number32.raw.exponent,temp[1],2);
	itoa(number32.raw.sign,temp[2],2);
	itoa(number64.raw.mantissa,temp[3],2);
	itoa(number64.raw.exponent,temp[4],2);
	itoa(number64.raw.sign,temp[5],2);
	printf("Numero 32: %s | %s | %s\n", temp[2],temp[1],temp[0] ); 
	printf("Numero 64: %s | %s | %s", temp[5],temp[4],temp[3]);
	return 0;
}
