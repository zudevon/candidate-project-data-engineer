## Introduction
Welcome to Aspen Capital's Data Engineering challenge. This assignment will help us better assess your technical skills. We recommend that you focus on the requirements listed below and if time permitting - work on any additional features (of your own choosing).

## Background
One aspect of this job is the forecasting of payments, and for this exercise, we need to create a payment schedule. Part of the schedule is projected, and the other is actual payments. We need to line up projection and actual payments given the provided database schema.

## Requirements
### High Level
* Given the provided scripts (./data/init.sql), create software that will display the following chart:

### Example (given sample data)
|Projection | Month/Year  | Activity   | Estimated | Actual | Estimated Balance
|---------- | ----------- | --------   | --------- | ------ | ----------------- |
|1|
|| April 2019  | Deposit: Insurance    | $54.95    |
||             | Withdrawal: Insurance | $-1.81   | $-2.04    | $214.85
|| May 2019    | Deposit: Insurance    | $54.95    |
||             | Withdrawal: Insurance | $-1.81   | $-2.27    | $267.99
|| June 2019   | Deposit: Insurance    | $54.95    |
||             | Withdrawal: Insurance | $-1.81   | $-2.18    | $321.13
|| July 2019   | Deposit: Insurance    | $54.95    |
||             | Withdrawal: Insurance | $-1.81   | $-2.26    | $374.27
|| August 2019 | Deposit: Insurance    | $54.95    |
||             | Withdrawal: Insurance | $-1.81   | $-9.38    | $427.41
||             | Withdrawal: Insurance |          | $-9.38    |
||             | Withdrawal: Insurance |          | $-9.38    |
||......|......|......|......
||......|......|......|......
|2|......|......|......|......
||......|......|......|......
||......|......|......|......

## Hints
* You can assume there are only 12 months of data in a single projection.
* This needs to work on a large number of rows (Only example data provided).
* It is ok to choose any database technology.
* Do your best with the information available.

## Bonus Points
* Provide the ability to run your solution.
* High level data injection design.
* Alternative solution to this type of schema and a possible path to migrate it.

## Submission
* Your submission should be accessible in a public git repository that includes a README.md with all the pertinent information of how to run your application. The expectation is that we can easily follow the steps provided and run the application without much leg/guesswork.
* If your submission does include additional artifacts that are not represented within the repository - the README should provide information on how to retrieve and access these items.
