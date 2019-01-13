# -*- coding: utf-8 -*-

# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
USER_AGENT = 'concord/research'

# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'
DOWNLOAD_HANDLERS = {'s3': None,} # from http://stackoverflow.com/a/31233576/2297751, TODO

SPIDER_MODULES = ['TweetScraper.spiders']
ITEM_PIPELINES = {
    'TweetScraper.pipelines.SaveToFilePipeline':100,
}

# settings for where to save data on disk
SAVE_TWEET_PATH = './Data/tweet/'
SAVE_USER_PATH = './Data/user/'