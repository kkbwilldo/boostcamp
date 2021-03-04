#include<cstdio>
#include<cstring>
#include<set>

using namespace std;

int N, K;
int cnt[100];
bool set_count[100];
set<int> cur;

int main() {

	// freopen("test.txt", "r", stdin);
	scanf("%d %d", &N, &K);

	int res = 0;
	for (int i = 0; i < K; i++) {
		scanf("%d", &cnt[i]);
	}

	for (int i = 0; i < K; i++) {
		if (cur.size() < N || cur.find(cnt[i]) != cur.end() ) {
			cur.insert(cnt[i]);
		}
		else { // 사이즈가 꽉 찼고 && set에 존재하지 않는 원소일 때
			// 뽑은 이후 처음 사용하는 시점이 가장 늦은 플러그를 뽑아줌.
			memset(set_count, false, 100 * sizeof(bool));
			int last = *cur.rbegin(); // 아무거나 세팅
			for (int j = i; j < K; j++) {
				if (cur.find(cnt[j]) != cur.end() && !set_count[cnt[j]]) { // 있을 경우 && 아직 사용 안됐을 경우
					set_count[cnt[j]] = true; // 처음 사용하는 시점을 찾음.
					last = cnt[j];			 // 가장 마지막 원소가 업데이트됨.
				}
			}
			set<int>::iterator iter;
			for (iter = cur.begin(); iter != cur.end(); iter++) {
				if (!set_count[*iter]) { // 한번도 쓰이지 않을 경우
					last = *iter;
				}
			}

			// 한번도 쓰이지 않거나 첫 등장 시점이 가장 마지막인 것 => 제거.
			cur.erase(last);
			cur.insert(cnt[i]);
			res++;
		}
	}

	printf("%d\n", res);

	return 0;
}