#include<stdio.h>

int main()
{
int a[3],b[3];
a={1,3,54};
b={2,4,7};
for(int i=0;i<sizeof(a);i++)
{
    printf(a[i]);
}
}

//int merge()