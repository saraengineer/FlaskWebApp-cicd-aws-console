#!/bin/bash

# Start Gunicorn server
gunicorn --bind 0.0.0.0:8000 application:app