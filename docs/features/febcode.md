![febcode.png](febcode.png)

# Febcode Manual

## Introduction

**Febcode** is a domain-specific language (DSL) designed for extending and customizing simulations with FEBio. Its primary goal is to allow users to define mathematical models, user-defined behavior, and custom logic in a concise, expressive, and computationally efficient way. It provides an alternative approach to extending FEBio with plugins. Plugins often introduce significant overhead in development, compilation, and maintenance. **Febcode** removes this barrier by providing:

- A lightweight scripting interface
- Strong mathematical expressiveness
- Built-in automatic differentiation (AD)
- Seamless integration with FEBio’s feature system

This enables rapid prototyping, easier experimentation, and more maintainable simulation workflows. However, **febcode** scripts are somewhat limited in the type of extensions that can be implemented. For more complex extensions plugins remain the preferred approach. 

### Approach
**Febcode** is an interpreted language that is compiled to bytecode. Briefly, the following steps are executed to compile the code from input text to bytecode:

1. **Tokenization**: convert the raw input text to a stream of tokens. Each token represents an atomic element of the language, like keywords, numbers, variable names, operations, etc. 
2. **Parsing**: Process the stream of tokens and construct an Abstract Syntax Tree (AST). The AST represents the code as a tree of statements and expressions. 
3. **Compilation**: The AST is now compiled to bytecode by recursively compiling each statement and expression in the tree. 
4. **Execution**: The resulting bytecode is executed at runtime by a special component, called the **virtual machine** (VM). 

To ensure optimal performance, **febcode** uses a static stack size. The stack size is determined during compilation. Since the stack size is fixed, no expensive memory allocations need to happen during execution of the bytecode. To guarantee that the stack size is known in advance, **febcode** uses static types so that the required memory of all variables and expressions is known at compile time. In addition, the language enforces some special rules that ensure the stack size is static. The most important rule is that user-defined functions cannot be called recursively. 


## Core Capabilities

**Febcode** is a relatively simple scripting language, focused on performance and safe execution within FEBio's multithreaded environment. For the most part, it uses a C-like syntax. 

The **febcode** language supports a static type system tailored to the needs of implementing mathematical expressions. It also offers some simple control flow. 

### Scalar and Vector Math

- Boolean: `bool`
- Scalars: `int`, `double`
- Vectors: `vec2`, `vec3`
- Matrices: `mat2`, `mat3`

Operations include:

- Arithmetic: `+`, `-`, `*`, `/`, `**`
- Dot product: `*` (when operands are `vec2` or `vec3`)
- Matrix-vector multiplication: `*` (when operands make sense)

Example:

```cpp
vec3 a = vec3(1, 2, 3);
vec3 b = vec3(4, 5, 6);
double d = a*b; // dot product

mat3 A = mat3(1.0);
vec3 v = A*b; // matrix-vector multiplication
```

### Variables
Variables are declared by first specifying the type, followed by a valid name. Valid names start with a letter (lower or upper case), followed by letters, numbers, or underscores (`_`). Here are examples of some valid variable declarations.

```cpp
double a;
int i0;
vec2 v_0;
```

Note that user-defined variables cannot start with an underscore (`_`). This is because variables that start with underscores have special meaning (see below). 

#### Input Variables
Using the `in` keyword, users can label certain variables as _input variables_. These are special variables for which the value is specified in the FEBio input file, not in the script. This allows users to expose script variables to the rest of FEBio's ecosystem. (Users can use parameter optimization on these variables, set the variables in FEBio Studio, etc.)

```cpp
in double a;
```

The FEBio input file defines the value for these variables using a special syntax.

```xml
<add_param name="a" data_type="double">1.23</add_param>
```

Aside from the different syntax, these parameters are treated as any other FEBio parameters. For instance, users can attach load controllers or maps for these parameters.


#### Injected Variables
Injected variables are special variables that are provided by FEBio and typically contain the value of solution variables at the point where the script is evaluated. Injected variables will always start with an underscore. Although the exact list of the injected variables depends on the context, many scripted model components offer these injected variables. 

