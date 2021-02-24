#include <iostream>
#include <algorithm>
#define endl '\n'
using namespace std;

const int MAX=1000;
int n,answer;
int DP[MAX+10];
int arr[MAX+10];

int main ()
{
	ios::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);
	
	//freopen("input.txt","r",stdin);
	
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
		DP[i]=1;
	}
	answer=1;
	for(int i=0;i<n;i++){
		int curNum=arr[i];
		for(int j=0;j<i;j++){
			int prevNum=arr[j];
			if(curNum>prevNum){
				DP[i]=max(DP[i],DP[j]+1);
			}
		}
		answer=max(answer,DP[i]);
	}
	cout<<answer<<endl;
	return 0;
}
