#https://leetcode.com/problems/reverse-pairs/
#https://leetcode.com/problems/reverse-pairs/discuss/97280/Very-Short-and-Clear-MergeSort-and-BST-Java-Solutions
#https://www.youtube.com/watch?v=S6rsAlj_iB4&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=4


public class Solution {
    public int reversePairs(int[] nums) {
        return mergeSort(nums, 0, nums.length-1);
    }
    private int mergeSort(int[] nums, int s, int e){
        if(s>=e) return 0; 
        int mid = s + (e-s)/2; 
        int cnt = mergeSort(nums, s, mid) + mergeSort(nums, mid+1, e); 
        for(int i = s, j = mid+1; i<=mid; i++){
            while(j<=e && nums[i]/2.0 > nums[j]) j++; 
            cnt += j-(mid+1); 
        }
        Arrays.sort(nums, s, e+1); 
        return cnt; 
    }
}