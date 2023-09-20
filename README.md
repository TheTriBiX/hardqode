# API Handlers
### request: GET api/v1/lessonslist/
### response: JSON
{
    "data": [
        {
            "id": 1,
            "lesson_id": 1,
            "time_watched": 485,
            "status": "Просмотрено"
        },



### request: GET api/v1/lessonslist/<int:pk>/
### response: JSON
[
	"data": [
        {
            "id": 1,
            "lesson_id": 1,
            "time_watched": 485,
            "status": "Просмотрено",
            "date_last": "2023-09-05"
        },
	{...},
...
]

### request: GET api/v1/stats/
### response: JSON
[
	"data": [
        {
            "product_id": 1,
            "watched_lesson_count": 2,
            "sum_watched_time": 515,
            "user_count": 1,
            "user_percent": 50
        },

	{...},
...
]
