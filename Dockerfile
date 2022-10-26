FROM python:3
RUN git clone https://github.com/MatiasBoldrini/CRUD_Personas.git
WORKDIR /CRUD_Personas
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]
