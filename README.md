# flask_page
This project was made as custom way to create Jira request. 

Tech stack:
* Python, Flask framework and HTML
* Docker for containerization
* Git Actions for CI process
* DockerHub to store builded images
* Actions secrets to store sensitive data

To run the project just enough:
* Clone the project locally
git clone https://github.com/adlost/flask_page.git
* Build an image
docker build . --file Dockerfile --tag sup_page
* Run it
sudo docker run --name app1 -p 80:5000 sup_page

* After web page should be availeble from browser
http://localhost/
