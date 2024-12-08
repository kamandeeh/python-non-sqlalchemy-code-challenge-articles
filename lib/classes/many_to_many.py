class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        author._articles.append(self)
        magazine._articles.append(self)


    @property
    def title(self):
        """Read-only property for title."""
        return self._title

class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def get_articles(self):
        return self._articles

    def magazines(self):
        # Return a unique list of magazines associated with the author's articles
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Create a new article and associate it with this author and the given magazine
        return Article(self, magazine, title)

    def topic_areas(self):
        # Return a unique list of categories of the magazines
        return list(set(magazine.category for magazine in self.magazines()))
       


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []  # Initialize an empty list to store articles

    def get_articles(self):
        return self._articles

    def contributors(self):
        # Return a unique list of authors who contributed to this magazine
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        # Return the titles of all articles for this magazine
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        # Return authors who have written more than 2 articles for this magazine
        authors = [article.author for article in self._articles]
        return [author for author in set(authors) if authors.count(author) > 2]


# Create Authors
author1 = Author("Alice")
author2 = Author("Bob")
author3 = Author("Elvis")

# Create Magazines
magazine1 = Magazine("TechWorld", "Technology")
magazine2 = Magazine("HealthFirst", "Health")
magazine3 = Magazine("SpaceTimes", "Science")
magazine4 = Magazine("EcoFuture", "Environment")
magazine5 = Magazine("ArtDaily", "Art")
magazine6 = Magazine("Finance360", "Finance")
magazine7 = Magazine("HistoryNow", "History")

# Add Articles
article1 = author1.add_article(magazine1, "AI Revolution")
article2 = author2.add_article(magazine2, "Healthy Habits")
article3 = author3.add_article(magazine3, "Mars Exploration")
article4 = author2.add_article(magazine4, "Climate Change")
article5 = author2.add_article(magazine5, "Renaissance Art")
article6 = author1.add_article(magazine6, "Investment Tips")
article7 = author2.add_article(magazine7, "Ancient Civilizations")
article8 = author2.add_article(magazine1, "Future of Robotics")
article9 = author1.add_article(magazine3, "Black Holes")
article10 = author1.add_article(magazine2, "Nutrition Myths")

# Test Outputs
print("Author 1 Articles:", [article.title for article in author1.get_articles()])
print("Author 1 Magazines:", [mag.name for mag in author1.magazines()])
print("Author 1 Topics:", author1.topic_areas())

print("Magazine 1 Articles:", [article.title for article in magazine1.get_articles()])
print("Magazine 1 Contributors:", [author.name for author in magazine1.contributors()])
print("Magazine 1 Titles:", magazine1.article_titles())
print("Magazine 1 Contributing Authors:", [author.name for author in magazine1.contributing_authors()])
