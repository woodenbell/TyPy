# TyPy :space_invader:
#### 1 decorator, multiple possibilities of type checking  
### Before we get started, take a look at this example:

    import typy.typed
    
    
    def f(string: str, numeric: {float, int}, employees: [list, [dict, str]]) -> (str, bool):
        #...
        return ("OK", True)
        
    """
    
    string => must be of type str or subclass (subclasses are accepted in all examples)
    
    numeric => must be subclass/type of one of the types listed (int , float)
    
    employees => must be sublcass/type of a list containing dictionaries with values of
    type str
    
    return type => a tuple with first element of type (/subclass) str and second
    element of type bool
    
    """
    
## Type checking types

**_Remember:_ values with a subclass type of the required type are also accepted**

#### value: type 
Simplest checking, only class of type are allowed

#### value: { type1, type2, type3... }
Checks if value type is one of the types
  
#### value: [type1, type2] 
Checks if the value type is on the first element, then checks if 
(expecting that the value is a data structure) it's elements are of type 2
Also, the list can be nested so you can check for data structures inside other data structures
*(e.g. [type1, [type2, type3]] )*

#### value: (type1, type2, type3) 
Checks for a tuple whose elements are of the given types. For example
if the type checking is set to (bool, str, int), one valid value would be (True, "hello", 3).
Type checking also fails if the given tuple differs in length of the value. This type checking
is useful for key-value values (e.g. ("number", 3))
  




    
        
    
