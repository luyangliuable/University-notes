# Requirements in Agile

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Requirements in Agile](#requirements-in-agile)
    - [Definition](#definition)
    - [How to nail down or solicit requirements?](#how-to-nail-down-or-solicit-requirements)
    - [Requirement checklist](#requirement-checklist)
    - [User stories](#user-stories)
    - [SAFe requirement](#safe-requirement)
    - [Benefits of **domain modelling **](#benefits-of-domain-modelling-)
    - [Visions](#visions)
    - [**PI planning** (Program increment planning)](#pi-planning-program-increment-planning)
        - [Inputs](#inputs)
        - [Outputs](#outputs)

<!-- markdown-toc end -->

## Definition

* Tells you what behaviour is considered correct, and **they are hugely important for testing**.
    * Every requirement should be tested
    * Each requirement should be traced back to its corresponding requirements
    * Each test should be traced backed to its corresponding requirements (e.g. traceability matrix)

* Can be very hard to nail down a complete set of requirements due to changing market and features.

* Instead get the product owner involved in the development
TODO

## How to nail down or solicit requirements?
* Try to get the product owner to nail down the requirement based on the **client's priorities**
* Try to add much value as possible each iteration
* Important to attempt **requirements management** during inception so ensure there are things to do for each iteration


## Requirement checklist
  * [ ] Complete
  
  * [ ] Correct

  * [ ] Precise

  * [ ] organised

  * [ ] unambiguous

  * [ ] verifiable

  * [ ] consistent

  * [ ] understandable

  * [ ] modifiable

  * [ ] traceable

  * [ ] **design independent** (i think there are many design choices as long as the requirement stay the safe)

  * [ ] annotated

  * [ ] concise

## User stories
Are short simple descriptions for designs and capabilities, usually in the perspective of a user or customer of the system.

```
As a <type of user>, I want <some goal> so that <some resaon>
```

Example

> As a **system admin**, I want to reset a user's password so that they can login

## SAFe requirement
If you only model one thing in Agile, model the domain.


## Benefits of **domain modelling ** (in SAFe)

* This allows the modelling of real world entities and the relationships between them.

* Also provides a common language for the entire organisation

* Connects backlog items together which includes:
  * Team
  * Program
  * Large solutions
  * Portfolio
  * Non-functional requirements (NRF)



* Analysis of epics
* Backlog refinement at large solutions, program and team levels.

* **Non-functional requirements**

* Design workshops at different levels

* Refining visions TODO


## Visions
A descriptions of the **future state of the Solution under development**

* Reflect customer and stakeholder needs as well as the feature and capabilities, proposed to meet those needs.

* Portfolio Vision
  * A longer term context for near term decisions in a way that is **both practical and inspirational**.

* Solution vision 
  * Translating the portfolio vision or solution vision **such as architecture and the reason and direction behind the chosen solution**.
  * Links
    * Solution intent
    * Solution Context
    * Solution backlog
    * Strategic Themes
    * Solution/Product management
    * Team inputs: Product owner/Agile
    * Architectures, Systems, Team, other
    * Customer feedback
  
## **PI planning** (Program increment planning)
* Important!
* Cadence based, face-to-face event that series as the heartbeat of the agile release train (ART), aligning all the teams on the ART of to a **shared mission and vision**.

* Similar to **Spring planning in Scrum**

### Inputs 
* Business context
* Roadmap and vision
* Top features of the program backlog (TODO similar to PBI?)

### Outputs
*  Business context
   * PI objectives
   
* Program board
  * New feature and delivery date
  * Feature dependency among teams
  * etc

## What each team does in PI planning preparation?
* **Agile release train engineering team:**
  * developing (and documenting) a plan for running the week program increment (PI) planning session, e.g., Video on Week **Product Management team is responsible for**
  * populating and prioritizing the Program Backlog with user stories from the client
  * evolving but at least need a few to start
* **System Architecture team is responsible for**
  * creating a Potential Solution Architectures (PSA) document exploring tool chains and communicating them to the project members.
  * high-level draft
* https://www.scaledagileframework.com/pi-planning/
