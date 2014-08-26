---
layout      : post
categories  : content
title       : SAS Chapter 5 - Further packages
comments    : true
---

<p>In this chapter we will examine three particular procedures in SAS.</p>
<ol style="list-style-type: decimal">
<li>proc sql: a procedure allowing for the use of sql syntax in SAS;</li>
<li>proc fcmp: a procedure allowing for the creation of custom functions;</li>
<li>proc optmodel: a package that allows for optimisation in SAS.</li>
</ol>
<h2 id="proc-sql"><span class="header-section-number">5.1</span> Proc sql</h2>
<h3 id="basic-sql"><span class="header-section-number">5.1.1</span> Basic SQL</h3>
<p>SQL is a language designed for querying and modifying databases. Used by a variety of database management software suites:</p>
<ol style="list-style-type: decimal">
<li>Oracle</li>
<li>Microsoft ACCESS</li>
<li>SPSS</li>
</ol>
<p>SQL uses one or more objects called TABLES where: rows contain records (observations) and columns contain variables. Importantly,</p>
<ol style="list-style-type: decimal">
<li>Starts with proc sql; (as expected)</li>
<li>Ends with quit; (some interactive procedures do)</li>
</ol>
<p>The following code creates a data set called test in the work library as a copy of the mat013.mmm data set:</p>
<pre><code>proc sql;
create table test as
select *
from mat013.mmm;
quit;</code></pre>
<p>The &quot;*&quot; command tells SAS to take all variables from mat013.mmm. We can however specify exactly what variables we want:</p>
<pre><code>proc sql;
create table test as
select Name, Age, Sex
from mat013.mmm;
quit;</code></pre>
<p>We can also create new variables:</p>
<pre><code>proc sql;
create table test as
select Name, Age, Sex, weight_in_kg/(height_in_metres**2) as bmi
from mat013.mmm;
quit;</code></pre>
<h3 id="further-sql"><span class="header-section-number">5.1.2</span> Further SQL</h3>
<p>In this section we'll take a look at what else SAS can do. For the purpose of the following examples let's write a new data set:</p>
<pre><code>data mat013.example;
input Var1 $ Var2 Var3 $ Var 4 Var5 $;
cards;
A 1 A 2 B
A 1 A 2 B
B 1 A 1 C
C 2 B 2 D
C 2 C 1 E
;
run;</code></pre>
<p>Some simple SQL code very easily helps us to get rid of duplicate rows (this can be very helpful when handling real data). To do this we use the &quot;distinct&quot; keyword.</p>
<pre><code>proc sql;
create table example as
select distinct *
from mat013.example;
quit;</code></pre>
<p>We can also select particular variables:</p>
<pre><code>proc sql;
create table example as
select distinct var1, var2, var3
from mat013.example;
quit;</code></pre>
<p>We can also use the &quot;where&quot; statement to select variables that obey a particular condition:</p>
<pre><code>proc sql;
create table example as
select *
from mat013.example
where var2&lt;=var4;
quit;</code></pre>
<p>We can sort data sets using the &quot;order by&quot; keyword:</p>
<pre><code>proc sql;
create table example as
select distinct *
from mat013.example
order by var1;
quit;</code></pre>
<p>A very nice application of SQL is in the aggregation of summary statistics. The following code creates a new variable that gives the average value of var2. The value of this variable is the same for all the observations:</p>
<pre><code>proc sql;
create table example as
select * mean(var2) as average_of_var2
from mat013.example;
quit;</code></pre>
<p>We could however get something a bit more useful by aggregating the data using a &quot;group&quot; statement:</p>
<pre><code>proc sql;
create table example as
select var1, mean(var2) as average_of_var2
from mat013.example
group by var1;
quit;</code></pre>
<h3 id="joining-tables-with-sql"><span class="header-section-number">5.1.3</span> Joining tables with SQL</h3>
<p>A very common use of SQL within SAS is to carry out &quot;joins&quot; which are equivalent to a merger of data sets. There are 4 types of joins to consider:</p>
<ol style="list-style-type: decimal">
<li>inner join
<ol style="list-style-type: decimal">
<li>output table only contains rows common to all tables</li>
<li>variable attributes taken from left most table</li>
</ol></li>
<li>outer join left
<ol style="list-style-type: decimal">
<li>output table contains all rows contributed by the left table</li>
<li>variable attributes taken from left most table</li>
</ol></li>
<li>outer join right
<ol style="list-style-type: decimal">
<li>output table contains all rows contributed by the right table</li>
<li>variable attributes taken from right most table</li>
</ol></li>
<li>outer join full
<ol style="list-style-type: decimal">
<li>output table contains all rows contributed by all tables</li>
<li>variable attributes taken from left most table</li>
</ol></li>
</ol>
<p>To work with these examples let's use the data sets created with the following code:</p>
<pre><code>data mat013.dogs;
input Owner $ Name $;
cards;
Jeff Ruffus
Janet Sam
Paul .
Joanna .
;
run;

