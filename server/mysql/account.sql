ALTER TABLE `account`
ADD COLUMN `autohunt_expire`  datetime NOT NULL DEFAULT '0000-00-00 00:00:00' AFTER `money_drop_rate_expire`;