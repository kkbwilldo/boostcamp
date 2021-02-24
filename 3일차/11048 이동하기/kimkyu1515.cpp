#include <iostream>
#include <algorithm>
#define endl '\n'
using namespace std;

const int MAX=1000;
int ROW,COL;
int candies[MAX+10][MAX+10];

int main ()
{
	ios::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);
	
	//freopen("input.txt","r",stdin);
	
	cin>>ROW>>COL;
	for(int r=0;r<ROW;r++){
		for(int c=0;c<COL;c++){
			cin>>candies[r][c];
		}
	}
	
	for(int c=1;c<COL;c++) candies[0][c]+=candies[0][c-1];
	for(int r=1;r<ROW;r++) candies[r][0]+=candies[r-1][0];
	
	for(int r=1;r<ROW;r++){
		for(int c=1;c<COL;c++){
			candies[r][c]=max(candies[r-1][c],candies[r][c-1])+candies[r][c];
		}
	}
	cout<<candies[ROW-1][COL-1]<<endl;
	return 0;
}