data mat013.cats;
input Owner $ Name $;
cards;
Jeff Kitty
Paul .
Joanna Tinkerbell
Vince Chick
;
run;</code></pre>
<p>The following code carries out an inner join of these two datasets also changing the name of the &quot;Name&quot; variable depending on which data set it was from, the output of which is shown.</p>
<pre><code>proc sql;
create table merged_table as
select a.Owner,a.Name as Dog_Name, b.Name as cat_Name
from mat013.dogs as a, mat013.cats as b
where a.Owner=b.Owner;
quit;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image23.png" /><br /> The following code carries out a left outer join, the output of which is shown.</p>
<pre><code>proc sql;
create table merged_table as
select a.Owner,a.Name as Dog_Name, b.Name as cat_Name
from mat013.dogs as a
left join mat013.cats as b
on a.Owner=b.Owner;
quit;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image46.png" /><br /> The following code carries out a right outer join, the output of which is shown.</p>
<pre><code>proc sql;
create table merged_table as
select a.Owner,a.Name as Dog_Name, b.Name as cat_Name
from mat013.dogs as a
right join mat013.cats as b
on a.Owner=b.Owner;
quit;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image07.png" /><br /> The following code carries out a full outer join, the output of which is shown.</p>
<pre><code>proc sql;
create table merged_table as
select a.Owner,a.Name as Dog_Name, b.Name as cat_Name
from mat013.dogs as a
full join mat013.cats as b
on a.Owner=b.Owner;
quit;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image33.png" /><br /></p>
<h2 id="proc-fcmp"><span class="header-section-number">5.2</span> Proc fcmp</h2>
<p>In previous chapters we have seen various in built functions in SAS. For various reasons it might be required to create a custom function. We will do this with the &quot;fcmp&quot; procedure. This procedure allows us to create custom functions using data step syntax (which allows for &quot;if&quot; and &quot;do&quot; statements to be used). The following code creates a function called &quot;ln&quot; that gives the natural log of a number:</p>
<pre><code>proc fcmp outlib=sasuser.funcs.ln;
function ln(x);
y=log(x);
return(y);
endsub;
quit;</code></pre>
<p>This code in fact creates a function named &quot;ln&quot; in a package named &quot;funcs&quot;. The package is stored in the data set sasuser.funcs. To use this function we need to tell SAS which data set contains the function. We do this with the following piece of code:</p>
<pre><code>option cmplib=sasuser.funcs;</code></pre>
<p>It is then straightforward to call this function:</p>
<pre><code>option cmplib=sasuser.funcs;
data test;
x=5;
y=log(x);
new_Y=ln(x);
run;</code></pre>
<p>The main advantage to using this procedure is that we can include complex data step syntax. The following function takes two inputs and gives a geometric sum:</p>
<pre><code>proc fcmp outlib=sasuser.funcs.Gsum;
function Gsum(i,n);
s=0;
do k=0 to n;
s=s+i**k;
end;
return(s);
endsub;
quit;</code></pre>
<p>Let's test this on the following data set:</p>
<pre><code>data test;
input n i;
cards;
1 1
2 1
3 2
4 2
5 2
6 2
;
run;

data G_sum_test;
set test;
y=Gsum(i,n);
run;</code></pre>
<h2 id="optimisation"><span class="header-section-number">5.3</span> Optimisation</h2>
<p>Another powerful aspect of SAS is it's optimisation engine. We can optimise various types of problems using the &quot;optmodel&quot; procedure. The following code optimises the polynomial: \(x^2-x-yx+y^2\).</p>
<pre><code>proc optmodel;
var x,y;
min z=x**2-x-2*y-x*y+y**2;
solve;
print x y;
quit;</code></pre>
<p>The output is shown, note that SAS automatically chooses a solver (in this case Non Linear Programming and Interior Point methods).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image27_opt.png" /><br /> We can also include a domain:</p>
<pre><code>proc optmodel;
var x&lt;=0,y&gt;=2;
min z=x**2-x-2*y-x*y+y**2;
solve;
print x y;
quit;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image22_opt.png" /><br /> We can solve further more complex optimisation problems, including constraints using the 'constraints' keyword:</p>
<pre><code>proc optmodel;
var x1&gt;=0, x2&gt;=0, x3&gt;=0;
max f=x1+x2+x3;
constraint c1: 3*x1+2*x2-x3&lt;=1;
constraint c2: -2*x1-3*x2+2*x3&lt;=1;
solve;
print x1 x2 x3;
quit;</code></pre>
<p>The output is shown (note the solver used was a variant of simplex).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image11_opt.png" /><br /></p>
<p>It is also possible to read in the constraints of a particular optimisation problem from a data set. This can prove to be very handy when dealing with huge problems so it's worth spending time researching that approach.</p>
<p>(Other versions of the above: <a href="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/MAT013AdvanceduseofstatisticalpackagesSAS.pdf">pdf</a> <a href="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/MAT013AdvanceduseofstatisticalpackagesSAS.docx">docx (not recommended)</a>)</p>
