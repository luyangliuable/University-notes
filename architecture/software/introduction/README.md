# What is architecture
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [What is architecture](#what-is-architecture)
    - [Definition](#definition)
        - [Software elements defined within architecture:](#software-elements-defined-within-architecture)
            - [What are software elements?](#what-are-software-elements)
    - [Key principles or modern design](#key-principles-or-modern-design)

<!-- markdown-toc end -->

## Definition

* **Not all design** are architectural. Designs of algorithms and data
  structures are encapsulated in classes or components of the final system.

* The design of the interfaces for such classes is an architectural issue though. 


> “The **software architecture** of a program or computing system is the structure or structures of the system, which comprise software elements, the **externally visible** properties of those elements, and the relationships among them.” <br />
> -- Bass et al.

### Software elements defined within architecture:
* Defines how elements **related** to each other
* Information that does not relate to interactions are omitted

 “An architecture is [thus] foremost an abstraction of a system that suppresses details of elements that do not affect how they use, are used by, relate to, or interact with other elements”

#### What are software elements?
* Elements can be objects processes, libraries, databases, services, a whole commercial application.

## Key principles or modern design
* Elements should be partitioned into public and private parts. (Particularly OO design)
* The public part defines externally visible interfaces. 
* Systems can be made up of more than one structure.
	* No one structure can claim to be **the structure**\

### Examples of architectures within a system:
* The break-down into smaller and simpler implementation units
* Synchronisation relationships between processes/threads in a parallel system. Background queue, broker and workers etc.
* Note that one of these is a static structure, the other is a run time structure.

* These definitions imply that *every computing system with software has **a** software architecture*
  * Software architecture does not need to be documented in order to exist. It is inherent to the software. Architecture documentation and the software architecture are different.
  * "Box-and-line" diagrams only capture part of a whole software architecture - particularly if they are only static views (e.g. class or package diagrams)

## Difference between architecture and design
* Architecture is clearly design
* Architecture is a part of design.
* Design is more detailed where as an architecture is a blue print.
* **Architecture is a subset of design**

### Architecture
* Web
	* MVC
* Android
	* MVVM
* Web or cloud
	* Microservices

Design
* Web
* Desktop
* Cloud

## Requirement Analysis

### OO analysis
* Analysis: Investigation of problems and the requirements
* OO analysis: Emphasis finding and describing objects and related concepts in the problem domain.
* Tool
	* Block diagram
	* UML
	* Usecases to analyse requirement
	* Class diagram to model the relation between classes (after use cases are developed)
	* Interaction diagrams to design the model.