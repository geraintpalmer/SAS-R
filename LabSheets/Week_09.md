# Week 9 - Linear Algebra

1. Use Sage to solve the following system of equations:

    $$\begin{cases}
    10x+2y=0\\
    2x-y=154
    \end{cases}$$

2. **TICKABLE** Note that the above system of equations is equivalent to the following systems of equations:

    $$\begin{cases}
    10a+2b=0\\
    2a-b=154
    \end{cases}$$

    $$\begin{cases}
    10m+2n=0\\
    2m-n=154
    \end{cases}$$

    In essense the only thing that defines the system of equations is the cofficients:

    $$\begin{pmatrix}
    10,2,0\\
    2,-1,154
    \end{pmatrix}$$

    We can of course seperate the right hand side of our equation and perhaps include those elements in a vector. Our system can now be represented as:

    $$\begin{pmatrix}10,2\\2,-1\end{pmatrix}\begin{pmatrix}0\\154\end{pmatrix}$$

    Let us attempt to represent the above system in Sage.

    The following defines `b` as a vector:

        b = vector(0,154)

    The representation of coefficients is a well defined mathematical object called a `matrix`. The following code defines `A` as a matrix:

        A = matrix([[10, 2], [2, -1]])

    If we define a vector `X` as a vector of the symbolic variables:

        X = vector([x, y])

    We can **multiply** `A` by `X`:

        A * X

    Verify that $X = (x_0, y_0)$ where $(x_0, y_0)$ is the solution to our system of equations (obtained in (1)).

3. **TICKABLE** In linear algebra (you will study this next semester) a matrix equation is an equation of the form:

    $$AX=b$$

    or

    $$XA=b$$

    If we define `A` and `b` as in question 2 we can solve this equation quite simply using the `solve_right` or `solve_left` methods. The following obtains a solution to the equation $AX=b$:

        A.solve_right(b)

    Note that `A\b` is shorthand for `A.solve_right`

    Use the above to solve the following system of equations using matrix notation:

    $$\begin{cases}
    4x - 2y + 3z = 10\\
    -x - 5y - 8z = 9\\
    x + y + z = 1
    \end{cases}$$

4. Matrix multiplication.

    - Describe matrix multiplication
    - Carry out mathematically
    - Multiple 4 example (2 which multiples by identity and 1 by inverse)

5. Matrix inversion
6. Enter the following matrices in to a list. Invert all of them.
7. Plotting something?
8. Solve a large number of systems of linear equations
9. Reading in data for a big system of linear equations
10. Creating a big linear system.
