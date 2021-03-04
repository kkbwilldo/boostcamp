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
		else { // ����� �� á�� && set�� �������� �ʴ� ������ ��
			// ���� ���� ó�� ����ϴ� ������ ���� ���� �÷��׸� �̾���.
			memset(set_count, false, 100 * sizeof(bool));
			int last = *cur.rbegin(); // �ƹ��ų� ����
			for (int j = i; j < K; j++) {
				if (cur.find(cnt[j]) != cur.end() && !set_count[cnt[j]]) { // ���� ��� && ���� ��� �ȵ��� ���
					set_count[cnt[j]] = true; // ó�� ����ϴ� ������ ã��.
					last = cnt[j];			 // ���� ������ ���Ұ� ������Ʈ��.
				}
			}
			set<int>::iterator iter;
			for (iter = cur.begin(); iter != cur.end(); iter++) {
				if (!set_count[*iter]) { // �ѹ��� ������ ���� ���
					last = *iter;
				}
			}

			// �ѹ��� ������ �ʰų� ù ���� ������ ���� �������� �� => ����.
			cur.erase(last);
			cur.insert(cnt[i]);
			res++;
		}
	}

	printf("%d\n", res);

	return 0;
}