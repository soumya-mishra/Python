## Make Python Faster
* often a good idea to use sets or dictionaries instead of lists
    * The collection will contain a large number of items
    * You will be repeatedly searching for items in the collection
    * You do not have duplicate items.
* Reduce Memory Footprints
    * msg = 'line1\n'| msg += 'line2\n'|msg += 'line3\n' instead of 
        join msg = ['line1', 'line2', 'line3'] 
        '\n'.join(msg)
    *  avoid the + operator on strings
    * 'if variable:' is faster than the un-idiomatic 'if variable == True:'
    * generators which result in the lazy
    * list.sort() is in place vs sorted()  --- Exception 
    * __slots__: 'the __slots__ declaration takes a sequence 
      of instance variables and reserves just enough space
      in each instance to hold a value for each variable.
 * Use built in function :
    * Builtin functions like sum, max, any, map, etc are implemented in C.
    * Use list comprehension
    * using builtins is the collections (deque, defaultdict, Counter)
 * Move calculations outside the loop
    
 * Less use of dot operator:
    * myfunc = myObj.func
      for i in range(n):
          myfunc(i)    # faster than myObj.func(i)
 * Spot Performance issue: 
    * Use of cProfiling 
