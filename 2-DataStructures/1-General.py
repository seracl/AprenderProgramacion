# Data Structure and Algorithms
"""
https://www.tutorialspoint.com/data_structures_algorithms/data_structures_basics.htm
Almost every enterprise application uses various types of data structures in one or the other way.

Why to Learn Data Structure and Algorithms?: As applications are getting complex and data rich, some problems arise:
- Data Search: As data grows, search will become slower.
- Processor speed: Processor speed although being very high, falls limited as the data grows.
- Multiple requests: As number of users raise, servers will fail if not incremented.
To solve the above-mentioned problem, data can be organized in such a way that items might be searched instantly

Applications of Data Structure and Algorithms: The following computer problems can be solved using Data Structures
	- Fibonacci number series
	- Knapsack problem
	- Tower of Hanoi
	- All pair shortest path by Floyd-Warshall
	- Shortest path by Dijkstra
	- Project scheduling
"""

## Data Structures
"""
Data Structures: Programmatic way of storing data so that data can be used efficiently.

Data structures foundation terms:
- Interface: Each data structure has an interface, or set of operations, accepted parameters and return types that a data structure supports. 
- Implementation: Implementation provides the internal representation and the definition of the algorithms used in the operations of the data structure. 

Characteristics of a Data Structure
- Correctness: Data structure implementation should implement its interface correctly.
- Time Complexity: Running time or the execution time of operations of data structure must be as small as possible.
- Space Complexity: Memory usage of a data structure operation should be as little as possible.

Execution Time Cases: Used to compare data structure's relative execution time (f(n) execution time in function of the f(data) ).
- Worst Case: Maximum amount of time a data structure operation time can take. 
	In worst case, operations won't take more than ƒ(n) time where ƒ(n) represents function of n.
- Average Case: Average execution time of an operation of a data structure. 
	If an operation takes ƒ(n) time in execution, then m operations will take m*ƒ(n) time.
- Best Case: An operation's least possible execution time.
	If execution takes ƒ(n) time, then the actual operation may take time as the random number with ƒ(n) maximum time.

"""

## Algorithms
"""
Algorithm: Step by step procedure, independent of programming languages, that creates a set of instructions 
	to be executed in a certain order to obtaine a determined output.

Categories of algorithms, from the data structure point of view
	- Search: Algorithm to search an item in a data structure.
	- Sort:   Algorithm to sort items in a certain order.
	- Insert: Algorithm to insert item in a data structure.
	- Update: Algorithm to update an existing item in a data structure.
	- Delete: Algorithm to delete an existing item from a data structure.
 
Characteristics of an Algorithm: Not all procedures are algorithm. An algorithm should... 
	- Unambiguous: Be clear, with clearly defined steps/phases and their inputs/outputs which should lead to only one meaning.
	- Input: An algorithm should have 0 or more well-defined inputs.
	- Output: An algorithm should have 1 or more well-defined output, which should match the expected ones.
	- Finiteness: Algorithms must terminate after a finite number of steps.
	- Feasibility: Should be feasible with the available resources.
	- Independent: An algorithm should have step-by-step directions, which should be independent of any programming code.

How to Write an Algorithm?
	There are no pre-defined standards for writing algorithms. They are problem and resource dependent, and are not written to support a particular programming code.
	Problem − Design an algorithm to add two numbers and display the result.
		THIS IS A PROCEDURE RATHER THAN AN ALGORITHM
			Step 1 − START
			Step 2 − declare three integers a, b & c
			Step 3 − define values of a & b
			Step 4 − add values of a & b
			Step 5 − store output of step 4 to c
			Step 6 − print c
			Step 7 − STOP
		THIS IS THE ALGORITHM
			Step 1 − START ADD
			Step 2 − get values of a & b
			Step 3 − c ← a + b
			Step 4 − display c
			Step 5 − STOP
		It makes it easy for the analyst to analyze the algorithm ignoring all unwanted definitions.
		A problem can be solved in more than one ways. As such a problem can have different solving algorithms

Algorithm Analysis
	Efficiency of an algorithm can be analyzed before and after implementation. 
	Algorithm analysis deals with the execution or running time of various operations involved. 
	The running time of an operation can be defined as the number of computer instructions executed per operation.
	- A Priori Analysis: Theoretical analysis where efficiency is measured by assuming that all other factors are constant and have no effect on the implementation.
	- A Posterior Analysis: Empirical analysis the algorithm is implemented using programming language, and statistics like running time and space required, are collected.

Algorithm Complexity
	Algorithm complexity f(n) gives the running time and/or storage space required by the algorithm X at a given n(size of input data).
	− Time Factor: Time is measured by counting the number of key operations such as comparisons in the sorting algorithm.
	− Space Factor: Space is measured by counting the maximum memory space required by the algorithm.

"""