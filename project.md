# Course Project


## Overview

The final project should represent significant original work applying data science techniques to an interesting problem. Final projects are individual attainments, but you should be talking frequently with your instructors and classmates about them.

Address a data-related problem in your professional field or a field you're interested in. Pick a subject that you're passionate about; if you're strongly interested in the subject matter it'll be more fun for you and you'll produce a better project!

To stimulate your thinking, here is an excellent list of [public data sources](public_data.md). Using public data is the most common choice. If you have access to private data, that's also an option, though you'll have to be careful about what results you can release. You are also welcome to compete in a [Kaggle competition](http://www.kaggle.com/) as your project, in which case the data will be provided to you.

You should also take a look at [past projects](https://github.com/justmarkham/DAT-project-examples) from other GA Data Science students, to get a sense of the variety and scope of projects.


## Project Deliverables

You are responsible for creating a **project paper** and a **project presentation**. The paper should be written with a technical audience in mind, while the presentation should target a more general audience. You will deliver your presentation (including slides) during the final week of class, though you are also encouraged to present it to other audiences.

Here are the components you should aim to cover in your paper:

* Problem statement and hypothesis
* Description of your data set and how it was obtained
* Description of any pre-processing steps you took
* What you learned from exploring the data, including visualizations
* How you chose which features to use in your analysis
* Details of your modeling process, including how you selected your models and validated them
* Your challenges and successes
* Possible extensions or business applications of your project
* Conclusions and key learnings

Your presentation should cover these components with less breadth and depth. Focus on creating an engaging, clear, and informative presentation that tells the story of your project.

Your project paper, presentation slides, and code should be included a **GitHub repository**, along with all of your data and a data dictionary. If it's not possible or practical to include your data, you should link to your data source and provide a sample of the data (anonymized if necessary).

Optionally, it would be exciting to actually implement a "live" system based on your work, and to the degree this is possible within the time frame of the course, it is certainly encouraged!


## Milestones

### Week 3 (10/21): Question and Data Set(s)

What is the question you hope to answer? What data are you planning to use to answer that question? What do you know about the data so far? Why did you choose this topic?

Example:
* I'm planning to predict passenger survival on the Titanic.
* I have Kaggle's Titanic dataset with 10 passenger characteristics.
* I know that many of the fields have missing values, that some of the text fields are messy and will require cleaning, and that about 38% of the passengers in the training set survive.
* I chose this topic because I'm fascinated by the history of the Titanic.

### Week 5 (11/4): Data Exploration and Analysis Plan

What data have you gathered, and how did you gather it? What steps have you taken to explore the data? Which areas of the data have you cleaned, and which areas still need cleaning? What insights have you gained from your exploration? Will you be able to answer your question with this data, or do you need to gather more data (or adjust your question)? How might you use modeling to answer your question?

Example:
* I've created visualizations and numeric summaries to explore how survivability differs by passenger characteristic, and it appears that gender and class have a large role in determining survivability.
* I estimated missing values for age using the titles provided in the Name column.
* I created features to represent "spouse on board" and "child on board" by further analyzing names.
* I think that the fare and ticket columns might be useful for predicting survival, but I still need to clean those columns.
* I analyzed the differences between the training and testing sets, and found that the average fare was slightly higher in the testing set.
* Since I'm predicting a binary outcome, I plan to use a classification method such as logistic regression to make my predictions.

### Week 8 (11/25): First Draft Due

Submit a rough copy of your work so far, including code, narrative, and visualizations. Describe your successess and challenges, and provide a detailed plan going forwards. Your peers and instructors will provide feedback.

### Week 10 (12/9): Second Draft Due

Submit a more polished version of your work, including drafts of your paper and your presentation. Your instructors will provide feedback.

### Week 11 (12/16): Presentation

Deliver your project presentation and submit all required deliverables (paper, slides, code, data, and data dictionary).
