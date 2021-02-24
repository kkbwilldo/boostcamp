#include <iostream>
#include <cstring>
#include <algorithm>
#define endl '\n'
using namespace std;

const int MAX=100000;
int testcase;
int COL;
int stickers[2][MAX+10];
int DP[2][MAX+10];

/*
DP[i]: i번째 열까지 얻을 수 있는 최대 합
-> 각 열에서 선택할 수 있는 경우의 수 3가지
->> 1. [0][i-1] 선택: DP[1][i-1]+stickers[0][i]
->> 2. [1][i-1] 선택: DP[0][i-1]+stickers[1][i]
->> 3. [0 or 1][i-2] 선택: max(DP[0][i-2],DP[1][i-2])
-> 3가지 중 최대값이 DP[i]
*/

int main ()
{
	ios::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);
	
	//freopen("input.txt","r",stdin);
	
	cin>>testcase;
	for(int test=1;test<=testcase;test++){
		memset(stickers,0,sizeof(stickers));
		cin>>COL;
		for(int r=0;r<2;r++){
			for(int c=0;c<COL;c++){
				cin>>stickers[r][c];
			}
		}
		DP[0][0]=stickers[0][0];
		DP[1][0]=stickers[1][0];
		DP[0][1]=DP[1][0]+stickers[0][1];
		DP[1][1]=DP[0][0]+stickers[1][1];
		for(int c=2;c<COL;c++){
			for(int r=0;r<2;r++){
				DP[r][c]=max(DP[1-r][c-1],DP[0][c-2]);
				DP[r][c]=max(DP[r][c],DP[1][c-2]);
				DP[r][c]+=stickers[r][c];
			}
		}
		cout<<max(DP[0][COL-1],DP[1][COL-1])<<endl;
	}
	
	return 0;
}
