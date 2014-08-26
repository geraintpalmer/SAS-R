---
layout      : post
categories  : problemsheet
title       : R Problem Sheet
comments    : false
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

16.  Create the following data set and execute a command that only chooses elements from the data set starting with the letter D:

            Dopey
            Sneezey
            Sleepy
            Happy
            Grumpy
            Bashful
            Doc

17.  Concatenate the JJJ and MMM data sets.

18.  Obtain the elements of the previous data set (concatenation of JJJ and MMM) for which the age is less than 18.

19.  Merge the following data sets:

            Name, Age
            Billy, 24
            Bob, 23

            Name, Weight
            Billy, 75
            Bob, 80

20.  Create a single data set that includes the bmi of the observations from the MMM and JJJ data sets

21.  Ensure there are just two type of observations for the variables sex in MMM and JJJ: M or F.

22.  Create a copy of the concatenated data set (of JJJ and MMM) with just the names and bmis of every observation.

23.  Rename the variable sex as gender in the data sets JJJ and MMM.

24.  Download the file [birthday_money.csv](../Data/C3/birthday_money.csv), import it and output a data set with a running total as well as a yearly difference.

25. Download the file [birthdays.csv](../Data/C3/birthdays.csv) import it and sort the data set by date of birth.

    The relevant data can be found [here](../Data/index.html):

26. (_Challenge: C4_) Create a function in R that outputs the first \\(k\\) prime number to a csv file (do so without using any built in test for primality).
Build the function so that it takes two input arguments:

    - \\(k\\)
    - a string: the name of the output file.

27.  Create a (single) data set containing the name of the observations from JJJ and MMM as well as a new variable which is Y if the individual is clinically obese and N otherwise.

28.  Create a (single) data set containing the total number of birthday candles used throughout the lives of every individual from both JJJ and MMM.

29.  Obtain the first even numbers less than 240.

30.  Create a function that outputs a scatter plot of height against weight for observations in the JJJ and MMM data sets. Modify the function so that it outputs the plot to a pdf file.

31.  Create a function that computes the left over life savings after a given quantity of spending on a given quantiy of shopping trips from the JJJ data set.

32.  Modify the above function so that a default value is given to spend of 430 and a default value of 3 trips.

33.  Modify the above function so that a message is printed if the spend is 0 and no other output is given.

34.  Create a function that creates 15 data sets each with updated savings in pounds for observations in the JJJ and MMM data sets for varying values for the number of trips (1 to 15).

35.  Download the files [Files_1-200.zip](../Data/C4/Files_1-200.zip) and create a function that automatically imports them.

36. Include the some of the above code in a script file that could be run using the source command and re run whenever the above data sets get updated.
