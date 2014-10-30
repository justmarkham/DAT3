## DAT3 Course Repository

Course materials for [General Assembly's Data Science course](https://generalassemb.ly/education/data-science/washington-dc/) in Washington, DC (10/2/14 - 12/18/14). View student work in the [student repository](https://github.com/justmarkham/DAT3-students).

**Instructors:** Josiah Davis and Kevin Markham

[Course Project information](project.md)

Week | Tuesday | Thursday
--- | --- | ---
0 | | 10/2: [Introduction](#class-1-introduction)
1 | 10/7: [Git and GitHub](#class-2-git-and-github) | 10/9: [Base Python](#class-3-base-python)
2 | 10/14: [Getting and Cleaning Data](#class-4-getting-and-cleaning-data) | 10/16: [Exploratory Data Analysis](#class-5-exploratory-data-analysis)
3 | 10/21: [Linear Regression](#class-6-linear-regression)<br>**Milestone:** Question and Data Set | 10/23: [Linear Regression Part 2](#class-7-linear-regression-part-2)
4 | 10/28: [Machine Learning and KNN](#class-8-machine-learning-and-knn) | 10/30: [Model Evaluation](#class-9-model-evaluation)
5 | 11/4: [Logistic Regression](#class-10-logistic-regression)<br>**Milestone:** Data Exploration and<br>Analysis Plan | 11/6: [Clustering](#class-11-clustering)
6 | 11/11: Dimension Reduction | 11/13: Naive Bayes and NLP
7 | 11/18: Decision Trees<br>**Milestone:** First Draft Due | 11/20: Ensembling: Random Forests
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

* Discuss homework solutions ([code](code/04_file_io_solutions.py))
* Scraping the web for data
    * What is web scraping? Why use it?
    * Web scraping example ([code](code/05_web_scraping_class.py)):
        * [Pages to scrape](http://www.chicagoreader.com/chicago/best-of-chicago-2011-food-drink/BestOf?oid=4106228) using [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
        * Adapted from [Web scraping 101 with Python](http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/)
* Pandas for data analysis ([code](code/05_pandas_class.py))
    * [Split-Apply-Combine](http://i.imgur.com/yjNkiwL.png) pattern

**Homework:**

* Project milestone: Submit your [question and data set](project.md) to DAT3-students by Tuesday!
* Read through this excellent example of [data wrangling and exploration in Pandas](http://nbviewer.ipython.org/github/cs109/content/blob/master/lec_04_wrangling.ipynb)

**Optional:**

* To learn more Pandas, read through this [three-part tutorial](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/) (some overlap with today's class), or read through these two excellent (but extremely long) notebooks: [Introduction to Pandas](http://nbviewer.ipython.org/github/fonnesbeck/Bios366/blob/master/notebooks/Section2_5-Introduction-to-Pandas.ipynb), [Data Wrangling with Pandas](http://nbviewer.ipython.org/github/fonnesbeck/Bios366/blob/master/notebooks/Section2_6-Data-Wrangling-with-Pandas.ipynb)

**Resources:**

* For more web scraping with Beautiful Soup 4, here's a longer example: [slides](http://www.nyu.edu/projects/politicsdatalab/workshops/BeautifulSoup.pdf), [code](https://github.com/aristotle-tek/BeautifulSoup_pres)
* Web scraping without writing any code: "turn any website into an API" with [import.io](https://import.io/) or [kimono](https://www.kimonolabs.com/)
* Simple examples of [joins in Pandas](http://www.gregreda.com/2013/10/26/working-with-pandas-dataframes/#joining), for when you need to merge multiple DataFrames together


## Class 6: Linear Regression

* Discuss your project question and data set
* Pandas for visualization ([code](code/05_pandas_class.py))
* Linear regression ([code](code/06_regression_class.py), [slides](slides/06_linear_regression.pdf))
    * What is linear regression?
    * How to interpret the output?
    * What assumptions does linear regression depend upon?
    * What is multicollinearity and heteroskedasticity, and why should I care?
    * How do I represent categorical variables?

**Optional:**

* Post your favorite visualization in the "viz" channel on Slack, and tell us what you like about it!

**Resources:**

* For more on Pandas plotting, browse through this [IPython notebook](http://nbviewer.ipython.org/github/fonnesbeck/Bios366/blob/master/notebooks/Section2_7-Plotting-with-Pandas.ipynb) or read the [visualization page](http://pandas.pydata.org/pandas-docs/stable/visualization.html) from the official Pandas documentation
* To learn how to customize your plots further, browse through this [IPython notebook](http://nbviewer.ipython.org/github/fonnesbeck/Bios366/blob/master/notebooks/Section2_4-Matplotlib.ipynb) on matplotlib
* To explore different types of visualizations and when to use them, [Choosing a Good Chart](http://www.extremepresentation.com/uploads/documents/choosing_a_good_chart.pdf) is a handy one-page reference, and here is an excellent [slide deck](http://www2.research.att.com/~volinsky/DataMining/Columbia2011/Slides/Topic2-EDAViz.ppt) from Columbia's Data Mining class
* If you are already a master of ggplot2 in R, you may prefer "ggplot for Python" over matplotlib: [introduction](http://blog.yhathq.com/posts/ggplot-for-python.html), [tutorial](http://blog.yhathq.com/posts/facebook-ggplot-tutorial.html)


## Class 7: Linear Regression Part 2

* Linear regression, continued

**Homework:**

* Complete the exercises at the end of the [python script](code/06_regression_class.py) from class

**Resources:**

* One of the best places to go for more information about linear regression is chapter 3 of our course "textbook": [An Introduction to Statistical Learning](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) - or just read Kevin's [highly abbreviated version](http://www.dataschool.io/applying-and-interpreting-linear-regression/)
* For more information about core assumptions, check out this [article](http://people.duke.edu/~rnau/testing.htm) and [this one](http://pareonline.net/getvn.asp?n=2&v=8)
* For more on log transformations, check out this [article](http://people.duke.edu/~rnau/411log.htm)
* This [handout](http://www3.nd.edu/~rwilliam/stats2/l02.pdf) provides an overview of the computation of the F-test
* This may be a helpful [article](http://web.stanford.edu/~mrosenfe/soc_meth_proj3/matrix_OLS_NYU_notes.pdf) on how to derive the coefficient estimates


## Class 8: Machine Learning and KNN

* Discuss homework solutions
* "Human learning" on iris data using Pandas ([code](code/08_iris_class.py))
* Introduction to numpy ([code](code/08_numpy_reference.py))
* Machine learning and K-Nearest Neighbors ([slides](slides/08_ml_knn.pdf))

**Homework:**

* Read this excellent article, [Understanding the Bias-Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html), and be prepared to discuss it on Thursday

**Optional:**

* Walk through the rest of the [numpy reference](code/08_numpy_reference.py) and see if you can understand each of the functions

**Resources:**

* For a more thorough introduction to numpy, [this guide](http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf) is quite good


## Class 9: Model Evaluation

* Introduction to scikit-learn with iris data ([code](code/08_sklearn_knn_class.py))
* Discuss the [article](http://scott.fortmann-roe.com/docs/BiasVariance.html) on the bias-variance tradeoff
* Model evaluation procedures ([slides](slides/09_model_evaluation.pdf), [code](code/09_model_evaluation_class.py))
    * Training error
    * Underfitting and overfitting
    * Test set approach
    * Cross-validation
* Model evaluation metrics ([slides](slides/09_model_evaluation.pdf), [code](code/09_model_evaluation_class.py))
    * Confusion matrix
    * [ROC curves and AUC](http://www.navan.name/roc/)
    * Root Mean Squared Error
* Introduction to [Kaggle](http://www.kaggle.com/)
* Advantages and disadvantages of KNN ([final slide](slides/08_ml_knn.pdf))

**Homework:**

* Project milestone: Submit your "[Data Exploration and Analysis Plan](project.md)" to DAT3-students by Tuesday!
* Read this [simple example](http://googleresearch.blogspot.com/2014/10/smart-autofill-harnessing-predictive.html) of machine learning and see if you understand everything in the article
* Watch Kevin's [Kaggle project presentation video](https://www.youtube.com/watch?v=HGr1yQV3Um0) (16 minutes) for a tour of the machine learning process

**Optional:**

* For more on Kaggle, watch the video [Kaggle Transforms Data Science Into Competitive Sport](https://www.youtube.com/watch?v=8w4UY66GKcM) (28 minutes)
* For much more on the [Kaggle Allstate competition](http://www.kaggle.com/c/allstate-purchase-prediction-challenge), read [Kevin's project paper](https://github.com/justmarkham/kaggle-allstate), read a brief [interview with the first place team](http://blog.kaggle.com/2014/07/11/first-place-in-purchase-prediction-challenge/), review the [Python code from the second place team](https://github.com/alzmcr/allstate), or skim the [solution sharing thread](http://www.kaggle.com/c/allstate-purchase-prediction-challenge/forums/t/8218/solution-sharing)
* If you want to try out the [Kaggle Bike Sharing Demand competition](http://www.kaggle.com/c/bike-sharing-demand), feel free to reuse Kevin's [starter code](code/09_kaggle_bike.py)

**Resources:**

* If you'd like to see more on today's topics, these videos from Hastie and Tibshirani are excellent: [bias-variance tradeoff](https://www.youtube.com/watch?v=VusKAosxxyk) (10 minutes), [test set (aka "validation set") approach](https://www.youtube.com/watch?v=_2ij6eaaSl0) (14 minutes), [cross-validation](https://www.youtube.com/watch?v=nZAM5OXrktY) (14 minutes) - or just read section 5.1 from [their book](http://www-bcf.usc.edu/~gareth/ISL/) (free PDF download!)
* Kevin wrote a [simple guide to confusion matrix terminology](http://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/) that you can use as a reference guide
* The Kaggle wiki has a decent page describing other common [model evaluation metrics](https://www.kaggle.com/wiki/Metrics)


## Class 10: Logistic Regression


## Class 11: Clustering
