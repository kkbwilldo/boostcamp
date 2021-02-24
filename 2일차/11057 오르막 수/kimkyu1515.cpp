#include <iostream>
#define endl '\n'
using namespace std;

const int DIV=10007;
const int MAX=1000;
int n,answer;
int DP[MAX+10][10];

/*
DP[i][j]: 마지막 수가 j인 길이 i의 모든 오르막 수
DP[i][4]=DP[i-1][0]~DP[i-1][4]
DP[1][0]=DP[1][1]=...=DP[1][9]=1
*/

int main ()
{
	ios::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);
	
	//freopen("input.txt","r",stdin);
	
	cin>>n;
	for(int i=0;i<=9;i++) DP[1][i]=1;
	
	for(int numDigit=2;numDigit<=n;numDigit++){
		for(int i=0;i<=9;i++){
			for(int j=0;j<=i;j++){
				DP[numDigit][i]+=DP[numDigit-1][j];
				DP[numDigit][i]%=DIV;
			}
		}
	}
	for(int i=0;i<=9;i++) answer+=DP[n][i];
	answer%=DIV;
	cout<<answer<<endl;
	return 0;
}
