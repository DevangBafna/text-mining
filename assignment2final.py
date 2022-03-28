import matplotlib.pyplot as plt
import difflib
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from thefuzz import fuzz
import string
from mediawiki import MediaWiki
import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')

wikipedia = MediaWiki()  # creating a class from the MediaWiki class

def get_wikipedia_page(page_name):
    '''Retrieve wikipedia page from the name of the page'''

    wikipedia_page = wikipedia.page(page_name)
    return wikipedia_page # returns the wikipedia page


def get_wikipedia_page_summary(movie):
    '''Retrieves the summary of the wikipedia page'''

    # retrieve summary of the page (first section) using this code
    movie_summary = movie.summary
    return movie_summary  # returns a string of summary


def get_wikipedia_page_plot(movie):
    '''Since it is a movie, it retrieves the plot of the wikipedia page, it will retrieve the section from the parameter'''

    # retrieve summary of the section called 'Plot' using this code
    movie_plot = movie.section('Plot')
    return movie_plot  # returns a string of plot


def process_text_plot(plot):
    """Makes a histogram that contains the words from the plot. Returns: map from each word to the number of times it appears."""

    # create a dictionary for the histogram
    hist_plot = {}

    strippables = string.punctuation + string.whitespace

    # split the string into a list of words
    plot = plot.split()

    for word in plot:
        # word could be 'Sussex.'
        # remove the strippables like space, commas
        word = word.strip(strippables)
        # lowercase the word
        word = word.lower()

        # update the dictionary
        hist_plot[word] = hist_plot.get(word, 0) + 1

    return hist_plot


def total_words_without_stopwords(hist):
    """Returns the total number of words without stopwords in the plot using histogram from above (dictionary)."""

    result = 0
    # for loop through all the values in the dictionary and sum it up
    for v in hist.values():
        result = result + v
    return result


def different_words(hist):
    """Returns the number of different words in the plot."""

    return len(hist)


def most_common(hist):
    """Makes a list of freq-word pairs in descending order of frequency. hist: map from word to frequency returns: list of (frequency, word) pairs"""

    lst = []
    for word, frequency in hist.items():
        lst.append((frequency, word))
    lst.sort(reverse=True)
    return lst


def top_10_words(hist, num=10):
    """Returns a dictionary with top 10 commons words, num suggests how many words is printed"""

    dict_top_10 = {}
    lst = most_common(hist)
    for i in range(num):
        dict_top_10[lst[i][1]] = lst[i][0]

    return dict_top_10


def sentiment_analysis(plot):
    '''Returns a sentiment analysis score for the string passed as parameter, neg suggests negative, neu suggests neutral, and pos suggests positive'''

    score = SentimentIntensityAnalyzer().polarity_scores(plot)
    return score


def cleaning_text(plot):
    '''Returns a cleaned up version of the text/plot given in parameter by taking out the basic punctuation, and lowering text and removing stopwords as well'''

    plot.strip()
    plot.strip("\n")
    text_clean_movie = "".join([i.lower()for i in plot if i not in string.punctuation])
    text_clean_movie_without_stopwords = ' '.join([word for word in text_clean_movie.split() if word not in stopwords.words("english")])

    # took help from https://stackoverflow.com/questions/19560498/faster-way-to-remove-stop-words-in-python
    # took help from https://www.analyticsvidhya.com/blog/2020/11/text-cleaning-nltk-library/
    # I wanted to use the nltk library as that saves time insteaf of importing stopwords into the code

    return text_clean_movie_without_stopwords


def similarity(plot1, plot2):
    '''Returns a distance between two texts/strings calculated using Levenshtein Distance which is in the Fuzz library and Difflib library, higher the score the more similar they are'''

    result = fuzz.ratio(plot1, plot2)
    result_2 = difflib.SequenceMatcher(None, plot1, plot2)
    return result, round(result_2.ratio() * 100, 2)


def bar_graph(title, dict_top_10):
    '''Shows a bar graph of the top 10 words in the plot/text of the movie'''

    # took help from https://www.tutorialspoint.com/plot-a-bar-using-matplotlib-using-a-dictionary

    names = list(dict_top_10.keys())
    values = list(dict_top_10.values())

    plt.bar(range(len(dict_top_10)), values, tick_label=names, )
    plt.title(title)
    plt.show()

# def word_bubble(dict_top_10):
#     '''Generate a word bubble with top 10 common words for each plot with size of words relative to their frequency'''

#     wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(dict_top_10)

#     plt.figure(figsize=(15,8))
#     plt.imshow(wordcloud)

# I tried creating a word cloud but apparently this module is not supported for python 3.7 and above


def common_words_in_plots(plot1, plot2, plot3):
    '''Finds out the common words excluding stop words across all 3 plots, returns list of the words'''

    lst = []
    for i in plot1.keys():
        if i in plot2.keys() and i in plot3.keys():
            lst.append(i)

    return lst


