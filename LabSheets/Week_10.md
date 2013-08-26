# Week 10 - LaTeX

Mathematicians, Computer Scientists, Physicists and others all need to present their research and this is usually through the written medium. Common word processors can be used for this but most prefer to use the typesetting language LaTeX (pronounced Lay-tech).

A typesetting language is a language that requires the user to write code that is then 'translated' to a form that is nice to read:

![](./Images/W10-img01.png)

1. **TICKABLE**  Open up TeXworks which should open a blank document. Write the following LaTeX code:

        \documentclass{article}

        \begin{document}
        Hello, world!
        \end{document}

    1. Save this document.
    2. Ensure the dropdown window has "pdfLaTeX" selected.
    3. Click on the green arrow (ctrl+T) to _compile_ this document which creates a pdf corresponding to your code.

    ![](./Screenshots/W10-S01.png)

    **This is the most basic of LaTeX documents, everything else you do using LaTeX will be done through writing code in your TeX file.**

    There exists some good cloud based solutions to LaTeX. The advantages of these are usually:

    1. No local install of LaTeX needed;
    2. Often possible to have multiple authors collaborating on a document **at the same time**;
    3. Your files are always available to you.

    The main disadvantage is that you need an internet collection to use it. A good such site is [www.writelatex.org](writelatex.org). The following link will create a new copy online of the above document: [](). Feel free to either use TeXworks or writelatex throughout your learning of LaTeX.

2. **TICKABLE** The following keys are used to type text in a source file:

        a-z A-Z 0-9
        + = * / ( ) [ ]

    The following punctuation marks:

        ' ? ! : ` ' -

    Finally there are 13 special keys that are used in commands:

        # $ % & ~ _ ^ \ { } @ " |

    For example, `%` sign is used to denote comments in LaTeX (like `#` in Python or Sage). Modify your python script so that it looks like the following and compile it:


        \documentclass{article} % There are various classes of documents, we will see a few later.

        \begin{document} % This line start the document
        Hello, world!
        \end{document}

3. In general all the code that comes before the `\begin{document}` statement is called the 'preamble' and is used to set a title for the document, call certain packages as well as various other things. The following code (to be inserted in the preamble of your document) sets a title:

        \title{Choose a title}
        \author{V Knight}
        \date{\today}

    If you compile your document this won't include the title in the output. To do so you need to include the following line (in the main body):

        \maketitle

4. The following will add an abstract to your document:

        \begin{abstract}
        This document contains some basic LaTeX code that will be useful to me in the future.
        \end{abstract}

5. There are various ways to obtain lists:

        \begin{itemize}
            \item Unorderd item number 1
            \item Unorderd item number 2
        \end{itemize}

        \begin{enumerate}
            \item Ordered item number 1
            \item Ordered item number 2
        \end{enumerate}

    Note that in \LaTeX\; indentation is not required it is just good practice. Unlike Python where specific environments are delimited by indentation levels, in \LaTeX\; they are ended by specific end statements `\end{enumerate}`.

6. The following code creates a simple table (note the `c`, `r`, and `l` tags that indicate text alignment, experiment by changing these):

        \begin{tabular}{|l|c|r|}
            \hline
            Name & Gender & Start Time\\
            \hline
            Angelico & Male & 1100\\
            \hline
            Leanne & Female & 0830\\
            \hline
            Lisa & Female & 0730\\
            \hline
        \end{tabular}

    In general in \LaTeX\; `\\` is used to denote a 'new line'.

7. To include a picture is straightforward in LaTeX. We make use of the `graphicx` package. In LaTeX packages are included in the preamble using `usepackage`. Include the following in the preamble:

        \usepackage{graphicx}

    The following code (somewhere in the body) will include a picture:

        \includegraphics{path_to_picture}

    We can put this in the `center` environment to centre the picture:

        \begin{center}
            \includegraphics{path_to_picture}
        \end{center}

    (Images can be in jpg, png and pdf format when using the pdflatex compiler.)


