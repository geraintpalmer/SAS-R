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

3. Title
4. Abstract
5. Lists
6. Tables
7. Sections
8. Pictures
9. Drawings
10. Bibliography
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
