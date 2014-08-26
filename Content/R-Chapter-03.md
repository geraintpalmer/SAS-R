---
layout      : post
categories  : content
title       : R Chapter 3 - Manipulating Data
comments    : false
---

<h2 id="vectors-and-data-frames"><span class="header-section-number">3.1</span> Vectors and data frames</h2>
<h3 id="vectors"><span class="header-section-number">3.1.1</span> Vectors</h3>
<p>When considering R data frames it is important to recall that they are composed of vectors. Even individual scalars and strings are vectors. This is a very powerful tool.</p>
<p>One important notion when handling vectors is the use of 'recycling'. As all elements are vectors, when performing an operation between two vectors of different length, R automatically repeats (or recycles) the shorter one until it is long enough.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image61.png" /><br /> In the previous example, (<code>u+v</code>) we add the elements of both vectors together. R automatically increases the length of <code>u</code> so that the operation becomes (1,2,3,4,5) + (0,1,0,1,0). In the second example we compare the elements of <code>v</code> to 4. R automatically increases the length of the vector containing 4 so that the operation becomes (1,2,3,4,5)&lt;(4,4,4,4,4) which returns a vector of size 5 with boolean (True or False) elements.</p>
<p>This second concept is important when understanding how to select certain variables in R (we saw this briefly in the previous section).</p>
<p>Another important notion in R is that of indexing. We can select elements of a vector by specifying the indices of the elements required:</p>
<pre><code>dwarfs&lt;-c(&quot;Dopey&quot;,&quot;Sneezey&quot;,&quot;Happy&quot;,&quot;Sleepy&quot;,&quot;Grumpy&quot;,&quot;Bashful&quot;,&quot;Doc&quot;)
dwarfs[c(1,4,5)]
dwarfs[3:length(dwarfs)]</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image23.png" /><br /> Both of the previous approaches use a vector of indices to indicate the elements we require. The second approach uses a shorthand to create a vector of elements (containing the integers 3 to 5). Another approach is to simply use a vector of boolean values (True or False) to indicate the positions that are to be selected.</p>
<pre><code>Index&lt;-c(TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,TRUE)
dwarfs[Index]</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image00.png" /><br /> It should be straightforward to realise that we can combine recycling and indexing to filter vectors:</p>
<pre><code>Index&lt;-substr(dwarfs,1,1)==&quot;D&quot;
dwarfs[Index]</code></pre>
<p>The first command creates an index set of boolean variables using the <code>substr</code> function and recycling (in this case used to take the first character of each element). This allows us to obtain the elements of the vector dwarfs with first letter <code>D</code> as shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image04.png" /><br /> We have seen how to subset vectors using filtering, the same logic applies to data frames.</p>
<p>We can first of all use indexing to obtain the variables we want. For example the following code will select the all the variables apart from the 4th and 5th:</p>
<pre><code>MMM[c(1,2,3,6,7,8)]</code></pre>
<p>A quicker way is to simply state the variables we want to drop:</p>
<pre><code>MMM[c(-4,-5)]</code></pre>
<p>The output of the above code is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image39.png" /><br /> We can also list the names of variables we want to keep:</p>
<pre><code>MMM[c(&quot;Name&quot;,&quot;Age&quot;,&quot;Sex&quot;,&quot;Home.Postcode&quot;,&quot;Savings.in.Pounds&quot;,&quot;Random.Number&quot;)]</code></pre>
<p>Finally we can create a vector of booleans that gives the same above result or the opposite result (i.e. drops the variables).</p>
<pre><code>Index&lt;-names(MMM) %in% c(&quot;Weight.in.Kg&quot;,&quot;Height.in.Metres&quot;)
MMM[Index]


