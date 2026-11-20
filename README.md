# Schedule Planner Assistant - Independent Idea

## Team
- Anand Raju: Planner and Learning
- John Galeas-Zhuang: Data
- Nel Quintanilla: Interface and Evaluation

## Overview
We plan to build a class schedule planner that is optimized to fit a student’s courses around their daily life; this would include: sleep, work shifts, and other preferences like walking distance between classes etc. 

## How it works
1. The student enters their classes, work shifts, and sleep schedule.
2. The planner builds every valid schedule and filters out impossible or unhealthy ones.
3. The student picks between two schedules.
4. Each pick updates the planner's feature weights, so the planner keeps improving.

## How we measure improvement
We will compare the planner against one that never learns, using the prediction accuracy as our number to be tracked over test pairs. The test pairs are never used during learning, so the planner cannot memorize them. As far as the graph the x-axis is our number of picks, the y-axis is the prediction accuracy with one line for each planner. We expect the planner that never learns to stay stagnant while our planner rises.

## Data sources
- Degree requirements: catalog.mtsu.edu
- Class times: PipelineMT class search (course info only, no personal student data)
- Buildings: MTSU campus map and Google Maps
- CSCI class sections for Spring 2027 were collected from PipelineMT class search on November 19th, 2026

*Unoffical student project for CSCI 4350.*
