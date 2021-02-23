import scrapy
from GoogleCrawler.items import GooglecrawlerItem
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSpiderSpider(scrapy.Spider):
    name = 'google_spider'
    # allowed_domains = ['www.google.com']    

    def geturls():
        
        data = {
                "type": "service_account",
                "project_id": "brad-jordan-crawler",
                "private_key_id": "5d2995cbde26b9243d839eee284b64250160ce86",
                "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCzCwMJvN8uWpJW\nPKc1tiYusER+tYMKSGKUk/XHCfUWPMkDNlZd+gvgAcvHhZ/APFmJGlXByDfYV6TS\nU68TRikk9gdRSoEA/y9R4Qd4b8s9apSEAhZ8p+zf00wbnZ9jl14Df0xgpIGRIc7q\nqu3jsLsrpfta8rbpI/Nry0D9kL4nquj3qH7tIp5Fq5+NaDdzpTt3kFiP1+/RkjXW\nZEDQHCvAO5bM0N7HkW72qG95ptrfGEb+UkLDZjAPiPGrfTVbVSiLjjXJficJ/bmc\nf6vNOwaAph26fyEap5KI7A8iMtdhJPKzHPeKV9oUmAQTHig0pT7O7RDd+UMQU1rr\n8r1Ip1qfAgMBAAECggEAIavPfXRUsJ396VPsylAgLCWgLAgsxbFJQNH2peD8g5sY\n3o7IfVH6C72qujIqEfgHip42RIRH5FrPN3LfeQt3z2iphaMyUaKsHoToZ8D2gu1Z\nUt4lpnnaNVnCdWsWP5+G4bd+AKrPZyDpjf5pUKm6+YF0nO0Kcxv8umf2J/mhmUnd\nNc+VYmPQ8hPlKYcg29o3S9k5IHmeWPgn9q3b3mfii1bbGkUmIze3UQACK6VPlu+J\n28W55zt86YYJrHKyo8qPqSdFhn5kRltNEUjxQ5U7SqDFzVjs2opgwYxHau++8lvi\nVd8vcDt7vW1aH5ygIOsWldpuVDADpolV1RizoFFSKQKBgQDrRWxheG1eNc2NtOtF\nC/Q+OSbUB64mhyeDal9Dz1kHwX/Qy1N7eRf+xsTxJLV8SfLv567cF8tSII6RaD+h\neYHRiC8WGN6+7tDZWw/wAd7JcRIWEiHuj6Fch7pKQwgbKuZJVH4Kyw+Cl/ivF6J1\n50lrYBnDnqCWEk40/cKnHrqd8wKBgQDC0VqPnNqRgac1hWYcnJfP27goC7sPlm1r\nWQSVD3kdUq5DZX71QVmrKUbbfvkSDtGIyVaI/ArG5gGPAfNCCPlslEUgHDeUCqaK\n4CAGTx6ygHdWJeM6KAFNih1fcYkJeiCSMclftHEdicS1PCXbMEZr6ZnohFxQYnfL\nlts5Dux/pQKBgQDLgfyy/0mTUXThm9pamnGGFUep5o7UktoyCaQn8sZvOAiIoigv\nSNrhriwS7w7xWMIElOKjTQ25l6Ha01MfKQyLI4KfWZnrjIYpTWSm1edRVjYv0zV4\nttL8SAdzTzJG1b/nNGfmjCl5bF1Xj1kfJZZThAglNyRvS5xMqChlCOah0wKBgQCo\n/pZCUdw/sGptwQQs+aGvS3faNSLViLXuEtAoxb1YNGq6SAbzlPbFxQ6URPamNXiJ\n4a1RMuHeW5MqjJSJyeMjzxKPoiqMHxkNCxJ8ppGIYmwirMcJob5PlumX65LmR6yN\nZOa8QHiHGQUr+bsVAjF0VrWNv5Ocn24vivMr8cgxiQKBgH0Qa7b/3Ec4zGUmG9QU\ngI1SmK92ZeNONfeVABHirF9L2sPsiqZJuTsH8ufNgQiL6POdSHK7tiB0u4ZFSqIu\nQeV7ZEAgok9oXYOyQW7Ml5vrJ+VUSPjf3LAjdsrRwPZ1lHgkrwaMi+76wAT/HFNX\nck2s8k9HdA+i8zOS/YoEpUul\n-----END PRIVATE KEY-----\n",
                "client_email": "brad-jordan@brad-jordan-crawler.iam.gserviceaccount.com",
                "client_id": "114560179762642758706",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/brad-jordan%40brad-jordan-crawler.iam.gserviceaccount.com"
                }

        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_dict(data, scope)
        client = gspread.authorize(creds)

        # get the instance of the Spreadsheet
        sheet = client.open('URLS')

        sheet_instance = sheet.get_worksheet(0)

        a = sheet_instance.get_all_records()

        urls=[x['URLS'] for x in a]
        return urls

    start_urls = geturls()

    def parse(self, response):
        results = response.xpath('//div[@class="ZINbbc xpd O9g5cc uUPGi"]/div/a')

        for result in results:
            url = result.xpath('.//@href').extract_first().replace('/url?q=','')
            url = url[0:url.find('&sa=')]
            #yield{'url': url}
            orig_url = response.request.url
            yield scrapy.Request(url,
                                    callback=self.parse_result,
                                    meta={'url':url,
                                          'orig_url': orig_url})
        for i in range(0,100):
            next_page_url = response.xpath('//a[@aria-label="Next page"]/@href').extract_first()
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url)
    
    def parse_result(self, response):

        item = GooglecrawlerItem()
        url = response.meta['url']
        orig_url = response.meta['orig_url']
        emails = response.xpath('//a[contains(@href, "mailto")]')

        if len(emails) > 0:
            for email in emails:
                item['url'] = url
                item['email_address'] = email.xpath('.//@href').extract_first()
                item['orig_url'] = orig_url

                yield item
        else:
            item['url'] = url
            item['email_address'] = ''
            item['orig_url'] = orig_url

            yield item