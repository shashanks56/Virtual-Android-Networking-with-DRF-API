CREATE TABLE "api_app" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app_name" varchar(105) NOT NULL,
    "version" varchar(105) NOT NULL,
    "description" text NOT NULL
);