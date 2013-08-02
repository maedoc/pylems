*Note: this rewrite branch is in the process of major refactoring.*
*Much of the information below is not up to date*
*See python scripts in examples directory for current functionality*

# PyLEMS - A LEMS/NeuroML simulator written in Python

## Usage
runlems.py [\<options\>] \<LEMS/NeuroML file\>

### Options
- -I/-include \<path\> - Adds a directory to the model file include search path
- -XI/-xsl-include \<path\> - Adds a directory to the XSL preprocessor include path

## Tasks
- Implement flattening
- Decouple events from runnables
- Perform dimension-checking on expressions.
- Simple LEMS API for creating, reading and writing LEMS model files.
- Implement LEMS API over lems.model.* (NeuroML API?)
  - Interface with libNeuroML and Pyramidal to export Neuron MOD files
  - Export C files (Interface? Steve Marsh’s project?)
- Assertions.
- XPath implementation.
- Implement Runnables from Component types instead of expanded typeless Components (Required for efficient C/C++ code generation)



## Examples
### LEMS examples
- example1 -- Working
- example2 -- Working
- example3 -- Working
- example4 -- Working
- example5 -- Not running
- example6 -- Working
- example7 -- Working
- example8 -- Working
- example9 -- Not running

### NeuroML examples
- Example 0 -- Working
- Example 1 -- Working
- Example 2 -- Working
- Example 3 -- Almost works (initial conditions) after disabling some model resolution checks.
- Example 4 -- Not working (I'm working on this)
- Example 5 -- Not running (XPath)
- Example 6 -- Working
- Example 7 -- Not running
- Example 8 -- Not running
- Example 9 -- Not working
- Example 10 -- Not working. Too many spikes.
- Example 11 -- Not running (Symbol parsing error?)
- Example 12 -- XML preprecessing error in lxml
- Example 13 -- Not running (XPath)
- Example 14 -- No model!
- Example 15 -- Not running (XPath)
      
## LEMS elements that do not work
- XPath based parameters - DerivedParameter, PathParameter
- Assertions
