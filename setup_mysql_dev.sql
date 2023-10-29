-- Sets up a Sql database and user
-- crate databse hbnb_dev_dCREATE DATABASE IF NOT EXISTS oloja_dev_db;

-- create user
CREATE USER IF NOT EXISTS oloja_dev@localhost IDENTIFIED BY 'oloja_dev_pwd';
CREATE DATABASE IF NOT EXISTS oloja_dev_db;
-- choose databse
USE oloja_dev_db

-- grant permisions to hbnb_dev on hbnb_dev_db
GRANT ALL ON oloja_dev_db.* TO oloja_dev@localhost;

-- grant permisions to hbnb_dev on performance_schema
GRANT SELECT ON performance_schema.* TO oloja_dev@localhost;
