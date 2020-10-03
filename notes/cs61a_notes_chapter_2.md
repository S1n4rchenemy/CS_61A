# CS 61A Class Notes

**Text book:** 
* [Structure and Interpretation of Computer Programs (SICP)](https://mitpress.mit.edu/sites/default/files/sicp/index.html) 
* [Composing Programs](http://composingprograms.com/) (Majorly referred in this course)
* [Dive into Python 3](https://diveintopython3.problemsolving.io/index.html)

---

## Chapter 2: Building Abstractions with Data

### 2.1 Introduction

#### 2.1.1 Native Data Types

Every value in Python has a <u>*class*</u> that determines what type of value it is.  Value that share a class also share behavior.

*e.g.*, the integers `1` and `2` are both instances of the `int` class.  These two values can be treated similarly, such as being negated or added to another integer.

The built-in `type` function allows us to inspect the class of any value:

```python
>>> type(2)
<class 'int'>
``` 
<br/>

The values we have used so far are instances of a small number of *native* data types that are buklt into the Python language.  Native data types have the following properties:

1. There are expressions that evaluate to values of native types, called <u>*literals*</u>.

2. There are built-in functions and operators to manipulate values of native types.

The `int` class is the native data type used to represent integers.  Integer literals (sequences of adjacent numerals) evaluate to `int` values, and mathematical operators manupulate these values.

```python
>>> 12 + 300000000
300000012
``` 
<br/>

Python includes three native numeric types: **integer** (`int`), **real numbers** (`float`), and **complex numbers** (`complex`).

```python
>>> type(1.5)
<class 'float'>

>>> type(1 + 1j)
<class 'complex'>
``` 
<br/>


##### <u>Floats</u>

The name `float` comes from the way in which real numbers are represented in Python and many other programming languages: a "floating point" representation.

Some high-level differences between `int` and `float` objects are important to know:

* `int` objects represent integers *exactly*, without any approximation or limits on their size.

* `float` objects can represent a wide range of fractional numbers but *not all numbers* can be represented exactly, and there are minimum and maximum values.

Therefore, `float` values should be reated as approximations to real values.  These approximations have only a finite amount of precision.  Combining `float` calues can lead to *approximation errors*:

```python
>>> 7 / 3 * 3
7.0

>>> 1 / 3 * 7 * 3
6.999999999999999
``` 

Problems with this approximation appear when we conduct equality tests:

```python
>>> 1 / 3 == 0.333333333333333312345  # Beware of float approximation
True
``` 
<br/>

These subtle difference between the `int` and `float` class have wide-ranging consequences for writing programs 
$\implies$ **must be memorized**

Fortunately,

* There are only a handful of native data types
* These same details are consistent across many programming languages.
<br/>



##### <u>Non-numeric types</u>

* Values can be represent many other types of data, such as sounds, images, locations, web addresses, network connections, and more.  

* A few are represented by native data types, such as the `bool` class for values `True` and `False`.

* The type of most values must be defined by programmers using the means of combination and abstraction.
<br/>
<br/>

--- 

### 2.2 Data Abstraction 

To represent compound structure which is widely seen in the real world (*e.g.*, we need both  latitude and longitude coordinates to represent a geographic position), we would like our programming language to have the capacity to form a <u>*compound data*</u> value that our programs can manipulate as a single conceptual unit, but which also has two parts that can be considered individually.

$\implies$ <u>***Data abstraction***</u>, a powerful design methodology represents the general technique of isolating the parts of a program that deal with <u>how data are represented</u> from the parts that deal with <u>how data are manipulated</u>.

*e.g.*, we can manipulate geographic positions as whole values, when we can shield parts of our program that compute using positions from the details of how those positions are represented.

Similar to <u>***function abstraction***</u>, which separates the <u>way the funciton is used</u> from the details of <u>how the function is implemented</U>.
<br/>

The basic idea of data abstraction is to structure programs so that they operate on abstract data.  That is, 

* our programs should use data in such a way as to make as few assumptions about the data as possible.
* A concrete data representation is defined as an independent part of the program.

These two parts are connected by a small set of *functions* that implement abstract data in terms of the concrete representation.
<br/>
<br/>


#### 2.2.1 Example: Rational Numbers 

A rational number is a ratio of integers, and rational numbers constitute an important sub-class of real numbers.  A rational number such as `1/3` or `17/29` is typically written as:

```python
<numerator>/<denominator>
``` 

where both the <numerator> and <denominator> are placeholders for **integer** values.

Actually dividing integers produces a `float` approximation, losing the exact precision of integers.

```python
>>> 1/3 
0.3333333333333333
>>> 1/3 == 0.333333333333333300000  # Dividing integers yields an approximation
True
``` 

However, we can create an exact representation for rational numbers by combing together the numerator and denominator.
<br/>

Analogous to the idea of function abstractions, let us begin by assuming that

* we already have a way of constructing a rational number from a numerator and denominator 

* given a rational number, we have a way of selecting its numerator and its denominator component

* the constructor and selectors are available as the following three functions:

    * `rational(n, d)` returns the rational number with numerator `n` and denominator `d`.
    * `numer(x)` returns the numerator of the rational number `x` 
    * `denom(x)` returns the denominator of the rational number `x` 

Here we are using a powerful strategy for designing programs: <u>*wishful thinkning*</u>.  We haven't yet said how a rational number is represented, or how the functions `numer`, `denom`, and `rational` should be implemented.  Even so, if we did define these functions, we could then add, multiply, print, and test equality of rational numbers:

```python
>>> def add_rationals(x, y):
        nx, dx = numer(x), denom(x)
        ny, dy = numer(y), denom(y)
        return rational(nx * dy + ny * dx, dx * dy)

>>> def mul_rationals(x, y):
        return rational(numer(x) * numer(y), denom(x) * denom(y))

>>> def print_rational(x):
        print(numer(x), '/', denom(x))

>>> def rationals_are_equal(x, y):
        return numer(x) * denom(y) == numer(y) * denom(x)
``` 

Now, we have the <u>operations on rational numbers</u> in terms of the selector functions `numer` and `denom`, and the constructor function `rational`, but we haven't yet defined these functions.

What we need is some way to glue together a numerator and a denominator into a compound value.
<br/>
<br/>



#### 2.2.2 Pairs 

Python provides a compound structure called a `list`, which can be constructed by placing expressions within square brackets separated by commas.  Such an expression is called a <u>*list literal*</u>.

```python
>>> [10, 20]
[10, 20]
``` 

The elements of a list can be accessed in two ways:

* multiple assignment:
  ```python
  >>> pair = [10, 20]
  >>> pair
  [10, 20]
  >>> x, y = pair
  >>> x
  10
  >>> y
  20
  ``` 

* element selection operator, which is also expressed using square brackets.  
  ```python
  >>> pair[0]
  10
  >>> pair[1]
  20
  ``` 
  * list in Python (and sequences in most other programming languages) are **0-indexed**, meaning that the index 0 selects the **first element**.
  * the equivalent function for the element selection operator is called `getitem`,
    ```python
    >>> from operator import getitem
    >>> getitem(pair, 0)
    10
    >>> getitem(pair, 1)
    20
    ``` 

Two-element lists are not the only method of representing pairs in Python.  Any way of bunding two values together into one can be considered a pair.
<br/>



##### <u>Representing rational numbers</u>

We can now represent a rational number as a pair of two integers: a numerator and a denominator.

```python
>>> def rational(n, d):
        return [n, d]

>>> def numer(x):
        return x[0]

>>> def denom(x):
        return x[1]
``` 

Together with the arithmetic operations we defined earlier, we can manipulate rational numbers with the functions we have defined.

```python
>>> half = rational(1, 2)
>>> print_rational(half)
1 / 2
>>> third = rational(1, 3)
>>> print_rational(mul_rationals(half, third))
1 / 6
>>> print_rational(add_rationals(third, third))
6 / 9
``` 

Our rational number implementation does not reduce rational numbers to lowest terms.  If we have a function for computing the <u>greatest common denominator</u> of two integers, we can remedy this flaw.  As with many useful tools, such a function already exists in the Python Library:

```python
>>> from fractions import gcd
>>> def rational(n, d):
        g = gcd(n, d)
        return (n // g, d // g)

>>> print_rational(add_rationals(third, third))
2 / 3
``` 
<br/>
<br/>




#### 2.2.3 Abstraction Barriers 

In general, the underlying idea of data abstraction:

1. identify a basic set of operations 
2. express all manipulations of values of some kind based on the basic set of operations 
3. use only these operations in manipulating the data 

$\implies$ By *restricting* the use of operations in this way, it is much easier to change the representation of abstract data **without** changing the behavior of a program.
<br/>

Let us consider the rational number example.

For rational numbers, different parts of the program manipulate rational numbers using different oprations, as described in the following table:

**Parts of the program that...**|**Treat rationals as...**|**Using only...**| **Level**
--|--|--|:--:
Use rational numbers to perform computation | whole data values | `add_rational`, `mul_rational`, `rationals_are_equal`, `print_rational` | $\text{high} \newline \huge\downarrow \newline \normalsize\text{low}$
Create rationals or implement rational operations | numerators and denominators | `rational`, `numer`, `denom` | ^
Implement selectors and constructor for rationals | two-element lists | list literals and element selection | ^
<br/>

In each **layer** above, the functions in the final column enforce an <u>**abstraction barrier**</u>.  These functions are called by a <u>higher level</u> and implemented using a <u>lower level</u> of abstraction.

An abstraction barrier *violation* occurs whenever a part of the program that can use a higher level function instead uses a function in a lower lever.

*e.g.*, a function that computes the square of a rational number is best implemented in terms of `mul_rational`, which does not assume anything about the implementation of a rational number.

```python
>>> def square_rational(x):
        return mul_rational(x, x)
``` 

Referring directly to numerators and denominators would violate one abstraction barrier:

```python
>>> def square_rational_violating_once(x):
        return rational(numer(x) * numer(x), denom(x) * denom(x))
``` 

Assuming that rationals are represented as two-element lists would violate two abstraction barriers:

```python
>>> def square_rational_violating_twice(x):
        return [x[0] * x[0], x[1] * x[1]]
``` 
<br/>

Abstraction barrier make programs easier to maintain and to modify.
$\implies$ The fewer functions that depend on a particular representation, the fewer changes are required when one wants to change that representation.

All three `square_rational` implementations have the *correct behavior*, but **only the first** is robust to future changes.

* The `square_rational` function would **not** require updating even if we altered the representation of rational numbers

* `square_rational_violating_once` would need to be changed whenever the selector or constructor signatures changed

* `square_rational_violating_twice` would need to be changed whenever the implementation of rational number changed.
<br/>
<br/>



#### 2.2.4 The Properties of Data 

Abstraction barriers shape the way in which we think about data.

A valid representation of a rational number is not restricted to any particular implementation (such as a two-element list); it is a value returned by `rational` that can be passed to `numer` and `denom`.

In addition, the appropriate relationship must hold among the constructor and selectors, *i.e.*, if we construct a rational number `x` from integers `n` and `d`, then it should be the case that `numer(x)/denom(x)` is equal to `n/d`.
<br/>

In general, we can epxress abstract data using a collection of selectors and constructors, together with some <u>behavior conditions</u>.  As long as the behavior conditions are met (such as the division property above), the selectors and constructors constitute a valid representation of a kind of data.  The implementation details below an abstraction barrier may change, but if the behavior does not, then the ata abstraction remains valid, and the program writtern using this data abstraction will remain correct.
<br/>

This idea can be applied broadly, including to the pair values that we used to implement rational numbers.  The behavior we require to implement a pair is that it glues two values together.  Stated as a behavior condition:

* If a pair `p`was constructed from values `x` and `y`, then `select(p, 0)` returns `x`, and `select(p, 1)` returns `y`.

Instead of using the `list`type, we can implement the two functions `pair` and `select` that fulfill this description just as well as a two-element list.

```python
>>> def pair(x, y):
        """Return a function that represents a pair."""
        def get(index):
            if index == 0:
                return x
            elif index == 1:
                return y
        return get

>>> def select(p, i):
        """Return the element at index i of pair p."""
        return p(i)

>>> p = pair(20, 14)
>>> select(p, 0)
20
>>> select(p, 1)
14
``` 

This functional representation, although obscure, is a perfectly adequate way to represent pairs, since it fulfills the only conditions that pairs need to fulfill.  The practice of data abstraction allows us to switch among representations easily.
<br/>
<br/>




---

### 2.3 Sequences 

A sequence is an ordered collection of values.  

Sequences are not instances of a particular built-in type or abstract data representation, but instead a collection of behaviors that are shared among several different types of data.  *i.e.*, there are many kinds of sequences, but they all share common behavior:

* <u>**Length.**</u> A sequence has a finite length.  An empty sequence has length 0.
  
* <u>**Element selection.**</u> A sequence has an element corresponding to any non-negative integer index less than its length, starting at 0 for the first element. 

Python includes several native data types that are sequences, the most important of which is the `list`.
<br/>
<br/>

#### 2.3.1 Lists 

A `list` value is a sequence that can have arbitary length.

Lists have a large set of built-in behaviors, along with specific syntax to express those behaviors.

*e.g.*,
```python
>>> digits = [1, 8, 2, 8]
>>> len(digits)
4
>>> digits[3]
8
``` 
<br/>

Additionally, lists can be added together and multiplied by integers.  For sequences, addition and multiplication do not add or multiply elements, but instead **combine** and **replicate** the sequences themselves. 

*e.g.*, 
```python
>>> [2, 7] + digits * 2
[2, 7, 1, 8, 2, 8, 1, 8, 2, 8]
``` 
<br/>

Any values can be included in a list, including **another list**.  Furthermore, the types of the list's contents need **not** be the same. (*i.e.*, the list needs **not** to be *homogenous*.)  Element selection can be applied multiple times in order to select a deeply nested element in a list containing lists.

*e.g.*, 
```python
>>> pairs = [[10, 20], [30, 40]]
>>> pairs[1]
[30, 40]
>>> pairs[1][0]
30
``` 
<br/>

##### <u>Containers</u>

Built-in operators for testing whether an element appears in a compound value.

*e.g.*, 
```python
>>> 1 in digits
True 
>>> 8 in digits 
True 
>>> not (5 in digits)
True 
>>> '1' in digits 
False
``` 

It is only a simple operator that searchs for <u>*individual element*</u> element by element. 

*e.g.*,
```python
>>> [1, 8] in digits
False
>>> [1, 2] in [3, [1, 2], 4]
True 
>>> [1, 2] in [3, [[1, 2]], 4]
False
``` 
<br/>

**Containers** describe all the types that can be used as <u>*iterable values*</u> (*e.g.*, `list`, `range`, *.etc*)

<br/>
<br/>


#### 2.3.2 Sequence Iteration 

In many cases, we would like to iterate over the elements of a sequence and perform some computation for each element in turn.
$\implies$ Python has an additional *control statement* to process sequential data: the `for` statement.
<br/>

##### [Example]: <u>counting how many times a value appears in a sequence</u>

```python
>>> def count(s, value):
        """Count the number of occurrences of value in sequence s."""
        total, index = 0, 0
        while index < len(s):
            if s[index] == value:
                total = total + 1
            index = index + 1
        return total 

>>> count(digits, 8)
2
``` 

The Python `for` statement can simplify this function body by iterating over the element values directly without introducing the name `index` at all.

```python
>>> def count(s, value):
        """Count the number of occurrences of value in sequence s."""
        total = 0
        for elem in s:
            if elem == value:
                total = total + 1
        return total 

>>> count(digits, 8)
2
``` 
<br/>


A `for` statement consists of a single clause with the form:

```python
for <name> in <expression>:
    <suite>
``` 
<br/>


A `for` statement is executed by the following procedure:

1. Evaluate the header `<expression>`, which must yield an iterable value.

2. For each element value in that iterable value, in order:
   1. Bind `<name>` to that value in the current frame.
   2. Execute the `<suite>`.

This execution procedure refers to <u>*iterable values*</u>.  Lists are a type of sequence, and sequence are iterable values.  (Python includes other iterable types.)

An important consequence of this evaluation procedure is that `<name>` will be bound to the last element of the sequence after the `for` statement executed. 

The `for` loop introduces yet another way in which the environment can be updated by a statement.
<br/>


##### <u>Sequence unpacking</u>

A common pattern in program is to have a sequence of elements that are themselves sequences, but all of a fixed length.  A `for` statement may include multiple names in its header to "unpack" each element sequence into its respective elements.

For example, we may have a list of two-element lists

```python
>>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
``` 

and wish to find the number of these pairs that have the same first and second element 

```python
>>> same_count = 0
``` 

The following `for` statement with two names in tis header will bind each name `x` and `y` to the first and second elements in each pair, respectively

```python
>>> for x, y in pairs:
        if x == y:
            same_count += 1

>>> same_count 
2
``` 

This pattern of binding multiple names to multiple values in a fixed-length sequence is called <u>**sequence unpacking**</u>;  it is the same pattern that we see in assignment statements that bind multiple names to multiple values.
<br/>


##### <u>Ranges</u>

A `range` is another built-in type of sequence in Python, which represents a range of integers.

Ranges are created with `range`, which takes *two integer arguments*: the <u>first number</u> and <u>one **beyond** the last number</u> in the desired range.

```python
>>> range(1, 10)  # Includes 1, but not 10
range(1, 10)
``` 

Calling the `list` constructor on a range evaluates to a list with the same elements as the range, so that the elements can be easily inspected:

```python
>>> list(range(5, 8))
[5, 6, 7]
``` 

If only one argument is given, it is interpreted as one beyond the last value for a range that starts at 0.

```python
>>> list(range(4))
[0, 1, 2, 3]
``` 

Ranges commonly appear as the expression in a `for` header to specify the number of times that the suite should be executed: A *common convention* is to use a <u>single underscore</u> character for the name in the `for` header if the name is unused in the suite:

```python
>>> for _ in range(3):
        print('Go Bears!')

Go Bears!
Go Bears!
Go Bears!
``` 

This underscore is just another name in the environment as far as the interpreter is concerned, but has a conventional meaning among programmers that indicates the name will not appear in any future expressions.
<br/>
<br/>


#### 2.3.3 Sequence Processing

<br/>

##### <u>List comprehension</u>

**List comprehension** is an *expression* that can <u>evaluate a fixed expression</u> for <u>element in a sequence</u> and collect the resulting values <u>in a result sequence</U>.

*e.g.*,
```python
>>> odds = [1, 3, 5, 7, 9]
>>> [x + 1 for x in odds]
[2, 4, 6, 8, 10]
``` 

The `for` keyword above is **not** a part of a `for` statement, but instead part of a list comprehension because it is contained within square brackets.
<br/>

Another common sequence processing operation is to select a <u>subset</u> of values that <u>satisfy some condition</u>.  List comprehension can also expression this patter.

*e.g.*,
```python
>>> [x for x in odds if 25 % x == 0]
[1, 5]
``` 
<br/>

The *general form* of a list comprehension is:

```python
[<map expression> for <name> in <sequence expression> if <filter expression>]
``` 

To evaluate the list comprehension:

1. evaluates the `<squence expression>`, which must return an <u>**iterable value**</u>

2. for each element in order, the element value is <u>bound to</u> `<name>`, 
    * the `<filter expression>` is evaluated, and if it yields a true value, 
    * the `<map expression>` is evaluated.

3. The values of the `<map expression>` are collected into a list.
<br/>

> *We can always rewrite a list comprehension as an equivalent **for statement**.*

<br/>


##### <u>Aggregation</u>

A third common pattern in sequence processing is to aggregate all values in a sequence into a single value.  The built-in functions `sum`, `min`, and `max` are all examples of <u>aggregation functions</u>.
<br/>

* `sum(iterable[, start]) -> value`: Return the sum of an iterable of **numbers** (**NOT** strings) plus the value of parameter 'start' (which defaults to 0).  When the iterable is empty, return start.
  ```python
  >>> sum([2, 3, 4], 5)
  14

  >>> sum([[2, 3], [4]]) 
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: unsupported operand type(s) for +: 'int' and 'list'

  >>> sum([[2, 3], [4]], [])  # notice the use of the start value
  [2, 3, 4]
  ``` 
  <br/>

* `max(iterable[, key=func]) -> value` / `max(a, b, c, ...[, key=func]) -> value`: With a single iterable argument (could also be strings), return its largest item.  With two or more arguments, return the largest argument.
  ```python
  >>> max(0, 1, 2, 3, 4)
  4
  
  >>> max(range(10), key=lambda x: 7 - (x - 4) * (x - 2))
  3
  ``` 
  <br/>

* `all(iterable) -> bool`: Return `True` if `bool(x)` is `True` for all values `x` in the iterable.  If the iterable is empty, return `True`.
  ```python
  >>> all([x < 5 for x in range(5)])
  True 

  >>> all(range(5))
  False
  ``` 
  <br/>

By combining the patterns of evaluating an expression for each element, selecting a subset of elements, and aggregating elements, we can solve problems using a sequence processing approach.
<br/>


##### [Example]: <u>Perfect number</u>

A perfect number is a positive integer that is equal to the sum of its divisors.  The divisors of `n` are positive integers less than `n` that divide evenly into `n`.  Listing the divisors of `n` can be expressed with a list comprehension.

```python
>>> def divisors(n):
        return [1] + [x for x in range(2, n) if n % x == 0]

>>> divisors(4)
[1, 2]
>>> divisors(12)
[1, 2, 3, 4, 6]
``` 

Using `divisors`, we can compute all perfect numbers from 1 to 1000 with another list comprehension.  (1 is typically considered as a perfect number, but it does not qualify under our previous definition.)

```python
>>> [n for n in range(2, 1000) if sum(divisors(n)) == n]
[6, 28, 496]
``` 
<br/>


##### [Example]: <u>Minimum perimeter of a rectangle</u>

We can reuse the `divisors` to find the minimum perimeter of a rectangle with integer side lengths, given its area.

```python
>>> def width(area, height):
        assert area % height == 0
        return area // height

>>> width(5, 1)
5
>>> width(5, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in width
AssertionError
``` 

we can compute the minimum perimeter by considering all heights

```python
>>> def perimeter(width, height):
        return 2 * (width + height)

>>> def minimum_perimeter(area):
        heights = divisors(area)
        perimeters = [perimeter(width, n) for n in heights]
        return min(perimeters)

>>> area = 80
>>> width(area, 5)
16
>>> perimeter(16, 5)
42
>>> minimum_perimeter(area)
36
>>> [minimum_perimeter(n) for n in range(1, 10)]
[4, 6, 8, 8, 12, 10, 16, 12, 12]
``` 
<br/>



##### <u>High-order functions</u>

The common patterns we observed in sequence processing can be expressed using higher-order functions.

1. Evaluateing an expression for each element in a sequence:
    ```python
    >>> def apply_to_all(map_fn, s):
            return [map_fn(x) for x in s]
    ``` 

2. Selecting only elements for which some expression is true:
    ```python
    >>> def keep_if(filter_fn, s):
            return [x for x in s if filter_fn(x)]
    ``` 

3. Many forms of aggregation can be expressed as repeatedly applying a two-argument function to the *reduced* value so far ad each element in turn:
    ```python
    >>> def reduce(reduce_fn, s, initial):
            reduced = initial
            for x in s:
                reduced = reduce_fn(reduced, x)
            return reduced
    
    >>> reduce(mul, [2, 4, 8], 1)
    64
    ``` 
<br/>

We can find perfect numbers using these higher-order functions as well.

```python
>>> def divisors_of(n):
        divides_n = lambda x: n % x == 0
        return [1] + keep_if(divides_n, range(2, n))

>>> divisors_of(12)
[1, 2, 3, 4, 6]

>>> from operator import add
>>> def sum_of_divisors(n):
        return reduce(add, divisors_of(n), 0)
>>> def perfect(n):
        return sum_of_divisors(n) == n

>>> keep_if(perfect, range(1, 1000))
[1, 6, 28, 496]
``` 
<br/>

##### <u>Conventional names</u>

In computer science community, the more common name for `apply_to_all` is `map`, and the more common name for `keep_if` is `filter`.  

In Python, the built-in `map` and `filter` are generalizations of these functions that do **not** return lists.  The definitions in the last subsection are equivalent to applying the `list` constructor to the result of built-in `map` and `filter` calls:

```python
>>> apply_to_all = lambda map_fn, s: list(map(map_fn, s))
>>> keep_if = lambda filter_fn, s: list(filter(filter_fn, s))
``` 
<br/>

The `reduce` function is built into the `functools` module of the Python standard library.  In this version, the `initial` argument is optional:

```python
>>> from functools import reduce 
>>> from operator import mul 
>>> def product(s):
        return reduce(mul, s)

>>> product([1, 2, 3, 4, 5])
120
``` 
<br/>

In Python programs, it is more common to use <u>list comprehensions</u> directly than <u>higher-order functions</u>, but both approaches to sequence processing are widely used.
<br/>
<br/>



#### 2.3.4 Sequence Abstraction 

We have introduced two native data types that satisfy the sequence abstraction: **lists** and **ranges**.  Both satisfy the conditions with which we began this section: **length** and **element selection**.

Python includes two more behaviors of sequence types that extend the sequence abstraction.
<br/>



##### <u>Membership</u>

A value can be tested for membership in a sequence.  Python has two operators `in` and `not in` that evaluate to `True` or `False` depending on whether an element appears in a sequence.

*e.g.*,
```python
>>> digits = [1, 8, 2, 8]
>>> 2 in digits 
True 
>>> 1828 not in digits 
True 
``` 
<br/>



##### <u>Slicing</u>

Sequences contain smaller sequences within them.  A *slice* of a sequence is any contiguous span of the original sequence, designated by a pair of integers.

*e.g.*,
```python
>>> digits[0 : 2]
[1, 8]
>>> digits[1 :]
[8, 2, 8]
>>> digits[: 2]
[1, 8]
>>> digits[:]
[1, 8, 2, 8]

>>> digits[1 : -1]
[8, 2]

>>> digits[-2 : 0 : -1]
[2, 8]
>>> digits[1 : -1 : -1]
[]
>>> digits[: : 2]
[1, 2]
``` 

* The slicing operation returns a **new list**
  
* As with the `range` constructor, the first integer indicates the srarting index of the slice and the second indicates one <u>beyond</u> the ending index.

* Any bound that is *omitted* si assumed to be an extreme value: **0** for the starting index, and the **length of the sequence** for the ending index.

* **Negative index** is also allowed in slicing.  The ending element has the index **-1**.
  * A way to view this: index `-1` == index `len(list) - 1`

* We can also specify the **step size** of slicing, written inside the bracket separated by the second colon.  The step size could also be *negative*, indicating the backward slicing direction.
  * If the step size is negative, the **default** start index becomse the end of the list, and the **default** end index becomes the beginning of the list.
<br/>
<br/>




#### 2.3.5 Strings 

Text values are perhaps more fundamental to computer science than even numbers.

> *e.g.*, Python programs are written and stored as text.
> ```python
> >>> 'curry = lambda f: lambda x: lambda y: f(x, y)'
> 'curry = lambda f: lambda x: lambda y: f(x, y)'
>
> >>> exec('curry = lambda f: lambda x: lambda y: f(x, y)')
> >>> curry
> <function <lambda> at 0x1003c1bf8>
> ``` 

The native data type for text in Python is called a **string**, and corresponds to the constructor `str`.
<br/>

* String literals can express arbitary text, surrounded by either *single* or *double* quotation marks:
  ```python
  >>> 'I am string!'
  'I am string!'
  >>> "I've got an apostrophe"
  "I've got an apostrophe"
  >>> '您好'
  '您好'
  ``` 

* Strings satisfy the two basic conditions of a sequence that we introduced before:
  * they have a **length**
  * they support **element selection** 
  ```python
  >>> city = 'Berkeley'
  >>> len(city)
  8
  >>> city[3]
  'k'
  ``` 

* The elements of a string are themselves strings that have only a *single character* (length of 1).  A character is any single letter or the alphabet, punctuaion mark, or other symbol. (Python does not have a separate character type.)

* Like lists, strings can also be combined via **addition** and **multiplication** 
  ```python
  >>> 'Berkeley' + ', CA'
  'Berkeley, CA'
  >>> 'Shabu ' * 2
  'Shabu Shabu '
  ``` 
<br/>


##### <u>Membership</u>

The behavior of strings diverges from other sequence types in Python.  The string abstraction does **not** conform to the full sequence abstraction that we described for lists and ranges.

In particular, the membership operator `in` applies to strings, but has an entirely <u>*different behavior*</u> than when it is applied to sequences.  **It matches substrings rather than elements.** 

*e.g.*,
```python
>>> 'here' in "Where's Waldo?"
True 
``` 
<br/>



##### <u>Multiline literals</u>

Strings are not limited to a single line.  *Triple* quotes delimit string literals that span multiple lines, like we see in the docstrings.

*e.g.*,
```python
>>> """The Zen of Python
claims, Readability counts.
Read more: import this."""
'The Zen of Python\nclaims, "Readability counts."\nRead more: import this.'
``` 

In the printed result above, the `\n` (pronounced "backslash en") is a **single element** that represents a <u>new line</u>.
<br/>



##### <u>String coercion</u>

A string can be created from **any object** in Python by calling the `str` constructor function with an object value as its argument. 

*e.g.*,
```python
>>> str(2) + ' is an element of ' + str(digits)
'2 is an element of [1, 8, 2, 8]'
``` 
<br/>



##### <u>Charactre encodings and Unicode</u>

Read [the string chapeter of Dive into Python 3](https://diveintopython3.problemsolving.io/strings.html) for details. 
<br/>
<br/>




#### 2.3.6 Trees 

Our ability to use lists as the elements of other lists provides a new means of combination in our programming language &mdash; a <u>*closure property*</u> of a data type.  In general, a method for combining data values has a closure property if the result of combination can itself be combined using the same method.

Closure is the key to power in any means of combination because it permits us to create hierarchical structures &mdash; structures made up of parts, which themselves made up of parts, and so on.

We can visualize lists in environment diagrams using *box-and-pointer* notation, as shown in the example below:

<div align = "center">
<img src='./assets/2_3_6_fig_1.png' width='' alt='2.3.6 fig. 1' />
</div>
<br/>

Nesting lists within lists can introduce complexity.  The ***tree*** is a fundamental data abstraction that imposes regularity on how hierarchinal values are structured and manipulated.

* A tree has a root label and a sequence of branches.

* Each branch of a tree is a tree.

* A <u>tree</u> with no branches is called a leaf.

* Any tree contained within a tree is called a sub-tree of that tree (such as a branch of a branch).

* The root of each sub-tree of a tree is called a node in that tree.
<br/>

The data abstraction for a tree consists of the <u>constructor</u> `tree` and the <u>selectors</u> `label` and `branches`.  Belwo is a simplified version:

```python
>>> def tree(root_label, branches=[]):
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [root_label] + list(branches)

>>> def label(tree):
        return tree[0]

>>> def branches(tree):
        return tree[1:]
``` 

A tree is well-formed only if it has a root label and all branches are also trees.  The `is_tree` function is applied in the `tree` constructor to verify that all branches are well-formed.

```python
>>> def is_tree(tree):
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True 
``` 

The `is_tree` function checks whether or not a tree has branches.

```python
>>> def is_leaf(tree):
        return not branches(tree)
``` 

These can be constructed by nested expressions.  The following tree `t` has root label 3 and two braches.

```python
>>> t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
>>> t
[3, [1], [2, [1], [1]]]
>>> label(t)
3
>>> branches(t)
[[1], [2, [1], [1]]]
>>> label(branches(t)[1])
2
>>> is_leaf(t)
False
>>> is_leaf(branches(t)[0])
True
``` 
<br/>


##### [Example]: <u>Tree-recursive functions and Fibonacci tree</u>

Tree-recursive functions can be used to construct trees.  

The nth Fibonacci tree has a root label on the nth Fibonacci number and, for `n > 1`, two branches that are also Fibonacci trees.  

A Fibonacci tree illustrates the tree-recursive computation of a Fibonacci number.

```python
>>> def fib_tree(n):
        if n == 0 or n == 1:
            return tree(n)
        else:
            left, right = fib_tree(n - 2), fib_tree(n - 1)
            fib_n = label(left) + label(right)
            return tree(fib_n, [left, right])

>>> fib_tree(5)
[5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
``` 

Tree-recursive functions are also used to process trees.  For example, the `count_leaves` function counts the leaves of a tree.

```python
>>> def count_leaves(tree):
        if is_leaf(tree):
            return 1
        else:
            branch_counts = [count_leaves(b) for b in branches(tree)]
            return sum(branch_counts)

>>> count_leaves(fib_tree(5))
8
``` 
<br/>


##### [Example]: <u>Partition trees</u>    

Trees can also be used to represent the partitions of an integer.  A partition tree for `n` using parts up to size `m` is a binary (two branches) tree that represents the choices taken during computation.

In a non-leaf partition tree:

* the left (index 0) branch contains all ways of partitioning `n`using at least one `m`,

* the right (index 1) branch contains partitions using parts up to `m - 1`, and 
  
* the root label is `m` 

The labels at the *leaves* of a partition tree express whether the path from the root of the tree to the leaf represents a successful partition of `n`.

```python
>>> def partition_tree(n, m):
        """Return a partition tree of n using parts of up to m."""
        if n == 0:
            return tree(True)
        elif n < 0 or m == 0:
            return tree(False)
        else:
            left = partition_tree(n - m, m)
            right = partition_tree(n, m - 1)
            return tree(m, [left, right])

>>> partition_tree(2, 2)
[2, [True], [1, [1, [True], [False]], [False]]]
``` 

Printing the partitions from a partition tree is another tree-recursive process that traverses the tree, constructing each partition as a list.  Whenever a `True` leaf is reached, the partition is printed.

```python       
>>> def print_parts(tree, partition=[]):
        if is_leaf(tree):
            if label(tree):
                print(' + '.join(partition))
        else:
            left, right = branches(tree)
            m = str(label(tree))
            print_parts(left, partition + [m])
            print_parts(right, partition)

>>> print_parts(partition_tree(6, 4))
4 + 2
4 + 1 + 1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1
``` 
<br/>


##### [Example]: <u>Tree binarization</u>

Slicing can be used on the branches of a tree as well.

A binarized tree has at most two branches.  A common tree transformation called <u>*binarization*</u> finds a binarized tree with the same labels as an original tree by grouping together branches.

```python
>>> def right_binarize(t):
        """Construct a right-branching binary tree."""
        return tree(label(t), binarize_branches(branches(t)))

>>> def binarize_branches(bs):
        """Binarize a list of branches."""
        if len(bs) > 2:
            first, rest = bs[0], bs[1:]
            return [right_binarize(first), right_binarize(rest)]
        else:
            return [right_binarize(b) for b in bs]

>>> right_binarize(tree(0, [tree(x) for x in [1, 2, 3, 4, 5, 6, 7]]))
[0, [1], [[2], [[3], [[4], [[5], [[6], [7]]]]]]]
``` 
<br/>
<br/>



#### 2.3.7 Linked Lists

We can also develop sequence representation that are *not* built into Python.  A common representation of a sequence constructed from nested pairs is called a <u>*linked list*</u>.

The environment diagram below illustrates the linked list representation of a four-element sequence containing 1, 2, 3, and 4.

<img src='./assets/2_3_7_fig_1.png' width='800' alt='2.3.7 fig. 1' /><br/>

A linked list is a pair containing the first element of the sequence (in the case 1) and the rest fo the sequence (in this case a representation of 2, 3, 4).  The second element is also a linked list.  The rest of the inner-most linked containing only 4 is `'empty'`, a value that represents an empty linked list.

Linked lists have recursive structure $\implies$ the rest of a linked list is a linked list or `'empty'`.

We can define an abstract data representation to validate, construct and select the components of linked lists.

```python
>>> empty = 'empty'
>>> def is_link(s):
        """s is a linked list if it is empty or a (first, rest) pair."""
        return s == empty or (len(s) == 2 and is_link(s[1]))

>>> def link(first, rest):
        """Construct a linked list from its first element and the rest."""
        assert is_link(rest), 'rest must be a linked list'
        return [first, rest]

>>> def first(s):
        """Return the first element of a linked list."""
        assert is_link(s), 'first only applies to linked lists.'
        assert s != empty, 'empty linked list has no first element.'
        return s[0]

>>> def rest(s):
        """Return the rest of the elements of a linked list s."""
        assert is_link(s), 'rest onl applies to linked lists.'
        assert s != empty, 'empty linked list has no rest.'
        return s[1]
``` 

* `link` is a constructor and `first` and `rest` are selectors for an abstract data representation of linked list.

* The behavior condition for a linked list is that, like a pair, its constructor and selectors are inverse functions.
  * *i.e.*, if a linked list `s` was constructed from first element `f` and linked list `r`, then `first(s)` returns `f`, and `rest(s)` returns `r`
<br/>

We can use the constructor and selectors to manipulate linked list:

```python
>>> four = link(1, link(2, link(3, link(4, empty))))
>>> first(four)
1
>>> rest(four)
[2, [3, [4, 'empty']]]
``` 
<u>Note:</u> Our implementation above uses pairs that are two-element `list` values.  It is also totally possible to use *functions* alone to implement the pair and thus the linked list.
<br/>


Using the abstract data representation we have defined, we can implement the two behaviors that characterize a sequence: **length** and **element selection**.

```python
>>> def len_link(s):
        """Return the length of linked list s."""
        length = 0
        while s != empty:
            s, length = rest(s), length + 1
        return length 

>>> def getitem_link(s, i):
        """Return the element at index i of linked list s."""
        while i > 0:
            s, i = rest(s), i - 1
        return first(s)

>>> len_link(four)
4
>>> getitem_link(four, 1)
2
``` 

This example demonstrates a common pattern of computation with linked lists, where each step in an iteration operates on an icreasingly shorter suffix of the original list.  

This incremental processing to find the length and elements of a linked list does take some time to compute.  Python's built-in sequence types are implemented in a more efficient way.
<br/>


##### <u>Recursive manipulation</u>

Both `len_link` and `getitem_link` are iterative.  We can also implement length and element selection using *recursion*.

```python
>>> def len_link_recursive(s):
        """Return the length of a linked list s."""
        if s == empty:
            return 0
        else:
            return 1 + len_link_recursive(rest[1])

>>> def getitem_link_recursive(s, i):
        """Return the element at index i of linked list s."""
        if i == 0:
            return first(s)
        return getitem_link_recursive(rest(s), i - 1)

>>> len_link_recursive(four)
4
>>> getitem_link_recursive(four, 1)
2
``` 

Recursion is also useful for transforming and combining linked lists.

```python
>>> def extend_link(s, t):
        """Return a list with the elements of s followed by those of t."""
        assert is_link(s) and is_link(t)
        if s == empty:
            return t 
        else:
            return link(first(s), extend_link(rest(s), t))

>>> extend_link(four, four)
[1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]]


>>> def apply_to_all_link(f, s):
        """Apply f to each element of s."""
        assert is_link(s)
        if s == empty:
            return s
        else:
            return link(f(first(s)), apply_to_all_link(f, rest(s)))

>>> apply_to_all_link(lambda x: x * x, four)
[1, [4, [9, [16, 'empty']]]]


>>> def keep_if_link(f, s):
        """Return a list with elements of s for which f(e) is true.""" 
        assert is_link(s)
        if s == empty:
            return s
        else:
            kept == keep_if_link(f, rest(s))
            if f(first(s)):
                return link(first(s), kept)
            else:
                return kept 

>>> keep_if_link(lambda x: x % 2 == 0, four)
[2, [4, 'empty']]


>>> def join_link(s, separator):
        """Return a string of all elements in s separated by separator."""
        if s == empty:
            return ""
        elif rest(s) == empty:
            return str(first(s))
        else:
            return str(first(s)) + separator + join_link(rest(s), separator)

>>> join_link(four, ", ")
'1, 2, 3, 4'
``` 
<br/>



##### <u>Recursive construction</u>

Linked lists are particularly useful when constructing sequences incrementally, a situation that arises ofeen in recursive computations.

The `count_partition` function from Chapter 1 counted the number of ways to partition an integer `n` using parts up to size `m` via a tree-recursive process.  With sequences, we can slo enumerate these partitions explicitly using a similar process.

We follow the same recursive analysis of the problem as we did while counting: partitioning `n` using integers up to `m`involves either

1. partitionning `n - m` suing integers up to `m`, or 
2. partitionning `n` using integers up to `m - 1`.

For base cases:

1. 0 has empty partition
2. partitioning a negative integer or using parts samller than 1 is impossible.

```python
>>> def partitions(n, m):
        """Return a linked list of partitions of n using parts of up to m.
        Each partition is represented as a linked list."""
        if n == 0:
            return link(empty, empty)
        elif n < 0 or m == 0:
            return empty 
        else:
            using_m = partitions(n-m, m)
            with_m = apply_to_all_link(lambda s: link(m, s), using_m)
            without_m = partitions(n, m - 1)
            return extend_link(with_m, without_m)
```
***[Not fully understood] What is the advantage of this method?***

The result is highly nested: a linked list of liked lists, and each linked list is represented as nested pairs that are `list` values.  

We can display it in a human-readable manner using the following code:

```python
>>> def print_partitions(n, m):
        lists = partitions(n, m)
        strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
        print(join_link(strings, "\n"))

>>> print_partitions(6, 4)
4 + 2
4 + 1 + 1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1
``` 
<br/>
<br/>

---




### 2.4 Mutable Data 

We need strategies to help us structure large systems to be *modular*, meaning that they divide naturally into coherent parts that can be separately developed and maintained.

***[Not fully understood]*** One powerful technique for creating modular programs is to incorporate data that may change state over time.  In this way, a single data object can represent something that evolves independently of the rest of the program.  Adding state to data is a central ingredient of a paradigm called <u>*object-oriented programming*</u>.
<br/>


#### 2.4.1 The Object Metaphor 

**Objects** combine data values with behavior.  Objects represent information, but also *behave* like the things that they represent.  The logic of how an boject interacts with other objects is bundled along with the information that encodes the object's value. ***[Not fully understood]*** 

When an object is printed, it knows how to spell itself out in text.  If an object is composed of parts, it knows how to reveal those parts on demand.  Objects are both information and processes, bundled together to represent the properties, interactions, and behaviors of complex things. ***[Not fully understood]*** 

Object behavior is implemented in Python through specialized object syntac and associated terminology.
<br/>

##### [Example]: <u>date</u> 

A data is a kind of object,

```python
>>> from datetime import date 
>>> tues = date(2014, 5, 13)
``` 

The name `date` is bound to a **class**.  A class represents a kind of value.  Individual dates are called **instances** of that class.  Instances can be *constructed* by calling the class on arguments that characterize the instance. 

```python
>>> print(date(2014, 5, 19) - tues)
6 days, 0:00:00
``` 

While `tues` was constructed from primitive numbers, it behaves like a date.  For instance, subtracting it from another date will give a time difference.
<br/> 



Objects have **attributes**, which are named values that are part of the object.  In Python, like many other programming languages, we use *dot notation* to designate an attribute of an object.

> \<expression\> . \<name\>

Above, the `<expression>` evaluates to an object, and `<name>` is the name of an attribute for that object. 

Unlike the names that we have considered so far, these attirbute names are **not** available in the *general environment*.  Instead, arribute names are particular to the object instance preceding the dot.

```python
>>> tues.year
2014
```

Objects also have **methods**, which are function-valued attibutes. The object "knows" how to carry out those methods. $\impliedby$ Methods are functions that compute their results rom both their <u>arguments</u> and their <u>object</u>.

For example, the `strftime` method (a classic function name meant to evoke "string format of time") of `tues` takes a single argument that specifies how to display a date (*e.g.*, `%A` means that the day of the week should be spelled out in full).

```python
>>> tue.strftime('%A, %B %d')
'Tuesday, May 13'
``` 

Computing the return value of `strftime` requires two inputs: 

1. the string that describes the format of the output and 
2. the date information bundled into `tues`.

Date-specific logic is applied within this method to yield this result.  We never stated that the 13th of May, 2014, was a Tuesday, bu knowing the corresponding weekday is part of what it means to be a date.  By bundling behavior and information together, this Python object offers us a convincing, self-contained abstraction of a date.

Dates are objects, but numbers, strings, lists, and ranges are all objects as well.  They represent values, but also behave in a manner that befits the value they represent.  They also have attributes and methods.  

For instance, *strings* have an array of methods that facilitate text processing. 

```python
>>> '1234'.isnumeric()
True 
>>> 'rOBERT dE nIRO'.swapcase()
'Robert De Niro'
>>> 'eyes'.upper().endswitch('YES')
True 
``` 

In fact, <u>all values in Python are **objects**.</u>  *i.e.*, all values have behavior and attributes.  They act like the values they represent.
<br/>
<br/>




#### 2.4.2 Sequence Objects

Instances of primitive built-in values such as <u>numbers</u> are **immutable**. $\implies$ The values themselves cannot change over the course of program execution.

Lists on the other hand are **mutable**.
<br/>

Mutable objects are used to represent values that change over time.  

A person is the same person from one day to the next, despite having aged, received a haircut, or otherwise changed in some way.  

Similarly, an object may have changing properties due to *mutating* operations. *e.g.*, it is possible to change the contents of a list.  Most changes are performed by invoking methods on list objects.
<br/>


##### [Example]: <u>history of playing cards</u>

We can introduce many list modification operations through an example that illustrates the history of playing cards.  Comments in the examples describe the effect of each method invocation.

Playing cards were invented in China, perhaps around the 9th century.  An early deck had three suits, which corresponded to denominations of money.

```python
>>> chinese = ['coin', 'string', 'myrid']  # A list literal
>>> suits = chinese                        # Two names refer to the same list
``` 

As cards migrated to Europe (perhaps through Egypt), only the suit of coins remained in Spanish decks (*oro*).

```python
>>> suits.pop()                            # Remove and return the final element
'myriad'
>>> suits.remove('string')                 # Remove the first element that equals the argument
``` 

Three more suits were added (they evolved in name and design over time),

```python
>>> suits.append('cup')                    # Add an element to the end
>>> suits.extend(['sword', 'club'])        # Add all elements of a sequence to the end
``` 

and Italians called swords *spades*,

```python
>>> suits[2] = 'spade'                     # Replace an element
``` 

giving the suits of a traditional Italian deck of cards.

```python
>>> suits
['coin', 'cup', 'spade', 'club']
``` 

The French variant used today in the U.S. changes the first two suits:

```python
>>> suits[0:2] = ['heart', 'diamond']      # Replace a slice
>>> suits 
['heart', 'diamond', 'spade', 'club']
``` 

Methods also exist for inserting, sorting, and reversing lists.  All of these mutation operations change the value of the list; they do not create new list objects.
<br/>



##### <u>Sharing and identity</u>

Because we have been changing a single list rather than creating new lists, the object bound to the name `chinese` has also changed, becuase it is the same list object that was bound to `suits`!

```python
>>> chinese                                # This name co-refers with "suits' to the same changing list
['heart', 'diamond', 'spade', 'club']
``` 

<u>This behavior is new!</u> $\impliedby$ Previously, if a name did not appear in a statement, then its value would not be affected by that statement.

With mutable data, *methods called on one name can affect another name at the same time.*

Could also check the [environment diagram](http://pythontutor.com/composingprograms.html#mode=edit) to see how the value bound to `chinese` is changed by statements involving only `suits`.
<br/>

Lists can be copied using the `list` constructor function.  Changes to one list do not affect another, unless they share structure.

```python
>>> nest = list(suits)                     # Bind "nest" to a second list with the same elements
>>> nest[0] = suits                        # Create a nested list
``` 

According to this environment,changing the list referenced by `suits` will affect the nested list that is the first element of `nest`, but not the other elements.

```python
>>> suits.insert(2, 'Joker')               # Insert an element at index 2, shifting the rest
>>> nest 
[['heart', 'diamond', 'Joker', 'spade', 'club'], 'diamond', 'spade', 'club']
``` 

And likewise, undoing this change in the first element of `nest` will change `suit` as well 

```python
>>> nest[0].pop(2)
'Joker'
>>> suits 
['heart', 'diamond', 'spade', 'club']
``` 
<br/>

Because two lists may have the same contents but in fact be different lists, we require a means to test whether two objects are the same.  Python includes two comparison operators, called `is` and `is not`, that test whether two expressions in fact evaluate to the *identical* object.  Two objects are identical if they are edqual in their current value, **and** any change to one will always be reflected in the other.  **Identity is a stronger condition than equality.** 

```python
>>> suits is nest[0]
True 
>>> suits is ['heart', 'diamond', 'spade', 'club']
False
>>> suits == ['heart', 'diamond', 'spade', 'club']
True 
``` 

The final two comparisons illustrate the difference between `is` and `==`.  The former checks for identity, while the latter checks for the equality of contents.
<br/>



##### <u>List manipualtion</u>

The behavior of list functions and methods can best be understood in terms of object mutation and identity.

* **Slicing** a list creates a new list and leaves the original list *unchanged*.  A slice from the beginning to the end of the list is one way to copy the contents of a list.

  <img src='./assets/2_4_2_fig_1.png' width='' alt='2.4.2 fig. 1' />
<br/>


* **Slicing assignment** replaces a slice with new values.
  <img src='./assets/2_4_2_fig_9.png' width='600' alt='2.4.2 fig. 9' />
  * It can also remove elements rom a list by assigning `[]` to a slice 
    ```python
    >>> s = [2, 3]
    >>> t = [5, 6]
    >>> s[:1] = []
    >>> t[0:2] = []
    >>> s
    [3]
    >>> t 
    []
    ``` 
<br/>

* *Interesting example*:
  <img src='./assets/2_4_2_fig_10.png' width='650' alt='2.4.2 fig. 10' />
<br/>


* Although the list is copied, the *values contained* within the list are *not*.  Instead, a new list is constructed that contains a subset of the same values as the sliced list.  Therefore, mutating a list within a sliced list will affect the original list.
  <img src='./assets/2_4_2_fig_2.png' width='' alt='2.4.2 fig. 2' />

  * The built-in function `list` has the same effects as the `s[:]`. *i.e.*, they both can copy the whole list, but the values placed in this list will not be copied.
<br/>


* Adding two lists together creates a new list that contains the values of the first list, followed by the values in the second list.  Therefore, `a + b` and `b + a` can result in different values for two lists `a` and `b`.
<br/>


* The `append` method of a list takes one value as an argument and adds it to the end of the list.  
  <img src='./assets/2_4_2_fig_3.png' width='' alt='2.4.2 fig. 3' />
  * The argument can be any value, such as a *number* or *another list*.  If *the argument is a list*, then that list (**and not a copy**) is added as an item in the list. 
  * The method always returns `None`, and it mutates the list by increasing its length by **one**.
<br/>


* The `extend` method of a list takes an iterable value as an argument and adds each of its elements to the end of the list.  
  <img src='./assets/2_4_2_fig_4.png' width='' alt='2.4.2 fig. 4' />
  * It mutates the list by increasing its length by the **length of the iterable argument**.
  * The statement `x += y` for a list `x` and iterable `y` is equivalent to `x.extend(y)` (*aside from some obscure and minor differences beyond the scope of this text*)
  * Passing any argument to `extend` that is not iterable will cause a `TypeError`.
  * The method does **not** return anything.
<br/>


* The `pop` method removes and returns the last element of the list.  When given an integer argument `i`, it removes and returns the element at index `i` of the list.
  <img src='./assets/2_4_2_fig_5.png' width='' alt='2.4.2 fig. 5' />
  * The method mutates the list, reducing its length by **one**.
  * Attempting to pop from an empty list causes an `IndexError` 
<br/>


* The `remove` method takes one argument that must be equal to a value in the list.  It removes the **first** item in the list that is equal to its argument.
  <img src='./assets/2_4_2_fig_6.png' width='' alt='2.4.2 fig. 6' />
  * Calling `remove` on a value that is not equal to any item in the list causes a `ValueError`
<br/>


* The `index` method takes one argument that must be equal to a value in the list.  It returns the **index** in the list of the **first** item that is **equal to the argument**.
  ```python
  >>> a = [13, 14, 13, 12, [13, 14], 15]
  >>> a.index([13, 14])
  4
  >>> a.index(13)
  0
  ``` 
  * Calling `index` on a value that is not equal to any item in the list causes a `ValueError`.
<br/>


* The `insert` method takes two arguments: **an index** and **a value to be inserted**.  The value is added to the list at the given index.  All elements before the given index stay the same, but all elements after the index have their indices increased by one.
  <img src='./assets/2_4_2_fig_7.png' width='' alt='2.4.2 fig. 7' />
  * This method mutates the list by increasing its size by **one**, then returns `None`.
<br/>


* The `count` method of a list takes in an item as an argument and returns **how many times** an equal item appears in the list.  
  ```python
  >>> a = [1, [2, 3], 1, [4, 5]]
  >>> a.count([2, 3])
  1
  >>> a.count(1)
  2
  >>> a.count(5)
  0
  ``` 
  * If the argument is not equal to any element of the list, then `count` returns 0.
<br/>




##### <u>List comprehensions</u>

A list comprehension always creates a new list.  

For example, the `unicodedata` module tracks the official names of every character in the Unicode alphabet.  We can look up the characters corresponding to names, including those for card suits.

```python
>>> from unicodedata import lookup
>>> [lookup('WHITE ' + s.upper() + ' SUIT') for s in suits]
['♡', '♢', '♤', '♧']
``` 

This resulting list **does not** share any of its contents with `suits`, and evaluating the list conprehension does not modify the `suits` list.

(*read more about the Unicode standard for representing text in the [Unicode section](https://diveintopython3.problemsolving.io/strings.html#one-ring-to-rule-them-all) of Dive into Python 3*)
<br/>




##### <u>Tuples</u>

A tuple, an instance of the built-in type, is an **<u>immutable</u> sequence**.  

Tuples are created using a tuple literal that separates element expressions by **commas**.  Parentheses are *optional* but used commonly in practice.

**Any objects** can be placed within tuples.

*e.g.*,
```python
>>> 1, 2 + 3
(1, 5)
>>> ("the", 1, ("and", "only"))
("the", 1, ("and", "only"))
>>> type( (10, 20) )
<class 'tuple'>
``` 

**Empty** and **one-element** tuples have special literal syntax.

```python
>>> ()          # 0 elements
()
>>> (10,)       # 1 element
(10,)
``` 
<br/>

Like lists, tuples have a finite **length** and support **element selection**.  They also have a few methods that are also available for lists, such as `count` and `index`.

*e.g.*,
```python
>>> code = ("up", "up", "down", "down") + ("left", "right") * 2
>>> len(code)
8
>>> code[3]
'down'
>>> code.count("down")
2
>>> code.index("left")
4
``` 

However, the methods for manipulating the contents of a list are not available for tuples because tuples are **immutable**.

* But it is possible to change the value of a **mutable element** contained within a tuple.
  <img src='./assets/2_4_2_fig_8.png' width='' alt='2.4.2 fig. 8' />
<br/>

Tuples are used implicitly in multiple assignment.  An assignment of two values to two names creats a two-element tuple and then unpacks it.

```python
>>> a = 1, 2
>>> a 
(1, 2)
>>> type(a)
<class 'tuple'>
``` 
<br/>



#### 2.4.3 Mutable Default Arguments 

A default argument value is part of a function value, not generated by a call.  Mutable default arguments could be **dangerous**.

<img src='./assets/2_4_2_fig_11.png' width='700' alt='2.4.2 fig. 11' /><br/>
<br/>
<br/>





#### 2.4.4 Dictionaries

Dictionaries are Python's built-in data type for storing and manipulating correspondence relationships.

A dictionary contains <u>key-value pairs</u>, where both the **keys** and **values** are *objects*.

The purpose of a dictionary is to provide an abstraction for storing and retrieving values that are indexed not by consecutive integers, but by *descriptive keys*.

Strings commonly serve as keys, because strings are our conventional representation for names of things.  An example of the dictionary literal is shown below:

```python
>>> numerals = {'I': 1.0, 'V': 5, 'X': 10}
``` 

The **element selection** operation for a dictionary:

```python
>>> numerals['X']
10
``` 

A dictionary can have **at most one value** for each key.  With **assignment statements**, we can 

1. adding new key-value pairs 
2. changing the existing value for a key 

```python
>>> numerals['I'] = 1
>>> numerals['L'] = 50
>>> numerals 
{'I': 1, 'X': 10, 'L': 50, 'V': 5}    # result of Python before 3.6
``` 

* Note that `'L'` was not added to the end of the output above.  Dictionaries were unordered collections of key-value pairs until Python 3.6.  Since Python 3.6, their contents will be **ordered by insertion**.  Since dictionaries were historically unordered collections, it is *safest* **not** to assume anything about the order in which keys and values will be printed.
<br/>

The environment diagram of a dictionary:

<img src='./assets/2_4_4_fig_1.png' width='' alt='2.4.4 fig. 1' /><br/>
<br/>

The dictionary type also supports various methods of iterating over the contents of the dictionary as a whole.  The methods `keys`, `values`, and `items` all return iterable values.
  ```python
  >>> numerals.keys()
  dict_keys(['I', 'V', 'X', 'L'])
  >>> numerals.values()
  dict_values([1.0, 5, 10, 50])
  >>> numerals.items()
  dict_items([('I', 1.0), ('V', 5), ('X', 10), ('L', 50)])
  
  >>> sum(numerals.values())
  66
  ``` 

A list of key-value pairs can be converted into a dictionary by calling the `dict` constructor function.
  ```python
  >>> dict([(3, 9), (4, 16), (5, 25)])
  {3: 9, 4: 16, 5: 25}
  ``` 

A useful method implemented by dictionaries is `get`, which returns the value for a key, if the key is present, or a default value.  The argument to `get` are the key and the default value.

```python
>>> numerals.get('A', 0)
0
>>> numerals.get('V', 0)
5
``` 

Dictionaries also have a comprehension syntax analogous to those of lists.  A key expression and a value expression are separated by a colon.  Evaluating a dictionary comprehension creates a new dictionary object.

```python
>>> {x: x * x for x in range(3, 6)}
{3: 9, 4: 16, 5: 25}
``` 
<br/>


Dictionaries do have some *restrictions*:

* A key of a dictionary cannot be or contain a mutable value.  *(Tuples are commonly used for keys.)*
* There can be at most one value for a given key.
<br/>
<br/>





#### 2.4.5 Local State 











