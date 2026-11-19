
#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int main(void)
{
    int passed = 0;
    int failed = 0;

    if (add(10, 20) == 30) {
        printf("PASS: Addition test\n");
        passed++;
    } else {
        printf("FAIL: Addition test\n");
        failed++;
    }

    if (add(5, 5) == 10) {
        printf("PASS: Second addition test\n");
        passed++;
    } else {
        printf("FAIL: Second addition test\n");
        failed++;
    }

    printf("Tests passed: %d\n", passed);
    printf("Tests failed: %d\n", failed);

    return failed == 0 ? 0 : 1;
}

