from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

process.crawl('nintendo_bot', domain='store.nintendo.co.uk')
process.crawl('nintendo_bot2', domain='store.nintendo.co.uk')
process.crawl('nintendo_bot_test', domain='store.nintendo.co.uk')
process.crawl('game_bot', domain='game.co.uk')
process.crawl('game_bot_test', domain='game.co.uk')
process.crawl('johnlewis_bot', domain='johnlewis.com')
process.crawl('johnlewis_bot_test', domain='johnlewis.com')
process.crawl('ao_bot', domain='ao.com')
process.crawl('ao_bot_test', domain='ao.com')
process.crawl('argos_ebay_bot', domain='ebay.co.uk')

# process.crawl('amazon_bot', domain='amazon.co.uk')
# process.crawl('amazon_bot_test', domain='amazon.co.uk')
# process.crawl('very_bot', domain='very.co.uk')
# process.crawl('currys_bot', domain='currys.co.uk')

# TODO Add slack mention to silent channel as indication that script is running
process.start()

# TODO Send message if there is an error during scrape e.g. 503
# TODO Argos, Very, Currys, Smyths
# TODO Tokens in config file, git, iMac
# TODO Timestamp in csv log
