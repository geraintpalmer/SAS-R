---
layout      : post
categories  : content
title       : R Chapter 5 - Further packages
comments    : true
---

<p>In this chapter we will examine three packages in particular:</p>
<ol style="list-style-type: decimal">
<li>sqldf: a package allowing for the use of sql syntax in R</li>
<li>ggplot2: a powerful package for the plotting of data</li>
<li>twitteR: a package that allows for the data mining of twitter</li>
</ol>
<h2 id="sqldf"><span class="header-section-number">5.1</span> sqldf</h2>
<h3 id="basic-sql"><span class="header-section-number">5.1.1</span> Basic SQL</h3>
<p>SQL is a language designed for querying and modifying databases. Used by a variety of database management software suites:</p>
<ol style="list-style-type: decimal">
<li>Oracle</li>
<li>Microsoft ACCESS</li>
<li>SPSS</li>
</ol>
<p>SQL uses one or more objects called TABLES where: rows contain records (observations) and columns contain variables.</p>
<p>To use SQL in R we need to use the sqldf package.</p>
<p>The following code creates a data set called test in the work library as a copy of the mmm data set:</p>
<pre><code>test&lt;-sqldf(&quot;select * from MMM&quot;)</code></pre>
<p>The &quot;*&quot; command tells R to take all variables from the data set. We can however specify exactly what variables we want:</p>
<pre><code>test&lt;-sqldf(&quot;select Name,Age,Sex from MMM&quot;)</code></pre>
<p>We can also create new variables:</p>
<pre><code>test&lt;-sqldf(&quot;select Name,Age,Sex,Weight_in_Kg/(power(Height_in_Metres,2)) as bmi from MMM&quot;)</code></pre>
<p>Some of the SQL operators are shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/SQL_operators_in_R.png" /><br /></p>
<h3 id="further-sql"><span class="header-section-number">5.1.2</span> Further sql</h3>
<p>In this section we'll take a look at what else R can do with sql. For the purpose of the following examples let's write a new data set:</p>
<pre><code>Var1&lt;-c(&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;C&quot;)
Var2&lt;-c(1,1,1,2,2)
Var3&lt;-c(&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;C&quot;)
Var4&lt;-c(2,2,1,2,1)
Var5&lt;-c(&quot;B&quot;,&quot;B&quot;,&quot;C&quot;,&quot;D&quot;,&quot;E&quot;)

example&lt;-data.frame(Var1,Var2,Var3,Var4,Var5)</code></pre>
<p>Some simple SQL code very easily helps us to get rid of duplicate rows (this can be very helpful when handling real data). To do this we use the &quot;distinct&quot; keyword.</p>
<pre><code>sqldf(&quot;select distinct * from example&quot;)</code></pre>
<p>We can also select particular variables:</p>
<pre><code>sqldf(&quot;select distinct Var1,Var2,Var3 from example&quot;)</code></pre>
<p>We can also use the &quot;where&quot; statement to select variables that obey a particular condition:</p>
<pre><code>sqldf(&quot;select * from example where Var2&lt;=Var4&quot;)</code></pre>
<p>We can sort data sets using the &quot;order by&quot; keyword:</p>
<pre><code>sqldf(&quot;select distinct * from example order by Var1&quot;)</code></pre>
<p>A very nice application of SQL is in the aggregation of summary statistics. The following code creates a new variable that gives the average value of var2. The value of this variable is the same for all the observations:</p>
<pre><code>sqldf(&quot;select avg(Var2) as average_of_Var2 from example&quot;)</code></pre>
<p>We could however get something a bit more useful by aggregating the data using a &quot;group&quot; statement:</p>
<p>sqldf(&quot;select Var1,avg(Var2) as average_of_Var2 from example group by Var1&quot;)</p>
<h3 id="joining-tables-with-sql"><span class="header-section-number">5.1.3</span> Joining tables with SQL</h3>
<p>A very common use of SQL is to carry out &quot;joins&quot; which are equivalent to a merger of data sets. There are 4 types of joins to consider:</p>
<ol style="list-style-type: decimal">
<li><p>inner join</p>
<ol style="list-style-type: decimal">
<li>output table only contains rows common to all tables</li>
<li>variable attributes taken from left most table</li>
</ol></li>
<li><p>outer join left</p>
<ol style="list-style-type: decimal">
<li>output table contains all rows contributed by the left table</li>
<li>variable attributes taken from left most table</li>
</ol></li>
<li><p>outer join right</p>
<ol style="list-style-type: decimal">
<li>output table contains all rows contributed by the right table</li>
<li>variable attributes taken from right most table</li>
</ol></li>
<li><p>outer join full</p>
<ol style="list-style-type: decimal">
<li>output table contains all rows contributed by all tables</li>
<li>variable attributes taken from left most table</li>
</ol></li>
</ol>
<p>To work with these examples let's use the data sets created with the following code:</p>
<pre><code>Owner&lt;-c(&quot;Jeff&quot;,&quot;Janet&quot;,&quot;Paul&quot;,&quot;Joanna&quot;)
Name&lt;-c(&quot;Ruffus&quot;,&quot;Sam&quot;,NA,NA)
Dogs&lt;-data.frame(Owner,Name)

