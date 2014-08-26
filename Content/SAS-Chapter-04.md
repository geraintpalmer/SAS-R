---
layout      : post
categories  : content
title       : SAS Chapter 4 - Programming
comments    : true
---

<h2 id="flow-control"><span class="header-section-number">4.1</span> Flow control</h2>
<p>A huge part of programming (in any language) is the use of so called &quot;conditional statements&quot;. We do this in SAS using &quot;if&quot; statements. The following code creates a new variable &quot;age_group&quot; which is &quot;young&quot; if the age is less than 29 and &quot;old&quot; if the age is larger than 29. Note we're also including a keep statement to just have the name and age_group in the new data set.</p>
<pre><code>data age_group(keep= name age_group);
set mat013.mmmjjj;
if age&lt;30 then age_group=&#39;young&#39;;
    else age_group=&#39;old&#39;;
run;</code></pre>
<p>We can also use this in conjunction with the else if statement as shown below:</p>
<pre><code>data age_group(keep= name age_group);
set mat013.mmmjjj;
if age&lt;18 then age_group=&#39;child&#39;;
    else if age&lt;30 then age_group=&#39;young&#39;;
        else age_group=&#39;old&#39;;
run;</code></pre>
<p>Note that we can also compare strings as shown with the following code:</p>
<pre><code>data age_group(keep= name age_group);
set mat013.mmmjjj;
if age&lt;18 then age_group=&#39;child&#39;;
    else if age&lt;30 then age_group=&#39;young&#39;;
        else age_group=&#39;old&#39;;
if substr(Name,1,1)=&#39;J &#39; then data_set=&#39;JJJ&#39;;
    else data_set=&#39;MMM&#39;;
run;</code></pre>
<p>Here are some of the comparison operators that can be used in conjunction with 'if' statements.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image29.png" /><br /> A further important notion in programming is the notion of loops. These are done in SAS using &quot;do&quot; statements. There are four ways the &quot;do&quot; statement is used:</p>
<ol style="list-style-type: decimal">
<li>do</li>
<li>do (iterative)</li>
<li>do while</li>
<li>do until</li>
</ol>
<p>The first use allows us to combine several statement into one. This is often used in conjunction with &quot;if&quot; statements:</p>
<pre><code>data age_group(keep= name age_group minor_Y_N);
set mat013.mmmjjj;
if age&lt;18 then do;
age_group=&#39;Child&#39;;
minor_Y_N=&#39;Y&#39;;
end;
else do;
age_group=&#39;Adult&#39;;
minor_Y_N=&#39;N&#39;;
end;
run;</code></pre>
<p>The 'do' statement can be used to push your computer a bit more. The &quot;do iterative statement&quot; allows you to automate various procedures. The following code output the total number of birthday candles that would have been used on everyones birthday cake in the JJJ data set.</p>
<pre><code>data candles(keep= name age candles);
set mat013.jjj;
candle=0;
do k=0 to age;
candle=candle+k;
end;
run;</code></pre>
<p>The last two uses of the 'do' statement are very similar and allow us to iterate &quot;until/while&quot; a particular condition is met.</p>
<p>The do until (expression) statement executes a group of statements until the expression within the brackets is satisfied. The validity of the expression is checked at the end of each loop.</p>
<pre><code>do until (expression);
data step commands;
end;</code></pre>
<p>The following code outputs the number of even numbers less than or equal to 70, computing each even number and checking whether or not it is more than 70.</p>
<pre><code>data even_numbers;
k=0;
even=0;
do until(even&gt;=70);
even=2**k;
k=k+1;
end;
run;</code></pre>
<p>We can do a similar calculation using the do &quot;while&quot; statement. The do while (expression) statement executes a group of statements whilst the expression within the brackets is satisfied. The validity of the expression is checked at the beginning of each loop.</p>
<pre><code>do while (expression);
data step commands;
end;

