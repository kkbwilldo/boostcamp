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
	for (int i = 0; i < K; i++) { // 각 가방에 대해서..
		while (idx < N && jewels[idx].first <= bags[i]) { // 가방에 넣을 수 있는 보석을 다 pq에 삽입.
			pq.push(jewels[idx++].second);  
		}

		if (!pq.empty()) {
			res += pq.top(); pq.pop(); // 가장 높은 가격의 보석을 넣음.
		}
	}

	printf("%lld\n", res);

	return 0;
}