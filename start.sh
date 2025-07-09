#!/bin/bash
source .env
uvicorn main:app --reload --port $PORT