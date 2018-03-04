# TidyPlus: a tool for data wrangling

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

[![HitCount](https://hitt.herokuapp.com/tidyplus_python.svg..)](https://github.com/tidyplus_python)

[![GitHub commit](https://img.shields.io/github/commits-since/UBC-MDS/tidyplus_python/v0.svg)](https://github.com/UBC-MDS/tidyplus_python/commit)

[![Downloads](https://img.shields.io/github/downloads/UBC-MDS/tidyplus_python/total.svg)](https://github.com/UBC-MDS/tidyplus_python/graphs/traffic)

[![forks](https://img.shields.io/github/forks/UBC-MDS/tidyplus_python.svg)](https://github.com/UBC-MDS/tidyplus_python/network)

[![issues](https://img.shields.io/github/issues/UBC-MDS/tidyplus_python.svg)](https://github.com/UBC-MDS/tidyplus_python/issues)


## Contributors:

* `Akshi Chaudhary` : [@akshi8](https://github.com/akshi8)
* `Tina Qian` : [@TinaQian2017](https://github.com/TinaQian2017)
* `Xinbin Huang`: [@xinbinhuang](https://github.com/xinbinhuang)

## Latest

* Date : Feb 11, 2018
* Release : v1.0

## About

The `tidyplus` package is an essential data cleaning package with features like `missing value treatment`, `data manipulation` and displaying data as `markdown table` for documents. The package adds a few additional functionalities on the existing data wrangling packages (i.e. Pandas). The objective of this package is to provide a few specific functions to solve some of the pressing issues in data cleaning.



## Functions included:
Three main parts including different functions in `tidyplus`
- `Data Manipulation` : Datatype cleansing
  - `typemix`
    * The function helps to find the columns containing different types of data, like character and numeric. The input of the function is a data frame, and the output of the function will be a list of 3 data frames.
  - `cleanmix`
    * The function helps to clean our data frame. After knowing the location of discrepancy of data types, one can use this function to keep a type of data in certain columns. Here, the input will be the output by `typemix` function, name of the column (a vector of the name of columns) that they want to clean, the type of data they want to work on, and if we want to keep or delete the certain type. The output will be a data frame like the original one but with specified data type in certain columns deleted.

- `Missing Value Treatment` : Basic Imputation and EM Imputation -`em` and  `mmm`
    * Basic Imputation: function used `mmm` replace missing values in a column of a dataframe, or multiple columns of dataframe based on the `method` of imputation

      - (Method = 'Mean') replace using mean
      - (Method = 'Median') replace using median
      - (Method = 'Mode') replace using mode
    * EM Imputation: **Bonus** function used `em` (method = "EM")
      - Uses EM(Expectation- Maximization) algorithm to predict the closest value to the missing value
      - Can be used for both numeric and categorical predictions
- `Markdown Table`:
  - `md_new()`: This function creates a bare bone for generating a markdown table. Alignments, padding, and size of the table can be input by users.
  - `md_data()`: This function converts a dataframe or matrix into a markdown table format.
  - `md_reg()`: This function converts a regression model object into a nice-formatted markdown table.


## Used Scenario

Using Data Manipulation functionalities

  * Users can use the package when they want to clean and wrangle their data. For example, if the data has not been cleaned yet, users can use function `typemix` to check where data is not clean and use `cleanmix` to clean data. Based on personal work experience, the mix of number and character is usually seen in the data collected from the survey. After clean data is ready, one can use the `Missing Value Treatment` to deal with missing data by EM algorithm. The `emphasizeon` function can be used to highlight the factors that he is interested in. After the wrangling of data, one can use function `Markdown Table` to output the data frame in a markdown format.


## Existing features in Python ecosystem similar to `tidyplus`

* Data Manipulation
  - [Pandas:string processing](http://pandas.pydata.org/pandas-docs/stable/missing_data.html#string-regular-expression-replacement) function and [Pandas:string processing](http://pandas.pydata.org/pandas-docs/stable/missing_data.html#string-regular-expression-replacement). [Brief Version](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Pandas_Cheat_Sheet_2.pdf) The existing pandas version doesn't have a functionality to explicitly perform string processing/datatype conversion without affecting the overall column type (which is inconvenient when you have really messed up data with mix of strings and numbers)
* Missing Value treatment
  - Python doesn't have imputation methods which use `EM algorithm` for missing value treatment, which in fact is very efficient and accurate [Imputation methods in python](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Imputer.html#sklearn.preprocessing.Imputer)
* Markdown table in Python
  * Python doesn't have a package or library which can output a dataset in the form of a markdown table (User defined)

## Ideas subject to change

* As a part of the initial proposal, the above ideas can be implemented. However, some functionalities are subject to change based on the project timeline or technical complexity

## License
[MIT](LICENSE.md)

## Contributing
This is an open source project. Please follow the guidelines below for contribution.
  - Open an issue for any feedback and suggestions.
  - For contributing to the project, please refer to [Contributing](CONTRIBUTING.md) for details.
