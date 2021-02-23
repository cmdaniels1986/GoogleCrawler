# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GooglecrawlerPipeline:
    def process_item(self, item, spider):
        
        emailraw = item['email_address']
        emailraw = emailraw.replace('mailto:','') 
        
        if emailraw.find('?subject') != -1:       
            emailraw = emailraw[0:emailraw.find('?subject')]
        
        if emailraw.find('@') != -1 and emailraw.find('.') != -1:
            item['email_address'] = emailraw
        else:
            item['email_address'] = ''
        
        return item
