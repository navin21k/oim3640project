### Authors: Navin Kheth and Xavier Torres

# Project Proprosal

## 1. The Big Idea

    The main goal for this project is to solve problems in the intersectionality of the Python programming and data science. We are both very interested in pursuing careers in big data and we hope to use this project as an opportunity to learn more about the utility of Python when it comes to working with big data structure. In this particular project, we will be working with Riot Games API to understand in depth the different predictive variables when it comes to winning in the company's PvP game, League of Legends. The extended scope of the project should also include a working GUI where users can interact with to learn about their chance of winning when they load into a game. 

## 2. Learning Goals

    The main learning goal of this project is to understand how to better utilize Python in a data science application. This comes with a few sub-goals such as automated data pulling from API's and learning how to use to data science focused packages such as Pandas and Numpy. We will also learn how to perform more extensive visualizations from the data, which can either be built into the Python codes and pulled into an external tool like Tableau. The next major goal is to familiarize ourselves with the software design aspect of this class. This includes learning how to build an interactive application where users can have input and navigate to different kind of information. This is also an opportunity to learn how to build GUI where we can learn some HTML and CSS.

## 3. Implementation Plan 
    The first thing that we wanted to do is start a project that both of us have an interest in. Both of us are interested in videogames, so we decided to look into api's that have to do with gaming. We found the Riot games api (https://developer.riotgames.com/)(20 reqs per second, 100 requs every 2 minutes). There are many API's that riot has and they give lots of information. This allows will allow us to access certain types of data from multiple games. Team Fight Tactics and League of Legends, Legend of RuneTerra and Valorant. Due to idea that we both had about predicting if a person should surrender or not we chose to use League of Legends. So a bit about our implementation plan: 1. we want to import data from one particular api(https://developer.riotgames.com/apis#league-v4), this will allow us to grab a large number of games from either a singular user or from the overall user base. 2. from there it will be decoded using the coding we learned about conversion to json and then we will look to include all this data to create a training set so that we can both visualize and create a model to be able to predict whether a game is worth playing or if the time you'll save by surrenderring is worth it in terms of possible LP (league points). This is one of the more important aspects for more professional or high ranking players. These players are constantly looking to optimze thier play to make sure they get to the top of the ladder(a leaderboard that includes the top players based on LP). This is only one our ideas that we wanted to work on, we also wanted to develop special visualizations for data that is directly related to the goal itself. things like xp per minute based on lane or place on the map, vision per minute, gold usage efficency, as well as other metrics that could be found to gain further explanation power for who wins and who doesn't.  

## 4. Project Schedule
    The final submission for this project is due on the 4/29 and it is current 4/7, meaning that we have about 3 weeks to complete everything. Due to the sped up timeline of the project, we have to make sure we setting up milestones appropriately. 

    **Week 1:** The first week will be focused on learning about the ins-and-outs of the API we will be working with to pull the appropriate data in the correct format for this project. We will then some early cleaning and analysis on this data to understand the potential limits and predictive power of different variables. We will also plan complete most of the predictive modeling by the end of this week.

    **Week 2:** The second week will a continuation of the modeling of the aspect and resolving any issues we run into. The majority of this week is then focus on building the front end of the application and determining where we want host it. Since this is the part we are least familiar with, we understand that we have to spend a lot of time doing research and learning as we go.

    **Week 3:** The third week is once again a continuation of building on the front end. Parts of this week will be allocated to prettifying the looks of the project and making sure the application itself is presentable. We will also last minute debugging and fixes if necessary. If we have enough time, we will plan on adding potential features to the application.

## 5. Collaboration Plan 
    Since this project is being completed by only two of us, we plan on performing coding in pairs whenever possible. This will allow us to efficiently collaborate on the codes without any lag in communications during the process. In the event that we cannot be in one place at once, we plan on splitting up the codes so that we don't work on the same features at once. If we have to work on the same file, we will work in cascade and communicating properly. We will also takes turn on leading the different aspect of the project. One person will take the responsibility for the analysis section and then we will switch so the other person will take a lead on building the GUI of the application. 

## 6. Risks

    The first major risk of the project is how wide the scope of the project is and how much we can accomplish in the span of 3 weeks. We are mitigating this risk by taking early actions and creating a solid plan of actions with reasonable timeline to make sure we are on track throughout the project. The second risk is the limit of what we can with the data available. We have been going over the documentation of the API and even though we are certain that we can most of the data we want, there are some data that we might need multiple workarounds to get access to it. The third and final risk is that at this point in time, we do not really possess the skills necessary to build a proper and presentable GUI. We betting on the fact that we can research the tools and learn how to use them as we go, but we do not know how to accurately calculate the time and effort necessary to perform these tasks.

### 7. Additional Course Content



The Big Idea: What is the main idea of your project? What topics will you explore and what will you generate? What is your minimum viable product? What is a stretch goal?
Learning Goals: Since this is a team project, you may want to articulate both shared and individual learning goals.
Implementation Plan: this will probably be pretty vague initially. Perhaps at this early juncture you will have identified a library or a framework that you think will be useful for your project. If you don't have any idea how you will implement your project, provide a rough plan for how you will determine this information.
Project schedule: You have 8 weeks (roughly) to finish the project. Sketch out a rough schedule for completing the project. Depending on your project, you may be able to do this in great specificity or you may only be able to give a broad outline. Additionally, longer projects come with increased uncertainty, and this schedule will likely need to be refined along the way.
Collaboration plan: How do you plan to collaborate with your teammates on this project? Will you split tasks up, complete them independently, and then integrate? Will you pair program the entire thing? Make sure to articulate your plan for successfully working together as a team. This might also include information about any software development methodologies you plan to use (e.g. agile development). Make sure to make clear why you are choosing this particular organizational structure.
Risks: What do you view as the biggest risks to the success of this project?
Additional Course Content: What are some topics that we might cover in class that you think would be especially helpful for your project?

software design and GUI


surrender scoring- time, what games should you surrender and which you should not. binning system, 1-10 ish. 