Owner&lt;-c(&quot;Jeff&quot;,&quot;Paul&quot;,&quot;Joanna&quot;,&quot;Vince&quot;)
Name&lt;-c(&quot;Kitty&quot;,NA,&quot;Tinkerbell&quot;,&quot;Chick&quot;)
Cats&lt;-data.frame(Owner,Name)</code></pre>
<p>The following code carries out an inner join of these two datasets also changing the name of the &quot;Name&quot; variable depending on which data set it was from.</p>
<pre><code>sqldf(&quot;select a.Owner, a.Name as Dog_Name, b.Name as Cat_Name from Dogs as a, Cats as b where a.Owner=b.Owner&quot;)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image30.png" /><br /> The following code carries out a left outer join, the output of which is show.</p>
<pre><code>sqldf(&quot;select a.Owner, a.Name as Dog_Name, b.Name as Cat_Name from Dogs as a left join Cats as b on a.Owner=b.Owner&quot;)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image16.png" /><br /> Right and full outer joins are not yet supported in sqldf however they can actually be obtained by simply using the &quot;merge&quot; function (as discussed in Chapter 3).</p>
<h2 id="ggplot2"><span class="header-section-number">5.2</span> ggplot2</h2>
<p>This is an extremely powerful package that allows for the creation of publication quality plots with ease. There are two basic functions in ggplot2:</p>
<ol style="list-style-type: decimal">
<li>qplot which allows us obtain quick graphs</li>
<li>ggplot which gives us more control of granularity (we will not go into it here)</li>
</ol>
<h3 id="basic-plots-with-qplot"><span class="header-section-number">5.2.1</span> Basic plots with qplot</h3>
<p>The qplot command is very similar to the plot command in that in will often produce the plot required based on the inputs. To obtain a histogram of the Height.in.Metres variable of the JJJ data set we simply use:</p>
<pre><code>qplot(data=JJJ,x=Height.in.Metres)</code></pre>
<p>This produces the plot shown.</p>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image08.png" /><br /> We can improve this by changing the bin width, including a title and changing the labels for the x axis and y axis.</p>
<pre><code>qplot(data=JJJ,x=Height.in.Metres,binwidth=.075,main=&quot;Height of people in the JJJ data set&quot;,xlab=&quot;Height&quot;,ylab=&quot;Frequency&quot;)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image28.png" /><br /> We can obtain a density plot corresponding to the above by using the &quot;density&quot; option for the &quot;geom&quot; argument as shown:</p>
<pre><code>qplot(data=JJJ,x=Height.in.Metres,binwidth=.075,main=&quot;Height of people in the JJJ data set&quot;,xlab=&quot;Height&quot;,ylab=&quot;Frequency&quot;,geom=&quot;density&quot;)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image43.png" /><br /> If we pass two vectors to qplot we obtain a scatter plot:</p>
<pre><code>qplot(data=JJJ,x=Weight.in.Kg,y=Height.in.Metres)</code></pre>
<p>we can also pass qplot a &quot;size&quot; argument to obtain the graph shown:</p>
<pre><code>qplot(data=JJJ,x=Height.in.Metres,y=Weight.in.Kg,size = Age)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image11.png" /><br /> We can of course obtain scatter plots against categorical variables as shown:</p>
<pre><code>qplot(data=JJJ,x=Sex,y=Height.in.Metres)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image07.png" /><br /> We can pass &quot;boxplot&quot; as the &quot;geom&quot; argument to get a boxplot as shown.</p>
<pre><code>qplot(data=JJJ,x=Sex,y=Height.in.Metres,geom=&#39;boxplot&#39;)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image27.png" /><br /></p>
<h3 id="advanced-features"><span class="header-section-number">5.2.2</span> Advanced features</h3>
<p>We can add various features to our scatter plot. The following code just plots a line between all the points:</p>
<pre><code>qplot(data=JJJ,x=Height.in.Metres,y=Weight.in.Kg,geom=&quot;line&quot;)</code></pre>
<p>We can combine various geom options so as to not just include a line but also the points:</p>
<pre><code>qplot(data=JJJ,x=Height.in.Metres,y=Weight.in.Kg,geom=c(&quot;point&quot;,&quot;line&quot;))</code></pre>
<p>Finally we can also add a smoothed line to our plot as shown:</p>
<pre><code>qplot(data=JJJ,x=Height.in.Metres,y=Weight.in.Kg,geom=c(&quot;point&quot;,&quot;line&quot;,&quot;smooth&quot;))</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image09.png" /><br /> We can very easily obtain a collection of any of the above plots across a categorical variables using the &quot;facets&quot; command as shown:</p>
<pre><code>qplot(data=JJJ,x=Height.in.Metres,binwidth=.075,facets=~Sex)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image70.png" /><br /> We can use the &quot;ggsave&quot; command to save the last plotted graph to file:</p>
<pre><code>ggsave(filename=&quot;~/Desktop/test.pdf&quot;)</code></pre>
<p>One final aspect we will take a look at in ggplot2 is that of layers. To do so we will use the following dataset:</p>
<pre><code>MMMJJJ_to_plot&lt;-within(MMMJJJ,{data_set&lt;-ifelse(substr(MMMJJJ$Name,1,1)==&quot;M&quot;,&quot;MMM&quot;,&quot;JJJ&quot;);Sex&lt;-substr(Sex,1,1)})</code></pre>
<p>Firstly we create a plot using qplot and assign it to p (recall that everything in R is an object).</p>
<pre><code>p&lt;-qplot(data=MMMJJJ_to_plot,x=Height.in.Metres,y=Weight.in.Kg,facets=~data_set~Sex,color=Sex)</code></pre>
<p>To view the plot we simply type &quot;p&quot; (note that we have also included a &quot;color&quot; option):</p>
<pre><code>p</code></pre>
<p>Finally we can add a new layer to this plot by &quot;adding&quot; (+) a linear model to our graph:</p>
<pre><code>p&lt;-p+stat_smooth(method=&quot;lm&quot;)</code></pre>
<p>The output of all this is shown.</p>
<p>Finally we can save a particular graph object in ggplot using ggsave:</p>
<pre><code>ggsave(p,filename=&quot;~/Desktop/plot.pdf&quot;)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image62.png" /><br /></p>
<h2 id="twitter"><span class="header-section-number">5.3</span> twitteR</h2>
<p>The last package we will consider is a package that can be used to data mine twitter.</p>
<p>To get the certain trends we use can use the following code:</p>
<pre><code>getTrends(period = &quot;daily&quot;, date=Sys.Date())
getTrends(period = &quot;daily&quot;, date=Sys.Date() - 1)
getTrends(period = &quot;weekly&quot;)</code></pre>
<p>To obtain tweets for a particular hashtag:</p>
<pre><code>searchTwitter(&quot;#orms&quot;)</code></pre>
<p>Finally to obtain tweets from a particular user (the following gives the tweets of the INFORMS as shown):</p>
<pre><code>userTimeline(&quot;INFORMS&quot;)</code></pre>
<p><img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image53.png" /><br /> <img src="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/images/image44.png" /><br /></p>
<p>(Other versions of the above: <a href="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/MAT013AdvanceduseofstatisticalpackagesR.pdf">pdf</a> <a href="http://drvinceknight.github.io/MAT013/Course_Notes/R_Notes/MAT013AdvanceduseofstatisticalpackagesR.docx">docx (not recommended)</a>)</p>
