#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

int N;
vector<int> seq;

int main() {

	freopen("test.txt", "r", stdin);
	scanf("%d", &N);

	int tmp, res = 0;
	for (int i = 0; i < N; i++) {
		scanf("%d", &tmp);
		seq.push_back(tmp);
	}

	// 양수일 때 (큰거부터)
	sort(seq.begin(), seq.end(), greater<int>());

	for (int i = 0; i < N; i++) {
		if (seq[i] <= 0) break;
		if (i + 1 == N || seq[i + 1] <= 0) { // 다음에 양수가 끝이면 더하고 끝냄
			res += seq[i];
			break;
		}
		if (seq[i + 1] == 1) { // 다음에 1인 경우 둘다 그냥 더해주고 끝내야 최댓값이 됨
			res += seq[i] + seq[i + 1];
			i++;	// 1 이 여러개 일 수 있음.
			// seq[i] == 1 인 경우는 seq[i+1] <= 0 조건에서 걸리기 때문에 상관 없음.
		}
		// 둘다 양수일 때
		else if ((seq[i] >= 0 && seq[i + 1] >= 0)) {
			res += seq[i] * seq[i + 1];
			i++;
		}
	}

	// 음수일 때 (작은거부터)
	sort(seq.begin(), seq.end());

	for (int i = 0; i < N; i++) {
		if (seq[i] >= 0) break; 
		if (i + 1 == N  || seq[i+1] > 0) { // 다음에 음수가 끝이면 더하고 끝냄
			res += seq[i];
			break;
		}
		// 둘다 음수일 때
		if ((seq[i] < 0 && seq[i + 1] < 0)) {
			res += seq[i] * seq[i + 1];
			i++;
		}
	}

	printf("%d\n", res);

	return 0;
}