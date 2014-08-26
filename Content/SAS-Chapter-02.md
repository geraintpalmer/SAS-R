---
layout      : post
categories  : content
title       : SAS Chapter 2 - Basic Statistical Procedures
comments    : true
---

<h2 id="procedures"><span class="header-section-number">2.1</span> Procedures</h2>
<p>In the previous chapter we were introduced to some very basic aspects of SAS:</p>
<ol style="list-style-type: decimal">
<li>what SAS looks like</li>
<li>how to import data into SAS</li>
<li>how to export data from SAS</li>
</ol>
<p>In this chapter we will take a closer look at &quot;procedure steps&quot; which allow us to call a SAS procedure to analyse or process a SAS dataset. In the previous chapter we have already seen two procedure steps:</p>
<ol style="list-style-type: decimal">
<li>proc import</li>
<li>proc export</li>
</ol>
<p>The procedures we are going to look at in this chapter are:</p>
<ol style="list-style-type: decimal">
<li>Viewing datasets</li>
<li>Summarising the contents of data sets</li>
<li>Obtaining summary statistics of data sets</li>
<li>Obtaining frequency tables</li>
<li>Obtaining linear models</li>
<li>Plotting data</li>
</ol>
<p>The general syntax for these procedures in SAS is given below:</p>
<pre><code>proc [NAME OF PROCEDURE] data=[NAME OF SAS DATA SET];
[Options for Procedure being used]
run;</code></pre>
<p>Some of the options that can be used in a procedure step include:</p>
<ol style="list-style-type: decimal">
<li>&quot;var&quot; - which tells SAS which variables are to be processed.</li>
<li>&quot;by&quot; - which tells SAS to compartementalize the procedure for each different value of the named variable(s). The data set must first be sorted by those variables.</li>
<li>&quot;where&quot; - select only those observations for which the expression is true.</li>
</ol>
<h2 id="a-list-of-procedures"><span class="header-section-number">2.2</span> A list of procedures</h2>
<h3 id="utility-procedures"><span class="header-section-number">2.2.1</span> Utility procedures</h3>
<p>We have already seen that we can open and view a data set by simply double clicking on the data set in the explorer window. A data set can also be viewed by using the &quot;print&quot; procedure.</p>
<p>We'll do this by considering the MMM data file shown (imported using an import procedure).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image41.png" /><br /> The following code will run the &quot;print&quot; procedure:</p>
<pre><code>proc print data=mat013.mmm;
run;</code></pre>
<p>which outputs the data set to the output window as shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image24.png" /><br /> At times we might not want to open the data set but simply gain some information as to what is in the data set. This is equivalent to checking the label on a present without unwrapping it. We do this using the &quot;contents&quot; procedure.</p>
<pre><code>proc contents data=mat013.mmm;
run;</code></pre>
<p>This outputs summary information as shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image59.png" /><br /> A procedure that will be needed, when using more complex procedures and larger data sets, is the &quot;sort&quot; procedure.</p>
<pre><code>proc sort data=mat013.mmm;
by age;
run;</code></pre>
<p>Note that this procedure makes use of the &quot;by&quot; statement which tells SAS which variable to sort our observations on (in this case the variable age). Recall that the data set is not sorted. If we run the above &quot;sort&quot; procedure, at first nothing seems to happen, however if we view the data set again (using proc print or otherwise) we see (as shown) that the data set is now sorted.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image06.png" /><br /> Important: If you have the mat013.mmm data set open in browser mode (i.e. having double clicked on the data set in the explorer window) when running the &quot;sort&quot; procedure, checking your log shows you an error as shown. Always close any browser windows when processing a data set - or use the &quot;print&quot; procedure!</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image20.png" /><br /> ### Descriptive statistics</p>
<p>In this section we will go over some of the procedures needed to obtain descriptive statistics.</p>
<p>The first procedure we consider is the &quot;means&quot; procedure. We can use the following code to obtain various summary statistics relating to the age variables of the mat013.mmm dataset.</p>
<pre><code>proc means data=mat013.mmm;
var age;
run;</code></pre>
<p>We can specify the particular summary statistics we want (if none are specified a default set is displayed).</p>
<pre><code>proc means data=mat013.mmm N mean std min max sum var css uss;
var age;
run;</code></pre>
<p>We can also choose to display the summary statistics for more than one variable</p>
<pre><code>proc means data=mat013.mmm N mean std min max sum var css uss;
var age height_in_metres;
run;</code></pre>
<p>We can compartmentalise our data results using the &quot;by&quot; statement. Note that the data set must be sorted on the same variable.</p>
<pre><code>proc means data=mat013.mmm N mean std min max sum var css uss;
var age height_in_metres;
by sex;
run;</code></pre>
<p>Another way of compartmentalising results is using the &quot;class&quot; statement. This is very similar to the &quot;by&quot; statement and does not require the prior sorting of your data set.</p>
<pre><code>proc means data=mat013.mmm N mean std min max sum var css uss;
var age height_in_metres;
class sex;
run;</code></pre>
<p>Finally, it's also possible to create a data set from the &quot;means&quot; procedure.</p>
<pre><code>proc means data=mat013.mmm N mean;
var age height_in_metres;
class sex;
output out=summary_of_mmm
N(age)=number_of_age_obs
mean(age)=average_of_age_obs
N(height_in_metres)=number_of_height_obs
mean(height_in_metres)=average_height;
run;</code></pre>
<p>The above code creates a data set called &quot;summary_of_mmm&quot; in the work library (the default library if no library is specified) with two variables &quot;number_of_obs&quot; and &quot;average_of_obs&quot; which give the number and mean for the observations as calculated by the &quot;means&quot; procedure as shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image16.png" /><br /> The &quot;univariate&quot; procedure allows for the calculation of univariate statistics in SAS. The following code will output all the default univariate statistics for all the variables.</p>
<pre><code>proc univariate data=mat013.mmm;
run;</code></pre>
<p>We can choose to run the &quot;univariate&quot; procedure on a subset of the variables, using the &quot;var&quot; statement.</p>
<pre><code>proc univariate data=mat013.mmm;
var savings_in_pounds;
run;</code></pre>
<p>The various outputs of the &quot;univariate&quot; procedure are shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image10.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image03.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image61.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image53.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image36.png" /><br /> ### Frequency tables</p>
<p>The &quot;freq&quot; procedure allows us to obtain frequency tables of data sets. As an example, let's consider the dataset shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image27.png" /><br /> The most basic &quot;freq&quot; procedure will give the frequencies of all the observations in the data set:</p>
<pre><code>proc freq data=mat013.math_tests;
run;</code></pre>
<p>We can specify the variables we want to look at by listing them after the &quot;tables&quot; statement (similar to the var statement for the &quot;means&quot; procedure):</p>
<pre><code>proc freq data=mat013.math_tests;
tables teacher pass_fail;
run;</code></pre>
<p>If we want to cross tabulate the data then we use a <code>*</code> in between the variables concerned:</p>
<pre><code>proc freq data=mat013.math_tests;
tables teacher*pass_fail;
run;</code></pre>
<p>The above code gives the table shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image08.png" /><br /> Various options can be passed to the &quot;freq&quot; procedure, the simplest of which is shown below:</p>
<pre><code>proc freq data=mat013.math_tests;
tables teacher*pass_fail / nocol norow nopercent;
run;</code></pre>
<p>Other options include computing a chi square test but we will not worry about that for now.</p>
<h3 id="correlations"><span class="header-section-number">2.2.2</span> Correlations</h3>
<p>The &quot;corr&quot; procedure can be used to obtain correlations in SAS. The following code is the basic &quot;corr&quot; procedure applied to the mat013.mmm data set which gives the output shown.</p>
<pre><code>proc corr data=mat013.mmm;
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image49.png" /><br /> If we want to run the &quot;corr&quot; procedure on a subset of the variables then we use the &quot;var&quot; statement:</p>
<pre><code>proc corr data=mat013.mmm;
var age savings_in_pounds;
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image22.png" /><br /></p>
<h3 id="linear-models"><span class="header-section-number">2.2.3</span> Linear Models</h3>
<p>In this section we'll very briefly see the syntax for some basic linear models in SAS. First of all we'll take a look at linear regression. The following code will run such an analysis on the mat013.jjj data set, checking if there is a linear model of height with predictors weight and savings:</p>
<pre><code>proc reg data=mat013.jjj;
model height_in_metres=weight_in_kg savings_in_pounds;
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image12.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image39.png" /><br /> Looking at the p-value we see that the overall model should not be rejected, however the detailed results show that perhaps we could remove savings from the model.</p>
<p>Analysis of variance (ANOVA) can be done very easily in SAS. We show this using a new data set.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image09.png" /><br /> We will use the &quot;anova&quot; procedure to see if the grades obtained by students depend on their teacher.</p>
<pre><code>proc anova data=mat013.math;
class prof;
model grade=prof;
run;</code></pre>
<p>Note the &quot;class&quot; keyword is needed to state which variable we are using to group on. The results show that there is indeed a difference between groups (further post-hoc tests are needed to investigate which groups differ etc.).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image25.png" /><br /> Another procedure that can be used for a variety of models (including the 2-way anova) is the &quot;glm&quot; (general linear model) procedure. The following code simply reproduces the above results.</p>
<pre><code>proc glm data=mat013.jjj;
model height_in_metres=weight_in_kg savings_in_pounds;
run;

