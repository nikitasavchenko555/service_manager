BEGIN;
--
-- Create model issues
--
CREATE TABLE "manager_issues" ("number_issue" integer NOT NULL PRIMARY KEY, "brief_description" varchar(200) NOT NULL, "start_down_date" date NOT NULL, "start_down_time" time NOT NULL, "start_issue_date" date NOT NULL, "start_issue_time" time NOT NULL, "progress" varchar(1000) NOT NULL, "number_history" integer NOT NULL, "comment" varchar(300) NOT NULL, "change_date" timestamp with time zone NOT NULL, "close_down_date" date NULL, "close_down_time" time NULL, "close_issue_date" date NULL, "close_issue_time" time NULL, "coordinator_id" integer NOT NULL, "creator_id" integer NOT NULL);
--
-- Remove field coordinator from issue
--
ALTER TABLE "manager_issue" DROP COLUMN "coordinator_id" CASCADE;
--
-- Remove field creator from issue
--
ALTER TABLE "manager_issue" DROP COLUMN "creator_id" CASCADE;
--
-- Remove field equipment from issue
--
ALTER TABLE "manager_issue" DROP COLUMN "equipment_id" CASCADE;
--
-- Remove field executor from issue
--
ALTER TABLE "manager_issue" DROP COLUMN "executor_id" CASCADE;
--
-- Remove field groups_of_work from issue
--
ALTER TABLE "manager_issue" DROP COLUMN "groups_of_work_id" CASCADE;
--
-- Remove field reason from issue
--
ALTER TABLE "manager_issue" DROP COLUMN "reason_id" CASCADE;
--
-- Remove field status from issue
--
ALTER TABLE "manager_issue" DROP COLUMN "status_id" CASCADE;
--
-- Remove field user_edit from issue
--
ALTER TABLE "manager_issue" DROP COLUMN "user_edit_id" CASCADE;
--
-- Remove field workspace from issue
--
ALTER TABLE "manager_issue" DROP COLUMN "workspace_id" CASCADE;
--
-- Remove field id_state from workers
--
ALTER TABLE "manager_workers" DROP CONSTRAINT "manager_workers_id_state_id_9d1ee2b1_fk_manager_state_id";
ALTER TABLE "manager_workers" DROP COLUMN "id_state_id" CASCADE;
--
-- Remove field user_edit from workers
--
ALTER TABLE "manager_workers" DROP CONSTRAINT "manager_workers_user_edit_id_67195c44_fk_auth_user_id";
ALTER TABLE "manager_workers" DROP COLUMN "user_edit_id" CASCADE;
--
-- Change Meta options on equipment
--
--
-- Change Meta options on groups_of_reason
--
--
-- Change Meta options on groups_of_work
--
--
-- Change Meta options on level_issue
--
--
-- Change Meta options on solutions
--
--
-- Change Meta options on state
--
--
-- Change Meta options on status_issue
--
--
-- Change Meta options on workspace
--
--
-- Change managers on equipment
--
--
-- Add field name to equipment
--
ALTER TABLE "manager_equipment" ADD COLUMN "name" varchar(300) DEFAULT '' NOT NULL;
ALTER TABLE "manager_equipment" ALTER COLUMN "name" DROP DEFAULT;
--
-- Add field description to level_issue
--
ALTER TABLE "manager_level_issue" ADD COLUMN "description" varchar(200) DEFAULT '' NOT NULL;
ALTER TABLE "manager_level_issue" ALTER COLUMN "description" DROP DEFAULT;
--
-- Alter field change_date on equipment
--
ALTER TABLE "manager_equipment" ALTER COLUMN "change_date" SET DEFAULT '2017-03-21T19:25:51.427531+00:00'::timestamptz;
ALTER TABLE "manager_equipment" ALTER COLUMN "change_date" DROP DEFAULT;
--
-- Alter field model on equipment
--
ALTER TABLE "manager_equipment" ALTER COLUMN "model" TYPE varchar(20) USING "model"::varchar(20);
ALTER TABLE "manager_equipment" ADD CONSTRAINT "manager_equipment_model_2f40cd4d_uniq" UNIQUE ("model");
CREATE INDEX "manager_equipment_model_2f40cd4d_like" ON "manager_equipment" ("model" varchar_pattern_ops);
--
-- Alter field change_date on groups_of_reason
--
ALTER TABLE "manager_groups_of_reason" ALTER COLUMN "change_date" SET DEFAULT '2017-03-21T19:25:51.562772+00:00'::timestamptz;
ALTER TABLE "manager_groups_of_reason" ALTER COLUMN "change_date" DROP DEFAULT;
--
-- Alter field change_date on groups_of_work
--
ALTER TABLE "manager_groups_of_work" ALTER COLUMN "change_date" SET DEFAULT '2017-03-21T19:25:51.636717+00:00'::timestamptz;
ALTER TABLE "manager_groups_of_work" ALTER COLUMN "change_date" DROP DEFAULT;
--
-- Alter field change_date on level_issue
--
ALTER TABLE "manager_level_issue" ALTER COLUMN "change_date" SET DEFAULT '2017-03-21T19:25:51.703515+00:00'::timestamptz;
ALTER TABLE "manager_level_issue" ALTER COLUMN "change_date" DROP DEFAULT;
--
-- Alter field change_date on solutions
--
ALTER TABLE "manager_solutions" ALTER COLUMN "change_date" SET DEFAULT '2017-03-21T19:25:51.769779+00:00'::timestamptz;
ALTER TABLE "manager_solutions" ALTER COLUMN "change_date" DROP DEFAULT;
--
-- Alter field change_date on state
--
ALTER TABLE "manager_state" ALTER COLUMN "change_date" SET DEFAULT '2017-03-21T19:25:51.844223+00:00'::timestamptz;
ALTER TABLE "manager_state" ALTER COLUMN "change_date" DROP DEFAULT;
--
-- Alter field change_date on status_issue
--
ALTER TABLE "manager_status_issue" ALTER COLUMN "change_date" SET DEFAULT '2017-03-21T19:25:51.911382+00:00'::timestamptz;
ALTER TABLE "manager_status_issue" ALTER COLUMN "change_date" DROP DEFAULT;
--
-- Alter field change_date on workspace
--
ALTER TABLE "manager_workspace" ALTER COLUMN "change_date" SET DEFAULT '2017-03-21T19:25:51.981236+00:00'::timestamptz;
ALTER TABLE "manager_workspace" ALTER COLUMN "change_date" DROP DEFAULT;
--
-- Delete model issue
--
DROP TABLE "manager_issue" CASCADE;
--
-- Delete model workers
--
DROP TABLE "manager_workers" CASCADE;
--
-- Add field current_status to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "current_status_id" integer NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "current_status_id" DROP DEFAULT;
--
-- Add field equipment_inventory to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "equipment_inventory_id" integer NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "equipment_inventory_id" DROP DEFAULT;
--
-- Add field equipment_model to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "equipment_model_id" integer NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "equipment_model_id" DROP DEFAULT;
--
-- Add field equipment_name to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "equipment_name_id" integer NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "equipment_name_id" DROP DEFAULT;
--
-- Add field executor to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "executor_id" integer NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "executor_id" DROP DEFAULT;
--
-- Add field group_of_reason to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "group_of_reason_id" integer NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "group_of_reason_id" DROP DEFAULT;
--
-- Add field groups_of_work to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "groups_of_work_id" integer NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "groups_of_work_id" DROP DEFAULT;
--
-- Add field level_issue to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "level_issue_id" integer NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "level_issue_id" DROP DEFAULT;
--
-- Add field solution to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "solution_id" integer NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "solution_id" DROP DEFAULT;
--
-- Add field user_edit to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "user_edit_id" integer DEFAULT 777 NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "user_edit_id" DROP DEFAULT;
--
-- Add field workspace to issues
--
ALTER TABLE "manager_issues" ADD COLUMN "workspace_id" integer NOT NULL;
ALTER TABLE "manager_issues" ALTER COLUMN "workspace_id" DROP DEFAULT;
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_issues_coordinator_id_20011fb8_fk_login_userprofile_id" FOREIGN KEY ("coordinator_id") REFERENCES "login_userprofile" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_issues_creator_id_1674bb07_fk_login_userprofile_id" FOREIGN KEY ("creator_id") REFERENCES "login_userprofile" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_78527ed6" ON "manager_issues" ("coordinator_id");
CREATE INDEX "manager_issues_3700153c" ON "manager_issues" ("creator_id");
CREATE INDEX "manager_issues_b0e0b0e0" ON "manager_issues" ("current_status_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_i_current_status_id_a7b93eac_fk_manager_status_issue_id" FOREIGN KEY ("current_status_id") REFERENCES "manager_status_issue" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_f989192a" ON "manager_issues" ("equipment_inventory_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_equipment_inventory_id_ee760e21_fk_manager_equipment_id" FOREIGN KEY ("equipment_inventory_id") REFERENCES "manager_equipment" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_83ff7b4a" ON "manager_issues" ("equipment_model_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_iss_equipment_model_id_e1bc1b6d_fk_manager_equipment_id" FOREIGN KEY ("equipment_model_id") REFERENCES "manager_equipment" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_a10e21de" ON "manager_issues" ("equipment_name_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_issu_equipment_name_id_5f3a06fa_fk_manager_equipment_id" FOREIGN KEY ("equipment_name_id") REFERENCES "manager_equipment" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_0ee1c207" ON "manager_issues" ("executor_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_issues_executor_id_5f9869c0_fk_login_userprofile_id" FOREIGN KEY ("executor_id") REFERENCES "login_userprofile" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_caa669d7" ON "manager_issues" ("group_of_reason_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "mana_group_of_reason_id_b9040f8e_fk_manager_groups_of_reason_id" FOREIGN KEY ("group_of_reason_id") REFERENCES "manager_groups_of_reason" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_261d0186" ON "manager_issues" ("groups_of_work_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_groups_of_work_id_fba6b44b_fk_manager_groups_of_work_id" FOREIGN KEY ("groups_of_work_id") REFERENCES "manager_groups_of_work" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_7151374c" ON "manager_issues" ("level_issue_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_issue_level_issue_id_a762aabc_fk_manager_level_issue_id" FOREIGN KEY ("level_issue_id") REFERENCES "manager_level_issue" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_7a8d8e6e" ON "manager_issues" ("solution_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_issues_solution_id_7201e1f4_fk_manager_solutions_id" FOREIGN KEY ("solution_id") REFERENCES "manager_solutions" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_5679ef08" ON "manager_issues" ("user_edit_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_issues_user_edit_id_e262e7f4_fk_auth_user_id" FOREIGN KEY ("user_edit_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "manager_issues_ffedea8b" ON "manager_issues" ("workspace_id");
ALTER TABLE "manager_issues" ADD CONSTRAINT "manager_issues_workspace_id_4cb039cc_fk_manager_workspace_id" FOREIGN KEY ("workspace_id") REFERENCES "manager_workspace" ("id") DEFERRABLE INITIALLY DEFERRED;
COMMIT;
