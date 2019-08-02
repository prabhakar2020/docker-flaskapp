# docker-flaskapp
Flask application with Docker

Execute below commands to build and run the flask application on docker container
-------
>> docker build -t "myflask_image" .<br/>
>> docker run -d -p 5000:5000 --name my-flask-application myflask_image
<br/>
After successful build, Check url : http://localhost:5000/
<br/><br/>
Note: For more details about docker commands https://github.com/prabhakar2020/docker