Index&lt;-names(MMM) %in% c(&quot;Weight.in.Kg&quot;,&quot;Height.in.Metres&quot;)
MMM[!Index]</code></pre>
<p>Recall the <code>names</code> function simply gives a vector containing the names of all the variables in the MMM dataset. The <code>%in%</code> operator is used to create a vector of booleans by testing if the elements of names(MMM) are <code>in</code> the vector c(&quot;Weight.in.Kg&quot;,&quot;Height.in.Metres&quot;). The <code>!</code> operator acting on <code>Index</code> simply negates the booleans contained in Index.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image17.png" /><br /></p>
<h3 id="selecting-observations"><span class="header-section-number">3.1.2</span> Selecting Observations</h3>
<p>We can select any particular element of a data frame in R using the following syntax:</p>
<pre><code>dataframe[i,j]</code></pre>
<p>This would give the entry for variable j of observation i as shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image57.png" /><br /> If we ignore one of the indices R simply returns all the entries corresponding to that index. For example the following code would return all the observations for the 7th observation of the JJJ data set:</p>
<pre><code>JJJ[7,]</code></pre>
<p>We can also use this to sort a data set. The &quot;order function&quot; returns a set of indices reflecting the ascending order of a vector, thus to sort the JJJ data set by age we use the following code:</p>
<pre><code>JJJ[order(JJJ$Age),]</code></pre>
<p>We can use filtering to expand on this and select all observations that obey a particular condition. For example the following code selects entries of JJJ that have age less than or equal to 18:</p>
<pre><code>JJJ[JJJ$Age&lt;=18,]</code></pre>
<h2 id="merging-and-concatenating-data-sets"><span class="header-section-number">3.2</span> Merging and concatenating data sets</h2>
<p>To concatenate two data sets in R we use the <code>rbind</code> function (i.e. we bind the two dataframes by rows).</p>
<pre><code>MMMJJJ&lt;-rbind(JJJ,MMM)</code></pre>
<p>Note that both these data sets need to contain all the variables. If one of the datasets does not contain all the variables then you need to add that variable to it and set its values to NA (missing).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image26.png" /><br /> To merge two dataframes in R we use the merge function. We'll illustrate this with the following data set:</p>
<pre><code>Name&lt;-c(&quot;Bob&quot;,&quot;Ben&quot;)
Weight&lt;-c(75,94)
other_data_set&lt;-data.frame(Name,Weight)</code></pre>
<p>We'll merge this new data set with the data set we created in Chapter 1.</p>
<pre><code>merged_data_set&lt;-merge(first_data_set,other_data_set,&quot;Name&quot;)</code></pre>
<p>(or equivalently:)</p>
<pre><code>merged_data_set&lt;-merge(x=first_data_set,y=other_data_set,by=&quot;Name&quot;)</code></pre>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image35.png" /><br /> Note that the merge statement only selects observations that are present in both files. We can pass further arguments to the merge statement that allow us to select all the values from a particular data set and/or both data sets. These operations are at times called 'joins' (and are very common in SQL which we shall see in Chapter 5). The basic merge statement (as above) would be referred to as an 'inner' join.</p>
<p>A left outer join (selecting all variables from the first data set):</p>
<pre><code>merged_data_set&lt;-merge(first_data_set,other_data_set,&quot;Name&quot;,all.x=TRUE)</code></pre>
<p>A right outer join:</p>
<pre><code>merged_data_set&lt;-merge(first_data_set,other_data_set,&quot;Name&quot;,all.y=TRUE)</code></pre>
<p>A full outer join:</p>
<pre><code>merged_data_set&lt;-merge(first_data_set,other_data_set,&quot;Name&quot;,all=TRUE)</code></pre>
<p>The output of the above is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image51.png" /><br /></p>
<h2 id="creating-new-variables"><span class="header-section-number">3.3</span> Creating new variables</h2>
<p>Creating new variables using various arithmetic and/or string relationships is straightforward in R. The following code creates a new data set call MMM_with_BMI as a copy of the MMM data set and then adds a new variable &quot;BMI&quot; as a function of the height and weight variables in the MMM_with_BMI dataset.</p>
<pre><code>MMM_With_BMI&lt;-MMM
MMM_With_BMI$BMI&lt;-MMM$Weight.in.Kg/(MMM$Height.in.Metres^2)
MMM_With_BMI</code></pre>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image55.png" /><br /> The above code is quite long though, so we can use the <code>within</code> function which is similar to the <code>with</code> function. It lets R know you are working within a particular data frame.</p>
<pre><code>MMM_With_BMI &lt;- within(MMM, BMI &lt;- Weight.in.Kg/(Height.in.Metres^2))</code></pre>
<p>The output is shown:</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image18.png" /><br /> Some of the arithmetic functions available in R are shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/R_math_operators.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/R_math_functions.png" /><br /> We can also do operations on strings, the following code replaces the variable <code>Sex</code> with the first character of <code>Sex</code> (which gets rid of the Male - M and Female - F issue).</p>
<pre><code>MMM_With_BMI$Sex&lt;-substr(MMM_With_BMI$Sex,1,1)</code></pre>
<p>Some examples of string functions are shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/R_string_functions.png" /><br /></p>
<p>It's also worth checking the web for other R functions (there is a huge amount of them).</p>
<h3 id="renaming-variables"><span class="header-section-number">3.3.1</span> Renaming variables</h3>
<p>To rename variables one can use the <code>rename</code> function from the <code>reshape</code> library (that can be installed as we have seen in previous section).</p>
<pre><code>library(reshape)
JJJ&lt;-rename(JJJ,c(Sex=&quot;Gender&quot;))</code></pre>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image06.png" /><br /> Another option is to use the &quot;fix&quot; function that opens the dataset in a GUI that easily allows for modification of the dataset (including the name of the variables). Note that changes are saved on close of the fix environment.</p>
<pre><code>fix(JJJ)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image25.png" /><br /></p>
<h3 id="operations-across-rows"><span class="header-section-number">3.3.2</span> Operations across rows</h3>
<p>As discussed previously, the columns of a data frame can be manipulated very easily as they are just vectors. In the next section we will see how to manipulate vectors using flow control statements but we will take a quick look at two functions that allow for quick and easy manipulation across rows.</p>
<p>We will demonstrate this using the birthday_money.csv data set as shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image65.png" /><br /> Suppose we want to take a cumulative sum of the birthday money, we create a new variable call total using the <code>cumsum</code> function that returns the cumulative sum of elements of a vector.</p>
<pre><code>birthday_money$total&lt;-cumsum(birthday_money$Amount)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image36.png" /><br /> Another similar tool is to use the &quot;diff&quot; function that calculates consecutive differences of elements of a vector:</p>
<pre><code>birthday_money$yearly_diff&lt;-c(NA,diff(birthday_money$Amount))</code></pre>
<p>Note that we also include a first entry of our column &quot;yearly_diff&quot; as &quot;NA&quot;, this is because the output of diff will be shorter than the length of the original vector.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image56.png" /><br /></p>
<h2 id="handling-dates-in-r"><span class="header-section-number">3.4</span> Handling dates in R</h2>
<p>Dates are a particular class in R. When importing dates, they are imported as strings.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image14.png" /><br /> We import the file and create a data frame in the usual way:</p>
<pre><code>birthdays&lt;-read.csv(&quot;~/birthdays.csv&quot;)</code></pre>
<p>Using the &quot;str&quot; command to view the structure of our data frame:</p>
<pre><code>str(birthdays)</code></pre>
<p>The output is shown confirming that the dates are recognized as strings (recall that by default <code>read.csv</code> imports strings as <code>factors</code>).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image48.png" /><br /> In this current format if we tried to carry out any mathematical manipulation of the dates we would not succeed. We can however tell R that certain variables are dates. We do this using the &quot;as.dates&quot; function by describing the format our dates are in:</p>
<pre><code>birthdays$Birthday&lt;-as.Date(birthdays$Birthday,&quot;%d/%m/%Y&quot;)</code></pre>
<p>The format is indicated using &quot;%x&quot; where &quot;x&quot; can be of various formats as show.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/R_date_formats.png" /><br /> We'll now check the structure of our data frame, re-order (using the <code>order</code> function - that returns the indices of the elements of a vector in order) our birthdays and calculate the difference between birthdays (using the <code>diff</code> function).</p>
<pre><code>str(birthdays$Birthday)
order(birthdays$Birthday)
sorted&lt;- birthdays[order(birthdays$Birthday),]
diff(birthdays$Birthday[order(birthdays$Birthday)])</code></pre>
<p>The output of all this is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image02.png" /><br /></p>
