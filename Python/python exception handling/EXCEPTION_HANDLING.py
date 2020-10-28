"""



Exceptions are events that are used to modify the flow of control through a program when the error occurs. Exceptions get triggered automatically on finding errors in Python.

These exceptions are processed using five statements. These are:

    try/except: catch the error and recover from exceptions hoist by programmers or Python itself.
    try/finally: Whether exception occurs or not, it automatically performs the clean-up action.
    assert: triggers an exception conditionally in the code.
    raise: manually triggers an exception in the code.
    with/as: implement context managers in older versions of Python such as - Python 2.6 & Python 3.0.

The last was an optional extension to Python 2.6 & Python 3.0. 



WHY ARE EXCEPTIONS USED?

Exceptions allow us to jump out of random illogical large chunks of codes in 
case of errors. Let us take a scenario that you have given a function to do a specific task. 
If you go there and found those things missing that are required to do that specific task, what 
will you do? Either you stop working or think about a solution - where to find those items to 
perform the task. The same thing happens here in case of Exceptions also. Exceptions allow 
programmers jump to an exception handler in a single step, abandoning all function calls. 
You can think exceptions to an optimized quality go-to statement, in which the program error 
that occurs at runtime gets easily managed by the exception block. When the interpreter 
encounters an error, it lets the execution go to the exception part to solve and continue 
the execution instead of stopping.

While dealing with exceptions, the exception handler creates a mark & executes some code.
 Somewhere further within that program the exception is raised that solves the problem & makes
 Python jump back to the marked location; by not throwing away/skipping any active functions that
 were called after the marker was left.
 
 
 ROLES OF AN EXCEPTION HANDLER IN PYTHON
 
 
     Error handling: The exceptions get raised whenever Python detects an error in a program at runtime. As a programmer, if you don't want the default behavior then code a 'try' statement to catch and recover the program from an exception. Python will jump to the 'try' handler when the program detects an error the execution will be resumed.
    Event Notification: Exceptions are also used to signal suitable conditions & then passing result flags around a program & text them explicitly.
    Terminate Execution: There may arise some problems or errors in programs that it needs a termination. So try/finally is used that guarantees that closing-time operation will be performed. The 'with' statement offers an alternative for objects that support it.
    Exotic flow of Control: Programmers can also use exceptions as a basis for implementing unusual control flow. Since there is no 'go to' statement in Python so exceptions can help in this respect.