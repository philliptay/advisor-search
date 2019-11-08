CREATE TABLE profs(
   prof_id serial PRIMARY KEY,
   bio VARCHAR (200),
   email VARCHAR (50),
   name VARCHAR(50)
);

CREATE TABLE past_projects(
   project_id serial PRIMARY KEY,
   prof_id serial,
   title VARCHAR(50),
   description VARCHAR(200),
   FOREIGN KEY (prof_id) REFERENCES profs(prof_id)
);

CREATE TABLE areas(
   area VARCHAR(100) PRIMARY KEY,
   prof_id serial,
   FOREIGN KEY (prof_id) REFERENCES profs(prof_id)
);

CREATE TABLE users(
   user_id serial PRIMARY KEY,
   username VARCHAR(50),
   password VARCHAR(50)
);
