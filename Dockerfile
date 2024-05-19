######################################################################################################
### Correctly set up the .github/workflows/docker.yml will update this to docker automatically. ###
#######################################################################################################
### To build this manually ###
# docker build -f Dockerfile -t username/app-name .
#
### To run it manually ###
# docker run --rm --name temp-name-p 8001:8501 username/app-name
#
### To push it manually ###
# docker push username/app-name
######################################################################################################

FROM python:3.10
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["app/home.py"]
