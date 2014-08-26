---
layout      : post
categories  : content
title       : R Chapter 4 - Programming
comments    : false
---

<h2 id="flow-control"><span class="header-section-number">4.1</span> Flow Control</h2>
<p>A huge part of programming (in any language) is the use of so called &quot;conditional statements&quot; that allow for flow control. We do this in R using &quot;if&quot; statements.</p>
<p>There are two types of &quot;if&quot; statements in R. The simple &quot;if&quot; statement as shown below:</p>
<pre><code>x&lt;-39
if (x&gt;20) y&lt;-1</code></pre>
<p>We can use this in conjunction with an &quot;else&quot; statement:</p>
<pre><code>x&lt;-19
if (x&gt;20) y&lt;-1 else y&lt;-0</code></pre>
<p>Finally, the if-else call is a function and as such we can rewrite the above code as:</p>
<pre><code>y&lt;- if (x&gt;20) 1 else 0</code></pre>
<p>Finally we can include multiple commands as outcomes of an if statement by using &quot;{}&quot;:</p>
<pre><code>x&lt;-20
if (x==21) {
y&lt;-1
z&lt;-&quot;T&quot;
} else{
y&lt;-0
z&lt;-&quot;F&quot;}</code></pre>
<p>The above statements checks a single value and whilst we'll learn in the next section how to loop offer sets of values it is very much worth learning how to use the 'vectorized' form of the if statement: the &quot;ifelse&quot; command. The general syntax is given below:</p>
<pre><code>ifelse(Boolean_Vector,Outcome_If_True,Outcome_If_False)</code></pre>
<p>An example of this is given below:</p>
<pre><code>ifelse(c(&quot;True&quot;,&quot;False&quot;,&quot;True&quot;,&quot;False&quot;),&quot;Young&quot;,&quot;Old&quot;)</code></pre>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image01.png" /><br /></p>
<p>Using this and our knowledge of filtering we see how we can create new variables using the ifelse statement. The following code creates a new variable &quot;age_group&quot;:</p>
<pre><code>MMMJJJ$Age_group&lt;-ifelse(MMM$Age&lt;30,&quot;Young&quot;,&quot;Old&quot;)
MMMJJJ[c(&quot;Name&quot;,&quot;Age_group&quot;)]</code></pre>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image67.png" /><br /></p>
<p>Some of the comparison operators that can be used in conjunction with 'if' statements are shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/R_comparison_operators.png" /><br /></p>
<p>A further important notion in programming is the notion of loops. There are two types of loops that we will consider:</p>
<ol style="list-style-type: decimal">
<li>for</li>
<li>while</li>
</ol>
<p>The for loop allows us to compute iterative procedures. As with most things in R, the for loop iterates a value over a vector. The following code outputs the total number of birthday candles that would have been used on everyones birthday cake in the JJJ data set.</p>
<pre><code>Candles=c()
for (Age in JJJ$Age){
c&lt;-0
for (n in 0:Age){
c&lt;-c+n
}
Candles&lt;-c(Candles,c)
}
Candles&lt;-data.frame(Name=JJJ$Name,Age=JJJ$Age,Candles)</code></pre>
<p>The first statement creates an empty vector called &quot;Candles&quot;. The first for loop, loops over the age variable in the JJJ data set (&quot;0:age&quot; is in fact a short way of writing a vector of integers from 0 to age). For each of those values of age we use a second for loop to sum the total number of candles and concatenate that value to the vector Candles. Finally we create a new data set Candles by concatenating the various vectors required (note that we're also renaming certain variables here).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image10.png" /><br /> Note that in general this is not the most efficient way of undertaking things in R. Vectorized versions of the above are much faster (we won't cover these here). Another improvement for the above code is to create the vector Candles initially as a vector of the correct size and type. For example we can create a numeric vector of a certain length using the following code (all initial values will be set to 0):</p>
<pre><code>Candles=vector(&quot;numeric&quot;,length=length(JJJ$Age))</code></pre>
<p>Using this the above code would be written as:</p>
<pre><code>Candles=vector(&quot;numeric&quot;,length=length(JJJ$Age))
k&lt;-0
for (Age in JJJ$Age){
k&lt;-k+1
c&lt;-0
for (n in 0:Age){
c&lt;-c+n
}
Candles[k]&lt;-c
}
Candles&lt;-data.frame(Name=JJJ$Name,Age=JJJ$Age,Candles)</code></pre>
<p>The second type of loop we will consider is the do while loop. This loop checks a condition before carrying out an operation. The following code creates a vector with all even numbers less than 70:</p>
<pre><code>k&lt;-0
even&lt;-2*k
even_numbers&lt;-c(even)
while(even&lt;70){
k&lt;-k+1
even&lt;-2*k;
even_numbers&lt;-c(even_numbers,even)
}</code></pre>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image21.png" /><br /></p>
<h2 id="functions"><span class="header-section-number">4.2</span> Functions</h2>
<p>One of the great capacities of R is the ease with which one can create new functions. The general syntax for this is given by:</p>
<pre><code>myfunction &lt;- function(arg1, arg2, ... ){
statements
return(object)
}</code></pre>
<p>The return statement is very important as it indicates the &quot;result&quot; of the function. This can be any R object, a vector, a data frame etc... Note that is can also be omitted, as long as the last command is what you want returned.</p>
<p>The following code creates a function called &quot;f1&quot; that adds 3 to a number if it is even and adds 2 to a number if it is odd.</p>
<pre><code>f1 &lt;- function(x){
r &lt;- if (x%%2==0) x+3 else x+2
return(r)
}</code></pre>
<p>To run the function we would then use it like any other R function. For example the following would return 11.</p>
<pre><code>f1(9)</code></pre>
<p>(The %% command return the modulo of the first number with respect to the second)</p>
<p>We can also create a function with no arguments that simply replicates shorthand for some code:</p>
<pre><code>My_plot &lt;- function(){
r&lt;-hist(JJJ$Height.in.Metres)
return(r)
}

