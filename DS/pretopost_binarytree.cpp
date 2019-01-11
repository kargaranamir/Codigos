#include<iostream>
using namespace std; 
#define MAXSIZE 10000
 
int postorder(int a[], int n, int& j, int first, int end)
{
	if (j == n || a[j] < first || a[j] > end)
		return 0;
	int ans = a[j++];
	postorder(a, n, j, first, ans);
	postorder(a, n, j, ans, end);
	printf("%d \n", ans);
}

int main()
{
	int i = 0;
	int	j = 0;
	int b = 0;
	int max = 0;
	int min = 0;
	int* a = new int[MAXSIZE];

	while (scanf("%d", &b) == 1)
	{
		a[i] = b;
		i++;
		if (max<b)
			max = b;
		if (min>b)
			min = b;
	}
	postorder(a, i + 1, j, min - 1, max + 1);
	return 0;
}