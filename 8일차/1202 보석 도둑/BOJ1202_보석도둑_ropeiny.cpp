#include<cstdio>
#include<algorithm>
#include<queue>

using namespace std;

int N, K;
int bags[300001];
pair<int, int> jewels[300001];
priority_queue<int> pq;

int main() {

	//freopen("test.txt", "r", stdin);
	scanf("%d %d", &N, &K);

	for(int i =0; i < N; i++){
		scanf("%d %d", &jewels[i].first, &jewels[i].second);
	}

	for(int i =0; i < K; i++){
		scanf("%d", &bags[i]);
	}

	sort(jewels, jewels + N);
	sort(bags, bags + K);

	long long res = 0;
	int idx = 0;
	for (int i = 0; i < K; i++) { // �� ���濡 ���ؼ�..
		while (idx < N && jewels[idx].first <= bags[i]) { // ���濡 ���� �� �ִ� ������ �� pq�� ����.
			pq.push(jewels[idx++].second);  
		}

		if (!pq.empty()) {
			res += pq.top(); pq.pop(); // ���� ���� ������ ������ ����.
		}
	}

	printf("%lld\n", res);

	return 0;
}