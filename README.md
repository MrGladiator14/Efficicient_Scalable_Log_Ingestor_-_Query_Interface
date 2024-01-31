<br />
<div align="center">
  <a href="https://github.com/dyte-submissions/november-2023-hiring-MrGladiator14">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Log Ingestor and Query Interface</h3>

  <p align="center">
    This project involves the creation of a log ingestor and a query interface system capable of managing massive volumes of log data efficiently. The log data will be obtained via an HTTP server running on port 3000, ingested, and filtered for specific fields, with scalability being a critical consideration. The project also requires a Query interface offering a user-friendly UI for full-text search across logs and enabling filters based on certain parameters like level, message, resourceId, etc. Advanced features, although not compulsory, could include date-specific searches, use of regular expressions, multi-filter combination, real-time log ingestion, and role-based access. Evaluation will be based on variables such as volume handling, search speed, scalability, usability, implementation of advanced features, and the readability of the source code.
    <br />
    <a href="https://dyte.notion.site/dyte/SDE-1-and-SDE-Intern-Assignment-6b7a7f324dc0450381b0fdb771a8ec40"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dyte-submissions/november-2023-hiring-MrGladiator14">View Demo</a>
    ·
    <a href="https://github.com/dyte-submissions/november-2023-hiring-MrGladiator14">Report Bug</a>
    ·
    <a href="https://github.com/dyte-submissions/november-2023-hiring-MrGladiator14">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* ![python]
* ![streamlit]
* ![flask]
* ![Elasticsearch]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python 3.10 or higher
* [Download latest elasticsearch zip file & complete extraction](https://www.elastic.co/downloads/elasticsearch)


### Installation

1. Go to the cofig folder at the extraction location of the Elasticsearch. paste the following lines in the elasticsearch.yml
```sh
action.auto_create_index: .monitoring*,.watches,.triggered_watches,.watcher-history*,.ml*

# uncomment the below section in case of low disk space 
# cluster.routing.allocation.disk.threshold_enabled: true 
# cluster.routing.allocation.disk.watermark.flood_stage: 200mb
# cluster.routing.allocation.disk.watermark.low: 500mb 
# cluster.routing.allocation.disk.watermark.high: 300mb
``` 
2. Note down the user account & details in a file.
log on to localhost:9200 to verify succesfull set of the elasticsearch DB

3. Clone the repo
   ```sh
   git clone https://github.com/MrGladiator14
   /november-2023-hiring-MrGladiator14.git
   ```
4. Install the packages
   ```sh
   pip install -r requirements.txt
   ```
5. run the updateSettings.py file  to configure the DB
   ```python
   python updateSettings.py
   ```
6. run main.py file to activate the Log Ingestor
   ```python
   python main.py
   ```
7. then run the filter.py file to access the Query Interface
   ```python
   python filter.py
   ```
8. To ingest multiple json files for testing modify & run req.py file
   ```python
   python req.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Elasticsearch is an open-source search and analytics engine designed for scalable, near real-time data search. Key advantages include distributed architecture for scalability, efficient full-text search, schema-free JSON storage, RESTful API for easy integration, and a powerful query language. It is part of the Elastic Stack, offering a comprehensive solution for data processing, storage, search, and visualization. The vibrant community and commercial support make Elasticsearch a popular choice for organizations dealing with large and dynamic datasets.

* A running Elasticsearch process is called a node 
* Nodes host shards, which are instances of Lucene 
* Primary shards are updated first when data is written 
* Replica shards mirror primaries, are always stored on a different node, and are written to after the primary Datasets are stored in an index, which is formed of one or more shards 
* Shards are the scaling unit of the dataset 
* Nodes on different servers can form a cluster 
* Every shard will affect cluster performance

The project's usage mainly revolves around two part - the log ingestor and the query interface. 

The log ingestor, which is an HTTP server running on port 3000 by default, is designed to efficiently handle and ingest high volumes of log data in a specific JSON format. This format includes various fields such as level, message, resourceId, timestamp, traceId, spanId, commit, and metadata.

On the other hand, the query interface provides a user interface (web UI or CLI) for full-text search across the logs that have been ingested. Additionally, it allows for filtering of search results based on specific fields such as level, message, resourceId, timestamp, traceId, spanId, commit, and metadata.parentResourceId.

Advanced features may include search within specific date ranges, usage of regular expressions for search, permitting the combination of various filters, providing real-time log ingestion and search capabilities, and finally, implementing role-based access to the query interface.

The primary use cases of the project might include searching for all logs with a particular level, e.g., 'error', finding logs with a specific term in the message, such as 'Failed to connect', and retreiving all logs linked to a certain 'resourceId'. It can also perform searches across a specific time range.

Thus, the purpose of the project is to ingest, manage, and query vast volumes of log data effectively and efficiently.  

* Note: Certain characters may not be parsed by the elasticsearch query framework by default. This should be fixed by changing the index tokenizer 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] a mechanism to ingest logs in the provided format.
```json
{
	"level": "error",
	"message": "Failed to connect to DB",
    "resourceId": "server-1234",
	"timestamp": "2023-09-15T08:00:00Z",
	"traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
        "parentResourceId": "server-0987"
    }
}
```
- [ ] Ensure scalability to handle high volumes of logs efficiently.
- [ ] Mitigate potential bottlenecks such as I/O operations, database write speeds, etc.
- [ ] Make sure that the logs are ingested via an HTTP server, which runs on port 3000 by default. 
- [ ] Offer a user interface (Web UI or CLI) for full-text search across logs.
- [ ] Included filters
- [ ] Aim for efficient and quick search results.
- [ ] Implement search within specific date ranges.
- [ ] Utilize regular expressions for search.
- [ ] Combining multiple filters.
- [ ] Provide real-time log ingestion and searching capabilities.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Bryson Gracias - brysongracias@gmail.com

Project Link: [link](https://github.com/MrGladiator14/november-2023-hiring-MrGladiator14)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




[product-screenshot]: images/interface.png
[python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[streamlit]: https://img.shields.io/badge/Streamlit-000000?style=for-the-badge&logo=streamlit&logoColor=blue
[streamlit]: https://img.shields.io/badge/Streamlit-20232A?style=for-the-badge&logo=streamlit&logoColor=61DAFB
[React-url]: https://reactjs.org/
[flask]: https://img.shields.io/badge/Flask-35495E?style=for-the-badge&logo=flask&logoColor=4FC08D
[Elasticsearch]: https://img.shields.io/badge/Elasticsearch-DD0031?style=for-the-badge&logo=Elasticsearch&logoColor=white
