DROP TABLE IF EXISTS video;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS ytdlp_opt;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS task_logs;
DROP TABLE IF EXISTS log_levels;


-- Project tables
CREATE TABLE IF NOT EXISTS versions
(
    id      TEXT NOT NULL,
    updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status  TEXT NOT NULL,
    link    TEXT NOT NULL,

    CONSTRAINT versions_pk PRIMARY KEY (id)
);

-- Add version to the table if the table exists and if the version has not been inserted at this time or later
INSERT INTO versions(id, status, link)
SELECT '0.1.0', 'ACTIVE DEVELOPMENT', '127.0.0.1/v1/'
WHERE EXISTS(SELECT b.name FROM sqlite_master b WHERE b.type = 'table' AND b.name = 'versions')
  AND NOT EXISTS(SELECT 'X' FROM versions c WHERE c.id == '0.1.0' AND c.updated <= CURRENT_TIMESTAMP);

-- Set last sql updated time to current time
UPDATE versions
SET updated = CURRENT_TIMESTAMP
WHERE id = '0.1.0';

CREATE TABLE IF NOT EXISTS log_levels
(
    level_code INTEGER,
    level_name TEXT NOT NULL,
    CONSTRAINT log_level_pk PRIMARY KEY (level_code)
);

INSERT INTO log_levels(level_code, level_name)
VALUES (0, 'ALL'),
       (1, 'TRACE'),
       (2, 'DEBUG'),
       (3, 'INFO'),
       (4, 'WARN'),
       (5, 'ERROR'),
       (6, 'FATAL');


-- API tables
CREATE TABLE IF NOT EXISTS video
(
    vid         TEXT NOT NULL,
    platform    TEXT NOT NULL,
    url         TEXT NOT NULL,
    title       TEXT,
    description TEXT,
    upload_date TEXT NOT NULL,
    uploader    TEXT NOT NULL,
    duration    TEXT NOT NULL DEFAULT '0:00',
    thumbnail   TEXT,

    CONSTRAINT video_pk PRIMARY KEY (vid)
);

CREATE TABLE IF NOT EXISTS status
(
    status  INTEGER NOT NULL,
    message TEXT    NOT NULL,

    CONSTRAINT status_pk PRIMARY KEY (status)
);

INSERT INTO status(status, message)
VALUES (1, 'waiting'),
       (2, 'processing'),
       (3, 'retrying'),
       (4, 'skipped'),
       (5, 'succeeded'),
       (6, 'failed');


CREATE TABLE IF NOT EXISTS task
(
    tid         TEXT    NOT NULL,
    vid         TEXT    NOT NULL,
    create_date TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finish_date TEXT,
    status      INTEGER NOT NULL DEFAULT 2,
    percent     REAL             DEFAULT 0.0,
    filename    TEXT,
    filesize    INTEGER NOT NULL DEFAULT 0,

    CONSTRAINT task_pk PRIMARY KEY (tid),
    CONSTRAINT task_video_vid_fk FOREIGN KEY (vid) REFERENCES video (vid),
    CONSTRAINT task_status_status_fk FOREIGN KEY (status) REFERENCES status (status)
);

CREATE TABLE IF NOT EXISTS ytdlp_opt
(
    tid     TEXT NOT NULL,
    options TEXT NOT NULL default '[]',

    CONSTRAINT ytdlp_opts_pk PRIMARY KEY (tid),
    CONSTRAINT ytdlp_opts_task_tid_fk FOREIGN KEY (tid) REFERENCES task (tid)
);

INSERT INTO ytdlp_opt(tid, options)
VALUES ('<global>', '[' ||
                    '"-i,"' ||
                    '"-o \"%(uploader)s (%(uploader_id)s)/%(title)s/%(title)s.%(ext)s\"",' ||
                    '"-f bestvideo+bestaudio/best"' ||
                    ']');


CREATE TABLE IF NOT EXISTS task_logs
(
    tid           TEXT    NOT NULL,
    log_timestamp TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    level         INTEGER NOT NULL,
    message       TEXT    NOT NULL,
    CONSTRAINT task_logs_pk PRIMARY KEY (tid, log_timestamp),
    CONSTRAINT task_logs_task_tid_fk FOREIGN KEY (tid) REFERENCES task (tid)
);
