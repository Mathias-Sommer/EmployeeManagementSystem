-- Create the users table with necessary fields
CREATE TABLE users (
    id SERIAL PRIMARY KEY,                             -- Auto-incrementing ID for each user
    username VARCHAR(255) UNIQUE NOT NULL,             -- Unique username
    password VARCHAR(255) NOT NULL,                    
    email VARCHAR(255) UNIQUE NOT NULL,                -- Unique email
    first_name VARCHAR(255) NOT NULL,                  
    last_name VARCHAR(255) NOT NULL,                   
    date_created TIMESTAMPTZ DEFAULT NOW(),            -- Date of account creation (current timestamp)
    last_password_change TIMESTAMPTZ,                  -- Date when the password was last changed
    last_login TIMESTAMPTZ,                            -- Date of the last login
    is_active BOOLEAN DEFAULT TRUE,                    -- If the account is active or not
    is_locked BOOLEAN DEFAULT FALSE                    -- If the account is locked (e.g., too many failed logins)
);
