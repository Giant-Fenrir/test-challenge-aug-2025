# Test Challenge

Congratulations on being selected to participate in our technical test. It consists of a test challenge and it will address different skills. Read the instructions carefully and we wish you the best of luck.

## Introduction

We want you to test a web project that makes uses of the FIFA 21 dataset. The details of the requirements are given below. Please pay attention to the details available in the source-code of the project, since you are responsible for building it from scratch.

## Project Information

This project is a web project, consisting of a front-end and a back-end, which are used to consume processed data from the FIFA 21 dataset.

### Preparing the Data

The first goal of this project is to obtain and prepare the data you will work with.

The dataset is [available in this repository](https://github.com/kavlac/test-challenge-november-2021/blob/main/source-code/players_21.zip).

### Making the Data Available

The second goal of this project is to make the processed data available for consumption.

To do so, a REST API was implemented and it should provide the following methods:

- List all players (using pagination): we want to know what players are stored in your database;
- List players by name: given a name, we want to know what players match such name;
- List players by team: given a team, we want to know what players match such team;
- List players by league: given a league, we want to know what players match such league;
- List players by nationality: given a nationality, we want to know what players match such nationality;
- List players by position: given a position, we want to know what players match such position;
- List player details: given an id, we want to know the most relevant details of the player (including their picture) that matches such id;
- List top-K players: given an integer K, we want to know the best K players according to their overall;
- List top-K players by position: given an integer K and a position, we want to know the best K players that match such position;
- List top-K players by nationality: given an integer K and a nationality, we want to know the best K players that match such nationality;
- List top-K players by league: given an integer K and a league, we want to know the best K players that match such league;
- List the best team: we want to know the best players that can form a squad;
- List the best team by league: we want to know the best players that can form a squad;
- List the best team by nationality: we want to know the best players that can form a squad.

### Consuming the Data

The third goal of this project is to consume the methods of the REST API via a front-end application.

## Deliverables

You must provide the following artifacts:

- All the test cases that you believe are needed to cover the requirements above;
- A test report, with your technical statement whether the application successfully meets the requirements or not;
- A list of all the bugs you have found (including your severity analysis);
- Any other artifact you find relevant for your overall evaluation.

## Tips

- In case you have any suggestion/improvements to the app, feel free to share;
- Automation is mandatory. You are free to choose black-box or white-box implementations though;
- Choose any template for your artifacts freely.