My_plot()</code></pre>
<p>The following code defines a function that creates a new dataset entitled &quot;JJJ_after_shopping&quot; that subtracts a quantity from the savings variable in the JJJ dataset:</p>
<pre><code>shopping &lt;- function(spend){
New.Savings&lt;-JJJ$Savings.in.Pounds-spend
JJJ_after_shopping&lt;-data.frame(JJJ$Name,Old.Savings=JJJ$Savings.in.Pounds,New.Savings)
return(JJJ_after_shopping)
}</code></pre>
<p>Note that this function makes use of recycling (when creating the New.Savings vector).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image12.png" /><br /> We can of course define functions with multiple arguments as below:</p>
<pre><code>shopping &lt;- function(spend,trips){
New.Savings&lt;-JJJ$Savings.in.Pounds-trips*spend
JJJ_after_shopping&lt;-data.frame(JJJ$Name,Old.Savings=JJJ$Savings.in.Pounds,New.Savings)
return(JJJ_after_shopping)
}</code></pre>
<p>It's also possible to set certain values as defaults:</p>
<pre><code>shopping &lt;- function(spend,trips=1){
New.Savings&lt;-JJJ$Savings.in.Pounds-trips*spend
JJJ_after_shopping&lt;-data.frame(JJJ$Name,Old.Savings=JJJ$Savings.in.Pounds,New.Savings)
return(JJJ_after_shopping)
}</code></pre>
<h2 id="vectorising"><span class="header-section-number">4.3</span> Vectorising</h2>
<p>In general the for loops we have seen can be written in a much more efficient way using function and various forms of the apply function (which apply functions over vectors, lists and matrices):</p>
<ol style="list-style-type: decimal">
<li>apply</li>
<li>lapply</li>
<li>sapply</li>
<li>mapply</li>
</ol>
<p>Note that an array in R is a very generic data type; it is a general structure of up to eight dimensions. For specific dimensions there are special names for the structures. A zero dimensional array is a scalar or a point; a one dimensional array is a vector; and a two dimensional array is a matrix. The general syntax of the apply function is given below:</p>
<pre><code>apply(matrix,margin,function)</code></pre>
<p>We have not yet seen matrices but they are relatively simple to understand: 2 dimensional objects. The following code produces a 2 by 3 matrix:</p>
<pre><code>mat&lt;-matrix(c(1,2,3,4,5,6),2,3)
mat</code></pre>
<p>The &quot;margin&quot; option (either 1,2 or both (1:2)) simply tells R what dimension to apply the required function to, experiment with the following:</p>
<pre><code>apply(mat,1,mean)
apply(mat,2,mean)
apply(mat,1:2,mean)</code></pre>
<p>We can use the apply function on data frames and vectors but in general it will be easier to use the &quot;lapply&quot; function which simply applies a function to a 1 dimensional object. The lapply function becomes especially useful when dealing with data frames. In R the data frame is considered a list and the variables in the data frame are the elements of the list. We can therefore apply a function to all the variables in a data frame by using the lapply function. Note that unlike in the apply function there is no margin argument since we are just applying the function to each component of the list. The following code simply returns the sqaure roots of a vector.</p>
<pre><code>lapply(c(1,2,3,4,5),sqrt)</code></pre>
<p>Note that the above returns a list (an R object that we will not pay much attention to here). We can get a vector by using the following:</p>
<pre><code>unlist(lapply(c(1,2,3,4,5),sqrt))</code></pre>
<p>The &quot;sapply&quot; function is simply a version of lapply that by default returns the most appropriate object type. The following code gives the exact same result as above:</p>
<pre><code>sapply(c(1,2,3,4,5),sqrt)</code></pre>
<p>Finally, there exists a multivariate example of the above function which allows us to pass multiple arguments to a function. The following code defines a simple function:</p>
<pre><code>simple_function&lt;-function(x,y) x/y</code></pre>
<p>We can now apply this function so that it takes the consecutive ratios of two vectors:</p>
<pre><code>mapply(simple_function,1:4,4:1)</code></pre>
<p>With these functions we can drastically improve the performance of R code. The following reproduces code from before:</p>
<pre><code>my_sum&lt;-function(x){
sum(x)
}

