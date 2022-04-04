# Destign patterns

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Destign patterns](#destign-patterns)
    - [Factories](#factories)
        - [Factory methods](#factory-methods)
        - [Applicability](#applicability)
        - [Pros](#pros)
        - [Cons](#cons)
    - [Abstract factories](#abstract-factories)
        - [Applicability](#applicability-1)
        - [Pros](#pros-1)
        - [Cons](#cons-1)
    - [Singleton](#singleton)
        - [Solution](#solution)
        - [Applicability](#applicability-2)
        - [Pros](#pros-2)
        - [Cons](#cons-2)
    - [Behaviour Patterns](#behaviour-patterns)
    - [Observer](#observer)
        - [TODO weather monitoring application](#todo-weather-monitoring-application)
        - [Magazine and newspaper subscription](#magazine-and-newspaper-subscription)
        - [Structure TODO](#structure-todo)
        - [Applicability](#applicability-3)
        - [Pros](#pros-3)
        - [Cons](#cons-3)
    - [Strategy](#strategy)
        - [Real world analogy of strategy](#real-world-analogy-of-strategy)
        - [Structure TODO](#structure-todo-1)
        - [Pros](#pros-4)
        - [Cons](#cons-4)
    - [Momento](#momento)
    - [Motivation of momento](#motivation-of-momento)
        - [Solution](#solution-1)
        - [Example: Text editor](#example-text-editor)
        - [Structure of memento TODO](#structure-of-memento-todo)
        - [Applicability of memento](#applicability-of-memento)
        - [Pros](#pros-5)
        - [Cons](#cons-5)

<!-- markdown-toc end -->
## Factories
> An interface for creating objects in a super class but allows sub classes to alter the type of objects that will be created <br />
>

### Factory methods
Replace direct object construction call (using the new operator) with calls to a special factory method.

Objects returned by a factor methods are often referred as products

Sub classes can alter the class of objects being returned by the factory methods

![Factory method structure](pic1.png) 


### Applicability
* Use the factory method when you **don't know beforehand the exact types and dependencies of the objects your code should work with**
* Use the factory method when you want to **provide users of your library or framework with a way to extend its internal components**
* Use the factory method when you want to save system resources by reusing existing objects instead of rebuilding them each time.


### Pros 

* You avoid tight coupling between the creator and the concrete products.
* **Single responsibility principle**. You can move the **product creating mode** into one place in the program, making the code easier to support
* **Open-Closed principle**. You can introduce new types of products into the program without breaking existing client code

### Cons
* The code may become more complicated since you need to introduce a lot of new sub classes to implement the pattern

TODO add images

## Abstract factories

> Abstract factory is a creations design pattern that lets you product families of related objects without specifying their contrite classes.

* Explicitly declare interfaces for each distinct product of the family (e.g. chair, sofa or coffee table)

* Make all variants of products follow those interfaces
    * e.g. all chair variants can implement the chair interface; all coffee table variants can implement the CoffeeTable interface and so on.

* All variants of the same object must be moved to a single class hierarchy.

* Each concrete factory corresponds to a specific product variant.

![abstract factory structure](pic2.jpeg) 

### Applicability 
* Use the Abstract Factory when your code needs to work with various families of related products, but you don't want it to depend on the concrete classes of those products - they might be unknown beforehand or you simply want to allow for future extensible.

* Consider implementing the abstract factory when you have a class with a set of Factory Methods that blur its primary responsibility.

### Pros
* You can be sure that products you are getting from a factory are **compatible** with arch other
* You avoid tight coupling between concrete product and client code
* **Single responsibility principle**. You can extract the product **create code into one place** making the code easier to support.
* **Open/closed principle**. You can introduce **new variants of products** without breaking existing client code


### Cons
* The code may become more complicated then it should be, since a lot of new interfaces and classes are introduced along with the pattern

## Singleton
> Singleton is a creational design pattern that lets you **ensure that a class has only one instance** while providing a **global access** point to this instance

* Singleton pattern solves two problems:
    * Access to some shared resources - for example a **database or file**
        * Imagine that you created an object, but after a while decided to create a new one
        * Instead of receiving a fresh object, you'll get the one you already created.
        
    * Provide a global access point to that instance
    
    
* However it violates the Single Responsibility Principle
    * TODO why?

* The singleton pattern has become so popular that people may call something a singleton even though hit solves just one of the listed problems.

### Solution
* All implementations of the Singleton pattern have these two steps in common:
    * Make the default constructor private, to prevent other objects from using the new operator with the singleton class
    * Create a static creation method that acts as a constructor. 
        * This method calls the private constrictor to create an object and saves it in a static field.
        * All following class to this method return the cached object.
        
    * Example: The government is an excellent example of the Singleton pattern:
        * A country can have only one official government
        * Regardless of the personal identities of the individuals who form governments, the title, "The government x", is a global access point that identifies the group of people in charge.
 
### Applicability
* Use the singleton pattern when a class in your program should have just a **single instance of available to all clients**, for example, a single database object shared by different parts of the program.
* Use the singleton pattern when you need stricter control over global variables.


### Pros
* You can  be sure that a class has **only a single instance**
* You gain a global access point to that instance
* The singleton object is initialised only when it's requested for the first time


### Cons
* Violates the **Single Responsibility Principle**
* The Singleton pattern **can mask bad design**, e.g. when the components of the program know too much about each other.
* The pattern requires special treatment in a multi threaded environment
* It maybe be difficult to unit test the client code of the Singleton because may test frameworks reply on inheritance when producing mock objects.

## Behaviour Patterns

* Behaviour patterns are concerned with choosing algorithms and the assignment of responsibiilities between different ojects

* Observer

* Strategy

* Memento

## Observer

> observer is a behaviour design pattern that lets you define a **subscription mechanism to notify multiple objects about any events that happen** to the object they are observing <br />
> The observer pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependants are notified and updated automatically. <br />
> An object, named the subject, maintains **a list of its dependants**, called observers, and notifies them automatically of any state changes usually by calling one of their methods <br/>

* Also know as **Event-Subscriber, Listener**


### TODO weather monitoring application


### Magazine and newspaper subscription
* If you subscribe to a newspaper or magazine, you no longer need to go to the store to check if the next issue is available.
* Instead, the publisher sends new issues directly to your mailbox right after publication or even in advance.
* The publisher maintains a list of subscribers and knows which magazines they are interested in.
* Subscribers can leave the list at any time when they wish to stop the publisher sending new magazine issues to them.

### Structure TODO


### Applicability

* Use the observe pattern when changes to the state of one object may require changing other objects and the actual set of objects is unknown beforehand or changes dynamically.

* Use the pattern when some objects in your app must observe others but only for a limited time or in specific cases.

### Pros
* Open/closed principle. You can introduce new subscriber classes without having to change the publisher's code (and vice versa if there's a publisher interface)
* We can reuse subjects or observers independently of each other.
* You can establish relations between objects at runtime
* Changes to either the subject or an observer will not affect the other.

### Cons
* Subscribers are notified in random order

## Strategy
> Strategy is a behaviour design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable. <br />

* Casual navigation application
* Automatic route planning
    * Add address and navigate through
    * Next update: walking or cycle routes and so on
    
* Every route requires a new algorithm to design which is giving you many headaches

* Any change to **one of the algorithms, affected the whole class, increasing the change of creating an error in already-working code.** 

* Merge conflicts

* Strategies
    * Extract all of these algorithms into separate classes called strategies.
    
* Context
    * A class that must have a field for storing a reference to one of the strategies.
    * It delegates the work to a linked strategy object instead of executing it on its own 
    
    
* Client

* Interface
    * Which only exposes a single method for triggering the algorithm encapsulated within the selected strategy

### Real world analogy of strategy

* Google maps
    * Imagine that you have to travel from MCG to Monash Caufield campus
        * You can catch a train drive a car or ride a bike
        
        * These are your transport strategiesp
        
        
 ![map strategies](pic3.png)  


### Structure TODO

* Use the strategy pattern when you want to use different variants of an algorithm with an object and be able to switch from one algorithm to another during runtime.

* Use the strategy when you have a lot of similar classes that only differ in the way they execute some behaviour

* Use the strategy pattern to isolate the business logic of a class from the implementation details of algorithms that may not be as important in the context of that logic.

* Use the pattern when your class has a massive conditional operator that switches between different variants of the same algorithm 

### Pros

* YOU can swap algorithms used inside an object at runtime.

* You can isolate the implementation details of an algorithm from the code that use it.

* You can replace inheritance with composition

* Open/closed princples. You can introduce new strategies without having to change the context.


### Cons
* If you have a couple of algorithms and they rarely change. There is not real reason to over complicate the program with new classes and interfaces that come along with the pattern

* Clients must be aware of the differences between strategies to be able to select a proper one.



## Momento
> Momento is a behaviour design pattern that lets you **save and restore the previous state of an object without revealing the details of its implementation** 

Also called a snapshot

## Motivation of momento
* Creating the state of snapshots to the actual owner of that state, the **originator** object
* Storing the copy of the object's state in a special object called **memento** 
* The contents of the memento aren't accessible to any other object except the one that produced it
* Other objects must communicate with mementos using a limited surface which may allow fetching the snapshot metadata but not the original object's state contained in the snapshot
* Such restrictive policy lets you store mementos inside other objects usually called **caretakers**

### Solution
* The originator has full access to the memento, whereas the caretakers can only access the metadata
* A stack of mementos stored inside the caretaker will grow each time the editor is about to execute an operation
* When a user triggers the undo, the history grabs the most recent memento from the stack and passes it back to the editor, requesting a roll-back


### Example: Text editor
* Text editor application
    * Simple text editing
    * Format text
    * Insert inline images etc
    
* Undo??
    * Direct approach
        * Save records in storage
        * Restore from the snapshot from the storage
        
* Broken encapsulation
    * Invading the private space of objects

### Structure of memento TODO

### Applicability of memento
* Use the memento pattern when you want to produce snapshots of the object's state to be able to restore previous state of the object.

* Use the pattern when direct acces to the object's fields/getters/setters violates its encapsulation.

### Pros
* You can produce snapshots of the object's state **without violating its encapsulation**
* You can simplify the originators code  by letting the caretaker maintain the history of the originators state.
* Keeping the saved state external from the key object helps maintain cohesion.
* Provides easy to implement recovery capability

### Cons
* The app might consume lots of RAM if clients create mementos too often.
* Saving and restoring can be time-consuming
* Caretakers should track the originators lifecycle to be able to destroy obsolete mementos.
* Most dynamic programming languages, such as PHP, Python and javascript, can't guarantee that the state within the memento stays untouched.

