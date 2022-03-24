# Solid principles


<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Solid principles](#solid-principles)
    - [Single requirement principle](#single-requirement-principle)
    - [Open close principle](#open-close-principle)
    - [Liskov substitution principle](#liskov-substitution-principle)
    - [Interface inversion principle](#interface-inversion-principle)

<!-- markdown-toc end -->

## Single requirement principle

## Open close principle

## Liskov substitution principle

1. Parameters types in a method of a subclass should match or be more abstract than parameter types in the method of the super
2. The return type in a method of a super class should match or be a subtype of the return type in the method of the superclass
3. The method in the sub classes shouldn't throw types of exceptions the base method isn't excepted to throw
    * An unexpected exception might slip through the defence system.
4. The **invariant of the superclass must be preserved**
    * e.g. all cats should have 4 legs, a tail and ability to meow.
5. A subclass shouldn't be able to change private fields of the superclass.

* Subclasses should be remain compatible with the behaviours of the parent class.

* Design by contract

* Based on polymorphism

* TODO subclasses should weak have pre-condition an stronger post-condition?

## Interface inversion principle

