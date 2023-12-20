import string
import uuid


class NotFoundError(Exception):
    pass


class URLShortener:
    def __init__(self):
        self.hash = {}
        
    def uuidGenerator(self):
        uuid_generator = str(uuid.uuid4())[:8]
        return int(uuid_generator,16)
        
    def reverse(self,s) :
        return s[::-1]
    
    def idToShortURL(self,n):
        # code here
        combined_str=""
        base_conversion=string.ascii_letters + string.digits
        while n:
            rem = n%62
            n=n//62
            combined_str+=base_conversion[rem]
        combined_str = self.reverse(combined_str)
        return combined_str
    
    def main(self,url):
        short_url_prefix = "http://bitly.com/"
        uuid_gen=self.uuidGenerator()
        print(uuid_gen)
        short_url =self.idToShortURL(uuid_gen)
        self.hash[short_url]=url
        print(short_url,url)
        return short_url
        
    def get_shortened_url_mapping(self,short_url):
        print(self.hash)
        if short_url in self.hash:
            return self.hash[short_url]
        else:
            raise NotFoundError("Could not find"+short_url)

# if __name__ == "__main__":
#     url = URLShortener()
#     url.main("https://www.google.com")
    
        
    

# getting a uuid generator in python
    ## collision chances in the UUID generation process.
# storing the data in a database , how can i make it a generic application and deploy my database and other things so that i can easily access it.