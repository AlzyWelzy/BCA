// write a program that will print the memory that data types take up


#include <stdio.h>

int main(void)
{
    printf("The size of an int is %lu bytes \n", sizeof(int));
    printf("The size of a float is %lu bytes \n", sizeof(float));
    printf("The size of a double is %lu bytes \n", sizeof(double));
    printf("The size of a char is %lu bytes \n", sizeof(char));
    printf("The size of a long is %lu bytes \n", sizeof(long));
    printf("The size of a long long is %lu bytes \n", sizeof(long long));
    printf("The size of a short is %lu bytes \n", sizeof(short));
    printf("The size of a long double is %lu bytes \n", sizeof(long double));
    printf("The size of a unsigned int is %lu bytes \n", sizeof(unsigned int));
    printf("The size of a unsigned long is %lu bytes \n", sizeof(unsigned long));
    printf("The size of a unsigned long long is %lu bytes \n", sizeof(unsigned long long));
    printf("The size of a unsigned short is %lu bytes \n", sizeof(unsigned short));
    printf("The size of a unsigned char is %lu bytes \n", sizeof(unsigned char));
    printf("The size of a signed int is %lu bytes \n", sizeof(signed int));
    printf("The size of a signed long is %lu bytes \n", sizeof(signed long));
    printf("The size of a signed long long is %lu bytes \n", sizeof(signed long long));
    printf("The size of a signed short is %lu bytes \n", sizeof(signed short));
    printf("The size of a signed char is %lu bytes \n", sizeof(signed char));
    return 0;
}
