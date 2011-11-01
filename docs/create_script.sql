SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS `mydb` ;
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`clients`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`clients` ;

CREATE  TABLE IF NOT EXISTS `mydb`.`clients` (
  `id` INT NOT NULL ,
  `username` VARCHAR(255) NOT NULL ,
  `senha` VARCHAR(255) NOT NULL ,
  `inscricao_data` DATETIME NOT NULL ,
  `access_token` TEXT NOT NULL ,
  `secret_token` TEXT NOT NULL ,
  `id_twitter` INT(11)  NULL ,
  `friends_cout` INT(11)  NULL ,
  `followers_count` INT(11)  NULL ,
  `profile_image_url` VARCHAR(255) NULL ,
  `location` TEXT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
COMMENT = 'Usuarios do sistema twintera';


-- -----------------------------------------------------
-- Table `mydb`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`users` ;

CREATE  TABLE IF NOT EXISTS `mydb`.`users` (
  `id` INT NOT NULL ,
  `id_twitter` INT(11)  NULL ,
  `profile_image_url` VARCHAR(255) NULL ,
  `location` VARCHAR(255) NULL ,
  `friend` INT(11)  NULL ,
  `follower` INT(11)  NULL ,
  `username` VARCHAR(255) NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
COMMENT = 'listagem dos friends e followers do usuario';


-- -----------------------------------------------------
-- Table `mydb`.`clients_users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`clients_users` ;

CREATE  TABLE IF NOT EXISTS `mydb`.`clients_users` (
  `clients_id` INT NOT NULL ,
  `users_id` INT NOT NULL ,
  PRIMARY KEY (`clients_id`, `users_id`) ,
  INDEX `fk_clients_users` (`users_id` ASC) ,
  CONSTRAINT `fk_clients_has_users_clients`
    FOREIGN KEY (`clients_id` )
    REFERENCES `mydb`.`clients` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_clients_has_users_users1`
    FOREIGN KEY (`users_id` )
    REFERENCES `mydb`.`users` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`posts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`posts` ;

CREATE  TABLE IF NOT EXISTS `mydb`.`posts` (
  `id` INT NOT NULL ,
  `criacao_data` VARCHAR(255) NULL ,
  `id_twitter` INT(11)  NULL ,
  `text` TEXT NULL ,
  `users_id` INT NOT NULL ,
  PRIMARY KEY (`id`, `users_id`) ,
  INDEX `fk_posts_users1` (`users_id` ASC) ,
  CONSTRAINT `fk_posts_users1`
    FOREIGN KEY (`users_id` )
    REFERENCES `mydb`.`users` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`token`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`token` ;

CREATE  TABLE IF NOT EXISTS `mydb`.`token` (
  `token` VARCHAR(255) NULL ,
  `posts_id` INT NOT NULL ,
  `posts_users_id` INT NOT NULL ,
  PRIMARY KEY (`posts_id`, `posts_users_id`) ,
  CONSTRAINT `fk_token_posts1`
    FOREIGN KEY (`posts_id` , `posts_users_id` )
    REFERENCES `mydb`.`posts` (`id` , `users_id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
