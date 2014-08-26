---
layout      : post
categories  : content
title       : SAS Chapter 1 - Introduction
comments    : true
---

<h2 id="the-environment"><span class="header-section-number">1.1</span> The Environment</h2>
<p>SAS may be run in a variety of modes, on this course we will concentrate on the interactive mode which allows users to submit selected portions of SAS code through a graphical user interface (GUI). When opening SAS a variety of windows immediately become visible as shown. Note that the screenshots and accompanying screen casts for this course were produced with SAS 9.3 running on ubuntu 11.10. The look and feel on other operating systems will differ slightly.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image21.png" /><br /> The visible windows are:</p>
<ol style="list-style-type: decimal">
<li>The explorer window</li>
<li>The results window</li>
<li>The command window</li>
<li>The output window</li>
<li>The log window</li>
<li>The editor window</li>
</ol>
<p>We write code directly in the editor window and the roles of the other windows will become clear shortly.</p>
<h2 id="libraries"><span class="header-section-number">1.2</span> Libraries</h2>
<p>The major strength of SAS is its ability to handle huge data sets. SAS does this by storing files in a particular format in spaces called libraries. SAS libraries are important. SAS manipulates data sets once they are converted to SAS data files. These data files are saved in libraries in SAS. They work just like folders (apart from not being able to nest further libraries). If you click on the libraries tab in the explorer window (as shown in in the screenshot) you should see the libraries available to you (as shown in the other screenshot).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image58.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image32.png" /><br /> On my system SAS has already created 6 libraries (this might differ on other versions and operating systems). The Work library which SAS automatically uses if no library is specified (more on this later, it's basically the default library). A very important fact about the Work library is that it is temporary. When SAS is shut down, all the contents of the Work library are deleted. Keeping this in mind, let's move on to creating a new library.</p>
<h3 id="creating-a-new-library"><span class="header-section-number">1.2.1</span> Creating a new library</h3>
<p>To create a new library, left click in the explorer window and select &quot;New...&quot;. You will see a new window appear as shown. Simply browse to the location on your computer at which you'd like your new library to be stored. Note also to click the &quot;Enable at startup&quot; option which ensures that SAS remembers this library the next time you open up SAS; if this is not selected, the link to the library created will be temporary (and erased when SAS is shut down). Finally make sure you name your library obeying the following rules (for the rest of the notes, I'll assume the library name for this course is <code>mat013</code>):</p>
<ol style="list-style-type: decimal">
<li>be less than or equal to 8 characters</li>
<li>must begin with an underscore or letter</li>
<li>remaining characters can be letters, numbers or underscores</li>
</ol>
<div class="figure">
<img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image57.png" /><p class="caption"></p>
</div>
<p>Now that we have a library let's import some data!</p>
<h2 id="importing-data"><span class="header-section-number">1.3</span> Importing Data</h2>
<p>There are two main ways to import data into SAS:</p>
<ol style="list-style-type: decimal">
<li>Direct input</li>
<li>Importing an external data set (xls, csv etc...)</li>
</ol>
<p>In practice you will never use the direct input method but let's take a look for completeness (although it is very useful when wanting to quickly test a few things). This will also give us our first experience of the editor window!</p>
<p>Let us create a data set named <code>first_data_set</code>, put it in the <code>mat013</code> library and include the following data:</p>
<pre><code>Name,Age
Bob,23
Billy,25</code></pre>
<p>To do so, write the following code in the editor window:</p>
<pre><code>data mat013.first_data_set;
input Name $ Age;
cards;
Bob 23
Billy 25
;
run;</code></pre>
<p>Let's take a look at the screenshot. First of all we see that the program editor automatically includes some syntax colouring (i.e. changes the colour of some of the words that it recognises). In blue in the editor window are the SAS keywords:</p>
<ol style="list-style-type: decimal">
<li><code>data</code> which tells SAS that we're about to write a <code>data step</code> which we'll look at a bit closer in the Chapter 3. The keyword data is always followed by the library and the data file (separated by a <code>.</code>) we're creating. If no library is given then SAS will put this file in the Work library.</li>
<li><code>input</code> which tells SAS that we're going to input raw data and what follows is the name of the variables. If a variable is a string then we must include a <code>\$</code> after the variable name.</li>
<li><code>cards</code> which is the SAS keyword that precedes the raw data. All the entries must be on separate rows.</li>
<li><code>run</code> which is the keyword that tells SAS where the statement ends.</li>
</ol>
<p>An important thing to remember is that a SAS statement always ends with a <code>;</code>. Forgetting the <code>;</code> is a common source of mistakes (and headaches).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image60.png" /><br /> We run this code by highlighting it and pressing the 'running man', clicking on run (or pressing F8 on Windows). It is good practice to always check the log window as soon as any code is run. In the screenshot we see that the log looks good (lines 1-7 don't show any errors) and simply gives some details as to the running of the program.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image35.png" /><br /></p>
<p>If we now look at the mat013 library in the explorer pane we can see the new data set is in there, double clicking on the data set opens it up.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image26.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image42.png" /><br /> Using direct input is of course not at all realistic when trying to import larger data sets.</p>
<p>Often large data sets will be saved in comma-separated values (csv) format which can be read by most (all?) software. We will import the data set shown (here viewed in a simple text editor).</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image13.png" /><br /> We will import this data set in to the mat013 library and call it <code>JJJ</code> using the following code:</p>
<pre><code>proc import datafile=&quot;~/JJJ.csv&quot;
    out=mat013.JJJ
    dbms=csv
    replace;
    getnames=yes;
