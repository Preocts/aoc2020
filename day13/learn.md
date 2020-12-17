## Euclid's algorithm
Note: `//` indicates integer division and `%` indicates modular division. These are Python expressions.

Used to find the GCD (greatest common divisor) of two numbers

Find the GCD of (a, b) where (a, b) are two whole numbers.

1. Use (a // b) to find the whole number of times b will fit into a, let this be m
1. Express this as: a = m(b)
1. Use (a % b) to find the remainder of express above, let this be r
1. Express this as: a = m(b) + r
   - The remainder theorem ensures that r is always less than b and a

Euclid's theory proves that the GCD of the first set of numbers (a, b) is equal to the GCD of (b, r). This allows us to repeat the process above until we reach a remainder of 0.

### Find the GCD of (7398, 2877)
- a = 7398
- b = 2877
- m = 7398 // 2877 = 2
- r = 7398 % 2877 = 1644

1. a = m(b) + r
1. 7398 = 2(2877) + 1644
   - Next step: let a = 2877, let b = 1644
1. 2866 = 1(1644) + 1233
   - Next step: let a = 1644, let b = 1233
1. 1644 = 1(1233) + 411
   - Next step: let a = 1233, let b = 411
1. 1233 = 3(411) + 0
   - Stop

Since the GCD of (a, b) is equal to the GCD of (b, r) then the GCD of `(7398, 2877)` is equal to `(411, 0)`, or just `411`.

---

## Modular inverse

Typical forms:

- Find (197)^-1 mod 3000
- Solve for d: 197d ≡ 1 mod 3000

1. Find the GCD of 3000 and 197 (Euclid's theory)
   - 3000 = 15(197) + 45
   - 197 = 4(45) + 17
   - 45 = 2(17) + 11
   - 17 = 1(11) + 6
   - 11 = 1(6) + 5
   - 6 = 1(5) + 1
   - 5 = 5(1) + 0
   - *If the GCD is not 1 then there is no inverse modular*
1. Express `1` as the difference between multiples of 3000 and 197
   - Work backward from previous results
   - Solve for the remainder
     - 11 = 1(6) + 5 becomes:
     - 11 - 1(6) = 5
   - Substitute into the first
     - 1 = 6 - 1(5)
       - `(5)` is then substituted
       - 1 = 6 - 1(11 - 1(6))
       - simplify:
         - 1 = 6 - 1(11) + 1(6)
         - 1 = 6 + 1(6) - 1(11)
         - 1 = 2(6) - 1(11)
     - 1 = 2(6) - 1(11)
       - `(6)` is then substituted
       - 1 = 2(17 - 1(11)) - 1(11)
       - simplify:
         - 1 = 2(17) - 2(11) - 1(11)
         - 1 = 2(17) - 3(11)
     - 1 = 2(17) - 3(11)
       - `(11)` is then substituted
       - 1 = 2(17) - 3(45 - 2(17))
       - simplify:
         - 1 = 2(17) - 3(45) + 5(17)
         - 1 = 2(17) + 6(17) - 3(45)
         - 1 = 8(17) - 3(45)
     - 1 = 8(17) - 3(45)
       - `17` is then substituted
       - 1 = 8(197 - 4(45)) - 3(45)
       - simplify:
         - 1 = 8(197) - 32(45) - 3(45)
         - 1 = 8(197) - 35(45)
     - 1 = 8(197) - 35(45)
       - `45` is then substituted
       - 1 = 8(197) - 35(3000 - 15(197))
         - simplify:
           - 1 = 8(197) - 35(3000) + 525(197)
           - 1 = 8(197) + 525(197) - 35(3000)
           - 1 = 533(197) - 35(3000)
     - 1 = 533(197) - 35(3000)
1. Apply modulo 3000 to both sides
   - 1(mod 3000) = 533(197)(mod 3000) - **35(3000)(mod 3000)**
   - 1 ≡ 533(197)(mod 3000)
1. Answer is 533

---

## Chinese Remainder Theorem
Used to find the answer to a problem such as:

- x ≡ 2(mod 3)
- x ≡ 2(mod 4)
- x ≡ 1(mod 5)
- Find x

**The GCD of each remainder must be equal to 1 for this theorem to be applied.**

- GCD(3, 4) = 1
- GCD(3, 5) = 1
- GCD(4, 5) = 1

---

## Extended Euclidean Algorithm (Bezout's Theorem)
The extended Euclidean algorithm answers the Bezout's theorem. Bezout's theorem says that whenever you are looking for the GCD of two numbers (a, b); there must always be two integers (s, t) such that: 

`a(s) + b(t) = GCD(a, b)`

*This drives many encryptions*

This is also the same process as the modular inverse but stops at the final step. Using the example above the final step yields `1 = 533(197) - 35(3000)`. This is in the form of `a(s) + b(t) = GCD(a, b)`

The answer to Bezout's Theorem through extending the Euclidean algorithm is then `(533, 35)`.

---
