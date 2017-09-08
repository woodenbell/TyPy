# TyPy :space_invader:
### One decorator, multiple possibilities of type checking  

**Remember**: TyPy decorator automatically skips arguments without annotations, so don't worry  
if you want to keep some of them unchecked :wink:

**_Warning_:** after version 1.1, TyPy is no longer _None-safe_ by default.  
To make an argument _None-safe_, use the `NONE_SAFE` [flag](#flags-since-11)
### Before we get started, take a look at this example:

    import typy.typed
    
    @typy.typed
    def f(string: str, numeric: {float, int}, employees: [list, [dict, str, str]]) -> (str, bool):
        #...
        return ("OK", True)
        
    """
    All subclasses of type are accepted by dafault, use the NOT_SUBCLASS flag if you don't want them to
    be accepted.
    
    string => must be of type str (or subclass)
    
    numeric => must be one of the types listed (int , float)
    
    employees => must be  of a list containing dictionaries with keys and values of
    type str
    
    return type => a tuple with first element of type str and second
    element of type bool
    
    """
    
## Type checking specifications

**_Remember:_ values with a subclass type of the required type are also accepted (except if you use the `NOT_SUBCLASS` [flag](#flags-since-11))**

#### value: type 
Simplest way of checking, only an object of specified type is allowed

#### value: { type1, type2, type3... }
Checks if value type is one of the given types
  
#### value: [type1, type2] 
##### Works for set, tuple and list
Checks if the value type is on the first element, then checks if 
(expecting that the value is a data structure) it's elements are of type 2
**Tip:** the list can be nested so you can check for data structures inside other data structures
*(e.g. [type1, [type2, type3]] )*

#### value: [dict_type, key_type, value_type]
##### Works for  (since 1.1)
The third element was introduced in @v1.1 to separate the key
type and value type. Both types were indicated by the second value before  
the update.

#### value: (type1, type2, type3) 
Checks for a tuple whose elements are of the given types. 
For example, if the type checking is set to *(bool, str, int)*, one valid value would be *(True, "hello", 3)*  
This kind of type checking fails if the given tuple differs in length of the value.  
This feature is useful for checking key-value values (e.g. ("number", 3))

#
  ### Flags (since 1.1)
  Using flags is a new way to specify extra preferences to your type checking.  TyPy currently has
  2 flags:
  
  - NONE_SAFE: specifies that the argument will not accept _None_ values.
  - NOT_SUBCLASS: specifies that subclasses of the type will not be accepted.
  
  Using flags is versy simple, take a look:
  
  #### {type-checking : [flag1, flag2....]}
  When using flags, you will use a dictionary where the only key is the type checking specification,
  and the only value will be a list (only lists will be accepted) conatining all the flags.
  
  Take an example below:
  
    @typy.typed
    def func(a : {[dict, int] : [typy.NONE_SAFE]}):
        pass
  

### none_safe decorator
The `none_safe` decorator is a small utility for None-safety without type checking. Here's a small example:

    import typy
    
    @typy.none_safe
    def func(never_none, never_none_too):
        pass
     


    
        
    
    
        
    
