#include <iostream>
using namespace std;
double n,t[2001],l[2001],r[2001];
int main()
{
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>t[i]>>l[i]>>r[i];
		if(t[i]>=3)
			l[i]+=0.5;
		if((int)t[i]%2==0)
			r[i]-=0.5;
	}
	int cnt=0;
	for(int i=1;i<=n;i++)
		for(int j=i+1;j<=n;j++)
			cnt+=(max(l[i],l[j])<=min(r[i],r[j]));
	cout<<cnt;
	return 0;
}
