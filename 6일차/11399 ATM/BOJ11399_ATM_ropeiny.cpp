#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

int N;
vector<int> line;

int main() {

	freopen("test.txt", "r", stdin);
	scanf("%d", &N);

	int tmp, res = 0;
	for (int i = 0; i < N; i++) {
		scanf("%d", &tmp);
		line.push_back(tmp);
	}

	sort(line.begin(), line.end());

	for (auto& i : line) {
		res += i * N--;
	}

	printf("%d\n", res);

	return 0;
}