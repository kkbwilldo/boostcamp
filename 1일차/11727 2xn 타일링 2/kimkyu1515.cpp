#include <iostream>
#define endl '\n'
using namespace std;

const int MAX=1000;
const int DIV=10007;
int num;
int DP[MAX+10];

int main ()
{
	ios::sync_with_stdio(false); // c 표준 스트림과 c++ 표준 스트림 동기화 끊기 -> 사용하는 버퍼의 수가 줄어들어 실행속도 향상됨
	cin.tie(0);cout.tie(0); // cin과 cout의 tie를 해제하여 실행 속도 향상
	
	//freopen("input.txt","r",stdin);
	
	cin>>num;
	/*
	DP[i]: 2*i 직사각형을 채우는 방법의 수
	DP[i]: 끝에 2x1,1x2,2x2를 놓고 그 이전을 생각
	-> 2x1: DP[i-1]
	-> 1x2: DP[i-2] // DP[i-1]에 DP[i-2]+1x2가 포함될 수 없으므로 위 경우와 더한다
	-> 2x2: DP[i-2]
	*/
	DP[1]=1;
	DP[2]=3;
	for(int i=3;i<=num;i++) DP[i]=(DP[i-1]+DP[i-2]+DP[i-2])%DIV;
	cout<<DP[num]<<endl;
	return 0;
}
