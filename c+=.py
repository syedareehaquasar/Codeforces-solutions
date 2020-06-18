tc = int(input())
for i in range(tc):
    a, b ,n = [int(x) for x in input().split()]
    l = sorted([a,b])
    c = 0
    while l[-1] <= n:
        l.append(l[-1] + l[-2])
        c += 1
    print(c) 


# #include <bits/stdc++.h>
# using namespace std;

# int main() {
    
#     long long int t;
    
#     cin>>t;
    
#     while(t--) {
        
#         long long int a, b, n;
        
#         cin>>a>>b>>n;
        
#         if(a > b) {
            
#             swap(a, b);
#         }
        
#         long long int result = b, k = 0;
        
#         while(result < n+1) {
            
#             result = a+b;
            
#             a = b;
#             b = result;
#             k++;
#         }
        
#         cout<<k<<"\n";
        
#     }
    
# 	return 0;
# }