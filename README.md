# Bug-Detection-in-code
Used CNN to build a model that detected the type of bug present in a given code snippet. 
Dataset used: https://github.com/microsoft/InferredBugs/blob/main/README.md
A bit about the dataset and how I used it:  The dataset was originally in JSON format. The bug.json file is treated as a dictionary and various fields like bug_class, severity, kind, visibility and bug_type are extracted from it. The dataset also contains method_before file that contains the buggy code segments. All these fields were extracted and a csv file was generated for further processing. The target label bug_type has mainly 3 types of bugs: NULL_DEREFERENCE, RESOURCE_LEAK and THREAD_SAFETY_VIOLATION which will be detected during model testing.
