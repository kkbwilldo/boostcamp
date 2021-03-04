#include<cstdio>
#include<algorithm>

using namespace std;

int N, L;
int punc[1001];

int main() {

	//freopen("test.txt", "r", stdin);
	scanf("%d %d", &N, &L);

	int res = 0;
	for (int i = 0; i < N; i++) {
		scanf("%d", &punc[i]);
	}

	// 물이 새는 곳의 위치가 오름차순으로 들어온다는 보장이 없으므로
	sort(punc, punc + N);
	
	for (int i = 0; i < N; ) {
		int start = punc[i];
		while(punc[i] <= start + L - 1 && i < N){
			i++;
		}
		res++;
	}

	printf("%d\n", res);

	return 0;
}