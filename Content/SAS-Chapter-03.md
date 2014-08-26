---
layout      : post
categories  : content
title       : SAS Chapter 3 - Manipulating Data
comments    : true
---

<h2 id="data-steps"><span class="header-section-number">3.1</span> Data steps</h2>
<p>A data step is a type of SAS statement that allows you to manipulate SAS data sets. Some of the things we can do include:</p>
<ol style="list-style-type: decimal">
<li>Copying a data set (with new variables)</li>
<li>Concatenating any number of data sets</li>
<li>Merging any number of data sets</li>
</ol>
<p>The following code simply creates a data set in the work library called &quot;j&quot; that is a copy of the data set jjj located in the mat013 library.</p>
<pre><code>data j;
set mat013.jjj;
run;</code></pre>
<p>To concatenate two data sets (as shown pictorially) we use the following syntax:</p>
<pre><code>data [New Data Set];
set A B;
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image00.png" /><br /> The following code concatenates the jjj and mmm data sets as shown.</p>
<pre><code>data mat013.mmmjjj;
set mat013.mmm mat013.jjj;
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image54.png" /><br /> To merge two data sets (as shown pictorially) we use the following syntax:</p>
<pre><code>data [New Data Set];
merge A B;
by [Merge Variable]
run;</code></pre>
<p>Note that the two data sets must be sorted on the merge variable prior to merging.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image19.png" /><br /> The following code would merge the two data sets first_data_set and other_data_set in the mat013 library as shown.</p>
<pre><code>proc sort data=mat013.first_data_set;
by name;
run;

proc sort data=mat013.other_data_set;
by name;
run;