data even_numbers;
k=0;
even=0;
do while(even&lt;70);
even=2**k;
k=k+1;
end;
run;</code></pre>
<p>Note that do iterative statements (also called &quot;do loops&quot;) are often used in conjunction with the &quot;output&quot; statement which empties the pdv to the output data set. The following code outputs the variables in the pdv: &quot;k&quot; and &quot;even&quot; at each iteration of the do statement. The output is shown.</p>
<pre><code>data even_numbers;
k=0;
even=0;
do while(even&lt;70);
even=2**k;
output;
k=k+1;
end;
run;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image18.png" /><br /></p>
<h2 id="how-does-sas-compile-code"><span class="header-section-number">4.2</span> How does SAS compile code?</h2>
<p>In this chapter we will see how to program macros in SAS. Macros generate and run code with varying arguments. The macro facility is a tool for extending and customising SAS and for reducing the amount of text you must enter to do common tasks. The macro facility enables you to assign a name to character strings or groups of SAS programming statements. From that point on, you can work with the names rather than with the text itself.</p>
<p>When you submit a SAS macro the Input stack receives content of the program. Word scanner scans each line of the macro for tokens. If a token contains a macro character (a % or a &amp;) that token is sent to the macro compiler. The Macro compiler does its work and places tokens back in the input stack. The token is examined by the word scanner and the process repeats. When the word scanner detects a step boundary it triggers the data step compiler. This process is represented diagrammatically.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image48.png" /><br /> When you submit a macro, it goes first to the macro processor which produces standard SAS code from the macro references (macro code is compiled first). Then SAS compiles and executes your program.</p>
<p>In general the syntax for a macro is as follows:</p>
<pre><code>%macro macro-name &lt;(macro-parameter-list&gt;;

… SAS Code...

%mend &lt;macro-name&gt;;</code></pre>
<p>The following example creates a macro called &quot;My_plot&quot; which when called will plot a graph of height against weight of the variables in mat013.jjj:</p>
<pre><code>%macro My_plot;
proc gplot data=mat013.jjj;
plot height_in_metres*weight_in_kg;
run;
%mend;</code></pre>
<p>To run the macro we call it with the following statement:</p>
<pre><code>%My_plot;</code></pre>
<p>As discussed above, it is possible to pass arguments to a macro. The following code creates a macro &quot;shopping&quot; that will remove a certain quantity &quot;spend&quot; from the variable &quot;life_savings&quot;:</p>
<pre><code>%macro shopping(spend);
data JJJ_after_shopping(keep= Name Old_savings New_savings);
set mat013.jjj;
Old_savings=savings_in_pounds;
New_savings=saving_in_pounds-&amp;spend;
run;
%mend;</code></pre>
<p>Note the ampersand &quot;&amp;&quot; which the &quot;word scanner&quot; will recognise, sending &quot;&amp;spend&quot; to the &quot;macro compiler&quot; where it will resolve to whatever value is passed to the macro.</p>
<p>We can define macros with multiple variables. Consider the following modification of the above code which allows for multiple shopping trips:</p>
<pre><code>%macro shopping(spend,trips);
data JJJ_after_shopping(keep= Name Old_savings New_savings);
set mat013.jjj;
Old_savings=savings_in_pounds;
New_savings=saving_in_pounds-&amp;trips*&amp;spend;
run;
%mend;</code></pre>
<p>The above code is using so called &quot;positional&quot; macro parameters. It is possible to also use &quot;keyword&quot; macro parameters as shown in the code below.</p>
<pre><code>%macro shopping(spend=,trips=);
data JJJ_after_shopping(keep= Name Old_savings New_savings);
set mat013.jjj;
Old_savings=savings_in_pounds;
New_savings=saving_in_pounds-&amp;trips*&amp;spend;
run;
%mend;</code></pre>
<p>We can then call the above macro and change the order of the parameters:</p>
<pre><code>%shopping(trips=2,spend=500);</code></pre>
<p>It's also possible to set default values:</p>
<pre><code>%macro shopping(spend=,trips=1);
data JJJ_after_shopping(keep= Name Old_savings New_savings);
set mat013.jjj;
Old_savings=savings_in_pounds;
New_savings=saving_in_pounds-&amp;trips*&amp;spend;
run;
%mend;</code></pre>
<p>Now if we call the macro without giving a value to trips it will take the default value 1.</p>
<pre><code>%shopping(spend=500);</code></pre>
<h3 id="macro-variables"><span class="header-section-number">4.2.1</span> Macro variables</h3>
<p>In this section we're going to take a slightly closer look at macro variables. A macro variable is a variable whose value is stored within the macro symbol table. When the macro variable is used in SAS code, SAS substitutes the value of the macro variable into the SAS code. SAS macro variables are distinguished by the &quot;&amp;&quot; sign before the variable name. Note that all SAS macro variables are stored as text strings.</p>
<p>We can experiment with macro variables using the %let statement which allows the construction of macro variables outside of a macro definition. This is the simplest form of a macro statement. It can be placed anywhere in a program, not only inside a Macro. &quot;%let&quot; creates global macro variables. An example of this is shown in the following code which gives the output shown.</p>
<pre><code>%let spend=400;
%let trips=500;

%macro shopping;
data JJJ_after_shopping(keep= Name Old_savings New_savings);
set mat013.jjj;
Old_savings=savings_in_pounds;
New_savings=saving_in_pounds-&amp;trips*&amp;spend;
run;
%mend;

%shopping;</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image52.png" /><br /> It's also possible to view (in the log) the values of a macro variable using the &quot;%put&quot; statement. There are two uses for it:</p>
<pre><code>%put &lt;text&gt; &amp;macro-variable-name;</code></pre>
<p>This outputs some <text> (optional) followed by the value of particular macro variable. The other use is shown below:</p>
<pre><code>%put  &lt;_all_ | _global_ | _local_ &gt;;</code></pre>
<p>This will output either all, all the global or all the local macro variables. These statements should allow us to better understand some of the issues related to the resolution of multiple ampersands. Multiple ampersands can be used to allow the value of a macro variable to become another macro variable reference. The macro variable reference will be rescanned until the macro variable is resolved. There are 2 rules to follow:</p>
<ol style="list-style-type: decimal">
<li>&amp;&amp; is a token in its own right and resolves to &amp;</li>
<li>Each token is handled independently</li>
</ol>
<p>The important thing to note here is that a double ampersand &quot;&amp;&amp;&quot; is a token in itself that resolves to a single ampersand &quot;&amp;&quot; (THIS IS IMPORTANT).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image44.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image43.png" /><br /></p>
<h2 id="sas-macro-programming-statements"><span class="header-section-number">4.3</span> SAS Macro programming statements</h2>
<p>The 'if' statements and 'do' loops discussed previously work in a very similar way to if statements and do loops within macros. The only modification is that these can be evaluated within the macro compiler before the entire submitted code is resolved. For this to work we need to use the &quot;%if&quot;, &quot;%then&quot; and &quot;%else&quot; statements when evaluating a conditional statement on a macro variable. The following code is an example of this:</p>
<pre><code>%macro shopping(spend,trips);
data JJJ_after_shopping(keep= Name Old_savings New_savings);
set mat013.jjj;
%if &amp;spend&lt;0 %then %put Carefull the spend is negative!;
%else %put The spend is positive;
Old_savings=savings_in_pounds;
New_savings=savings_in_pounds-&amp;trips*&amp;spend;
run;
%mend;</code></pre>
<p>The &quot;%do&quot; statement can be used in conjunction with &quot;%if&quot; statements. The following code creates one of two data sets depending on the sign of the macro variable spend.</p>
<pre><code>%macro shopping(spend,trips);
%if &amp;spend&lt;0 %then %do;
data JJJ_after_saving(keep= Name Old_savings New_savings);
set mat013.jjj;
%end;
%else %do;

data JJJ_after_spending(keep= Name Old_savings New_savings);
set mat013.jjj;
%end;

Old_savings=savings_in_pounds;
New_savings=savings_in_pounds-&amp;trips*&amp;spend;
run;

%mend;</code></pre>
<p>Another use of the %do statement is in iterative statements (as before). The difference being that on this occasion the %do statement creates macro variables. The following code creates various data sets each with a title indexed by a macro variable.</p>
<pre><code>%macro shopping(spend);
%do trips=1 %to 10;

data JJJ_after_saving_&amp;trips(keep= Name Old_savings New_savings);

set mat013.jjj;

Old_savings=savings_in_pounds;
New_savings=savings_in_pounds-&amp;trips*&amp;spend;

run;
%end;
%mend;</code></pre>
<p>The %do statement can also be used in conjunction with the %while and %until statements.</p>
<p>The way SAS compiles macro code can be an extremely useful tool. For example the following code creates a macro that imports 5 separate csv file:</p>
<pre><code>%macro import;
%do i=1 %to 5;
proc import datafile=&quot;\~/File_&amp;i.csv&quot;
    out=File_&amp;i
    dbms=csv
    replace;
    getnames=yes;
run;
%end;
%mend;</code></pre>
<p>The output is shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image04.png" /><br /></p>
<h2 id="macro-functions"><span class="header-section-number">4.4</span> Macro functions</h2>
<p>Since all macro variables are text strings it is not possible to directly perform computations on macro variables that contain numbers. The following code would give an error:</p>
<pre><code>%let var=5**2;

%put &amp;var;</code></pre>
<p>One must make use of the following function to be able to evaluate (in the macro compiler) such computations:</p>
<pre><code>%let var=5**2;

%put %eval(&amp;var);

%put %sysevalf(&amp;var);</code></pre>
<p>The &quot;%sysevalf&quot; function works in a very similar way to the &quot;%eval&quot; but will compute fractions such as 9/2 in the Real numbers (as opposed to eval which would round the result).</p>
<p>Another use of macro functions is when it comes to ignoring certain SAS keywords. The following code puts two different statements to the log.</p>
<pre><code>%let myvar=abc;
%put %str(this string is; &amp;myvar);
%put %nrstr(this string is; &amp;myvar %let);</code></pre>
<p>The first macro function &quot;%str&quot; ignores the &quot;;&quot; and treats it as a string. The second macro function &quot;nrstr&quot; ignores all the SAS statements including &quot;;,&amp;&quot; and &quot;%&quot;.</p>
<p>There are a large number of macro functions and it's worth looking around if you think there's one you might need. Also, of interest are the following commands (look them up) that can help with debugging:</p>
<ol style="list-style-type: decimal">
<li>mprint</li>
</ol>
<ul>
<li>writes all non-macro code generated by the macro</li>
</ul>
<ol start="2" style="list-style-type: decimal">
<li>mlogic</li>
</ol>
<ul>
<li>when a macro begins executing</li>
<li>values of macro parameters</li>
<li>when program statements execute</li>
<li>the status of any %if or %do condition</li>
<li>when a macro stops executing</li>
</ul>
<ol start="3" style="list-style-type: decimal">
<li>Symbolgen</li>
</ol>
<ul>
<li>writes information concerning the resolution of macro variables to the log</li>
</ul>
