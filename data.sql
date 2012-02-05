BEGIN;
CREATE TABLE "abit_abiturient" (
    "id" integer NOT NULL PRIMARY KEY,
    "surname" varchar(50) NOT NULL,
    "name" varchar(50) NOT NULL,
    "father" varchar(50) NOT NULL,
    "birth_date" date NOT NULL,
    "passport_ser" varchar(5) NOT NULL,
    "passport_num" varchar(10) NOT NULL,
    "passport_date" date NOT NULL,
    "passport_org" varchar(150) NOT NULL,
    "id_number" varchar(15) NOT NULL,
    "city" varchar(20) NOT NULL,
    "address" varchar(100) NOT NULL,
    "phone" varchar(15) NOT NULL,
    "att_school" varchar(25) NOT NULL,
    "att_date" date NOT NULL,
    "att_srbal" real NOT NULL
)
;
CREATE TABLE "abit_abitrequest_testresults" (
    "id" integer NOT NULL PRIMARY KEY,
    "abitrequest_id" integer NOT NULL,
    "testresult_id" integer NOT NULL,
    UNIQUE ("abitrequest_id", "testresult_id")
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
    "abit_id" integer NOT NULL REFERENCES "abit_abiturient" ("id"),
    "subject_id" integer NOT NULL REFERENCES "abit_testsubject" ("id"),
    "cert_num" varchar(15) NOT NULL,
    "cert_pin" varchar(4) NOT NULL,
    "cert_year" varchar(4) NOT NULL,
    "value" real NOT NULL
)
;
CREATE INDEX "abit_abitrequest_5f1df27f" ON "abit_abitrequest" ("speciality_id");
CREATE INDEX "abit_abitrequest_2202b977" ON "abit_abitrequest" ("abiturient_id");
CREATE INDEX "abit_testresult_2eab3056" ON "abit_testresult" ("abit_id");
CREATE INDEX "abit_testresult_638462f1" ON "abit_testresult" ("subject_id");
COMMIT;