sapply(JJJ$Age,my_sum(1:x))</code></pre>
<p>Note that there is no need to actually define the function we can refer directly to the function object:</p>
<pre><code>sapply(JJJ$Age,function(x) sum(1:x))</code></pre>
<h2 id="handling-strings"><span class="header-section-number">4.4</span> Handling strings</h2>
<p>SAS is a macro language and philosophically macros allow a user to substitute pieces of text for a variable, and evaluate the result. R is not a macro language and thus does the opposite: evaluates the arguments and then uses the values.</p>
<p>The paste command allows us to concatenate strings. The following code outputs the string &quot;Hello-World&quot;. Note that we can use any string as a separator (include the empty string &quot;&quot;).</p>
<pre><code>x&lt;-&quot;Hello&quot;
paste(x,&quot;World&quot;,sep=&quot;-&quot;)</code></pre>
<p>This immediately allows for quite complex manipulation of data files. For example the following code, imports the 5 datafiles File_1.csv - File_5.csv:</p>
<pre><code>f&lt;-function(i){read.csv(paste(&quot;File_&quot;,i,&quot;.csv&quot;,sep=&quot;&quot;))}
dat&lt;-lapply(1:5,f)</code></pre>
<p>Note that this piece of code introduces a new structure a bit more formally. The object &quot;dat&quot; is here a list and we use the &quot;lappy&quot; function (we haven't seen this yet) to apply the newly created function &quot;f&quot; (that imports data).</p>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image41.png" /><br /> We can also revisit a previous function (the shopping function) and create a different data set for every value of spend. We'll even make this a bit more complicated and nest functions so that we can repeat this operation for various values of the variable &quot;spend&quot;.</p>
<pre><code>shopping &lt;- function(spend,trips=1){
New.Savings&lt;-JJJ$Savings.in.Pounds-trips*spend
infile&lt;-paste(&quot;JJJ_after_shopping_&quot;,trips,sep=&quot;&quot;)
data_frame&lt;-data.frame(JJJ$Name,Old.Savings=JJJ$Savings.in.Pounds,New.Savings)
assign(infile,data_frame,envir=.GlobalEnv)
}

multiple_shopping&lt;- function(spend,max_trips=10){

for (i in 1:max_trips){
shopping(spend,i)
}
}</code></pre>
<p>Note the extra option that has been passed to the &quot;assign&quot; command &quot;envir=.GlobalEnv&quot;. This is to ensure that the data sets created in the function are global (i.e. are still there when the function stops running).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image40.png" /><br /></p>
<h2 id="memory-and-scripts."><span class="header-section-number">4.5</span> Memory and scripts.</h2>
<p>In this section we will take a brief look at how R handles the &quot;workspace&quot;. If you have already quit R you would have seen the prompt &quot;Save workspace image?&quot;. If you answer &quot;yes&quot; then R saves various things to various files (in the current working directory): 1. .Rdata holds all the objects (data frames, vectors, functions etc...) currently in memory (note that this file is written in an R specific file and so can't be read). 2. .Rhistory holds all the commands used (and so can be recalled).</p>
<p>Being prompted whether or not to save the workspace is helpful (in my opinion) as you can simply open an R session to try a few things and not save (similar to using the work library in SAS). It is possible to save the workspace image as you go (this is worthwhile in case your system happens to crash):</p>
<pre><code>save.image()</code></pre>
<p>Note: we can leave the argument of the &quot;image&quot; function empty (as above), in which case the file will be saved in the current directory. We can also pass the required location to the &quot;image&quot; function.</p>
<p>It is also possible to save particular objects to particular files as well as load files but we won't go into that here.</p>
<p>One final aspect to consider is that of running script files from the command line. We do this using the &quot;source&quot; command. Note that this command executes all the code in the script as if it was typed in one after the other. To see this let us write the following code in a text file (saving it as &quot;first_script.r&quot; on the desktop for example):</p>
<pre><code>x&lt;-c(1,2,3,4)
y&lt;-c(1,0)
print(x+y)
print(x*y)</code></pre>
<p>We then run the script using the following code:</p>
<pre><code>source(&quot;~/Desktop/first_script.r&quot;)</code></pre>
<p>Repetitive command that are run often (for example, routine data analysis) can be saved as scripts and called if and when new data is received.</p>
