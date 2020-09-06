FROM python:3.7

WORKDIR /usr/src/app

COPY ww3.glob_24m.202007.nc .
COPY plot_hs.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update -y
RUN apt-get install -y libgeos++-dev
RUN apt install -y libproj-dev
RUN pip install shapely --no-binary shapely
RUN pip install git+https://github.com/SciTools/cartopy.git

CMD ["python","./plot_hs.py"]
