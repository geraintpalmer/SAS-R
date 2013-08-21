# Week 8 - Differential Equations

Sage can be used to solve differential equations. Often complex systems can be modelled simply in terms of differential equations however solving these differential equations is not always straightforward. At the end of this week you will be able to:

- Solve differential equations using Sage;
- Solve differential equations numerically using Sage;
- Plot the results of the above.

1. **TICKABLE** The general syntax for solving a differential equation of the form $f(x, y)== g(x, y)$ is shown below:

        desolve(f(x, y) == g(x, y), y)

    Try out the following code which solves the differential equation: $\frac{dy}{dx}=y$.

        desolve(diff(y,x)==y,y)

    Note that that there is no need to specify the independent variable ()

2. Plot the solution of a differential equation.
3. A problem that needs to be written in terms of differential equations.
4. Systems of differential equations
5. Plotting solution to system of differential equations
6. A problem with differential equations
4. Numerical solution to a differential equation.
5. Plotting the solutions to numerical differential equations
6. A problem with differential equations.
