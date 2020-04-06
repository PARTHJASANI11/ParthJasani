#include<bits/stdc++.h>
using namespace std;
signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t1,b1;
    cin>>t1>>b1;
    while(t1--)
    {
        string str1;
        for(int i=0;i<10;i++)
        {
            char c;
            cout<<(i+1)<<"\n";
            cout.flush();
            cin>>c;
            str1+=c;

        }
        cout<<str1<<"\n";
        cout.flush();
        char ch1;
        cin>>ch1;
        if(ch1=='N' || ch1=='n')
            break;
    }
    return 0;
}