8. Graphs, pictures and diagrams can thus be created in any software of choice (Sage, inkscape, google drive etc...) and then included as required **but** it is often easier to draw a picture in LaTeX itself using code. A great package to do this with is `tikz`. Include the following in the preamble:

        \usepackage{tikz}

    Using this package we start a picture by setting up a tikzpicture environment.

        \begin{tikzpicture}

        \end{tikzpicture}

    We then draw various shapes and connectors using the `\draw` command including coordinates:

        \begin{tikzpicture}
            \draw (0,0) -- (0,2); % This draws a line from (0,0) to (0,2)
            \draw (-1,1) -- (1,1); % This draws a line from (-1,1) to (1,1)
            \draw (0,0) -- (1,-1); % This draws a line from (0,0) to (1,-1)
            \draw (0,0) -- (-1,-1); % This draws a line from (0,0) to (-1,-1)
            \draw (0,2.5) circle(.5); % This draws a circle at (0,2.5) with radius .5
        \end{tikzpicture}

   This is very much touching the surface of what can be down with tikz. The simplest next step is to include various color and thickness options:

        \begin{tikzpicture}
            \draw [ultra thick] (0,0) -- (0,2); % This draws a line from (0,0) to (0,2)
            \draw [thin, color=blue] (-1,1) -- (1,1); % This draws a line from (-1,1) to (1,1)
            \draw [thick] (0,0) -- (1,-1); % This draws a line from (0,0) to (1,-1)
            \draw [thick] (0,0) -- (-1,-1); % This draws a line from (0,0) to (-1,-1)
            \draw [color=red, fill=green] (0,2.5) circle(.5); % This draws a circle at (0,2.5) with radius .5
        \end{tikzpicture}

    A lot more can be done with tikz and there are a variety of great examples, tutorials online.

9. It is possible to organise parts of a document using 'sections':

        \section{My first section}

        This is a section with a few subsections.

        \subsection{A part of my first section}

        Here I could write about the problem I'm trying to solve.

        \subsection{Another part of my first section}

        In this subsection I could solve the problem.

        \subsubsection{Further fragmentation...}

        \section{My second section}

        etc...

    We can include labels to sections so that we can refer to them:

        \section{My first section}\label{first_section}

        \section{My second section}\label{second_section}

        In Section \ref{first_section} we saw that...

    When compiling one needs to compile twice:

    1. The first time to find all the labels;
    2. The second time to match the labels to the references.

    If you are using writelatex then this happens automatically.

    Note, labels can be using in conjunction with `tabular` (for tables) and `figure` (for images) environments.

10. To create a bibliography we need to store the bibliographic information in a separate 'bibtex' file. In this file you include bibliographic information for the various references you might have.

    The following is the code for a book on LaTeX. Save the following in a separate file: `bibliography.bib`:

        @book{Gratzer2007,
        author = {Gr\"{a}tzer, George},
        publisher = {Springer},
        title = {{More Math Into LaTeX: A Guide for
        Documentation and Presentation}},
        year = {2007}
        }

    We can then reference the 'key' (for the above it is Gratzer2007) for any document in the bibliography file using the following:

        A very helpful reference for LaTeX is \cite{Gratzer2007}.

    We need to however include a pointer towards the bibliography, at the end of the document include:

    \bibliographystyle{plain}
    \bibliography{bibliography.bib}

   We now need to compile a document twice (as above to find all internal references for sections, figure etc...) **and then** we compile the bibliography with `bibtex` and then we need to compile one last time to match the bibliography items with the citations.

    ![](./Images/W10-img02.png)

    If you are using writelatex then this happens automatically.

11. Mathematics
12. Math in Text
13. Displayed mathematics
14. Text in Maths
15. Arithmetic operators
16. Integrals
17. Matrices
18. Align
19. Cases
20. Beamer
