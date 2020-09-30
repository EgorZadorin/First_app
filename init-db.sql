
create table users
(
    id           serial not null
        constraint users_pkey
            primary key,
    login        varchar,
    money_amount integer,
    card_number  varchar,
    status       boolean
);


create table user_passwords
(
    user_id  integer not null
        constraint user_passwords_pkey
            primary key
        constraint user_passwords_user_id_fkey
            references users,
    password varchar
);



INSERT INTO users(login, money_amount, card_number, status)
VALUES ('admin', 1000000, 4539656195306668, true);


INSERT INTO users(login, money_amount, card_number, status)
VALUES ('user1', 100000, 5473943691492712, true);


INSERT INTO users(login, money_amount, card_number, status)
VALUES ('user2', 10000, 6011620677080292, true);


INSERT INTO users(login, money_amount, card_number, status)
VALUES ('user3', 1000, 349459356661411, false);


INSERT INTO users(login, money_amount, card_number, status)
VALUES ('user4', 100, 4916520565709112, false);



INSERT INTO user_passwords(user_id, password)
VALUES (
        (SELECT id FROM users where login = 'admin'),
        'admin'
       );



INSERT INTO user_passwords(user_id, password)
VALUES (
        (SELECT id FROM users where login = 'user1'),
        'user1'
       );




INSERT INTO user_passwords(user_id, password)
VALUES (
        (SELECT id FROM users where login = 'user2'),
        'user2'
       );




INSERT INTO user_passwords(user_id, password)
VALUES (
        (SELECT id FROM users where login = 'user3'),
        'user3'
       );




INSERT INTO user_passwords(user_id, password)
VALUES (
        (SELECT id FROM users where login = 'user4'),
        'user4'
       );



