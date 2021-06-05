## Installation
```bash
pip3 install -r requirements.txt
```
## Usage
Run the command :
```bash
scrapy crawl numadic
```
To run the server API, run the command: 
```bash
python app.py
```
## API 
The spider crawls the following data:
| Key  | Type |Description|
| ------------- | ------------- | ------------- |
| author  | Array of strings  |Author(s) of the article.|
| headline  | String | Headline of the article. |
| url  | String | The article's page url. |
| published_at  | Date | Published date of the article. |

#### BASE URL
http://localhost:3000

The server API provides the following: 
#### GET /api/articles
Get the list of crawled articles. 

* Response : 

```javascript
{ 
  'status' : 'success',
  'num_articles_found' : 'the total number of articles queried',
  'results' : [array of items queried]
}
```
#### GET /api/search/(headline | author)
Search for articles either keywords in content or headline, or author name.
* Path parameters :

| Key  | Type |Default value| Description |
| ------------- | ------------- | ------------- | ------------- |
| `query`   | string | empty | Pass a text query to search. This value should be URI encoded. |

* Response : 

```javascript
{ 
  'status' : 'success',
  'num_articles_found' : 'the total number of articles queried',
  'results' : [array of items queried]
}
```