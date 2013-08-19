# Week 7 - Symbolic Calculus

Using Sage we can carry out various operations from Calculus. This week we will investigate how to:

- Carry out limits in Sage;
- Carry out differentiation in Sage;
- Carry out integration in Sage.

1. Last week we saw how to define a function in Sage:

    f(x) = x ^ 3 + 3 * x + sin(x)

    To obtain the variables of a function we can use the `variables` method:

    print f.variables()

    Try this with a function of more than one variable:

    f(x, y) = x * y + x ^ 2 + y ^ 2

2. In calculus the following definition of a limit is well know:

    >  $\lim_{x\to a}f(x)=L$ iff $\forall\; \epsilon>0$ $\exists$ $\delta$ such that $\forall\; x$: $|x-a|<\delta$ $\Rightarrow$ $|f(x)-L|\leq \epsilon$.

3. Two sides limits
4. Algebra of limits
5. $\lim_{x\to 0}\frac{sin(x)}{x}$
6. $e^(x)$
7. Basic differentiation
8. Limiting definition of a derivative
9. Plotting the limiting definition of a derivative
10. Visualising the limiting definition of a derivative
11. Differentiation rules
11. Basic integration
12. Integration by parts
13. Riemann integration
14. Numerical integration
15. Integrate polynomials in a data file
