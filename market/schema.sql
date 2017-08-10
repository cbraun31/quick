drop table if exists transactions;
create table transactions (
  id integer primary key autoincrement,
  item text not null,
  price integer not null,
  qty integer not null,
  hq text,
  seller text not null,
  mat text
);