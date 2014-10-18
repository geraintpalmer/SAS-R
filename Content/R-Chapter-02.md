---
layout      : post
categories  : content
title       : R Chapter 2 - Basic Statistical Procedures
comments    : true
---

<h2 id="procedures"><span class="header-section-number">2.1</span> Procedures</h2>
<p>In the previous chapter we were introduced to some very basic aspects of R:</p>
<ol style="list-style-type: decimal">
<li>what R looks like</li>
<li>how to import data into R</li>
<li>how to export data into R</li>
</ol>
<p>In this chapter we will take a closer look at procedures that allow us to analyse and manipulate data. Vectors are the building blocks of all R objects. Single numeric/string variables are in fact vector of size 1. Almost all procedures in R are obtained by applying functions to vectors. Details as to how R handles these operations will be explained in the next chapter (so don't worry about it too much for now).</p>
<p>The procedures we are going to look at in this chapter are:</p>
<ol style="list-style-type: decimal">
<li>Viewing datasets</li>
<li>Summarising the contents of data sets</li>
<li>Obtaining summary statistics of data sets</li>
<li>Obtaining frequency tables</li>
<li>Obtaining linear models</li>
<li>Plotting data</li>
</ol>
<h2 id="a-list-of-procedures"><span class="header-section-number">2.2</span> A list of procedures</h2>
<h3 id="utility-procedures"><span class="header-section-number">2.2.1</span> Utility procedures</h3>
<p>We have seen how to view and entire data set (by simply printing the name of the object in question).</p>
<p>We illustrate this once again by considering the MMM data set shown, (imported using read.csv).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image24.png" /><br /> At times we might not want to open the data set but simply gain some information as to what is in the data set.</p>
<p>To view only the names of the variables of our data set we use the <code>name</code> function as shown.</p>
<pre><code>names(MMM)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image69.png" /><br /> If we had a very large data set then we could quickly view the first/last few entries using the <code>head</code>/<code>tail</code> function as shown.</p>
<pre><code>head(MMM)
tail(MMM)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image49.png" /><br /> Finally if we would like to view a description of the overall structure of a data set we can use the <code>str</code> function as shown.</p>
<pre><code>str(MMM)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image34.png" /><br /> The class of the imported character variables are <code>Factors</code>, this is due to the importation method (<code>read.csv</code>) automatically converting the character variables in this form - details about &quot;Factors&quot; are given below. The reason this occurs is the default value of stringsAsFactors (used in the read.csv function) is TRUE, the following code forces the characters retain their class without conversion.</p>
<pre><code>MMM&lt;-read.csv(&quot;MMM.csv&quot;,stringsAsFactors=FALSE)</code></pre>
<p>The factor stores the nominal values as a vector of integers in the range [ 1... k ] (where k is the number of unique values in the nominal variable), and an internal vector of character strings (the original values) mapped to these integers. This is often a much more efficient way of handling strings.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image31.png" /><br /></p>
<h3 id="descriptive-statistics"><span class="header-section-number">2.2.2</span> Descriptive statistics</h3>
<p>To gain an initial set of summary statistics of a data frame we can use the <code>summary</code> function:</p>
<pre><code>summary(MMM)</code></pre>
<p>The output of which is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image50.png" /><br /> Recall that most &quot;things&quot; in R are objects and &quot;summary&quot; is a good example of a generic function that works on most objects. If you are faced with a new object (for example the output of a regression analysis) it is sometimes worth trying to apply summary on it to get some initial information.</p>
<p>To obtain a particular summary statistic of a specific variable, we can use functions that apply to vectors and select the vectors from the dataset.</p>
<p>To select a particular column (as a vector) from our dataset, we use the following command:</p>
<pre><code>MMM$Age</code></pre>
<p>We can then apply various functions to this vector:</p>
<pre><code>length(MMM$Age)
mean(MMM$Age)
sd(MMM$Age)
min(MMM$Age)
max(MMM$Age)
sum(MMM$Age)
var(MMM$Age)</code></pre>
<p>The output of which is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image52.png" /><br /> We can compartmentalise our results using the <code>by</code> function. The general syntax for the <code>by</code> function is given below:</p>
<pre><code>by(data=dataFrame , Indices=grouping variables, FUN= a function)</code></pre>
<p>We'll use this to obtain the mean age and height compartmentalised by sex:</p>
<pre><code>by(MMM$Age, MMM$Sex, mean)
by(MMM$Height.in.Metres, MMM$Sex, mean)</code></pre>
<p>The output of which is shown.</p>
<div class="figure">
<img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image13.png" /><p class="caption"></p>
</div>
<p>The above code subsets the data frame by the grouping variable. If we want to just carry out an action on a vector (as above, we're only actually interested in the Age vector or the Height vector) then we can also use the &quot;tapply function&quot;. This applies a function to a vector according to the levels of another vector:</p>
<pre><code>tapply(MMM$Age, MMM$Sex, mean)</code></pre>
<p>Finally, to reduce the number of keystrokes, we can use the <code>with</code> statement. This tells R to evaluate everything within a given data frame. The following code reproduces the above results:</p>
<pre><code>with(data=MMM,by(Age,Sex,mean) )
with(data=MMM,tapply(Age, Sex, mean))</code></pre>
<p>Note: the <code>data=</code> statement can be omitted.</p>
<h3 id="frequency-tables"><span class="header-section-number">2.2.3</span> Frequency Tables</h3>
<p>The <code>table</code> function allows us to obtain frequency tables of data sets. As an example let us consider the data set shown. The <code>table</code> function creates a &quot;table&quot; (a particular type of R object):</p>
<pre><code>table(math_tests$Teacher,math_tests$Pass.Fail)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image19.png" /><br /> Again we can write this as:</p>
<pre><code>with(math_tests,table(Teacher,Pass.Fail))</code></pre>
<p>We can save this table as a new object and use the <code>prop</code> command to gain row and column totals and proportions:</p>
<pre><code>mytable&lt;-table(math_tests$Teacher,math_tests$Pass.Fail)
margin.table(mytable, 1)
margin.table(mytable, 2)
prop.table(mytable,1)
prop.table(mytable,2)</code></pre>
<p>The output of all this is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image32.png" /><br /></p>
<h3 id="correlations"><span class="header-section-number">2.2.4</span> Correlations</h3>
<p>The following lines of code select only the columns from MMM that are numeric. An explanation of this will follow in the next chapter.</p>
<pre><code>MMM[,sapply(MMM,is.numeric)]</code></pre>
<p>The correlation 'cor' function only acts upon numeric vectors (and/or dataframes), hence the selection of solely numeric values first.</p>
<pre><code>MMMnum&lt;-MMM[,sapply(MMM,is.numeric)]
cor(MMMnum)</code></pre>
<p>The <code>cor</code> function however does not give tests of significance. We can obtain significance tests between two variables using <code>cor.test</code>:</p>
<pre><code>cor.test(MMM$Age,MMM$Height.in.Metres)</code></pre>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image29.png" /><br /> As is often the case in open source software, packages are independently developed and need to be called to be used in R. Above we have shown the very basic approach to obtaining correlations in R, we will now use the rcorr function from the Hmisc package.</p>
<p>To install the package we use the following code:</p>
<pre><code>install.packages(&quot;Hmisc&quot;)</code></pre>
<p>Once that happens a window opens asking us to choose the mirror from which to download. This is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image54.png" /><br /> Once that is done to load the package the following code is required:</p>
<pre><code>library(Hmisc)</code></pre>
<p>or:</p>
<pre><code>require(Hmisc)</code></pre>
<p>To see the packages currently loaded we can use the following code:</p>
<pre><code>search()</code></pre>
<p>Note: Packages can also be installed by selecting the 'Packages' tab and selecting the package required for installation.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image63.png" /><br /> Using this package, we will use the <code>rcorr</code> function that gives the correlation matrix for a data set. Note that the data set must be numeric and in <code>matrix</code> form. The following code selects the numeric variables from the MMM data set and converts the result to a matrix:</p>
<pre><code>MMMnum&lt;-MMM[,sapply(MMM,is.numeric)]
MMMmat&lt;-as.matrix(MMMnum)</code></pre>
<p>Once this is done we can get the correlation matrix using the following code:</p>
<pre><code>rcorr(MMMmat)</code></pre>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image20.png" /><br /></p>
<h3 id="linear-models"><span class="header-section-number">2.2.5</span> Linear Models</h3>
<p>In this section we very briefly see the syntax for some basic linear models in R.</p>
<p>The general syntax for linear regression is as follows in R:</p>
<pre><code>lm(outcome~predictors)</code></pre>
<p>The following code will be used to investigate whether or not there is a linear model of height with weight and savings and predictors (in two ways, the second is slightly more compact and leaves less room for confusion):</p>
<pre><code>lm(JJJ$Height.in.Metres~JJJ$Weight.in.Kg+JJJ$Savings.in.Pounds)
lm(Height.in.Metres~Weight.in.Kg+Savings.in.Pounds,data=JJJ)</code></pre>
<p>The results are shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image38.png" /><br /> To get the full set of results from the regression analysis we use the following code:</p>
<pre><code>summary(lm(Height.in.Metres~Weight.in.Kg+Savings.in.Pounds,data=JJJ))</code></pre>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image45.png" /><br /> Looking at the p value we see that the overall model should not be rejected, however the detailed results show that perhaps we could remove savings from the model.</p>
<p>Analysis of variance (ANOVA) can be done easily in R. We shall show this using a new data set (math.csv) shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image58.png" /><br /> aov(outcome~class,data)</p>
<p>We will use the &quot;aov&quot; function to see if the grades obtained by students depend on their teacher (in two ways, the second is slightly more compact):</p>
<pre><code>aov(math$GRADE~math$PROF)
aov(GRADE~PROF,data=math)</code></pre>
<p>The results are shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image42.png" /><br /> To get the full set of results from the ANOVA we use the following code:</p>
<pre><code>summary(aov(GRADE~PROF,data=math))</code></pre>
<p>The results are shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image60.png" /><br /></p>
<h3 id="plots-and-charts"><span class="header-section-number">2.2.6</span> Plots and charts</h3>
<p>Note that due to the object oriented nature of  R, almost all of the above outputs have a &quot;plot&quot; attribute.</p>
<p>The simplest way to produce a histogram in R is to use the &quot;hist&quot; function. The following code gives a histogram for the height of entries in the JJJ data set as shown.</p>
<pre><code>hist(JJJ$Height.in.Metres)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image15.png" /><br /> The simplest way to produce a scatter plot in R is to use the &quot;plot&quot; function. The following code gives a scatter plot for the height against weight of entries in the JJJ data set as shown.</p>
<pre><code>plot(JJJ$Weight.in.Kg,JJJ$Height.in.Metres)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image47.png" /><br /> There are various other ways to obtain similar graphs, as well as change the look and feel of our graphs. We won't go into this here but you are encouraged to look into it (in particular the ggplot package is widely used).</p>
<h2 id="exporting-output"><span class="header-section-number">2.3</span> Exporting output</h2>
<p>All the non graphical outputs from R are objects, as such they can be output to a file (to be copied into another document if need be) using the write statements of Sections 1.4. However to export graphical output, we use any of the following statements (depending on the output format required):</p>
<pre><code>pdf(&quot;mygraph.pdf&quot;)
win.metafile(&quot;mygraph.wmf&quot;)
png(&quot;mygraph.png&quot;)
jpeg(&quot;mygraph.jpg&quot;)
bmp(&quot;mygraph.bmp&quot;)
postscript(&quot;mygraph.ps&quot;)</code></pre>
<p>Once that command is written we use a normal R command to create a plot and finally we close the output file with the following statement:</p>
<pre><code>dev.off( )</code></pre>
<p>The following code creates a png file entitled &quot;height_v_weight_plot&quot; with the previous scatter plot.</p>
<pre><code>png(&quot;height_v_weight_plot.png&quot;)
plot(JJJ$Weight.in.Kg,JJJ$Height.in.Metres)
dev.off( )</code></pre>
