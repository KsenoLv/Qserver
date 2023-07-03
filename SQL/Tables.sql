-- Detailed description you can read in my blog: 
-- https://psql.pro/server-set-up-sql-part/

-- Main table with all data. Sorted.
CREATE TABLE IF NOT EXISTS nyse.nyse_data
(
    date date,
    symbols varchar(5),
    open numeric(8,3),
    high numeric(8,3),
    low numeric(8,3),
    close numeric(8,3)
);

-- Unsorted NEW data.
CREATE TABLE IF NOT EXISTS nyse.nyse_data_new
(
    ticker varchar(5),
    date date,
    open numeric(21,15),
    high numeric(21,15),
    low numeric(21,15),
    close numeric(21,15),
    adj_close numeric(21,15),
    vol varchar(10)
);

-- Description for all ticker.
CREATE TABLE IF NOT EXISTS nyse.ticker_list
(
    ticker varchar(5) NOT NULL,
    name varchar(100)
);

-- File path for ticker.
CREATE TABLE IF NOT EXISTS nyse.file_path
(
    id integer NOT NULL DEFAULT nextval('nyse.file_paths_id_seq'::regclass),
    path text NOT NULL,
    CONSTRAINT file_paths_pkey PRIMARY KEY (id)
);

-- Insert in to file path.
INSERT INTO nyse.file_paths (path) VALUES ('/var/lib/postgresql/data/nyse/AAPL.csv');
INSERT INTO nyse.file_paths (path) VALUES ('/var/lib/postgresql/data/nyse/GOOG.csv');

-- Audit log.
CREATE TABLE IF NOT EXISTS nyse.error_log
(
    date timestamp DEFAULT CURRENT_DATE,
    error_path text NOT NULL,
    error_message text
);

-- Function
CREATE OR REPLACE FUNCTION nyse.load_csv_files()
RETURNS text AS $$
DECLARE
  file_path record;
  file_path_string text;
BEGIN
  FOR file_path IN SELECT path FROM nyse.file_paths LOOP
    BEGIN
      file_path_string := file_path.path;
      -- Creating a file path link, depending on the file name.
      EXECUTE 'COPY nyse.nyse_data_new FROM ''' || file_path_string

 || ''' DELIMITER '','' CSV HEADER';
    EXCEPTION -- Error log data
      WHEN OTHERS THEN
        INSERT INTO nyse.error_log (error_message, error_path) 
        VALUES (SQLERRM, file_path_string);
    END;
  END LOOP;

  RETURN 'Good';
END;
$$ LANGUAGE plpgsql;