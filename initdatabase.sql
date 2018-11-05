CREATE TABLE `testmaster`.`users` (
  `UID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `role` VARCHAR(45) NULL,
  PRIMARY KEY (`UID`),
  UNIQUE INDEX `UID_UNIQUE` (`UID` ASC));

INSERT INTO `testmaster`.`users` (`username`, `password`, `role`) VALUES ('bjorn', 'asdf', 'låntagare');
INSERT INTO `testmaster`.`users` (`username`, `password`, `role`) VALUES ('admin', 'admin', 'administratör');
