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
5 | 11/4: [Logistic Regression](#class-10-logistic-regression)<br>**Milestone:** Data Exploration and<br>Analysis Plan | 11/6: [Logistic Regression Part 2, Clustering](#class-11-logistic-regression-part-2-clustering)
6 | 11/11: [Dimension Reduction](#class-12-dimension-reduction) | 11/13: [Clustering Part 2, Naive Bayes](#class-13-clustering-part-2-naive-bayes)
7 | 11/18: [Natural Language Processing](#class-14-natural-language-processing) | 11/20: [Decision Trees](#class-15-decision-trees)
8 | 11/25: [Recommenders](#class-16-recommenders)<br>**Milestone:** First Draft Due | *Thanksgiving*
9 | 12/2: [Ensembling](#class-17-ensembling) | 12/4: [Ensembling Part 2, Python Companion Tools](#class-18-ensembling-part-2-python-companion-tools)
10 | 12/9: [Working a Data Problem](#class-19-working-a-data-problem) <br>**Milestone:** Second Draft Due | 12/11: [Neural Networks](#class-20-neural-networks)
11 | 12/16: [Review](#class-21-review) | 12/18: [Project Presentations](#class-22-project-presentations)


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
* [Directory of API wrappers](http://www.pythonforbeginners.com/api/list-of-python-apis) for Python


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

* Discuss homework solutions ([code](code/06_regression_solutions.py))
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
* Introduction to [Kaggle](http://www.kaggle.com/)

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

* Any questions from last time: model evaluation, Kaggle, article on Smart Autofill?
* Summary of your feedback
* Discuss your data exploration and analysis plan
* Logistic Regression ([slides](slides/10_logistic_regression.pdf), [code](code/10_logistic_regression_exercise.py))

**Homework:**

* Continue to work on Part I of the [exercise from class](code/10_logistic_regression_exercise.py) and submit your solution to DAT3-students


## Class 11: Logistic Regression Part 2, Clustering

* Logistic Regression, continued ([exercise solution](code/10_logistic_regression_class.py))
* Clustering ([slides](slides/11_clustering.pdf))
    * Why cluster?
    * Introduction to the K-means algorithm
    
**Homework:**

* Read through section 8.2 on [K-means Clustering](http://www-users.cs.umn.edu/~kumar/dmbook/ch8.pdf) from Introduction to Data Mining by next Thursday. What are some of the strengths and limitations of k-means clustering?

**Resources:**

* If you would like a review on the topics we covered today (and Tuesday), the videos from Hastie and Tibshirani from Stanford are very good:
    * [Introduction to Classification](https://www.youtube.com/watch?v=sqq21-VIa1c) (10 minutes)
    * [Logistic Regression and Maximum Likelihood](https://www.youtube.com/watch?v=31Q5FGRnxt4) (9 minutes)
    * [Multivariate Logistic Regression and Confounding Variables](https://www.youtube.com/watch?v=MpX8rVv_u4E) (10 minutes)
* If you want to understand the math of how coefficients are estimated, check out these [notes](http://www.stat.cmu.edu/~cshalizi/uADA/12/lectures/ch12.pdf) from CMU's Advanced Data Analysis class. Written by Cosma Shalizi, one of CMU's professors.
* [Documentation](http://matplotlib.org/users/mathtext.html) for plotting math text
* [Documentation](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter) for plotting scatter plots


## Class 12: Dimension Reduction

* Model evaluation metrics, continued
    * ROC curves and AUC ([visualization](http://www.navan.name/roc/), [code](code/10_logistic_regression_roc.py))
    * Root Mean Squared Error ([slides](slides/09_model_evaluation.pdf))
* Dimension Reduction (Guest Lecturer: [Sinan Ozdemir](https://generalassemb.ly/instructors/sinan-ozdemir/2644))
    * [Slides](slides/12_dimension_reduction.pdf)
    * Code: [PCA and SVD](code/12_pca_svd_class.py)
    * Code: [image compression with PCA](code/12_shakira.py) ([original source](http://glowingpython.blogspot.com/2011/07/pca-and-image-compression-with-numpy.html))

**Homework:**

* Read Paul Graham's ["A Plan for Spam"](http://www.paulgraham.com/spam.html) in preparation for Thursday's class on Naive Bayes

**Resources:**

* Kevin has a [video tutorial](http://youtu.be/OAl6eAyP-yo) (14 minutes) and [blog post](http://www.dataschool.io/roc-curves-and-auc-explained/) summarizing ROC curves and AUC
* scikit-learn has extensive documentation on [model evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html)
* On Cross Validated, [this question](http://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues) has dozens of explanations of PCA, and [this question](http://stats.stackexchange.com/questions/62092/bottom-to-top-explanation-of-the-mahalanobis-distance) has a useful visualization of what is essentially PCA


## Class 13: Clustering Part 2, Naive Bayes

* Clustering Analysis ([slides](slides/11_clustering.pdf))
    * Understanding the K-means algorithm
    * Choosing K for k-means
    * [Exercises](code/11_kmeans_clustering_class.py)
    * Visualizing data in multi-dimensional space
    * [Limitations of K-means](code/11_kmeans_limitations.py), [K-means cluster validation](code/11_evaluating_cluster_validation.py)
* Naive Bayes ([slides](slides/13_naive_bayes.pdf))
    * Briefly discuss ["A Plan for Spam"](http://www.paulgraham.com/spam.html)
    * Probability and Bayes' Theorem ([original source](http://oscarbonilla.com/2009/05/visualizing-bayes-theorem/), [confusion matrix reference](http://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/))
    * Naive Bayes classification

**Homework:**

* Open Python, type `import nltk`, type `nltk.download()`, find the "NLTK Downloader" popup window, click on "all", then click on "Download". Do this at home, since it's more than 300 MB! If you have space constraints on your computer, we can tell you next class exactly which packages to download.

**Resources:**

* For clustering, scikit-learn has documentation on [K-means clustering](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html), [alternative clustering algorithms](http://scikit-learn.org/stable/modules/clustering.html), and [clustering metrics](http://scikit-learn.org/stable/modules/classes.html#clustering-metrics)
* Vipin Kumar from the University of Minnesota has a [helpful chapter on clustering](http://www-users.cs.umn.edu/~kumar/dmbook/ch8.pdf) from his textbook: Introduction to Data Mining
* For an alternative introduction to Bayes' Theorem, [Bayes' Rule for Ducks](https://planspacedotorg.wordpress.com/2014/02/23/bayes-rule-for-ducks/), [Bayes' Rule in an animated gif](http://simplystatistics.org/2014/10/17/bayes-rule-in-a-gif/), and this [5-minute video on conditional probability](https://www.youtube.com/watch?v=Zxm4Xxvzohk) may be helpful
* For more details on Naive Bayes classification, Wikipedia has two useful articles: [Naive Bayes classifier](http://en.wikipedia.org/wiki/Naive_Bayes_classifier), [Naive Bayes spam filtering](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)
* If you enjoyed Paul Graham's article, you can read [his follow-up article](http://www.paulgraham.com/better.html) on how he improved his spam filter and this [related paper](http://www.merl.com/publications/docs/TR2004-091.pdf) about state-of-the-art spam filtering in 2004


## Class 14: Natural Language Processing

* Naive Bayes, continued ([code](code/13_naive_bayes_class.py))
    * Create a spam classifier using [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) and [MultinomialNB](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)
* Natural Language Processing ([code](code/14_nlp_class.py))
    * Real-world examples
    * [NLTK](http://www.nltk.org/): tokenization, stemming, lemmatization, stopwords, Named Entity Recognition ([Stanford NER Tagger](http://nlp.stanford.edu:8080/ner/process)), TF-IDF, document summarization
    * Alternative: [TextBlob](http://textblob.readthedocs.org/en/dev/index.html)

**Resources:**

* [Natural Language Processing with Python](http://www.nltk.org/book/): free online book to go in-depth with NLTK
* [NLP online course](https://www.coursera.org/course/nlp): no sessions are available, but [video lectures](https://class.coursera.org/nlp/lecture) and [slides](http://web.stanford.edu/~jurafsky/NLPCourseraSlides.html) are still accessible
* [Brief slides](http://files.meetup.com/7616132/DC-NLP-2013-09%20Charlie%20Greenbacker.pdf) on the major task areas of NLP
* [Detailed slides](https://github.com/ga-students/DAT_SF_9/blob/master/16_Text_Mining/DAT9_lec16_Text_Mining.pdf) on a lot of NLP terminology
* [A visual survey of text visualization techniques](http://textvis.lnu.se/): for exploration and inspiration
* [DC Natural Language Processing](http://www.meetup.com/DC-NLP/): active Meetup group
* [Stanford CoreNLP](http://nlp.stanford.edu/software/corenlp.shtml): suite of tools if you want to get serious about NLP
* Getting started with regex: [Python introductory lesson](https://developers.google.com/edu/python/regular-expressions) and [reference guide](code/99_regex_reference.py), [real-time regex tester](http://www.regexr.com/), [in-depth tutorials](http://www.rexegg.com/)

**Homework:**

* We will use Graphviz to visualize the output of the classification trees. Please download this before class.  
    * In order to [download and install for Windows](http://www.graphviz.org/Download_windows.php), you will also need to manually add the folder location (e.g., C:\Program Files (x86)\Graphviz2.30\bin;) to your environment path. (download graphviz-2.38.msi)
    * You can also [download and install for Mac](http://www.graphviz.org/Download_macos.php). I am not aware of any issues with installation.


## Class 15: Decision Trees

At the end of this class, you should be able to do the following:
* Describe the output of a decision tree to someone without a data science background
* Describe how the algorithm creates the decision tree 
* Predict the likelihood of a binary event using the decision tree algorithm in scikit-learn
* Create a decision tree visualization
* Determine the optimal tree size using a tune grid and the AUC metric in Python
* Describe the strengths and weaknesses of a decision tree

**Homework:**

* Work on your project. The first draft of your project is due on Tuesday at 5 pm.

**Resources:**

* Dr. Justin Esarey from Rice University has a nice [video lecture](https://www.youtube.com/watch?v=HW7Aib842Oo&hd=1) on CART that also includes a [code walkthrough](http://jee3.web.rice.edu/cart-and-random-forests.r)
* For those of you with background in javascript, d3.js has a nice tree layout that would make more presentable tree diagrams 
   * Here is a link to a [static version](http://bl.ocks.org/mbostock/4339184), as well as a link to a [dynamic version](http://bl.ocks.org/mbostock/4339083) with collapsable nodes
   * If this is something you are interested in, Gary Sieling wrote a nice [function](http://www.garysieling.com/blog/rending-scikit-decision-trees-d3-js) in python to take the output of a scikit-learn tree and convert into json format
   * If you are intersted in learning d3.js, this a good [tutorial](http://www.d3noob.org/2014/01/tree-diagrams-in-d3js_11.html) for understanding the building blocks of a decision tree. Here is another [tutorial](http://blog.pixelingene.com/2011/07/building-a-tree-diagram-in-d3-js/) focusing on building a tree diagram in d3.js.
* Chapter 8.1 of the Introduction to Statistical Learning also covers the basics of Classification and Regression Trees


## Class 16: Recommenders

* Recommenders (Guest Lecturer: [Sinan Ozdemir](https://generalassemb.ly/instructors/sinan-ozdemir/2644))
    * [Slides](slides/16_recommenders.pdf)
    * [Framework code](code/16_recommenders_class.py), [solution](code/16_recommenders_solution.py)


## Class 17: Ensembling

**Resources:**

* Leo Brieman's [paper](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf) on Random Forests
* yhat has a brief [primer](http://blog.yhathq.com/posts/random-forests-in-python.html) on Random Forests that can provide a review of many of the topics we covered today. 
* Here is a link to some Kaggle competitions that were won using [Random Forests](https://www.kaggle.com/wiki/RandomForests)
* Ensemble models... tend to strongly outperform their component models on new data. Doesn't this violate “Occam’s razor”? In this paper entitled: [The Generalization Paradox of Ensembles](http://datamininglab.com/media/pdfs/Paradox_JCGS.pdf) John Elder IV argues for a more refined understanding of model complexity. 


## Class 18: Ensembling Part 2, Python Companion Tools

* Ensembling
    * Review the Random Forest algorithm
    * Discuss tuning the Random Forest Algorithm
    * Give an overview of the AdaBoost algorithm
    * Implement boosted trees in Python
* IPython Notebook
    * [nbviewer](http://nbviewer.ipython.org/)
    * Biostatistics course: [GitHub repo](https://github.com/fonnesbeck/Bios366/tree/master/notebooks), [direct links to nbviewer](http://fonnesbeck.github.io/Bios366/lectures.html)
    * [A gallery of interesting IPython Notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)

**Resources:**

* Chapter 10 of the [Elements of Statistical Learning ](http://statweb.stanford.edu/~tibs/ElemStatLearn/) covers Boosting. See page 339 for the algorithm presented in class.
* Dr. Justin Esary has a nice [tutorial](https://www.youtube.com/watch?v=jAVHB3D04EY) on Boosting. Watch from 32:00 – 59:00 for relevant material. 
* Tutorial by Professor Rob Schapire of Princeston on the [AdaBoost Algorithm](http://www.cs.princeton.edu/~schapire/talks/nips-tutorial.pdf)
* IPython documentation in [website form](http://ipython.org/ipython-doc/stable/index.html) and [notebook form](http://nbviewer.ipython.org/github/ipython/ipython/blob/2.x/examples/Index.ipynb): does not focus exclusively on the IPython Notebook


## Class 19: Working a Data Problem

* [Kaggle: Avazu Click-Through Rate Prediction](http://www.kaggle.com/c/avazu-ctr-prediction)


## Class 20: Neural Networks

* Inspiration for Neural Networks
* Neural Networks
* Gradient Descent

**Resources:**

* Michael Neilson has a free book called [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) that gives thorough introduction to Neural Networks
* Geoffrey Hinton, one of the pioneers of the deep learning movement, has an entire class on Coursera called [Neural Networks for Machine Learning](https://class.coursera.org/neuralnets-2012-001/lecture)
* The Python wiki has a list of Python packages commonly used for [Neural Networks](https://wiki.python.org/moin/PythonForArtificialIntelligence)

**Homework:**

* Read this "classic" paper, which may help you to connect many of the topics we have studied throughout the course: [A Few Useful Things to Know about Machine Learning](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf)


## Class 21: Review

* Review of all of data science ([slides](slides/21_review.pdf))
* [Comparing supervised learning algorithms](https://docs.google.com/spreadsheets/d/16i47Wmjpj8k-mFRk-NnXXU5tmSQz8h37YxluDV8Zy9U/edit?usp=sharing)
* Special guest: Laura Lorenz

**Resources:**

* [scikit-learn "machine learning map"](http://scikit-learn.org/stable/tutorial/machine_learning_map/): Guide for choosing the optimal estimator
* [Choosing a Machine Learning Classifier](http://blog.echen.me/2011/04/27/choosing-a-machine-learning-classifier/): Short and highly readable
* [Machine Learning Done Wrong](http://ml.posthaven.com/machine-learning-done-wrong): Thoughtful advice on common mistakes to avoid in machine learning
* [Practical machine learning tricks from the KDD 2011 best industry paper](http://blog.david-andrzejewski.com/machine-learning/practical-machine-learning-tricks-from-the-kdd-2011-best-industry-paper/): More advanced advice than the resources above
* [An Empirical Comparison of Supervised Learning Algorithms](http://www.cs.cornell.edu/~caruana/ctp/ct.papers/caruana.icml06.pdf): Research paper from 2006
* [Getting in Shape for the Sport of Data Science](https://www.youtube.com/watch?v=kwt6XEh7U3g): 75-minute video of practical tips for machine learning (by the past president of Kaggle)
* [Resources for continued learning](resources.md)
* Bonus content (below)
* Keep using Slack!


## Class 22: Project Presentations

* Note: Guests are welcome! Invite your friends and family!


## Bonus Content

* [Python reference guide](code/99_python_reference.py)
* Regular expressions ("regex"):
    * Simple example of regex usage: [code](code/99_regex_example.py), [data](data/homicides.txt)
    * [Detailed reference guide](code/99_regex_reference.py)
    * [Python introductory lesson](https://developers.google.com/edu/python/regular-expressions)
    * [In-depth tutorials](http://www.rexegg.com/)
    * [Real-time regex tester](http://www.regexr.com/)
    * Fun example: [Exploring Expressions of Emotions in GitHub Commit Messages](http://geeksta.net/geeklog/exploring-expressions-emotions-github-commit-messages/)
* Tidy data
    * [Brief summary of tidy data](http://www.prometheusresearch.com/good-data-management-practices-for-data-analysis-tidy-data-part-2/)
    * Tidy data resources from Hadley Wickham: [detailed paper](http://www.jstatsoft.org/v59/i10/paper), [shorter version of the paper with more R code](http://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html), [slides](http://stat405.had.co.nz/lectures/18-tidy-data.pdf) from his class on tidy data, [video presentation](https://vimeo.com/33727555)
    * Examples: [tidy](https://github.com/fivethirtyeight/data/tree/master/bob-ross), [untidy](https://github.com/fivethirtyeight/data/tree/master/airline-safety), [very untidy](https://github.com/fivethirtyeight/data/tree/master/region-survey)
    * [Common issues](http://stats.stackexchange.com/a/83711/39543) with obtaining tidy data from Excel
* Reproducibility
    * [Overview of reproducibility and reproducible research](http://www.dataschool.io/reproducibility-is-not-just-for-researchers/)
    * [Twitter definition of reproducibility](https://twitter.com/jakevdp/status/519563939177197571)
    * [How to share data with a statistician](https://github.com/jtleek/datasharing): practical guide for turning raw data into tidy data in a reproducible and documented manner
    * [Example of reproducible data processing](https://github.com/fivethirtyeight/data/tree/master/classic-rock): includes raw data, processed data, processing scripts, and documentation
    * [Colbert on reproducibility](http://thecolbertreport.cc.com/videos/dcyvro/austerity-s-spreadsheet-error) (8-minute video)
* [Domino Data Lab](http://www.dominodatalab.com/)
    * Primary use cases: [run your model in the cloud](http://www.dominodatalab.com/benefits/model_development), [create a self-service web form](http://www.dominodatalab.com/benefits/web_forms) or [API](http://www.dominodatalab.com/benefits/web_services) that interacts with your model
    * [Usage rates](https://app.dominodatalab.com/usageRates) and [subscription pricing](http://www.dominodatalab.com/pricing)
    * [Command reference](http://help.dominodatalab.com/howToReference)
