FROM node:latest as build-deps
WORKDIR /frontend
COPY ./frontend/package.json ./frontend/yarn.lock ./
RUN yarn
COPY ./frontend /frontend
RUN yarn build

# Use an official Python runtime as a parent image
FROM python:rc

WORKDIR /app/backend

# Install Python dependencies
COPY ./backend/requirements /app/backend/requirements
RUN pip install -r requirements/production.txt

WORKDIR /

COPY . .
COPY --from=build-deps /frontend/build /app/frontend/build

WORKDIR /app/frontend/build
RUN mkdir root && mv *.ico *.js *.json root
RUN mkdir /app/staticfiles

WORKDIR /backend

# SECRET_KEY is only included here to avoid raising an error when generating static files
RUN DJANGO_SETTINGS_MODULE=backend.settings.production \
  SECRET_KEY=somethingsupersecret \
  python manage.py collectstatic --noinput

EXPOSE $PORT

CMD python manage.py runserver 0.0.0.0:$PORT