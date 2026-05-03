# gemini-machine-learning
This application is using llama to index pdfs in order to generate content for a working chatbot application that only interacts with the data that it is trained on. 

Included Files
Server.py 	
    FastAPI backend
Client.py 	
    Dash client
Llama-indexing.py 	
    ml_index/
Requirements.txt	
    module installations
.env	
    OpenAI Key
Dockerfile	
    Uses a slim Python base 
	Installs your dependencies 
	Copies index
	Exposes both ports (FastAPI + Dash)
	Runs both apps inside one container using uvicorn + python

To Run application
    uvicorn server:app --reload

To Build and Rebuild a Docker Image
docker build -t machine-learning-chatbot .

To Run Docker Container
docker run -p 8000:8000 -p 5600:5000 machine-learning-chatbot

Port in use Error
Find what's using a Port:  lsof -i :5000
Kill Container that is using ports:  kill -9 12345
Kill all on a port:  kill -9 $(lsof -t -i :5000)


Troubleshooting
Review Docker Containers running:  docker ps 
Stop Docker Containers:  docker stop <container_id>
Kill any leftover Docker processes:   ps aux | grep -i docker
Check for Countainers still bound to ports:  docker ps -a
d
To Clear all stale containers
docker stop $(docker ps -aq) 2>/dev/null
docker rm $(docker ps -aq) 2>/dev/null


Push to Github
git add .
git commit -m "your message"
git push

Get the most recent commit
git reset --hard HEAD

Pull the latest from remote and discards all local changes
git fetch --all
git reset --hard origin/main