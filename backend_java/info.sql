/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80031 (8.0.31)
 Source Host           : localhost:3306
 Source Schema         : info

 Target Server Type    : MySQL
 Target Server Version : 80031 (8.0.31)
 File Encoding         : 65001

 Date: 29/02/2024 20:18:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_activity_info
-- ----------------------------
DROP TABLE IF EXISTS `t_activity_info`;
CREATE TABLE `t_activity_info`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `title` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '活动名称',
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '活动地点',
  `start_date` date NOT NULL COMMENT '起始日期',
  `end_date` date NULL DEFAULT NULL COMMENT '结束日期',
  `start_time` time NULL DEFAULT NULL COMMENT '起始时间',
  `end_time` time NULL DEFAULT NULL COMMENT '结束时间',
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '活动简介',
  `college` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '学院',
  `account_link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '链接',
  `extra_info` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '附加信息',
  `view` int NULL DEFAULT 0 COMMENT '浏览量',
  `subscribe` int NULL DEFAULT 0 COMMENT '订阅量',
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '活动类型',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_activity_info
-- ----------------------------
-- INSERT INTO `t_activity_info` VALUES (21, '测试活动3', NULL, '2024-02-28', NULL, NULL, NULL, '测试测试测试', NULL, '3', NULL, 123, 1, '0');
-- INSERT INTO `t_activity_info` VALUES (22, '测试活动4', NULL, '2024-02-29', NULL, NULL, NULL, '1111', NULL, '4', NULL, 10, 0, '0');
-- INSERT INTO `t_activity_info` VALUES (23, '测试活动5', NULL, '2024-02-27', NULL, NULL, NULL, '2222', NULL, '5', NULL, 999, 0, '0');
-- INSERT INTO `t_activity_info` VALUES (24, 'Test', 'Unknown', '2024-02-26', '2024-02-26', '12:00:00', '12:00:00', 'TestDesc', 'Unknown', 'TestLink', 'TestInfo', 0, 20, 'TestType');

-- ----------------------------
-- Table structure for t_activity_subscription
-- ----------------------------
DROP TABLE IF EXISTS `t_activity_subscription`;
CREATE TABLE `t_activity_subscription`  (
  `activity_id` int NOT NULL COMMENT 'activity id',
  `user_id` int NOT NULL COMMENT 'user id',
  PRIMARY KEY (`activity_id`, `user_id`) USING BTREE,
  INDEX `subscription_user_id`(`user_id` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_activity_subscription
-- ----------------------------
INSERT INTO `t_activity_subscription` VALUES (20, 1);
INSERT INTO `t_activity_subscription` VALUES (20, 2);
INSERT INTO `t_activity_subscription` VALUES (21, 2);

-- ----------------------------
-- Table structure for t_admin_account
-- ----------------------------
DROP TABLE IF EXISTS `t_admin_account`;
CREATE TABLE `t_admin_account`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'account',
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'password',
  `salt` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'salt',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_admin_account
-- ----------------------------
INSERT INTO `t_admin_account` VALUES (1, 'pKuInFo2024', '57d2730ccaed5446b4f454c937b1d5a4', 'GPdpfO');

-- ----------------------------
-- Table structure for t_user_account
-- ----------------------------
DROP TABLE IF EXISTS `t_user_account`;
CREATE TABLE `t_user_account`  (
  `user_id` int NOT NULL AUTO_INCREMENT COMMENT 'user id',
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'username',
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'encrypted password',
  `salt` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'ciphertext',
  `deleted` int NOT NULL DEFAULT 0 COMMENT 'is deleted',
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_user_account
-- ----------------------------
INSERT INTO `t_user_account` VALUES (2, 'testtest', 'da5c50f0bb7730537c5784a6980a553a', 'dLvOtC', 0);
INSERT INTO `t_user_account` VALUES (6, 'testtesttest', '1aa5bf7d9add6dabed42b2473df6b837', 'HkXN5H', 0);
INSERT INTO `t_user_account` VALUES (7, 'testtesttesttest', '4229ae9341fdc9fd0fa5296765e8e181', 'TRjqQa', 0);

-- ----------------------------
-- Table structure for t_user_info
-- ----------------------------
DROP TABLE IF EXISTS `t_user_info`;
CREATE TABLE `t_user_info`  (
  `user_id` int NOT NULL COMMENT 'user id',
  `user_nickname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'nickname',
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'email',
  PRIMARY KEY (`user_id`) USING BTREE,
  CONSTRAINT `user_info_user_id` FOREIGN KEY (`user_id`) REFERENCES `t_user_account` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_user_info
-- ----------------------------
INSERT INTO `t_user_info` VALUES (6, 'testtesttest', 'test.email');
INSERT INTO `t_user_info` VALUES (7, 'testtesttesttest', 'test.email');

-- ----------------------------
-- Triggers structure for table t_activity_subscription
-- ----------------------------
DROP TRIGGER IF EXISTS `add_activity_subscribe`;
delimiter ;;
CREATE TRIGGER `add_activity_subscribe` AFTER INSERT ON `t_activity_subscription` FOR EACH ROW BEGIN
UPDATE t_activity_info SET subscribe = subscribe + 1 WHERE id = NEW.activity_id;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table t_activity_subscription
-- ----------------------------
DROP TRIGGER IF EXISTS `sub_activity_subscribe`;
delimiter ;;
CREATE TRIGGER `sub_activity_subscribe` AFTER DELETE ON `t_activity_subscription` FOR EACH ROW BEGIN
UPDATE t_activity_info SET subscribe = subscribe - 1 WHERE id = OLD.activity_id;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
