#include <iostream>
#define endl '\n'
using namespace std;

const int DIV=15746;
const int MAX=1000000;
int n;
int DP[MAX+10];
/*
DP[i]: 길이 i일 때 모든 가능한 2진수 경우
DP[1]:1
DP[2]:11,00
DP[3]:1 11,1 00,00 1
DP[4]:1 111,1 100,1 001,00 11,00 00
DP[5]:1 1111, 1 1100, 1 1001, 1 0011, 00 111, 00 100, 00 001
*/

int main ()
{
	ios::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);
	
	//freopen("input.txt","r",stdin);
	
	cin>>n;
	
	DP[1]=1;DP[2]=2;
	for(int i=3;i<=n;i++){
		DP[i]=DP[i-1]+DP[i-2];
		DP[i]%=DIV;
	}
	cout<<DP[n]<<endl;
	return 0;
}