def main():
    '''Main function of the python code, this will be run first'''

    movie_1 = get_wikipedia_page('Batman Begins') # get the wikipedia page from the page name
    movie_2 = get_wikipedia_page('The Dark Knight (film)')
    movie_3 = get_wikipedia_page('The Dark Knight Rises')

    movie_1_plot = get_wikipedia_page_plot(movie_1) # movie plot from wikipedia page
    movie_2_plot = get_wikipedia_page_plot(movie_2)
    movie_3_plot = get_wikipedia_page_plot(movie_3)

    text_clean_movie_1 = cleaning_text(movie_1_plot)  # cleaned version of plot
    text_clean_movie_2 = cleaning_text(movie_2_plot)
    text_clean_movie_3 = cleaning_text(movie_3_plot)

    movie_1_hist = process_text_plot(text_clean_movie_1)  # frequency of words in plot
    movie_2_hist = process_text_plot(text_clean_movie_2)
    movie_3_hist = process_text_plot(text_clean_movie_3)

    movie_1_most_common = most_common(movie_1_hist) # most common words in plot in descending order of frequency
    movie_2_most_common = most_common(movie_2_hist)
    movie_3_most_common = most_common(movie_3_hist)

    movie_1_plot_total = total_words_without_stopwords(movie_1_hist)  # total words without stopwords
    movie_2_plot_total = total_words_without_stopwords(movie_2_hist)
    movie_3_plot_total = total_words_without_stopwords(movie_3_hist)

    movie_1_plot_different = different_words(movie_1_hist)  # total amount of different words
    movie_2_plot_different = different_words(movie_2_hist)
    movie_3_plot_different = different_words(movie_3_hist)

    movie_1_top_10_words = top_10_words(movie_1_hist)  # top 10 words by frequency in movie plot
    movie_2_top_10_words = top_10_words(movie_2_hist)
    movie_3_top_10_words = top_10_words(movie_3_hist)

    movie_1_sentiment_analysis = sentiment_analysis(movie_1_plot)  # sentiment analysis of plot
    movie_2_sentiment_analysis = sentiment_analysis(movie_2_plot)
    movie_3_sentiment_analysis = sentiment_analysis(movie_3_plot)

    movie_1_similarity_with_movie_2 = similarity(text_clean_movie_1, text_clean_movie_2)  # similarity between plots
    movie_1_similarity_with_movie_3 = similarity(text_clean_movie_1, text_clean_movie_3)
    movie_2_similarity_with_movie_3 = similarity(text_clean_movie_2, text_clean_movie_3)

    common_words_in_all_3_plots = common_words_in_plots(movie_1_hist, movie_2_hist, movie_3_hist) # common words across all 3 plots

    print('\n')
    print(f'The word, frequency pair dictionary for Batman Begins Plot is: {movie_1_most_common}')
    print('\n')
    print(f'The word, frequency pair dictionary for The Dark Knight Plot is: {movie_2_most_common}')
    print('\n')
    print(f'The word, frequency pair dictionary for The Dark Knight Rises Plot is: {movie_3_most_common}\n')

    print(f'The total amount of words without stopwords in Batman Begins Plot is: {movie_1_plot_total}')
    print(f'The total amount of words without stopwords in The Dark Knight Plot is: {movie_2_plot_total}')
    print(f'The total amount of words without stopwords in The Dark Knight Rises Plot is: {movie_3_plot_total}\n')

    print(f'The total amount of different words in Batman Begins Plot is: {movie_1_plot_different}')
    print(f'The total amount of different words in The Dark Knight Plot is: {movie_2_plot_different}')
    print(f'The total amount of different words in The Dark Knight Rises Plot is: {movie_3_plot_different}\n')

    print(f'The top 10 most common words in Batman Begins Plot is: {movie_1_top_10_words}')
    print(f'The top 10 most common words in The Dark Knight Plot is: {movie_2_top_10_words}')
    print(f'The top 10 most common words in The Dark Knight Rises Plot is: {movie_3_top_10_words}\n')

    print(f'The sentiment analysis for Batman Begins Plot is: {movie_1_sentiment_analysis}')
    print(f'The sentiment analysis for The Dark Knight Plot is: {movie_2_sentiment_analysis}')
    print(f'The sentiment analysis for The Dark Knight Rises Plot is: {movie_3_sentiment_analysis}\n')

    print(f'The similarity between Batman Begins and The Dark Knight Plots is {movie_1_similarity_with_movie_2} by Fuzz Ratio and by Sequence Matcher respectively') # returns 2 and 1.88
    print(f'The similarity between Batman Begins and The Dark Knight Rises Plots is {movie_1_similarity_with_movie_3} by Fuzz Ratio and by Sequence Matcher respectively') # returns 1 and 1.11
    print(f'The similarity between The Dark Knight and The Dark Knight Rises Plots is {movie_2_similarity_with_movie_3} by Fuzz Ratio and by Sequence Matcher respectively\n') # returns 1 and 0.76

    print(f'The words that are common across all three plots are: {common_words_in_all_3_plots}\n')

    # have to close one graph to view the next one
    movie_1_bar_graph = bar_graph('Batman Begins', movie_1_top_10_words) # bar graph with the top 10 words in movie plot
    movie_2_bar_graph = bar_graph('The Dark Knight', movie_2_top_10_words)
    movie_3_bar_graph = bar_graph('The Dark Knight Rises', movie_3_top_10_words)

    # Not functional as explained above, under word_bubble function
    # movie_1_word_cloud = word_bubble(movie_1_top_10_words)
    # movie_2_word_cloud = word_bubble(movie_2_top_10_words)
    # movie_3_word_cloud = word_bubble(movie_3_top_10_words)


if __name__ == "__main__":
    main()
