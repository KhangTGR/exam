# Week 4 Exam

You are a Junior DevOps Engineer and a Junior Python Developer and you have to help your startup to present how many tons of fruit were deliver today so the customer can see the fruit delivered.

You have an initial Python code provided which you will have to complete. The code has to clean data read from a csv file provided by a factory worker so it only contains rows that have numeric values.

Example of the CSV file:

```
"orders","oranges","apples","bananas"
"!091","x10","20","25a"
"092","15","20","25"
"093","16","17","22"
"094#","10","20v","25b"
"095","15","20","25"
```

File after processing:

```
"orders","oranges","apples","bananas"
"092","15","20","25"
"093","16","17","22"
"095","15","20","25"
```

You will need to complete the upload code and the code behind the upload screen (html provided) and populate the database.

You will also need to complete the code that displays the database content in a `result` screen (html provided) to the customer.

In addition, once the user uses the upload screen to `upload` the csv file successfully, the user should be redirected to the `result` screen.

## Instructions

1. The home-page `GET /` will show the upload form (html provided to you).

1. The route `POST /upload` will process upload the csv file to the folder `./uploaded` (for clarity purposes please rename the file to `yyyy-mm-dd-hh-mm-ss.csv`).  
   In case the file upload fails write an entry into a log file `./logs/upload.log` with the format  
    "[timestamp]: ERROR: The file [filename] has failed to upload"

1. The uploaded file should be processed to `remove any row containing any non-numeric characters` (you can write a function to process this after the file was uploaded successfully).

1. The processed data (after the above cleanup) should be inserted into the table `exam_table` (use MySQL or Postgres, DB schema will provided to you).

1. The page `GET /result` will show the date loaded from the DB formatted as a table (html provided to you) and the `processed file name`.  
   After the user successfully uploads the file via the upload screen he should be redirected to this page.

1. Containerize the application with a docker-image and run it as docker-container.

1. Run the database service (MySQL/Postgres) by docker-container (from Docker Hub). Initialize the database and table structure when starting the DB service (sql file provided).

1. Run the nginx as proxy (by docker-container) to receive traffics from the user and redirect it to the application.

1. Package all the following services with docker-compose:

- backend (your-application)  
  mapping-volume for folder `logs` to easy trace the error logs when needed
- proxy (serve by nginx and the config file)
- db (mysql/postgres)  
  mapping-volume for the DB’s data to keep it persistent

  \*\* Notes:
  Your application should not expose any port, except port 80 for the proxy, so the application can be accessed from the URL http://localhost/

10. Draw diagrams showing the application work-flows.

1. For the db service, config the following: `init-database`, environment `variables` (user/password), `healthcheck` and enable plugin `mysql_native_password`.
1. Create 2 docker-networks to separate to 2 parts:

- `frontend_network` uses for `backend` and `proxy`
- `backend_network` uses for `backend` and `db`

13. Config the `proxy` service so it has a dependency on the `backend` service being started.

1. Config the `backend` service depends so it has a dependency on the `db` service with `condition: service_healthy`.

1. Create a bash-script file `init.sh` to start the whole application.

1. Create a bash-script file `cleanup.sh` to clean all the resources (stopping containers, removing containers, deleting images, cleanup volumes, networks, etc...)

   \*\* Make sure that each step works perfectly before continuing to the next. It is better to submit a working project (even if not completed) than a non-working project.

## Directory structure

```
.
├── README.md
├── app
│   ├── logs
│   │   └── result.html
│   ├── main.py
│   ├── requirements.txt
│   ├── templates
│   │   ├── index.html
│   │   └── result.html
│   ├── uploaded
│   │   └── 2022-06-29-21-01-27.csv
│   │   └── 2022-06-29-21-02-28.csv
│   └── venv
│       ├── bin
│       │   ├── activate
│       │...............
├── csv_example
│   ├── file1.csv
│   └── file2.csv
├── db_dump
│   ├── db-structure.txt
│   └── schema.sql
├── Dockerfile
├── nginx
│   └── nginx.conf
├── docker-compose.yml
├── entry-point.sh
├── init.sh
├── clean.sh
```

### Notes

- Example csv files are keep in folder `csv_exam`
- SQL file for DB schema and table initial is keep in folder `db_dump`
