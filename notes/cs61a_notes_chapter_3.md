---
export_on_save:
  html: true
html:
  toc: true
  offline: true 
toc:
  depth_from: 3
  depth_to: 5
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



---

## Chapter 3: Interpreting Computer Programs 

### 3.1 Introduction

A programming language like Python is useful because we can define an ***interpreter***, a program that carries out Python's *evaluation* and *execution* procedures.

An interpreter is just another **program** which determines the meaning of expressions in a programming language.

$\implies$  the *most fundamental* idea in programming.
<br/>

#### 3.1.1 Programming Languages 

Programming languages vary widely in their *syntactic structures*, *features*, and *domain of application*.

Among general purpose programming languages, the constructs of function and function application are pervasive.

On the other hand, powerful languages exist that do **NOT** include an object system, higher-order functions, assignmeng, or even control constructs such as `while` and `for` statements.

* As an example with a *minimum* set of features, we are going to use the [Scheme](https://en.wikipedia.org/wiki/Scheme_(programming_language)) programming language. (The subset of Scheme used in this text does **not** allow mutable values at all.)
<br/>

In this chapter, we study 

* the **design of interpreters** and, 
* the **computational processes** they create when executing programs.
<br/>


Many interpreters have an elegant common structure: two **mutually recursive functions**,

1. one evaluates expressions in environments;
2. one applies functions to arguments.

These functions are recursive in that they are defined in terms of each other: applying a function requires evaluating the expressions in its body, while evaluating an expression may involve applying one or more functions.
<br/>
<br/>



---



### 3.2 Functional Programming 



