BEGIN;
DROP TABLE "abit_testresult";
DROP TABLE "abit_testsubject";
DROP TABLE "abit_speciality";
DROP TABLE "abit_speciality_subjects";
DROP TABLE "abit_abitrequest";
DROP TABLE "abit_abiturient";
CREATE TABLE "abit_abiturient" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "surname" varchar(50) NOT NULL,
    "father" varchar(50) NOT NULL
)
;
CREATE TABLE "abit_abitrequest" (
    "id" integer NOT NULL PRIMARY KEY,
    "code" varchar(7) NOT NULL,
    "speciality_id" integer NOT NULL,
    "abiturient_id" integer NOT NULL REFERENCES "abit_abiturient" ("id")
)
;
CREATE TABLE "abit_speciality_subjects" (
    "id" integer NOT NULL PRIMARY KEY,
    "speciality_id" integer NOT NULL,
    "testsubject_id" integer NOT NULL,
    UNIQUE ("speciality_id", "testsubject_id")
)
;
CREATE TABLE "abit_speciality" (
    "id" integer NOT NULL PRIMARY KEY,
    "code" varchar(15) NOT NULL,
    "name" varchar(50) NOT NULL
)
;
CREATE TABLE "abit_testsubject" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL
)
;
CREATE TABLE "abit_testresult" (
    "id" integer NOT NULL PRIMARY KEY,
    "request_id" integer NOT NULL REFERENCES "abit_abitrequest" ("id"),
    "subject_id" integer NOT NULL REFERENCES "abit_testsubject" ("id"),
    "value" integer NOT NULL
)
;
CREATE INDEX "abit_abitrequest_5f1df27f" ON "abit_abitrequest" ("speciality_id");
CREATE INDEX "abit_abitrequest_2202b977" ON "abit_abitrequest" ("abiturient_id");
CREATE INDEX "abit_testresult_792812e8" ON "abit_testresult" ("request_id");
CREATE INDEX "abit_testresult_638462f1" ON "abit_testresult" ("subject_id");
COMMIT;
