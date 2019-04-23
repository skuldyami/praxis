public class twoSum {
    public static void main(String[] args) {
        int[] nums = new int[]{2, 7, 11, 15};
        int target=9;
        int[] two_sum = two_sum(nums, target);
        System.out.println("["+two_sum[0]+", "+two_sum[1]+"]");
        
    }

    public static int[] two_sum(int[] nums, int target) {
      int[] sum= new int[2];
      for(int i=0; i<nums.length; i++) {
        for(int j=0; j<nums.length; j++) {
          if(i!=j && nums[i]+nums[j]==target) {
            sum[0]=i;
            sum[1]=j;
            return sum;
          }
        }
      }
      return sum;
    }
}