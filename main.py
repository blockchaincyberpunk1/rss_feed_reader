import feedparser

def fetch_and_display_feed(feed_url):
    try:
        feed = feedparser.parse(feed_url)
        if feed.entries:
            print(f"Title: {feed.feed.title}\n")
            for entry in feed.entries:
                print(f"Title: {entry.title}")
                print(f"Link: {entry.link}\n")
        else:
            print("No articles found in the feed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    feed_url = input("Enter the RSS feed URL: ")
    fetch_and_display_feed(feed_url)
