
# **Project Overview [~1 paragraph]**

*The data source that I used for this assignment is Wikipedia and the three different pages that I retrieved from Wikipedia were Batman Begins, The Dark Knight, and The Dark Knight Rises. In order to process these pages, I used multiple techniques such as counting number of words without stop words, similarity analysis, sensitivity analysis, bar graphs etc. In order to do the analysis, I had to use the MediaWiki library. So then, I read the documentation and found several functions such as wiki_page.summary and wiki_page.section(‘Plot’), which I decided to use in my analysis. Before diving into the analysis, my goal was to find out how similar were the movies in this Batman trilogy. Also, I wanted to compare how dark or negative the film is compared to its sequels/prequels based on their plots and summary. So by using the techniques mentioned above, I was able to derive results (which will be described below) and come to a conclusion.*

# **Implementation [~2-3 paragraphs]** 

*For this assignment, as mentioned above, through the use of the MediaWiki library, I was able to get access and information from the Wikipedia pages by inputting the title/page name. The majority of my variables use the data structures of lists, and dictionaries. This was easier for me because I was able to sort them with ease and I was also dealing with frequency of words. Also throughout my analysis, I used the for loop algorithm multiple times to go through the lists and dictionaries. For example, in order to get the top 10 words from a dictionary, I used a for loop to go through the dictionary.*

*For the design decisions, I could have chosen to analyze all the text in the Wikipedia page, but then I chose to focus only on the plot because that summarizes the film as a whole. The other sections included cast, production, release etc. I felt these were not relevant to what I was trying to illustrate through the code. Another place where I had multiple options was when I was trying to perform the similarity analysis. I used two different methods, which are associated with Difflib and Fuzz. At first, I used Fuzz ratio, but I was not confident with my results, so I decided to follow another approach and with the help of the internet, I found another function called Sequence matcher and this gave me the same result. Hence, I was then sure about my results.*

*Furthermore, in terms of design and architecture, I made sure that all functions return something except for the one with bar graph, which will display the bar graph at that same moment. I chose to have return everywhere for consistency purposes and to avoid confusion. Now, for the advanced algorithms, I used the sentiment analyzer which is from the nltk library, the similarity analyzer which is from the Difflib and Fuzz library, and the bar graph which is from the Matplotlib library. For instance, the similarity analyzer uses the Levenshtein Distance to calculate the distance between two strings. The sentiment analyzer gives a breakdown of the string in positive, negative, and neutral percentage, which sum up to 100%. Lastly, the bar graph is simple to code as it requires the x values, y values, and title to produce a simple, but effective way of representing results.*

# **Results [~2-3 paragraphs + figures/examples]** 

*The first text analysis that I performed is finding the frequency of the words in the movie plot. Using the process_text_plot function, I was able to create a dictionary which would have the keys as the words in the plot and the values as the number of times they were used in the plot. This was done after cleaning and removing the stop words. For example, here is an image of the text analysis for Batman Begins and the dictionary it returns:*

![](images/Batman%20Begins%20Word%20Dictionary.png)

*The second text analysis that I perfomed is using the above dictionary and finding the top 10 common words. I did this after converting the dictionary into a list. I used a for loop and iterated through the dicitonary and appended items into the list and returnd a list with frequency, word tuples. For example, here is an image of the top 10 words for Batman Begins:*

![](images/Batman%20Begins%20Top%2010%20Words.png)

*The third text analysis that I performed is using all three movie plots in the form of three different strings. I did a sentiment analysis for each plot and the results showed that The Dark Knight Plot was had the most negative words out of all three, but it also had the most positive words out of all three. So, this suggests that the story is darker than the rest, but also has a sense of hope or love in that movie, which is true because of the whole dynamic between Harvey Dent, Batman and Rachel. The fact that neutral is the majority also could imply that the plot doesn't give much away to the readers and encourages them to watch the movie. Here is the sentiment analysis for reference:*

![](images/Sentiment%20Analysis.png)

*The fourth text analysis that I performed is the similarity analysis. For this I had to use the Fuzz Ratio and Sequence Matcher. The results show that only 1%-2% of the plots are similar. At first even I was confused, but then it made sense because the plots are not meant to be similar, otherwise it would not be a great movie. The 1%-2% that is similar are the common words which are used across all three plots and can be seen in the next paragraph. Here is the similarity analysis.*

![](images/Similarity%20Analysis.png)

*The fifth text analysis that I performed is finding the words that are common across all three plots and referring to the paragraph above, the 1%-2% that is similar are below. These results make sense because they describe what batman is with using words such as hero, crime etc. Therefore, I can also approximately check if this right by reading all three plots and I can confirm that these words are common:*

![](images/Common%20words%20in%20three%20plots.png)

*Lastly, I performed an extra analysis using the visualization technique in Python. I made a bar graph of the top 10 words used in the plot as seen in the analysis above. The y axis is the frequency of the word and the x axis are the common words. For instance, here is the bar graph for Batman Begins: *

![](images/Batman%20Begins%20Bar%20Graph.png)

*Note: For the remaining results for The Dark Knight and The Dark Knight Rises, please run the code, as these are taken for reference purposes only.*

# **Reflection [~1 paragraph]**

*In terms of the process, something that went well is my organization of code. For this assignment, I made sure that I created different functions for each and every action. By doing this, it helped me avoid unnecessary duplication of code and this made my code run faster as well. In terms of improvement, I can definitely try to implement more complex functions for text analysis. For example, next time, I would try implementing the Markov Text Synthesis and Text clustering. But I believe that will come with more practice. Also I think this project is appropriately scoped for the level we are at right now because we are given certain resources from class and we are also given the freedom to implement techniques of our choice. During the process of this assignment, there was a lot of testing involved. For each function, I made sure to test it with all 3 movies and only proceeded ahead after I got the results I needed. Going forward, I see the application of text analysis in analyzing essay similarity between students for plagiarism and also between books by the same author to understand their writing style. Moreover, since I chose to analyze the plot of movies, there wasn’t a big part of emotion displayed, but filled with facts instead. So, in the future, I would analyze the reviews for this movie or even emotional articles/journals. Lastly, something that I wish I knew before starting would be the extent to which I can use the different libraries and also the different types of errors. Reading the documentation of each library is one thing, but implementing them is completely different. And for errors, I had to google what they meant and it took me quite a while to get the solution because Python has several versions as well. But overall, this assignment allowed me to think deeply in regards to different types of analysis and I was very happy with what I achieved.*
