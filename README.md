_Faced those interview questions for Js_

**Q.Write a mul function which will produce the following outputs when invoked**
A. 
function mul(){
    	var flag = 0;
    	var result = 1;
    	while (flag <= arguments.length){
    		result*=arguments[flag];
    		flag++;
    		}
    	return result
    	}

**Q. What is the syntax of ‘Self Invoking Function’? Give an example?** 
A. 
//Syntax
//Normal function
//(function () { /* logic here */ });
//IIFE
<!--
(function (// argument here) {
    // logic here
})(// parameter here);
//-->
//Example
var foo = "bar";

(function (innerFoo) {
	innerFoo = "foo";
    console.log(innerFoo);
})(foo);

**Q. How to find a missing number in an array of numbers? The array has numbers from 1 to 100. The numbers in the array are unsorted.**
A.
function findMissingNumber(new_array)
{
	var sum1 = (new_array.length+1)*(new_array.length+2)/2;
    var flag = 0;
    var sum2 = 0;
    while (flag<new_array.length)
    {
    	sum2+=new_array[flag];
    	flag+=1;
    }
    var abc = sum1 - sum2;
    return abc;
}

**Q. Write a function that will loop through a list of integers and print the index of each element after a 3 second delay.**
A.
function delayed_index_printer(new_array){
	var flag = 0;
	while(flag < new_array.length){
	console.log(new_array[flag]+"'s index is"+flag+"\n")
	flag++
	(function sleep(delay) {
        var start = new Date().getTime();
        while (new Date().getTime() < start + delay);
      }
	)(3000);
	
	}
}

a = [1,2,3,4,5]
console.log(delayed_index_printer(a))

**Q. Write a function to find the 2nd largest element in a binary search tree.**