* `_time`: the current time
* `_pos0`: the position of the material point in the reference configuration. 
* `_pos` : the position of the material point in the current configuration. 


### Functions

**Febcode** supports user-defined functions:

```cpp
double add(double x, double y)
{
    return x + y;
}
```

Note that **febcode** functions cannot be called recursively. This limitation is a consequence of the need to have a static stack size that can be determined at compile time. A static stack size avoids expensive memory re-allocations during the execution of the script. 

**Febcode** also supports native functions, including many commonly used mathematical functions. 

- `abs`
- `acos`
- `acosh`
- `asin`
- `asinh`
- `atan`
- `atanh`
- `cos`
- `cosh`
- `exp`
- `log`
- `log10`
- `sin`
- `sinh`
- `sqrt`
- `tan`
- `tanh`


Example:
```cpp
double f = sin(x) * exp(y);
```

It also supports native functions that operate on vectors and matrices:

| functions   | description                   |
|-------------|-------------------------------|
| `dot`       | evaluates the dot product between two `vec2` or `vec3` variables. |
| `cross`     | evaluates the cross product between two `vec3` variables. |
| `outer`     | returns a `mat2` (`mat3`) that is the outer product between two `vec2`(`vec3`) variables. |
| `length`    | calculate the length of a `vec2` or `vec3` variables. |
| `normalize` | returns a normalized (i.e. unit) vector of a `vec2` and `vec3` variables. |
| `transpose` | returns the transposed of a `mat2` or `mat3` variable. |
| `inverse`   | returns the inverse of a `mat2` or `mat3` variable. |

Example
```cpp
mat3 A = transpose(B); // take the transpose of the mat3 B
```

### Control Flow

The following control flow elements are supported:


#### If Statements
If statements allow branching based on logical criteria. They are defined using the `if` keyword. If statements can also contain an optional `else` branch that will be executed if the condition of the if statement evaluates to `false`. 

Syntax:
```cpp
if (condition) 
{
    // branch executed if condition evaluates to true
}
else // optional
{
    // branch executed if condition evaluates to false
}
```

#### While Statements
A while statement repeatedly executes a block of code as long as a given condition remains true.

Syntax:
```cpp
while (condition)
{
    // body
}
```

The condition is evaluated before each iteration. If the condition is `true`, the loop body executes. If the condition is `false`, the loop terminates. If the condition never becomes `false`, the loop runs indefinitely. 

Example:
```cpp
int i = 0;
while (i < 5)
{
    i = i + 1;
}
```

#### For Statements
A `for` statement is a control flow construct used to execute a loop with explicit initialization, condition checking, and iteration.

Syntax:
```cpp
for (initialization; condition; update)
{
    // body
}
```

The initialization runs once at the start. The condition is evaluated before each iteration. If the condition is true, the loop body executes. After each iteration, the update expression runs. The loop ends when the condition becomes false.

Example:
```cpp
for (int i = 0; i < 5; i = i + 1)
{
    // executes 5 times
}
```

#### Return Statement

A `return` statement terminates the execution of a function or script and optionally provides a value back to the caller.

Syntax:
```cpp
return expression;
```

It's important to know that the expected return type is determined by the model component that uses the script. For instance, for a `pressure script`, the return value is the pressure value at the material point. Since the pressure is a scalar, the return type must be `double`. During compilation, FEBio checks that the return type is correct. 

## Automatic Differentiation (AD)

**Febcode** scripts can depend on the solution variables of the problem (using injected variables). This usually implies that it needs a contribution to the global stiffness matrix. The contributions require the evaluation of the derivative of the script with respect to the solution variable. To free the user of having to provide these derivatives, **febcode** implements automatic differentiation (AD) as a a core feature. 


### Approach

**Febcode** uses symbolic differentiation over the AST, not numerical or dual-number methods. This approach enables exact derivative computation of expressions without numerical approximation.

Key steps:

