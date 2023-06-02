
BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'



# SPLASH_URL = 'http://localhost:8050'
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shien (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Obey robots.txt rules
# ROBOTSTXT_OBEY = False


# SCRAPEOPS_PROXY_ENABLED = True

# Add In The ScrapeOps Monitoring Extension
# EXTENSIONS = {
# # 'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
# }


# DOWNLOADER_MIDDLEWARES = {

#     # ## ScrapeOps Monitor
#     # 'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
#     # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    
#     # ## Proxy Middleware
#     # 'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
# }

# Max Concurrency On ScrapeOps Proxy Free Plan is 1 thread
CONCURRENT_REQUESTS = 1
