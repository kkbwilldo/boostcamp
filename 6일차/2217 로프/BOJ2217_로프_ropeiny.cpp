#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

int N, W;
vector<int> rope;

int main() {

	freopen("test.txt", "r", stdin);
	scanf("%d",&N);
	int tmp;
	for(int i =0; i < N; i++){
		scanf("%d", &tmp);
		rope.push_back(tmp);
	}

	sort(rope.begin(), rope.end(), less<int>());

	W = 0;
	for (auto& i : rope) {
		tmp = i * N--;
		W = W < tmp ? tmp : W;
	}

	printf("%d\n", W);

	return 0;
}