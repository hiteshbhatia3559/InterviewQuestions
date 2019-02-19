_Faced those interview questions for Js_

**Q.Write a mul function which will produce the following outputs when invoked**
A. 
```function mul(){
    	var flag = 0;
    	var result = 1;
    	while (flag <= arguments.length){
    		result*=arguments[flag];
    		flag++;
    		}
    	return result
    	}
```

**Q. What is the syntax of ‘Self Invoking Function’? Give an example?** 
A.
```
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
```
**Q. How to find a missing number in an array of numbers? The array has numbers from 1 to 100. The numbers in the array are unsorted.**
A.
```
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
```
**Q. Write a function that will loop through a list of integers and print the index of each element after a 3 second delay.**
A.
```
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
```
**Q. Write a function to find the 2nd largest element in a binary search tree.**
A.
```
<!--
Hoping you didn't ask for a full implementation of BST in Javascript :) If you did, please drop me an email and I shall implement a whole BST with the necessary functions with the below code working.
There's two cases to consider,
Case A: The largest element has no subtrees - therefore the parent is the second largest element in the BST
Case B: The largest element has a left subtree - if there is a left child of the largest (because there cannot be a right child), find the largest child of this tree
//-->

function find_largest(parent)
{
	this_node = parent;
	flag = 0;
	//Traversing children of this_node now, length would be an attribute of 		the list of nodes of a parent
	while (flag < this_node.length)
	{
		//if there is no right node, send back the largest value in this 				subtree, if there is, return the right node - the right function 			 will have to either return the node or a bool false value
		if (this_node.right() !== true) {return this_node.value;} 
		else 
		{
		find_largest(this_node.right());
		flag++;
		}
	}
}

function find_second_largest(parent)
{
	this_node = parent;
	flag = 0;
	
	while (flag < this_node.length)
    {
		//Case A: Current is the parent of the largest, therefore it is the 			second largest because it has a child on the right, and the child has no nodes on the right or left
		if (this_node.left().left() !== true && this_node.right().right() !== true && this_node.right() === true){return this_node.value;}
	
		//Case B: Current is the largest but has a left subtree - logic says the largest in this subtree is the second largest in the whole tree
		if (this_node.left() === true && this_node.right() !== true)
		{
			return find_largest(this_node.left()); 
		}
	}
}
```