- Traverse AST recursively
- Apply differentiation rules per AST node
- Simplify the resulting expression

The result is a modified AST that represents the code for evaluating the derivative of the original script. This derivative AST is now compiled like the original code and used to evaluate the derivatives during the stiffness matrix computation. 

## Using febcode in FEBio
To use febcode in FEBio you need to add a model component that uses a script to define its behavior. These components typically have the word _script_ in it. (For instance, `pressure script`, `body force script`.) These components define the `script` property where you define the script's name and input variables. 

Example:
```xml
<script name="MyScript">
    <add_param name="a" data_type="double" lc="1">3.14</add_param>
</script>
```

The code for the script is defined in the `Scripts` section of the input file. Each script is defined using the `script` child element. This element takes the name as the script as an attribute. The code for the script is defined as the value for the element.

Example:
```xml
<Scripts>
    <script name="MyScript"><![CDATA[
        in double a;
        return a**2;
    ]]></script>
</Scripts>
```

Note that the value is defined via a `<![CDATA[]]>` section. This is necessary since the code can contain special xml formatting characters (e.g. `<`) that can confuse xml readers. Any text in a `<![CDATA[]]>` section will be read as raw text. 

## For Developers
This section describes how you can make use of scripts in your plugins.

First, create a new class that inherits from `FEScripted`. This is a template class that takes the FEBio base class as a template argument. Make sure to pass the `FEModel` class to this base class. For example,

```cpp
class MyScriptedFEature : public FEScripted<FESurfaceLoad>
{
    MyScriptedFEature(FEModel* fem) : FEScripted<FESurfaceLoad>(fem) {}
};
```

The `FEScripted` base class will automatically add a new `script` property to the plugin class. Users will use this property to define the script and the input parameters to the script. 

The next step is to define the _script context_, which defines the expected return type of the script and the list of injected variables. It is advised to set the script context in the constructor of the plugin class. 

```cpp
MyScriptedFEature::MyScriptedFEature(FEModel* fem) : FEScripted<FESurfaceLoad>(fem)
{
    ScriptContext sc;
    sc.returnType = FEValueType::Double; // script should return a double variable.
    sc.addVariable("pos", FEValueType::Vec3d, true); // add pos as an differentiable injected variable. 
    sc.addVariable("time", FEValueType::Double, false); // add time as a constant injected variable. 
    SetScriptContext(sc);
}

```

When it's time to evaluate the script, use the `FEScripted::Value` method. This function takes two parameters, a `FEMaterialPoint` and a vector of `FEValue` variables that contain the values of the injected variables. Make sure that the size and order of the vector matches the list of injected variables defined in the script context.

```cpp
vector<FEValue> vars(2);
vars[0] = mp.m_rt;
vars[1] = GetTimeInfo().currentTime;

double P = Value(mp, vars).toDouble();

```

The `Value` function will return a `FEValue` variant that can be used to extract the value. You can use the `to<type>` methods to extract the value of the correct type. 

```cpp
FEValue v;
bool b = v.toBool();
int i = v.toInt();
double a = v.toDouble();
vec2d v2 = v.toVec2d();
vec3d v3 = v.toVec3d();
mat2d m2 = v.toMat2d();
mat3d m3 = v.toMat3d();
```

Similarly, to evaluate derivatives, you can use the `DerivValue` method. In addition to a `FEMaterialPoint` and a `std::vector<FEValue>` parameter, it also takes an index parameter that indicates which derivative you want. The index is the index of the injected variable as defined in the script's context. You can query whether the script has a non-zero derivative using the `HasDerivative` method. 

```cpp
vec3d gradP(0,0,0); // gradient of pressure
if (HasDerivative(0)) // do we have a derivative w.r.t. position? 
{
    // prepare values for injected variables. 
    vector<FEValue> vars(2);
    vars[0] = mp.m_rt;
    vars[1] = GetTimeInfo().currentTime;

    gradP = Value(mp, vars).toVec3d();
}
return gradP;
```

