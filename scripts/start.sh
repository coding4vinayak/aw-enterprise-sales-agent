#!/bin/bash

# Create the backend application
echo "Starting Enterprise Sales Agent Application..."

# Start the backend
cd backend
echo "Starting backend server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!

# Wait for backend to start
sleep 5

# Start the frontend (if available)
cd ../frontend
if [ -d "node_modules" ]; then
    echo "Starting frontend server..."
    npm run dev &
    FRONTEND_PID=$!
else
    echo "Node modules not found. Please run 'npm install' in the frontend directory."
fi

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID