CREATE TABLE profs(
   prof_id serial PRIMARY KEY,
   bio VARCHAR (500),
   email VARCHAR (50),
   name VARCHAR(50),
   favorites serial,
   pic_link VARCHAR(100)
);

CREATE TABLE projects(
   title VARCHAR(50),
   description VARCHAR(200),
   prof_id serial,
   FOREIGN KEY (prof_id) REFERENCES profs(prof_id)
);

CREATE TABLE past_theses(
   title VARCHAR(200),
   link VARCHAR(200),
   prof_id serial,
   FOREIGN KEY (prof_id) REFERENCES profs(prof_id)
);


CREATE TABLE areas(
   area VARCHAR(100),
   prof_id serial,
   FOREIGN KEY (prof_id) REFERENCES profs(prof_id)
);

CREATE TABLE users(
   username VARCHAR(50) PRIMARY KEY,
);

CREATE TABLE favorited_profs(
  FOREIGN KEY (username) REFERENCES users(username)
  FOREIGN KEY (prof_id) REFERENCES profs(prof_id)
);



CREATE TABLE courses(
  course VARCHAR(10) PRIMARY KEY,
  FOREIGN KEY (prof_id) REFERENCES profs(prof_id)
);
