# Tic-Tac-Toe Game

This is a simple Tic-Tac-Toe game implemented in Python with a web interface using Flask.

## Project Structure

```
.
├── src
│   ├── app.py
│   └── tictactoe.py
├── tests
│   ├── test_app.py
│   └── test_tictactoe.py
└── README.md
```

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/githubnext/workspace-blank.git
    cd workspace-blank
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Game Locally

1. Navigate to the `src` directory:
    ```sh
    cd src
    ```

2. Run the Flask application:
    ```sh
    flask run
    ```

3. Open your web browser and go to `http://127.0.0.1:5000` to play the game.

## Running the Unit Tests

1. Navigate to the `tests` directory:
    ```sh
    cd tests
    ```

2. Run the tests using `unittest`:
    ```sh
    python -m unittest discover
    ```
