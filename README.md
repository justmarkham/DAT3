## DAT3 Course Repository

Course materials for [General Assembly's Data Science course](https://generalassemb.ly/education/data-science/washington-dc/) in Washington, DC (10/2/14 - 12/18/14). View student work in the [student repository](https://github.com/justmarkham/DAT3-students).

**Instructors:** Josiah Davis and Kevin Markham

[Course Project information](project.md)

Week | Tuesday | Thursday
--- | --- | ---
0 | | 10/2: [Introduction](#class-1-introduction)
1 | 10/7: [Git and GitHub](#class-2-git-and-github) | 10/9: [Base Python](#class-3-base-python)
2 | 10/14: [Getting and Cleaning Data](#class-4-getting-and-cleaning-data) | 10/16: [Exploratory Data Analysis](#class-5-exploratory-data-analysis)
3 | 10/21: Linear Regression<br>**Milestone:** Question and Data Set | 10/23: Logistic Regression
4 | 10/28: Machine Learning, KNN | 10/30: Model Evaluation
5 | 11/4: Clustering<br>**Milestone:** Data Exploration and<br>Analysis Plan | 11/6: Naive Bayes and NLP
6 | 11/11: Dimension Reduction | 11/13: Decision Trees
7 | 11/18: Project Working Time<br>**Milestone:** First Draft Due | 11/20: Ensembling: Random Forests
8 | 11/25: Recommenders | *Thanksgiving*
9 | 12/2: Ensembling: Boosting | 12/4: Neural Networks
10 | 12/9: Review<br>**Milestone:** Second Draft Due | 12/11: Project Working Time
11 | 12/16: Project Presentations | 12/18: Project Presentations


### Class 1: Introduction

* Introduction to General Assembly
* Course overview and philosophy ([slides](slides/01_course_overview.pdf))
* What is data science? ([slides](slides/01_intro_to_data_science.pdf))
* Brief demo of [Slack](https://slack.com/)

**Homework:**

* Install [Anaconda distribution of Python 2.7](http://continuum.io/downloads), [Git](http://git-scm.com/book/en/Getting-Started-Installing-Git), and [Slack](https://slack.com/)
* Add a photo to your Slack profile
* Create a [GitHub account](https://github.com/)
* Read [Analyzing the Analyzers](http://cdn.oreillystatic.com/oreilly/radarreport/0636920029014/Analyzing_the_Analyzers.pdf) (40 pages) and think about where you'd like to fit in!

**Optional:**

* Subscribe to some data-focused newsletters, to keep current: [Center for Data Innovation](http://www.datainnovation.org/), [O'Reilly Data Newsletter](http://www.oreilly.com/data/index.html), [Data Community DC](http://datacommunitydc.org/blog/newsletter/)
* Watch [Introduction to Data Science and Analysis](https://generalassemb.ly/online/videos/introduction-to-data-science-and-analysis) (50 minutes) for another look at the data science workflow
* Find an open source project hosted on GitHub that interests you


### Class 2: Git and GitHub

* Homework discussion: Any installation issues? Find any interesting GitHub projects? Any takeaways from "Analyzing the Analyzers"?
* Introduce yourself: What's your technical background? Why did you join this course? How do you define success in this course?
* Office hours
* Git and GitHub lesson ([slides](slides/02_git_github.pdf))
    * Create a repo on GitHub, clone it, make changes, and push up to GitHub
    * Fork the [DAT3-students](https://github.com/justmarkham/DAT3-students) repo, clone it, add a Markdown file (`about.md`) in your folder, push up to GitHub, and create a [pull request](https://help.github.com/articles/using-pull-requests)

**Homework:**

* Review the [course project information](project.md), [past projects](https://github.com/justmarkham/DAT-project-examples) from other GA students, and [public data sources](public_data.md)

**Optional:**

* Clone this repo (DAT3) for easy access to the course files
* Watch [Introduction to Git and GitHub](https://www.youtube.com/playlist?list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD) (36 minutes) to repeat a lot of today's presentation
* Read the first two chapters of [Pro Git](http://git-scm.com/book) for a much deeper understanding of version control and the basic Git commands
* Learn some more [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) and add it to your `about.md` file, then push those edits to GitHub and send another pull request
* Read this friendly [command line tutorial](http://seankross.com/notes/cli/cli.html) if you are brand new to the command line
* For more project inspiration, browse the [student projects](http://cs229.stanford.edu/projects2013.html) from Andrew Ng's [Machine Learning course](http://cs229.stanford.edu/) at Stanford

**Resources:**

* [Dillinger](http://dillinger.io/) is a browser-based Markdown editor, useful for checking your Markdown code
* [GitRef](http://gitref.org/) is an excellent reference guide for Git commands
* [Git quick reference for beginners](http://www.dataschool.io/git-quick-reference-for-beginners/) is a shorter reference guide with commands grouped by workflow


## Class 3: Base Python

* Any questions about Git/GitHub?
* Discuss the [course project](project.md). What's one thing you learned from reviewing student projects?
* Base Python lesson, with exercises ([code](code/03_base_python_class.py))

**Homework:** 

* Complete the exercises at the end of the [Python script](code/03_base_python_class.py) we went over in class today and add your solutions to your folder in the [DAT3-students repo](https://github.com/justmarkham/DAT3-students)
* Keep thinking about your [project](project.md), and consult [past projects](https://github.com/justmarkham/DAT-project-examples) and [public data sources](public_data.md) for more inspiration


## Class 4: Getting and Cleaning Data

* Discuss homework solutions ([code](code/03_base_python_solutions.py))
* File input/output in Python
    * [Article](http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/), [original data](https://github.com/fivethirtyeight/data/blob/master/alcohol-consumption/drinks.csv), [modified data](data/drinks.csv)
    * Open in [Sublime Text](http://www.sublimetext.com/3)
    * Reading and writing files ([code](code/04_file_io_class.py))
* Getting data from APIs
    * What is an API? Why provide one?
    * Apigee: [API providers](https://apigee.com/providers), [Echo Nest API console](https://apigee.com/console/echonest)
    * [Echo Nest Developer Center](http://developer.echonest.com/) for API key and documentation
    * Three options for reading data into Python ([code](code/04_api_json_class.py)):
        * [curl](http://curl.haxx.se/docs/manpage.html) to [file](data/echo_nest_top.txt), [view file in browser](https://github.com/callumlocke/json-formatter), read with [json module](https://docs.python.org/2/library/json.html)
        * Use [requests](http://docs.python-requests.org/en/latest/)
        * Use [Pyechonest](https://github.com/echonest/pyechonest)

**Homework:**

* Exercise 2 from [file input/output](code/04_file_io_class.py)
* Read [What I do when I get a new data set as told through tweets](http://simplystatistics.org/2014/06/13/what-i-do-when-i-get-a-new-data-set-as-told-through-tweets/)
* Watch [Look at Your Data](https://www.youtube.com/watch?v=coNDCIMH8bk) (18 minutes)

**Optional:**

* Exercise 3 from [file input/output](code/04_file_io_class.py)
* Read this [fun article](http://www.theatlantic.com/technology/archive/2014/01/how-netflix-reverse-engineered-hollywood/282679/?single_page=true) about using web scraping to analyze Netflix's "micro-genres"

**Resources:**

* [Online Python Tutor](http://pythontutor.com/) is useful for visualizing (and debugging) your code
* [Directory of API wrappers](http://www.pythonapi.com/) for Python


## Class 5: Exploratory Data Analysis

* Discuss homework solutions (code coming soon)
* Scraping the web for data
    * What is web scraping? Why use it?
    * Web scraping example ([code](code/05_web_scraping_class.py)):
        * [Pages to scrape](http://www.chicagoreader.com/chicago/best-of-chicago-2011-food-drink/BestOf?oid=4106228) using [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
        * Adapted from [Web scraping 101 with Python](http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/)
* Tidy data and reproducibility
    * What is [tidy data](http://www.prometheusresearch.com/good-data-management-practices-for-data-analysis-tidy-data-part-2/)? Examples: [tidy](https://github.com/fivethirtyeight/data/tree/master/bob-ross), [untidy](https://github.com/fivethirtyeight/data/tree/master/airline-safety), [very untidy](https://github.com/fivethirtyeight/data/tree/master/region-survey)
    * What is [reproducibility](https://github.com/jtleek/datasharing)? [Twitter definition](https://twitter.com/jakevdp/status/519563939177197571), [example](https://github.com/fivethirtyeight/data/tree/master/classic-rock)
* Pandas for data analysis ([code](code/05_pandas_class.py))
    * [Split-Apply-Combine](http://i.imgur.com/yjNkiwL.png) pattern
    * Simple examples of [joins in Pandas](http://www.gregreda.com/2013/10/26/working-with-pandas-dataframes/#joining)
* Visualization
* Regular expressions ("regex"), briefly
    * What are [regular expressions](http://xkcd.com/208/)? [Why use them](http://geeksta.net/geeklog/exploring-expressions-emotions-github-commit-messages/)?
    * Regex example ([code](code/05_regex_class.py), [data](data/homicides.txt))

**Homework:**

* Project milestone: Submit your [question and data set](project.md) to DAT3-students by Tuesday!

**Optional:**

* Post your favorite visualization in the "viz" channel on Slack
* Read [Reproducibility is not just for researchers](http://www.dataschool.io/reproducibility-is-not-just-for-researchers/)
* Watch [Colbert on reproducibility](http://thecolbertreport.cc.com/videos/dcyvro/austerity-s-spreadsheet-error) (8 minutes)
* Scan the [Python reference](code/03_base_python_reference.py) to find things you don't know, and then learn more about those things!

**Resources:**

* Longer web scraping example using Beautiful Soup 4 ([slides](http://www.nyu.edu/projects/politicsdatalab/workshops/BeautifulSoup.pdf), [code](https://github.com/aristotle-tek/BeautifulSoup_pres))
* Alternatives to web scraping: "turn any website into an API" with [import.io](https://import.io/) or [kimono](https://www.kimonolabs.com/)
* Getting started with regex: [Python introductory lesson](https://developers.google.com/edu/python/regular-expressions) and [reference guide](code/05_regex_reference.py), [real-time regex tester](http://www.regexr.com/), [in-depth tutorials](http://www.rexegg.com/)
