create database if not exists torchflow;

use torchflow;

create table if not exists env_meta (
  env_id int unsigned not null unique primary key auto_increment,
  env_name varchar(64) not null,
  env_ver varchar(64) not null
);

create table if not exists env (
  env_id int unsigned not null,
  model_name varchar(64) not null,
  env_where varchar(512) not null,
  env_time datetime not null default current_timestamp,
  constraint c_env_meta foreign key(env_id) references env_meta(env_id)
);

create table if not exists record (
  record_id int unsigned not null unique primary key auto_increment,
  model_name varchar(64) not null,
  env_id int unsigned not null,
  record_cmd varchar(512),
  record_loss_function varchar(128) not null,
  record_loss double not null,
  record_time datetime not null default current_timestamp,
  model_size int unsigned not null,
  constraint cc_env_meta foreign key(env_id) references env(env_id)
);