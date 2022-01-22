drop table if exists posts;

create table if not exists posts (
    post_id integer primary key autoincrement,
    created timestamp not null default current_timestamp,
    title text not null,
    content text not null
)