---
export_on_save:
  html: true
html:
  toc: true
  offline: true 
toc:
  depth_from: 3
  depth_to: 6
  ordered: false
---

# CS 61A Class Notes

<u>**Text book**</u>
 
* [Structure and Interpretation of Computer Programs (SICP)](https://mitpress.mit.edu/sites/default/files/sicp/index.html) 
* [Composing Programs](http://composingprograms.com/) (Majorly referred in this course)
* [Dive into Python 3](https://diveintopython3.problemsolving.io/index.html)

---

<u>**Table of Contents**</u>


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CS 61A Class Notes](#cs-61a-class-notes)
  - [Chapter 4: Data Processing](#chapter-4-data-processing)
    - [4.1 Introduction](#41-introduction)
    - [4.2 Implicit Sequences](#42-implicit-sequences)
      - [4.2.1 Iterators](#421-iterators)
      - [4.2.2 Iterables](#422-iterables)
      - [4.2.3 Built-in Iterators](#423-built-in-iterators)
      - [4.2.4 For Statements](#424-for-statements)
      - [4.2.5 Generators](#425-generators)
      - [4.2.6 Python Streams](#426-python-streams)

<!-- /code_chunk_output -->



---

## Chapter 4: Data Processing

### 4.1 Introduction

<br/>
<br/>


---

### 4.2 Implicit Sequences

A sequence can be represented *without* each element being stored explicitly in the memory of the computer.  That is, we can construct an object that provides access to all of the elements of some sequential dataset without computing the value of each element in advance.  Instead, we compute elements on demand.

Take `range` container as an example: Only when an element is requested from a `range`, it is computed.  Hence, we can represent very large ranges of integers *without* using large blocks of memory.  Only the **end points** of the range are **stored** as part of the `range` object.

> *Computing values on demand, rather than retrieving them from an existing representation, is an example of **lazy** computation.*

In computer science, lazy computation describes any program that delays the computation of a value until that value is needed.
<br/>
<br/>


> **NOTE**: The following contents on iterators and generators (*i.e.*, 4.2.1, 4.2.2, 4.2.3, 4.2.5) are **identical** with the corresponding contents in [Chapter 2](cs61a_notes_chapter_2.md).

#### 4.2.1 Iterators

Python and many other programming languages provide a unified way to process elements of a container value sequentially, called an <u>*iterator*</u>.

> *An iterator is an object that provides sequential access to values, one by one.*

The iterator has two components:

1. a mechanism for retrieving the next element in the sequence being processed, and
2. a mechanism for signaling that the end of the sequence has been reached and no further elements remain.

For any container, such as a list or range, an iterator can be obtained by calling the built-in `iter` function.  The contents of the iterator can be accessed by calling the built-in `next` function.

*e.g.*,
```python
>>> primes = [2, 3, 5, 7]
>>> type(primes)
<class 'list'>
>>> iterator = iter(primes)
>>> type(iterator)
<class 'list iterator'>
>>> next(iterator)
2
>>> next(iterator)
3
>>> next(iterator)
5
``` 

Python signals that there are no more values available by raising a `StopIteration` exception when `next` is called.  This exception can be handled using a `try` statement **[How?]**.

```python
>>> next(iterator)
7
>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
<br/>



An iterator maintains **local state** to represent its position in a sequence.  Each time `next` is called, that position advances.  

* Two separate iterators can track two different positions in the same sequence.  
* Two names for the same iterator will *share* a position.

*e.g.*,
```python
>>> r = range(3, 13)
>>> s = iter(r)         # 1st iterator over r
>>> next(s)
3
>>> next(s)
4
>>> t = iter(r)         # 2nd iterator over r
>>> next(t)
3
>>> next(t)
4
>>> u = t               # alternate name for the 2nd iterator
>>> next(u)
5
>>> next(u)
6
``` 

Advancing the second iterator does not affect the first.  

```python
>>> next(s)
5 
>>> next(t)
7
``` 

Calling `iter` on an iterator will return that iterator, **not a coay**.  This behavior is included in Python so that a programmer can call `iter` on a value to get an iterator without having to worry about whether it is an iterator or a container. 

```python
>>> v = iter(t)         # Another alternate name for the second iterator
>>> next(v)
8 
>>> next(u)
9
>>> next(t)
10
``` 
<br/>



The **usefulness** of iterators is derived from the fact that the underlying series of data for an iterator may not be represented explicitly in memory.  An iterator provides a mechanism for considering each of a series of values in turn, but all of those elements do not need to be stored simultaneously.  Instead, when the next element is requested from an iterator, that element may be computed on demand instead of being retrieved from an existing memory source.

Ranges are able to compute the elements of a sequence lazily because the sequence represented is *uniform*, and any element is easy to compute form the starting and ending bounds of the range.  Iterators allow for lazy generation of a much broader class of underlying series.  Instead, iterators are only required to compute the next element of the series, in order, each time another element is requested.

While not as flexible as *random access* (accessing arbitary elements of a sequence in any order), *sequential access* to sequential data is often sufficient for data processing applications.
<br/>
<br/>





#### 4.2.2 Iterables 

Any value that can produce iterators is called an <u>*iterable*</u> value.  

In Python, an iterable value is anything that can be passed to the built-in `inter` function.  

* Sequence values, *e.g.*, strings, tuples, 
* Other containers, *e.g.*,  sets, dictionaries.
* *Iterators* (because they can also be passed to the `inter` function)

Unordering collections, such as dictionaries in Python 3.5 and earlier, must define an ordering over their contents when they produce iterators.

> Dictionaries and sets are unordered because the programmer has no control over the order of iteration, but Python does guarantee certain properties about their order in its specification.

*e.g.*,
```python
>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d
{'one': 1, 'three': 3, 'two': 2}
>>> k = iter(d)
>>> next(k)
'one'
>>> next(k)
'three'
>>> v = iter(d.values())
>>> next(v)
1
>>> next(v)
3
``` 

If a dictionary changes in structure because a key is added or removed, then all iterators become *invalid*, and future iterators may exhibit changes to the order of their contents.

On the other hand, changing the value of an existing key does not invalidate iterators or change the order of their contents.

```python
>>> d.pop('two')
2
>>> next(k)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
``` 

A `for` statement can be used to iterate over the contents of any iterable or iterator.

```python
>>> r = range(3, 6)
>>> s = iter(t)
>>> next(s)
3
>>> for x in s:
        print(x)
4
5
>>> list(s)
[]
>>> for x in r:
        print(x)
3
4
5
``` 
<br/>
<br/>




#### 4.2.3 Built-in Iterators 

Several built-in functions take as arguments iterable values and return iterators.  These functions are used extensively for lazy sequence processing.

The `map` function is lazy: calling it does not perform the computation required to compute elements of its result.  Instead, an iterator object is created that can return results if queried using `next`.

*e.g.*,
```python
>>> def double_and_print(x):
        print('***', x, '=>', 2*x, '***')
        return 2*x
>>> s = range(3, 7)
>>> doubled = map(double_and_print, s)       # double_and_print not yet called
>>> next(doubled)                            # double_and_print called once
*** 3 => 6 ***
6
>>> next(doubled)
*** 4 => 8 ***
8
>>> list(doubled)
*** 5 => 10 ***
*** 6 => 12 ***
[10, 12]
``` 

The `filter` function returns an iterator over a subset of the values in another iterable.

The `zip` function returns an iterator over tuples of values that combine one value from each of multiple iterables.
<br/>
<br/>




#### 4.2.4 For Statements 

Objects are *iterable* (an interface) if they have an `__iter__` method that returns an *iterator*.

The `for` statement in Python operates on iterators.  Iterable objects can be the value of the `<expression>` in the header of a `for` statement:

```python
for <name> in <expression>:
    <suite>
``` 

To execute a `for` statement, 

1. Python evaluates the header `<expression>`, which must yield an *iterable value*.

2. The `iter` function is applied to that value.

3. Until a `StopIteration` exception is raised, Python repeatedly calls `next` on that iterator and binds the result to the `<name>` in the `for` statement.

4. It executes the `<suite>`

*e.g.*,
```python
>>> counts = [1, 2, 3]
>>> for item in counts:
        print(item)
1
2
3
``` 

In the above example, the `for` statement implicitly calls `iter(counts)`, which returns an iterator over its contents.  The `for` statement then calls `next` on that iterator repeatedly, and assigns the returned value to `item` each time.  This process continues until the iterator raises a `StopIteration` exception, at which point execution of the `for` statement concludes.

We can also implement the execution rule of a `for` statement in terms of `while`, assignment, and `try` statements:

```python
>>> items = iter(counts)
>>> try:
        while True:
            item = next(items)
            print(item)
    except StopIteration:
        pass 
1
2
3
``` 

Above, the iterator returned by calling `iter` on `counts` is bound to a name `items` so that it can be queried for each element in turn.  The handling clause for the `StopIteration` exception does nothing, bu handling the exception provides a control mechanism for exiting the `while` loop.

<br/>
<br/>




#### 4.2.5 Generators

Generators allow us to define iterations over arbitary sequences, even *infinite* sequence, by leveraging the features of the Python interpreter.

A generator is an iterator returned by a special class of function called a <u>*generator function*</u>. 

* <u>Regular functions</u>: use `return` statement 
* <u>Generator functions</u>: use `yield` statements to return elements of a series.

Generators do not use attributes of an object to track their progress through a series.  Instead, they control the execution of the generator function, which runs until the next `yield` statement is executed each time `next` is called on the generator.

*e.g.*,
```python
>>> def letters_generator():
        current = 'a'
        while current <= 'd'
            yield current
            current = chr(ord(current) + 1)

>>> for letter in letters_generator():
        print(letter)
a
b
c
d
``` 

When called, a generator function doesn't return a particular yielded value, but instead a `generator` (which is a type of iterator) that itself return the yielded values.  Calling `next` on the generator continues execution of the generator function from wherever it left off previously until another `yield` statement is executed.

1. The first time `next` is called, the program executes statements from the body of the `letters_generator` function until it encounters the `yield` statement.

2. Then, it **pauses** and **returns** the value of `current`.  `yield` statements do not destroy the newly created environment; they **preserve** it for later.

3. When `next` is called again, execution resumes where it left off.  The values of `current` and of any other bound names in the scope of `letters_generator` are preserved across subsequent calls to `next`.
  
We can walk through the generator by manually calling `next()`:

```python
>>> letters = letters_generator()
>>> type(letters)
<class 'generator'>
>>> next(letters)
'a'
>>> next(letters)
'b'
>>> next(letters)
'c'
>>> next(letters)
'd'
>>> next(letters)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
``` 

The generator does not start executing any of the body statements of its generator function until the first time `next` is called.  The generator raises a `StopIteration` exception whenever its generator function returns.
<br/>
<br/>




#### 4.2.6 Python Streams

<u>*Streams*</u> offer another way to represent sequential data implicitly.