#include <iostream>
#include <algorithm>
#include <cmath>
#define endl '\n'
using namespace std;

const int MAX=100000;
int n;
int DP[MAX+10];

/*
DP[i]: i를 제곱수의 합으로 나타낼 때 그 제곱수 항의 최소 개수
DP[i]: i가 최대값
DP[1]: 1
DP[2]: 1+1
DP[3]: 1+1+1
DP[4]: 1+1+1+1,4
DP[5]: DP[1]+4,DP[4]+1
DP[17]: DP[1]+16,DP[8]+9,DP[13]+4,DP[16]+1
DP[i]: DP[i-제곱(제곱근(i)보다 작은 수)]+1
*/

int main ()
{
	ios::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);
	
	//freopen("input.txt","r",stdin);
	
	cin>>n;
	
	for(int i=1;i<=n;i++) DP[i]=i;
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=sqrt(i);j++){
			DP[i]=min(DP[i],DP[i-j*j]+1);
		}
	}
	
	cout<<DP[n]<<endl;
	return 0;
}
