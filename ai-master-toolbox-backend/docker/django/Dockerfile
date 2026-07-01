FROM python:3.11

WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

COPY . /app

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "ai_master_toolbox.asgi:application"]

