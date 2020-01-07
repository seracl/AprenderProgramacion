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

# Algorithm Analysis
"""
Asymptotic analysis
	An algorithm mathematical boundation/framing of its run-time performance.
	With this analysis we can define the best case, average case, and worst case scenario of an algorithm.
	This analysis is time dependent, meaning, when there's no input thge algorithm is concluded to work at constant time

	The time required by an algorithm falls under three types:
	- Best Case:    Minimum time required for program execution.
	- Average Case: Average time required for program execution.
	- Worst Case.   Maximum time required for program execution.

Notations
	Commonly used asymptotic notations to calculate the running time complexity of an algorithm.
	Big Oh Notation, Ο
		- The notation Ο(n) is the formal way to express the upper bound of an algorithm's running time. 
			It measures the worst case time complexity or the longest amount of time an algorithm can possibly take to complete.
			Ο(f(n)) = { g(n) : there exists c > 0 and n0 such that f(n) ≤ c.g(n) for all n > n0. }
	Omega Notation, Ω
		- The notation Ω(n) is the formal way to express the lower bound of an algorithm's running time. 
			It measures the best case time complexity or the best amount of time an algorithm can possibly take to complete.
			Ω(f(n)) ≥ { g(n) : there exists c > 0 and n0 such that g(n) ≤ c.f(n) for all n > n0. }
	Theta Notation, θ
		- The notation θ(n) is the formal way to express both the lower bound and the upper bound of an algorithm's running time.
			θ(f(n)) = { g(n) if and only if g(n) =  Ο(f(n)) and g(n) = Ω(f(n)) for all n > n0. }
	Common Asymptotic Notations
		- Constant    | Ο(1)
		- Logarithmic | Ο(log n)
		- Linear      | Ο(n)
		- n log n     | Ο(n log n)
		- Quadratic   | Ο(n2)
		- Cubic       | Ο(n3)
		- Polynomial  | nΟ(1)
		- Exponential | 2Ο(n)

"""

# Problem solving patterns
"""
Frequency counter
Multiple pointers
Sliding window
Divide and conquer
Greedy algorithm
	In greedy algorithm approach, decisions are made from the given solution domain, which is the closest to optimal. 
	
	This approach try to find a localized optimum solution, in an attempt to obtain globally optimized solutions. 
	However, they do not provide globally optimized solutions.
Back tracking


"""

# Dynamic programming
"""

	Space Complexity: Amount of memory space required by the algorithm in its life cycle, that is equal to the sum of the following two components.
		- A fixed part: Space required to store data and variables that are independent of the size of the problem: simple variables and constants used, program size, etc.
		- A variable part: Space required by variables, whose size depends on the size of the problem: dynamic memory allocation, recursion stack space, etc.
		Space complexity S(P) of any algorithm P is S(P) = C + SP(I), where C is the fixed part and S(I) is the variable part of the algorithm, which depends on instance characteristic I. 
			Algorithm: SUM(A, B)
			Step 1 -  START
			Step 2 -  C ← A + B + 10
			Step 3 -  Stop
			Three variables A, B, and C and one constant. Hence S(P) = 1 + 3.

	Time Complexity: Amount of time required by the algorithm to run. 
		Time requirements are a numerical function T(n), 
  	where T(n) can be measured as the number of steps, provided each step consumes constant time.
"""