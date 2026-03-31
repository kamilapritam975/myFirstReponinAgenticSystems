CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    signup_date DATE
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount INTEGER
);

CREATE TABLE activity (
    user_id INTEGER,
    login_count INTEGER
);