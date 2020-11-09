BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "User" (
	"id"	INTEGER,
	"nama"	TEXT,
	"email"	TEXT,
	"password"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "items" (
	"id"	INTEGER,
	"nama"	TEXT,
	"deskripsi"	TEXT,
	"harga"	REAL,
	"stok"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;
