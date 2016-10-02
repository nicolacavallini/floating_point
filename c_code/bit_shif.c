#include <stdio.h>

void left_shift(int i, int shift)
{
    int result =  i << shift;

    printf("%d left shifted by %d digits equals %d\n", i, shift, result);
}

void right_shift(int i, int shift)
{
    int result =  i >> shift;

    printf("%d right shifted by %d digits equals %d\n", i, shift, result);
}

int main()
{
    int i = 1;
    int shift = 3;

    left_shift(1,3);

    right_shift(8,3);

    return 0;
}
