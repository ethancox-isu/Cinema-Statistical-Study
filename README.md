# Cinema-Statistical-study
Hypothesis testing and statistical analysis using Python libraries.

# Introduction
Movie production companies communicate through multimodal marketing to engage as wide an audience as possible and make as much money as possible. They market their movie through digital marketing, events, merchandise, partnerships, and traditional methods (billboards, posters, etc.). Their audience is the general movie-goers, who are targeted to obsess over the next blockbuster.

# Research Question
Is there a significant statistical difference between the profits of movies before the COVID-19 Pandemic (2018) and after (2022)?

# Description
This question interests me because I like movies and I’ve wondered if movie theaters are significantly dying post-pandemic, in part due to new streaming services and home-releases. I chose 2018 and 2022 specifically because the year is just before the pandemic or just after theater re-openings, respectively. I also think it will be interesting to see if people are getting burnt out from the growing number of blockbusters being released year-round. My claim is that there is a significant statistical difference because of singular profit and budget reports I have read over the last few years, as well as the general discussion about theater attendance post- pandemic. In my opinion, the growth of the blockbuster has been a major issue these last 20 or so years. In the 90’s, 80’s and 70’s, blockbusters were special summer events, and now they multiple release monthly year-round. This is not an isolated issue but is indicative of the larger factors affecting the economy, such as corporate greed, dissent from creativity, mass-production, and the turn from art to “content”/products. However, good movies made by passionate filmmakers are still being made but are just becoming harder and harder to find. You would think from my claims that I prefer solely older movies, but my 2nd favorite movie came out in just 2022 (Aftersun by Charlotte Wells). Going into this study, I don’t think my claim will be disproven, but I am excited to see the specific statistical findings for movies in these two years, like which ones made a lot of profit while only working with a smaller budget compared to others on these lists.

# Experiment Population
All movies released in 2018 and 2022.

# Sample Space
- Highest profit movies (proCt includes international box office and home-release sales)
- Top 35 highest profit movies from 2018 Top 35 highest profit movies from 2022

# Variable
Average movie profit for 2018 and 2022.

# Data Collection Plan
I am only considering the total profit a movie makes in its theatrical run & home-release, not its exact total grossing sales. It is important to consider the amount of money it takes to produce each movie, since growing budgets is a factor in the “blockbuster-fatigue” conversation. So, I will be using this equation to calculate the profit per movie: Average Profit = Total Gross - Budget x 2. All total grossing sales are officially recorded online, which I will record using an Excel spreadsheet and record my sources. I am only considering the top 35 highest proCting movies from 2018 and 2022 because if I were to randomly choose 35 movies from each year, major bias will be introduced because of factors like season release (non-summer or non-festival), studio production (independent?), set-aside marketing budget, and audience variety (ex. indie horror Vs. Marvel). I will also make a note in my project of the number of movies each year that had a budget of over $100 Million, since the highest grossing most likely have medium to large budgets.

# Method
I conducted my research by using boxofficemojo to find the box office reports for each movie and the-numbers to find the budget reports for each movie. These were the best websites I could find that provided the information I needed. I had to manually search for each of the 70 movies twice, so 140 Excel values were manually entered, where the number ranged from a few million to a billion. Once these values were recorded, I had to create a custom formula to create the two new proCt columns. Since the proCt values were in the millions, it would have taken hours for me to enter them all into my graphing calculator, so I first copied the profit columns into the Notepad app to arrange them into a list than used a website (https://www.statology.org/two-sample-t-test-calculator/) to perform t-test for me.

# Data Collection
Box office reports: https://www.boxofficemojo.com/year/world/2018/ (IMDbPro Verified) Production budget reports: https://www.the-numbers.com/movie/budgets (Studios Directly
Partnered)

# Findings
μ_1 equals movies from 2018 and μ_2 equals movies from 2022.

H_0: μ_1 = μ_2
H_1: μ_1 ≠ μ_2 (Claim)

At α = 0.5, can it be concluded that there is a significant statistical difference between the average profits of movies from 2018 and movies from 2022?

Test Value:
Formula: 2SampTtest: t = ((396408348.28571-242609351.91429)-(0-0))/
√(〖310361561.08253〗^2/35+〖321126040.39203〗^2/35) = 2.008076

P-Value (Two-Tailed): 0.048610
P-Value (0.048610) < α (0.05) = We Reject H_0

Conclusion: At the 5% significance level, there is enough evidence to suggest a statistical difference between the average profits of movies before COVID-19 (2018) and after (2022). This supports my claim that there is a significant difference, proving that movie theaters are declining in popularity post-pandemic since the average mean of profit from 2018 movies is significantly higher than that of movies in 2022.
