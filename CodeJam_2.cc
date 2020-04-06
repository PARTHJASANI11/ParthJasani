#include <bits/stdc++.h>

    using namespace std;

    signed main()
    {
        int p;
        cin>>p;
        for(int i=1;i<=p;i++){
            string string1,string2="";
            cin>>string1;
            int n=string1.size();
            stack<char> stack1;
            for(int k=0;k<n;k++)
            {
                int l=string1[k]-'0';
                if(stack1.empty())
                {
                    for(int j=0;j<l;j++)
                    {
                        stack1.push('(');
                        string2+="(";
                    }
                }
                else{
                    if(k!=0 && string1[k]==string1[k-1])
                    {
                        ;
                    }
                    else if(k!=0 && string1[k]>string1[k-1])
                    {
                        for(int j=0;j<l-(string1[k-1]-'0');j++)
                        {
                            stack1.push('(');
                            string2+='(';
                        }

                    }
                    else if(k!=0 && string1[k]<string1[k-1]){
                        for(int j=0;j<(string1[k-1]-'0')-l;j++)
                        {
                            stack1.pop();
                            string2+=")";
                        }
                    }


                }
                string2+=string1[k];
            }
            int l=string1[n-1]-'0';
            for(int j=0;j<l;j++)
            {
                string2+=")";
            }
            cout<<"Case #"<<i<<": "<<string2<<endl;
        }
    }
