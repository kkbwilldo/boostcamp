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

	// ����� �� (ū�ź���)
	sort(seq.begin(), seq.end(), greater<int>());

	for (int i = 0; i < N; i++) {
		if (seq[i] <= 0) break;
		if (i + 1 == N || seq[i + 1] <= 0) { // ������ ����� ���̸� ���ϰ� ����
			res += seq[i];
			break;
		}
		if (seq[i + 1] == 1) { // ������ 1�� ��� �Ѵ� �׳� �����ְ� ������ �ִ��� ��
			res += seq[i] + seq[i + 1];
			i++;	// 1 �� ������ �� �� ����.
			// seq[i] == 1 �� ���� seq[i+1] <= 0 ���ǿ��� �ɸ��� ������ ��� ����.
		}
		// �Ѵ� ����� ��
		else if ((seq[i] >= 0 && seq[i + 1] >= 0)) {
			res += seq[i] * seq[i + 1];
			i++;
		}
	}

	// ������ �� (�����ź���)
	sort(seq.begin(), seq.end());

	for (int i = 0; i < N; i++) {
		if (seq[i] >= 0) break; 
		if (i + 1 == N  || seq[i+1] > 0) { // ������ ������ ���̸� ���ϰ� ����
			res += seq[i];
			break;
		}
		// �Ѵ� ������ ��
		if ((seq[i] < 0 && seq[i + 1] < 0)) {
			res += seq[i] * seq[i + 1];
			i++;
		}
	}

	printf("%d\n", res);

	return 0;
}