proc glm data=mat013.math;
class prof;
model grade=prof;
run;</code></pre>
<h3 id="plots-and-charts"><span class="header-section-number">2.2.4</span> Plots and charts</h3>
<p>There are various ways to obtain histograms in SAS, the easiest way is to use the &quot;univariate&quot; procedure with the &quot;histogram&quot; option. The following code gives a histogram for the height of individuals in the mat013.jjj dataset as shown.</p>
<pre><code>proc univariate data=mat013.jjj;
var height_in_metres;
histogram;
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image01.png" /><br /> There are various ways to obtain scatter plots in SAS, the easiest way is to use the &quot;gplot&quot; procedure. The following code gives a scatter plot for the height of individuals against their weight in the mat013.jjj dataset as shown.</p>
<pre><code>proc gplot data=mat013.jjj;
plot height_in_metres*weight_in_kg;
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image28.png" /><br /> There are various other ways to obtain similar graphs as well as change the look and feel of our graphs. We won't go into this here but you are encouraged to look into it.</p>
<h2 id="exporting-output"><span class="header-section-number">2.3</span> Exporting output</h2>
<p>We can output results of procedures in SAS using the &quot;output delivery system&quot;. The syntax is straightforward and we surround normal SAS code with the &quot;ods&quot; statements to output to various formats (html, pdf, rtf).</p>
<pre><code>ods [format of your choice] file=[Location of file to be output];
[Normal SAS code]
ods [format of your choice] close;</code></pre>
<p>As an example, the following code creates an html file called &quot;freq_table&quot; in html format stored at the location &quot;~/Desktop&quot; (note that in Window's the <code>/</code> should be a <code>\</code>) as shown.</p>
<pre><code>ods html file=&quot;\~/Desktop/freq_table.htm&quot;;

proc gplot data=mat013.jjj;
plot height_in_metres*weight_in_kg;
run;

ods html close;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image17.png" /><br /> The following code will create a file called &quot;scatter_plot.pdf&quot; in pdf format stored at the location &quot;~/Desktop&quot; (note that in Window's the &quot;/&quot; should be a &quot;&quot;) as shown.</p>
<pre><code>ods pdf file=&quot;\~/Desktop/scatter_plot.pdf&quot;;

proc gplot data=mat013.jjj;
plot height_in_metres*weight_in_kg;
run;

ods pdf close;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image02.png" /><br /> The following code will create a file called &quot;regression.rtf&quot; in rtf format (Word, LibreOffice etc.) stored at the location &quot;~/Desktop&quot; (note that in Window's the &quot;/&quot; should be a &quot;&quot;) as shown.</p>
<pre><code>ods rtf file=&quot;\~/Desktop/regression.rtf&quot;;

proc reg data=mat013.jjj;
model weight_in_kg=height_in_metres;
run;

ods rtf close;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image55.png" /><br /></p>
