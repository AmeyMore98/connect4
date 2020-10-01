# Connect4 API

RESTful API to play Connect4 game created using Django Restframework
<br />

## Game Module

### Start Game

| Method | Endpoint  | Access |
|--|--|--|
| `POST` | `/game` | Everyone |
<br />

#### Case 1 : Valid input

#### Request

```json
{
    "data": {
        "action": "start"
    }
}
```
#### Response

```json
{
    "status": 200,
    "result": "Ready"
}
```
<br />

#### Case 2: Invalid input, with incorrect action

#### Request

```json
{
    "data": {
        "action": "staart"
    }
}
```
#### Response

```json
{
    "status": 400,
    "result": "Invalid Action"
}
```
---
### Play Game
| Method | Endpoint  | Access |
|--|--|--|
| `POST` | `/game` | Everyone |
<br />

#### Case 1: Valid input, for player 1

#### Request

```json
{
    "data": {
        "action": "play",
        "column": 1
    }
}
```
#### Response

```json
{
    "status": 200,
    "result": "Valid Move",
    "move": {
        "player": "Yellow",
        "column": 1
    }
}
```
<br />

#### Case 2: Valid input, for player 2

#### Request

```json
{
    "data": {
        "action": "play",
        "column": 6
    }
}
```
#### Response

```json
{
    "status": 200,
    "result": "Valid Move",
    "move": {
        "player": "Red",
        "column": 6
    }
}
```
<br />

#### Case 3: Winning move, for player 1

#### Request

```json
{
    "data": {
        "action": "play",
        "column": 4
    }
}
```
#### Response

```json
{
    "status": 200,
    "result": "Yellow Wins!",
    "move": {
        "player": "Yellow",
        "column": 4
    }
}
```
<br />

#### Case 4: Input after game has ended

#### Request

```json
{
    "data": {
        "action": "play",
        "column": 4
    }
}
```
#### Response

```json
{
    "status": 400,
    "result": "Game has ended"
}
```
<br />

#### Case 5: Invalid Input

#### Request

```json
{
    "data": {
        "action": "play",
        "column": 14
    }
}
```
#### Response

```json
{
    "status": 400,
    "result": "Invalid Move"
}
```
<br />
