#include<iostream>
#include<vector>
using namespace std;
int main(){
    
    vector<int> nums = {2,3,2,3,4};
    int ans = 0;
    for(int i : nums){
        ans ^= i ;
    }
    
    cout<<"Single Number is : "<<ans;
    return 0 ;
}