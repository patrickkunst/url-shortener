from sql import connectToSql

db = connectToSql()

cursor = db.cursor()
sql = """CREATE TABLE `url_shortener`.`new_table` 
(`short` VARCHAR(45) NOT NULL,`full` MEDIUMTEXT NULL,PRIMARY KEY (`short`), 
UNIQUE INDEX `short_UNIQUE` (`short` ASC) VISIBLE)"""

cursor.execute(sql)
