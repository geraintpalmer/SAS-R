---
layout      : post
categories  : problemsheet
title       : R Problem Sheet
comments    : true
---


01. (_Challenge: C1 + C2_) The datafile [Stock_Report.csv](../Data/C1+C2/Stock_Report.csv) contains data on the stock for a supermarket. There are 4 variables:

    - The department of the product
    - The name of the product
    - The value in loyalty points of the product
    - The cost of the product

    Answer the following questions:

    - How many products are there in each department?
    - How much variation is there in the price of the products?
    - Is this similar to the loyalty points value?
    - Is there a linear relationship between the loyalty points and the price of products?

02.  Create the data set "first_data_set" from the notes and export to csv.

03.  Download the files [JJJ.csv](../Data/C1+C2/JJJ.csv) and [MMM.csv](../Data/C1+C2/MMM.csv) import them in to R.

04.  View both the MMM and JJJ data sets.

05.  View the structure of the MMM and JJJ data sets using the str command.

06.  Obtain the mean age, height in metres and weight in kg for the observations of the MMM and JJJ datasets.

07.  Obtain the mean age, height in metres and weight in kg for the observations of the MMM and JJJ datasets compartmentalising your output by sex (you'll need to use the by function).

08.  Download the file [math_tests.csv](../Data/C1+C2/math_tests.csv), import it in to R and output a frequency table of teachers against pass\_fail.

09.  Obtain correlation tables for all the numerical values in JJJ and MMM (using 2 separate approaches (one of which will require you to download a package).

10.  Do a regression analysis of the variable height\_in\_metres against weight\_in\_kg and savings\_in\_poundsfor the data sets JJJ and MMM.

11. Download the data set [math.csv](../Data/C1+C2/math.csv) and run an ANOVA test to see if the grades depends on the professor.

12. Obtain a histogram for the variables weight\_in\_kg for the data sets JJJ and MMM.

13. Obtain a scatter plot of weight\_in\_kg against height\_in\_metres for the data sets JJJ and MMM

14. Output all of the above graphs to a pdf file.


    The relevant data can be found [here](../Data/index.html):

    - [JJJ.csv](../Data/C1+C2/JJJ.csv)
    - [MMM.csv](../Data/C1+C2/MMM.csv)
    - [math_tests.csv](../Data/C1+C2/math_tests.csv)
    - [math.csv](../Data/C1+C2/math.csv)

15. (_Challenge: C3_) The datafiles [Dates\_1996.csv](../Data/C3/Dates_1996.csv) and [Prices\_1996.csv](../Data/C3/Prices_1996.csv) contain data for holidays taken in 1996. There are 3 variables in Dates_1996.csv:

    - The ID
    - Start Date
    - End Date

    There are 2 variables in Prices.csv:

    - The ID
    - The Price

    The data file [Holidays_1995.csv](../Data/C3/Holidays_1995.csv) contains data for holidays taken in 1995. There are 4 variables:

    - The ID
    - Start Date
    - End Date
    - The Price

    Obtain a report regarding the holidays taken in 1995 and 1996. Pay particular attention to the price per day of a holiday.

16. Create the following data set and execute a command that only chooses elements from the data set starting with the letter D:

        Dopey
        Sneezey
        Sleepy
        Happy
        Grumpy
        Bashful
        Doc

17. Concatenate the JJJ and MMM data sets.

18. Obtain the elements of the previous data set (concatenation of JJJ and MMM) for which the age is less than 18.

19. Merge the following data sets:

        Name, Age
        Billy, 24
        Bob, 23

        Name, Weight
        Billy, 75
        Bob, 80

20. Create a single data set that includes the bmi of the observations from the MMM and JJJ data sets

21. Ensure there are just two type of observations for the variables sex in MMM and JJJ: M or F.

22. Create a copy of the concatenated data set (of JJJ and MMM) with just the names and bmis of every observation.

23. Rename the variable sex as gender in the data sets JJJ and MMM.

24. Download the file [birthday_money.csv](../Data/C3/birthday_money.csv), import it and output a data set with a running total as well as a yearly difference.

25. Download the file [birthdays.csv](../Data/C3/birthdays.csv) import it and sort the data set by date of birth.

    The relevant data can be found [here](../Data/index.html):

26. (_Challenge: C4_) Create a function in R that outputs the first \\(k\\) prime number to a csv file (do so without using any built in test for primality).
Build the function so that it takes two input arguments:

    - \\(k\\)
    - a string: the name of the output file.

27. Create a (single) data set containing the name of the observations from JJJ and MMM as well as a new variable which is Y if the individual is clinically obese and N otherwise.

28. Create a (single) data set containing the total number of birthday candles used throughout the lives of every individual from both JJJ and MMM.

29. Obtain the first even numbers less than 240.

30. Create a function that outputs a scatter plot of height against weight for observations in the JJJ and MMM data sets. Modify the function so that it outputs the plot to a pdf file.

31. Create a function that computes the left over life savings after a given quantity of spending on a given quantiy of shopping trips from the JJJ data set.

32. Modify the above function so that a default value is given to spend of 430 and a default value of 3 trips.

33. Modify the above function so that a message is printed if the spend is 0 and no other output is given.

34. Create a function that creates 15 data sets each with updated savings in pounds for observations in the JJJ and MMM data sets for varying values for the number of trips (1 to 15).

35. Download the files [Files_1-200.zip](../Data/C4/Files_1-200.zip) and create a function that automatically imports them.

36. Include the some of the above code in a script file that could be run using the source command and re run whenever the above data sets get updated.

37. (_Challenge: C5_) Find an example and illustrate the use of one (or more) of the following R packages:

    - sqldf
    - ggplot2
    - twitteR

38. Using sql, create a copy of the MMM and JJJ data sets, including all the variables.

39. Using sql, create the previous copies selecting just the variables, Name, Age, Sex, Random\_Number, as well as the bmi of the observations.

40. For the following data set:

        Var1, Var2, Var3, Var4, Var5
        A, 1, A, 2, B
        A, 1, A, 2, B
        B, 1, A, 1, C
        C, 2, B, 2, D
        C, 2, C, 1, E

    1. Create a copy of the data set removing complete duplicate rows.
    2. Create a copy of the data set removing duplicates of Var2.
    3. Create a copy of the data set removing duplicates of Var3 and Var4.
    4. Create a copy of the data set selecting only observations where Var2 \\(>\\) Var4.
    5. Create a copy of the data set ordering by Var1.
    6. Create a data set containing the mean, std, max, min and variance of Var4 and Var2 by Var1.

41. Download the data sets [dogs.csv](../Data/C5/dogs.csv) and [cats.csv](../Data/C5/cats.csv) use sql to:

    1. create an inner join.
    2. a left outer join.
    3. a right outer join (you won't be able to use sql for this in R).
    4. a full outer join (you won't be able to use sql for this in R).

42. Create a histogram for the Height of people in the JJJ data set.

43. Modify the above plot to be a density plot with your own legends labels and title.

44. Obtain a scatter plot of weight against height for people in the JJJ data set.

45. Modify the above plot so that the points are proportional to the age.

46. Obtain a box plot for the Height of people in the JJJ data set by sex.

47. Obtain a scatter plot of Weight against Height with a smoothed trend line.

48. Obtain histograms of height against weight, compartmentalised by sex.

49. Create a scatter plot with a fitted linear model for Height against Weight for all people in MMM and JJJ. Compartmentalise your graphs based on the data set and the sex.

50. Save the above graph to file.

51. Get all of todays trends on twitter.

52. Search for all tweets with the `orms` hashtag.

53. Find the tweets from INFORMS.

54. (_Class Test 2012-2013_) Create a function that will give all numbers less than \\(k\\) (an input), not divisible by \\(3,7\\) or \\(13\\). Furthermore let your function take as input the name of a file and write those numbers to a csv file with that name.

    Demonstrate this with \\(k=2341\\) and the file name "classtest".

55. (_Class Test 2012-2013_) Using either SAS or R:

    The files [Game_1.csv](./Data/Game_1.csv), [Game_2.csv](./Data/Game_2.csv), [Game_3.csv](./Data/Game_3.csv), [Game_4.csv](./Data/Game_4.csv), [Game_5.csv](./Data/Game_5.csv), [Game_6.csv](./Data/Game_6.csv) contain data for guesses of the game "2/3rds of the average":

    > "All individuals must guess a number between 0 and 100 (inclusive). The winner of the game is the guess that is closest to two thirds of the average of all guesses."

    1. Obtain histograms showing the distribution of guesses in each individual game and over all games (i.e. produce 7 plots).
    2. Identify the winning guess in each individual game and over all games.
    3. Every game is played with a different number of players, obtain a scatter plot of the winning guesses against the number of players (include the overall).
    4. Comment on the relationship (if any) between the number of players and the winning guess.

56. (_Class Test 2013-2014_) Using both SAS and R (in other words attempt this question using SAS and then using R):

    Create a data set with two variables: "Week" and "Ranking". For every week of the MAT013 course (1-5 including this class test) give a ranking of your enjoyment of each week of the course (1 being the best). Write some code (in both SAS and R) to sort this data set in descending order of the enjoyment ranking.

57. (_Class Test 2013-2014_) Using R:

    Obtain the profits (income \\(-\\) costs) of each company that is present in **both** data sets [incomes.csv](./Data/incomes.csv) and [costs.csv](./Data/costs.csv).

    Draw a histogram of these profits and also obtain a linear relationship between income and profits.

58. (_Class Test 2013-2014_) Using either SAS or R:

    1. Write code that will obtain \\(k\\) random points \\((x,y)\\) where \\(x,y\\) are uniformly sampled between 0 and 1.
    2. Identify how many of these points satisfy \\(x^2+y^2\leq 1\\) (this number will be referred to as \\(N=N(k)\\)).
    3. Plot \\(\frac{4N(k)}{k}\\) for \\(1\leq k\leq 5000\\) and comment on the result.
