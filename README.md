# Bug Detection in Code

## Overview
This project utilizes a Convolutional Neural Network (CNN) to build a model capable of detecting the type of bug present in a given code snippet.

## Dataset
The dataset used for this project is sourced from Microsoft's [InferredBugs Repository](https://github.com/microsoft/InferredBugs/blob/main/README.md). It contains detailed information about various types of bugs in JSON format.

### Dataset Description
- **bug.json**: Acts as a dictionary with fields such as:
  - **bug_class**: The class of the bug.
  - **severity**: The severity level of the bug.
  - **kind**: The category of the bug.
  - **visibility**: The visibility level of the bug.
  - **bug_type**: The target label representing the type of bug.
- **method_before**: Contains the buggy code segments.

### Processing the Dataset
1. The dataset, originally in JSON format, was preprocessed to extract relevant fields from `bug.json`.
2. Key fields like `bug_class`, `severity`, `kind`, `visibility`, and `bug_type` were extracted.
3. The `method_before` file was parsed to retrieve buggy code segments.
4. All extracted fields were consolidated into a CSV file for further processing and model training.

### Target Labels
The `bug_type` field serves as the target label for classification and includes the following types of bugs:
- **NULL_DEREFERENCE**
- **RESOURCE_LEAK**
- **THREAD_SAFETY_VIOLATION**

## Model
A Convolutional Neural Network (CNN) was implemented to classify the type of bug based on the provided buggy code snippet. During testing, the model identifies and categorizes bugs into one of the three defined target labels.

## Features
- End-to-end pipeline for preprocessing JSON data into a structured format.
- Automated detection of bug types using deep learning techniques.
- Focus on three critical bug categories that are common in software development.

## References
- [Microsoft InferredBugs Repository](https://github.com/microsoft/InferredBugs)


