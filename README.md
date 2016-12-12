imgsort sorts your images in directories using a pattern based on your image dates

# Usage

```bash
python imgsort.py DIRECTORY MODE
```
where _MODE_ is a combination of the following possibilities:
* _y_ for year
* _m_ for month
* _d_ for day
* _-_ as separator

See the following examples:
* _y-m-d_ creates _2016-12-01_ or _1995-01-06_
* _m-y_ creates _12-2016_ or _01-1995_
