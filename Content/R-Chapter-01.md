---
layout      : post
categories  : content
title       : R Chapter 1 - Introduction
comments    : false
---

<h2 id="the-environment"><span class="header-section-number">1.1</span> The Environment</h2>
<p>R can be run in a number of different modes, for the purpose of this course we will be focusing on 'interactive mode' through the graphical user interface (GUI); 'batch mode' is also available but will not be covered here. Note that the screenshots and accompanying screencasts for this course were produced with R version 2.14 running on Mac OSX The look and feel on other operating systems will differ slightly.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image64.png" /><br /> The visible windows are:</p>
<ol style="list-style-type: decimal">
<li>The editor window</li>
<li>The console</li>
</ol>
<p>We can write commands directly into the console window or we can create a script file and edit it in the editor window, highlighting specific text we wish to run. The second approach has the benefit of being able to save the commands written in the script files, although it takes more time (and in fact the commands we write directly in the console can also be saved to a file).</p>
<p>When writing scripts it is good practice to include comments in our files that help describe what the code does. The way to do this in R is with the <code>#</code> symbol before text. The following code is ignored by R:</p>
<pre><code>#2+2</code></pre>
<p>Using the highlight + run approach is akin to copying and pasting the text in the interpreter but R scripts can also be run directly (so that they can be run on servers or as routines without the need to have a user interact).</p>
<h2 id="objects"><span class="header-section-number">1.2</span> Objects</h2>
<p>R is an extremely versatile programming language. In particular R is an &quot;object oriented language&quot;. The significance of this is that everything (functions, data files, outputs of a regression analysis) is an &quot;object&quot;. The type of object is called the &quot;class&quot; and what one can do to a class is called a &quot;method&quot;. The advantage of this is that when a new &quot;class&quot; is developed one simply needs to ensure that is has relevant &quot;methods&quot;, to be compatible with other objects.</p>
<p>As an example, various objects in R have a &quot;plot&quot; method, for example the output of a regression analysis can be plotted using the same command as one would use to plot a scatter plot of a data set.</p>
<p>R has a wide range of data types (which are themselves objects). The 2 classes corresponding to data sets we will concentrate on in this course are:</p>
<ol style="list-style-type: decimal">
<li>Vectors</li>
<li>Data frames</li>
</ol>
<p>Vectors are simply collections of variables of a particular type (&quot;Numeric&quot;, &quot;Character&quot;, &quot;Boolean&quot; etc). In R a type of variable is called a &quot;mode&quot;, representing how it is stored in the computer memory. Data frames are collections of vectors and correspond to data sets. Technically, data frames are lists with dimensions, which are themselves just generic vectors. One might say a collection of equal length vectors (thus allowing the rectangular shape). Some examples of vectors and data frames are shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image05.png" /><br /> Let's import some data!</p>
<h2 id="importing-data"><span class="header-section-number">1.3</span> Importing Data</h2>
<p>We will consider two approaches to importing data:</p>
<ol style="list-style-type: decimal">
<li>Direct input</li>
<li>Importing an external data set (xls, csv etc...)</li>
</ol>
<p>In practice you will never use the direct input method but let's take a look for completeness (although it is very useful when wanting to quickly test a few things). This will also give us our first experience of the editor window!</p>
<p>Let us create a data set named <code>first_data_set</code> which will include the following data:</p>
<pre><code>    Name, Age
    Bob, 23
    Billy, 25</code></pre>
<p>To do so write the following code in the editor window:</p>
<pre><code>Name &lt;- c(&quot;Bob&quot;,&quot;Billy&quot;)
Age &lt;- c(23,25)
first_data_set &lt;- data.frame(Name,Age)</code></pre>
<p>Let's take a look at the shown screenshot of this. You may notice that some elements of the text are highlighted, this is to emphasise key words (note that this doesn't happen automatically on Windows).</p>
<ol style="list-style-type: decimal">
<li>The first two lines of code make use of the <code>&lt;-</code> operator that assigns an object to a variable.</li>
<li>The objects in questions are created using the <code>c</code>(ombine) function that creates a vector. We use this to create 2 vectors: Name and Age.</li>
<li>Finally we put the 2 vectors into a data frame using the <code>data.frame</code> command.</li>
</ol>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image22.png" /><br /> We run this code by highlighting it and pressing ctrl + 'r' (.html + enter on Mac). Note that when we submit code this way it also appears in the console window. We could have in fact directly type this code into the console window. For those familiar with command line commands the console works in a very similar way. We can press the up arrow repeatedly to cycle through previous commands and use tab to autocomplete.</p>
<p>The data set <code>first_data_set</code> is now saved to memory. To view all the data structures in memory we use the simple line of code:</p>
<pre><code>ls()</code></pre>
<p>A screenshot of the output is shown. We see that there are actually 3 objects in memory, the two vectors (Name and Age) as well as the data frame (first_data_set).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image03.png" /><br /> To view our data set, we simply type the name (as shown):</p>
<pre><code>first_data_set</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image68.png" /><br /> Using direct input is of course not at all realistic when trying to import larger data sets.</p>
<p>Often large data sets will be saved in comma-separated values (csv) format which can be read by most (all?) software. We will import the data set shown (here viewed in a simple text editor).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image33.png" /><br /> We will import this data set into R using the following code:</p>
<pre><code>JJJ &lt;- read.csv(file=&quot;~/JJJ.csv&quot;,head=TRUE)</code></pre>
<p>Let's take a look at the screenshot shown. Note here that we are not using the text editor but directly writing code in the console (this is often how I prefer to use R for short bits of code).</p>
<ol style="list-style-type: decimal">
<li><code>read.csv</code> - is the command which is used to tell R to read in data from a csv file.</li>
<li><code>file</code> - an option tells R where the csv file is located.</li>
<li><code>head</code> - an option tells R to read the variable names from the first row of the csv file. Note that this command can be omitted (the default value is <code>TRUE</code>).</li>
</ol>
<p>We have omitted other options (such as <code>sep</code> which can be used to change the default separator from <code>,</code> to something else).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image37.png" /><br /> Running the code (by either pressing enter if using the console or highlighting and running as before is using the editor) gives the required object as shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image66.png" /><br /> In the following chapters we will learn how to create new data sets from old data sets and as such it may become necessary to export files to csv.</p>
<h2 id="exporting-data-sets"><span class="header-section-number">1.4</span> Exporting Data Sets</h2>
<p>We will export our first data set (<code>first_dataset</code>) to csv using the following line of code:</p>
<pre><code>write.csv(first_data_set,&quot;~/Desktop/first_data_set.csv&quot;)</code></pre>
<p>Let's take a look at the screenshot.</p>
<ol style="list-style-type: decimal">
<li><code>write.csv</code> is the command which is used to tell R to read in data from a csv file.</li>
<li>The first command tells R which R object to export.</li>
<li>The second command tells R the location of the csv file.</li>
</ol>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image59.png" /><br /></p>
