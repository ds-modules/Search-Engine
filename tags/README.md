# Tags for Respositories

The `tags.json` file includes data for each _public_ repository owned by `ds-modules`. 



Each key is the name of a `ds-modules` repository, and each value contains a dictionary of the following form: 

```json
{   ...,
    "<course_name>" : {

        "name" : "<course_name>",
        "department": "<department_name>",
        "course_number": "<course_name>",
        "semester": "<course_semester>",
        "prerequisites": [
            "<prereq1>",
            "<prereq2>",
            ...
        ],
        "domain": null,
        "technologies": [
            "<tech1>",
            "<tech2>",
            ...
        ],
        "concepts": [
            "<tech1>",
            "<tech2>",
            ...
        ],
        "professor": "<prof_name>",
        "is_course": true | false
    }
    ...
}
```

Reference the explaination of each field below:

| Name                      | Type        | Explaination                        | Example                              |
| ------------------------- | ----------- | ----------------------------------- | ------------------------------------ |
| `course_name`             | `str`       | Name of the course                  | `"Foundations of Data Science"`      | 
| `department_name`         | `str`       | Name of the department              | `"Data Science"`                     |
| `course_number`           | `str`       | Course number                       | `"4AC"`                              |
| `course_semester`         | `str`       | Semester the course was taught      | `"Fall 2020"`                        |
| `domain`                  | `str`       | Domain of the course                | `"Social Science"`                   |
| `prereq1, prereq2, ...`   | `List[str]` | Prerequisite for the course         | `["Data 8", "CS 61A", ...]`          |
| `tech1, tech2, ...`       | `List[str]` | Technologies used in the course     | `["pandas", "numpy", ...]`           |
| `concept1, concept2, ...` | `List[str]` | Concepts covered in the course      | `["correlation", "regression", ...]` |
| `prof_name`               | `str`       | Name of the professor               | `"John DeNero"`                      |
| `is_course`               | `bool`      | Whether the repo is a course or not | `true`                               |