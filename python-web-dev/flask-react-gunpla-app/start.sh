#!/bin/bash
# start.sh
# This script starts the Flask backend and the React frontend concurrently.

# Exit immediately if a command exits with a non-zero status.
set -e

# Function to kill background processes on exit
cleanup() {
  echo "Shutting down servers..."
  kill "$FLASK_PID" "$FRONTEND_PID"
  exit 0
}

# Trap termination signals to call cleanup()
trap cleanup SIGINT SIGTERM

# Activate Python virtual environment
echo "Activating Python virtual environment..."
if [ -d "backend/venv" ]; then
  source backend/venv/bin/activate
else
  echo "Virtual environment not found in backend/venv"
  exit 1
fi

# Start the Flask server in the background
echo "Starting Flask server..."
cd backend
python app.py &
FLASK_PID=$!
cd ..

# Start the React development server in the background
echo "Starting React development server..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo "Servers are running. Press Ctrl+C to stop."

# Wait for background processes to exit
wait