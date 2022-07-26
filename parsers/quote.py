from locators.quote_locators import QuoteLocator

class QuoteParser:
    """
    Given one of the specific quote div, find out the data about
    the quote (quoate,content,author,tags).
    """
    def __init__(self,parent):
        self.parent=parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator=QuoteLocator.CONTENT
        return self.parent.select_one(locator).string
    @property
    def author(self):
        locator=QuoteLocator.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator=QuoteLocator.TAG
        return self.parent.select(locator)