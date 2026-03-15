class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int>result;
        unordered_set<int>s(nums.begin(),nums.end());
        for (int i=1;i<=nums.size();i++){
            if(s.find(i)==s.end()){
                result.push_back(i);
            }
        }
        return result;
    }
};