run;</code></pre>
<p>Let's take a look at the screenshot shown. We again see that the program editor automatically includes some syntax colouring (i.e. changes the colour of some of the words that it recognises). In blue in the editor window are the SAS keywords:</p>
<ol style="list-style-type: decimal">
<li><code>proc</code> which tells SAS that we're about to write a 'procedure step' which we'll look at a bit closer in the next chapter. The <code>proc</code> keyword is always followed by the name of the particular procedure we're going to use. In this case: <code>import</code>, which is then followed by the statement <code>datafile=path-to-datafile</code>. Following this are various options relating to the import statement.</li>
<li><code>out</code> - this tells SAS the name of the SAS datafile created from the imported file.</li>
<li><code>dbms</code> - this tells SAS the type of file being imported (in our case csv, but can be <code>dlm</code>, <code>xls</code>, etc.). Note that this is not necessary if SAS can recognise the file extension.</li>
<li><code>replace</code> - this tells SAS to replace any SAS datafiles with the same name as specified by <code>out</code>.</li>
<li><code>getnames=yes</code> which, although this is not a SAS keyword, it is a special option for the import statement that allows you to tell SAS to get the variable names from the first row of your external data file.</li>
<li><code>run</code> is the keyword that tells SAS where the statement ends.</li>
</ol>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image62.png" /><br /> Running the code in the same way as before (highlighting and F8) will create the required datafile as shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image05.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image31.png" /><br /> In the following chapters we will learn how to create new data sets from old data sets and as such it may become necessary to export files to csv.</p>
<h2 id="exporting-data-sets"><span class="header-section-number">1.4</span> Exporting data sets</h2>
<p>We will export our first data set (&quot;mat013.first_dataset&quot;) to csv using the following code:</p>
<pre><code>proc export data=mat013.first_data_set
    outfile=&quot;~/Desktop/first_data_set.csv&quot;
    dbms=csv
    replace;
run;</code></pre>
<p>Let's take a look at the screenshot shown. In blue are the SAS keywords:</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/SAS_Notes/images/image56.png" /><br /></p>
<ol style="list-style-type: decimal">
<li><code>proc</code> which tells SAS that we're about to write a 'procedure step' which we'll look at a bit closer in the next chapter. The <code>proc</code> keyword is always followed by the name of the particular procedure we're going to use. In this case: <code>export</code>, which is then followed by the statement <code>data=</code> followed by the library and name of the SAS data file you want to export. Following this are various options relating to the export statement.</li>
<li><code>outfile</code> - this tells SAS where the exported file should go.</li>
<li><code>dbms</code> - this tells SAS the type of file to create when exporting (in our case csv, but can be <code>dlm</code>, <code>xls</code>, etc...). Note that this is not necessary if SAS can recognise the file extension.</li>
<li><code>replace</code> - this tells SAS to replace any file with the same name as specified by <code>outfile</code>.</li>
<li><code>run</code> is the keyword that tells SAS where the statement ends.</li>
</ol>
<p>In the next chapter we will see more complex (and potentially useful) procedures.</p>