data mat013.merged_data_set;
merge mat013.first_data_set mat013.other_data_set;
by name;
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image34.png" /><br /> Data steps can be used in conjunction with the <code>where</code> statement to select certain variables. For example consider the data set shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image11.png" /><br /> The following code selects only the elements of the above data set that start with a <code>D</code>.</p>
<pre><code>data Dwarfs;
set Dwarfs;
where substr(Name,1,1)=&quot;D&quot;;
run;</code></pre>
<p>The result is shown in (note that the above code makes use of the <code>substr</code> function that we will see later).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image45.png" /><br /></p>
<h2 id="the-program-data-vector"><span class="header-section-number">3.2</span> The program data vector</h2>
<p>SAS is able to handle very large data sets because of the way data steps work. In this section we'll explain how it uses the &quot;program data vector&quot; (pdv) to efficiently handle data. The basic steps of compiling a data step are as follows:</p>
<ol style="list-style-type: decimal">
<li>SAS creates an empty data set.</li>
<li>SAS checks the data step for any unrecognized keywords and syntax errors.</li>
<li>SAS creates a PDV to store the information for all the variables required from the data step.</li>
<li><p>SAS reads in the data line by line using the PDF.</p>
<p>(If a &quot;by&quot; statement is used (for example when merging two data sets) the PDF does not empty if there are still observations with the same value of the &quot;by&quot; variable).</p></li>
<li><p>SAS creates the descriptive portion of the SAS data set (viewable using the &quot;contents&quot; procedure).</p></li>
</ol>
<p>An example of how this works with concatenation and an example of how this works with merging is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image15.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image30.png" /><br /></p>
<h2 id="creating-new-variables"><span class="header-section-number">3.3</span> Creating new variables</h2>
<p>Creating new variables using various arithmetic and/or string relationships is relatively straightforward in SAS. The following code creates a new data set call MMM_with_BMI, with a new variable &quot;BMI&quot; as a function of the height and weight variables in the MMM dataset in the mat013 library.</p>
<pre><code>data mat013.MMM_with_BMI;
set mat013.MMM;
bmi=weight_in_kg/(height_in_metres**2);
run;</code></pre>
<p>Some of the arithmetic functions are shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/SAS_math_operators.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/SAS_math_functions.png" /><br /> We can also do operations on strings, the following code replaces the variable &quot;Sex&quot; with the first entry of &quot;Sex&quot; (which gets rid of the Male - M and Female - F issue).</p>
<pre><code>data mat013.MMM_with_BMI;
set mat013.MMM;
sex=substr(sex,1,1);
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/SAS_string_functions.png" /><br /> It's worth checking the web for a full list of various SAS functions (there are a huge amount of them).</p>
<h3 id="dropping-and-keeping-variables."><span class="header-section-number">3.3.1</span> Dropping and keeping variables.</h3>
<p>In this section we'll take a quick look at two simple ways of improving the efficiency of a data step. Recalling how SAS handles a data step (using the pdv as described previously), one immediate way of improving efficiency is to ensure that the pdv only &quot;transports&quot; the variables we require. We do this with the &quot;drop&quot; or &quot;keep&quot; statement.</p>
<p>Let us consider the previous example and assume that we want our MMM_with_BMI data set without the weight and height variables. We use a &quot;drop&quot; statement to get rid of those variables:</p>
<pre><code>data mat013.MMM_with_BMI_nhw(drop=weight_in_kg height_in_metres);
set mat013.MMM;
bmi=weight_in_kg/(height_in_metres**2);
run;</code></pre>
<p>Note that the following code would not give the required output as we are trying to drop the variables from the original data set, however we need those variables to calculate the bmi:</p>
<pre><code>data mat013.MMM_with_BMI_nhw;
set mat013.MMM(drop=weight_in_kg height_in_metres);
bmi=weight_in_kg/(height_in_metres**2);
run;</code></pre>
<p>The keep statement (basically) does the same thing as the drop statement but in reverse, by only keeping the variables we have specified. Which one to use depends simply on whether or not you want to drop or keep more variables.</p>
<p>Note that you cannot use a drop statement and a keep statement in the same data step.</p>
<p>The following code will create a data set with just the bmi variable.</p>
<pre><code>data mat013.just_bmi(keep=bmi);
set mat013.MMM;
bmi=weight_in_kg/(height_in_metres**2);
run;</code></pre>
<h3 id="renaming-variables"><span class="header-section-number">3.3.2</span> Renaming variables</h3>
<p>The following code creates a data set &quot;JJJ&quot; in the work library which is a copy of the &quot;JJJ&quot; dataset in the mat013 library, renaming the &quot;sex&quot; variable to &quot;gender&quot;.</p>
<pre><code>data JJJ(rename=(sex=gender));
set mat013.JJJ;
run;</code></pre>
<p>This can also be used in the set data set:</p>
<pre><code>data JJJ;
set mat013.JJJ(rename=(sex=gender));
run;</code></pre>
<h3 id="operations-across-rows"><span class="header-section-number">3.3.3</span> Operations across rows</h3>
<p>We have seen in previous sections how to create new variables for any given observation (i.e. across columns of a data set). In this section we see how to create variables across rows. Recalling how the program data vector works, this implies that we must find a way to keep certain entries in the pdv for future calculation.</p>
<p>We will demonstrate this using the birthday_money.csv data set as shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image38.png" /><br /> The first such way is to use the &quot;retain&quot; statement. The &quot;retain&quot; statement keeps the last entry for a given variable in the pdv for future calculation. Note that we can give an initial value for a particular variable as shown in the following code (which produces a variable &quot;total&quot; that is a running total of &quot;amount&quot;) the output of which is shown.</p>
<pre><code>data bm_analysis;
set mat013.birthday_money;
retain total 0;
total=total+amount;
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image47.png" /><br /> Another tool for such calculations is the &quot;lagn&quot; function which gives the value of a variable from a certain number n of prior steps. The following code gives two new variables, the yearly difference and 2 yearly difference, the result of which is shown.</p>
<pre><code>data bm_analysis;
set mat013.birthday_money;
retain total 0;
total=total+amount;
yearly_diff=amount-lag1(amount);
two_yearly_diff=amount-lag2(amount);
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image40.png" /><br /> The lag functions can be used in much more complex assignments and in fact when simply wanting to calculate a difference there is a quicker way: using the &quot;difn&quot; function as shown in the code below which gives the same result as shown.</p>
<pre><code>data bm_analysis;
set mat013.birthday_money;
retain total 0;
total=total+amount;
yearly_diff=dif1(amount);
two_yearly_diff=dif2(amount);
run;</code></pre>
<h2 id="handling-dates"><span class="header-section-number">3.4</span> Handling dates</h2>
<p>Dates are handled in a particular way in SAS. Let's consider the csv file shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image37.png" /><br /> We have seen in Chapter 1 how to import data using proc import. If we use the normal approach an error would occur. This is due to the confusion associated with our birthday variables (the first 20 rows have the date and month values both less than 12). A further option that can be incorporated in proc import is the number of rows that SAS will &quot;pre-read&quot; to identify the type of variables that are to be imported. This is often an easy way to ensure that SAS recognises dates.</p>
<pre><code>proc import datafile=&#39;\~birthdays.csv&#39;
out=birthdays
replace;
getnames=yes;
guessingrows=25;
run;</code></pre>
<p>A proc contents run on the above data set shows that the birthday variable data was imported using the informat DDMMYY10. In other words SAS has recognised that the dates were in that particular format.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image50.png" /><br /> Another approach is to import files in SAS using a data step and the infile statement. When doing this we can tell SAS the format of the data (whether or not it is a string, numerical or date variables).</p>
<pre><code>data birthdays;
infile &#39;~/birthdays.csv&#39; dlm=&#39;,&#39; firstobs=2;
input Name $ Birthday ddmmyy10.;
run;</code></pre>
<p>The infile statement tells SAS where the data is located and the 'dlm' statement tells SAS how the file is delimited (in this case with a comma). The 'firstobs' statement tells SAS where the data starts in the file (in this case the second row as the first row is the name of the variables in our data set). The input statement then allows us to tell SAS the names of the variables as well as the format they are in, here we tell SAS that the second variable is to be called 'Birthday' and it is in the ddmmyy8. format.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image63.png" /><br /> The above output might be a bit confusing, this is due to the fact that SAS handles dates as numbers, using the convention that the 1st of January 1960 is the number 0 (this allows for straightforward arithmetic manipulation of dates). The following code imports the data as above and displays the underlying numeric dates in the date9. format.</p>
<pre><code>data birthdays;
infile &#39;\~/birthdays.csv&#39; dlm=&#39;,&#39; firstobs=2;
input Name $ Birthday ddmmyy8.;
format Birthday date9.;
run;</code></pre>
<p>The output is shown. Note that applying the date9. format only changes the appearance of the data.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image51.png" /><br /> There are various formats that can be used when importing variables (for dates as well as other variables) and subsequently these same formats can be used to display the data if this is required. Searching online quickly finds other SAS formats.</p>
