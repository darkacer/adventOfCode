function lengthOfLIS(nums) {
  // Binary search approach
  const n = nums.length;
  const ans = [];

  // Initialize the answer array with the first element of nums
  ans.push(nums[0]);

  for (let i = 1; i < n; i++) {
    if (nums[i] > ans[ans.length - 1]) {
      // If the current number is greater than the last element
      // of the answer array, it means we have found a
      // longer increasing subsequence. Hence, we push the current number
      // to the answer array.
      ans.push(nums[i]);
    } else {
      // If the current number is not greater than the last element of
      // the answer array, we perform a binary search to find the smallest
      // element in the answer array that is greater than or equal to the
      // current number.

      // The indexOf function returns the first index at which the current
      // number can be inserted to maintain sorted order.
      const low = ans.findIndex((el) => el >= nums[i]);

      // We update the element at the found position with the current number.
      // By doing this, we are maintaining a sorted order in the answer array.
      ans[low] = nums[i];
    }
  }

  // The length of the answer array represents the length of the
  // longest increasing subsequence.
  console.log(ans);
  return ans.length;
}

// Driver program to test the function
const nums = [10, 22, 9, 33, 21, 50, 41, 60];
// Function call
console.log("Length of LIS is " + lengthOfLIS(nums));
