function twoSum(nums: number[], target: number): number[] {
    let result:number[]  = []
    nums.forEach((ele:number,i:number)=>{
        let temp = target - ele;
        if(nums.includes(temp) && i !== nums.indexOf(temp)){
            result = new Array(i,nums.indexOf(temp))
        }
    })
    return result
};


const result  = twoSum([2,7,11,15],9);

console.log(result)