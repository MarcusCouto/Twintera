-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.1.54-1ubuntu4


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema twintera
--

CREATE DATABASE IF NOT EXISTS twintera;
USE twintera;

--
-- Definition of table `twintera`.`clients`
--

DROP TABLE IF EXISTS `twintera`.`clients`;
CREATE TABLE  `twintera`.`clients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  `inscricao_data` datetime DEFAULT NULL,
  `access_token` varchar(255) DEFAULT NULL,
  `secret_token` varchar(255) DEFAULT NULL,
  `id_twitter` varchar(255) DEFAULT NULL,
  `friends_count` int(11) DEFAULT NULL,
  `followers_count` int(11) DEFAULT NULL,
  `profile_image_url` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `screen_name` varchar(255) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `twintera`.`clients`
--

/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
LOCK TABLES `clients` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;


--
-- Definition of table `twintera`.`clients_users`
--

DROP TABLE IF EXISTS `twintera`.`clients_users`;
CREATE TABLE  `twintera`.`clients_users` (
  `client_id` varchar(255) NOT NULL,
  `users_id` varchar(255) NOT NULL,
  `friend` int(11) NOT NULL,
  `follower` int(11) NOT NULL,
  `status` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `twintera`.`clients_users`
--

/*!40000 ALTER TABLE `clients_users` DISABLE KEYS */;
LOCK TABLES `clients_users` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `clients_users` ENABLE KEYS */;


--
-- Definition of table `twintera`.`posts`
--

DROP TABLE IF EXISTS `twintera`.`posts`;
CREATE TABLE  `twintera`.`posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `criacao_data` varchar(255) DEFAULT NULL,
  `id_twitter` varchar(255) DEFAULT NULL,
  `text` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `twintera`.`posts`
--

/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
LOCK TABLES `posts` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;


--
-- Definition of table `twintera`.`users`
--

DROP TABLE IF EXISTS `twintera`.`users`;
CREATE TABLE  `twintera`.`users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_twitter` varchar(255) NOT NULL,
  `profile_image_url` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `protected` varchar(255) DEFAULT NULL,
  `friends_count` int(11) DEFAULT NULL,
  `followers_count` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `statuses_count` int(11) DEFAULT NULL,
  `lang` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `twintera`.`users`
--

/*!40000 ALTER TABLE `users` DISABLE KEYS */;
LOCK TABLES `users` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
